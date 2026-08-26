# 81. Read File Line by Line

# First create sample.txt in the same folder and add some text.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print("File not found. Please create sample.txt first.")
# with open(...) automatically closes the file after reading.

# 82. Write Content to File

# This creates sample.txt if it does not exist. If it already exists, "w" replaces all old content.

content = """Python file handling is useful.
This content is written into a file.
Learning Python step by step."""

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Content written successfully.")

# 83. Append Text to File

# Append means add new text at the end without deleting existing content.

new_text = "\nThis line was added using append mode."

with open("sample.txt", "a", encoding="utf-8") as file:
    file.write(new_text)

print("Text appended successfully.")

# 84. Count Words and Lines in File

try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

    print("Number of lines:", line_count)
    print("Number of words:", word_count)

except FileNotFoundError:
    print("File not found. Please create sample.txt first.")

