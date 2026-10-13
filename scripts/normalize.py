
from pathlib import Path


def normalize_persian_text(text):
    # Convert Arabic characters to Persian characters
    text = text.replace("ÙŠ", "ÛŒ")
    text = text.replace("Ù‰", "ÛŒ")
    text = text.replace("Ùƒ", "Ú©")

    # Remove unnecessary whitespace
    lines = text.splitlines()
    normalized_lines = []

    for line in lines:
        line = line.strip()

        if line:
            normalized_lines.append(line)

    return "\n".join(normalized_lines)


# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "knowledge" / "insurance_knowledge.md"
OUTPUT_PATH = (
    BASE_DIR
    / "knowledge"
    / "processed"
    / "insurance_knowledge_normalized.md"
)

# Ensure the output directory exists
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Read the insurance knowledge file
with INPUT_PATH.open("r", encoding="utf-8") as file:
    knowledge = file.read()

# Normalize the text
normalized_knowledge = normalize_persian_text(knowledge)

# Save the normalized version
with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    file.write(normalized_knowledge)

print("Normalization completed.")
