# *** Task 2 ***
# Write the message "Hello SoftServe" in the file (some_file.txt), close the file,
# then write to the file in a new line the message "Hello Python!!!", close the file.
# After that read information from a file some_file.txt and print it.

FILE = r"some_file.txt"
MESSAGE_1 = "Hello SoftServe"
MESSAGE_2 = "Hello Python!!!"

with open(FILE, "w", encoding="utf-8") as file:
    file.write(MESSAGE_1)

with open(FILE, "a", encoding="utf-8") as file:
    file.write(f"\n{MESSAGE_2}")

with open(FILE, "r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
