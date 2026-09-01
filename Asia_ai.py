from openai import OpenAI

# تنظیمات اتصال به Agnes AI
client = OpenAI(
    api_key="sk-HpS4NnEuGF3lGOqaedJ6vpT3OJCt2OgpopiRHwvlBbA25kO7",
    base_url="https://apihub.agnes-ai.com/v1"
)

# ✅ مدل درست از Agnes
MODEL = "agnes-2.5-flash"  # یا agnes-2.5-pro

print("🤖 چت‌بات Agnes آماده است!")
print("برای خروج، بنویس: exit یا quit\n")
print("-" * 50)

# تاریخچه مکالمه
messages = [
    {"role": "system", "content": "تو یک دستیار مفید و دوستانه هستی."}
]

while True:
    # دریافت پیام کاربر
    user_input = input("\n👤 شما: ")
    
    # بررسی خروج
    if user_input.lower() in ["exit", "quit", "خروج"]:
        print("\n👋 خداحافظ! موفق باشی.")
        break
    
    # اضافه کردن پیام کاربر به تاریخچه
    messages.append({"role": "user", "content": user_input})
    
    try:
        # درخواست به API
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7
        )
        
        # استخراج پاسخ
        answer = response.choices[0].message.content
        
        # اضافه کردن پاسخ به تاریخچه
        messages.append({"role": "assistant", "content": answer})
        
        # نمایش پاسخ
        print(f"\n🤖 ربات: {answer}")
        
    except Exception as e:
        print(f"\n❌ خطا: {e}")
        messages.pop()