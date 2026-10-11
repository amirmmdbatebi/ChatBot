def normalize_persian_text(text):
    # Convert Arabic characters to Persian characters
    text = text.replace("ي", "ی")
    text = text.replace("ى", "ی")
    text = text.replace("ك", "ک")

    # Remove unnecessary whitespace
    lines = text.splitlines()

    normalized_lines = []

    for line in lines:
        line = line.strip()

        if line:
            normalized_lines.append(line)

    return "\n".join(normalized_lines)


# Read the insurance knowledge file
with open("insurance_knowledge.md", "r", encoding="utf-8") as file:
    knowledge = file.read()


# Normalize the text
normalized_knowledge = normalize_persian_text(knowledge)


# Save the normalized version
with open("insurance_knowledge_normalized.md", "w", encoding="utf-8") as file:
    file.write(normalized_knowledge)


print("Normalization completed.")