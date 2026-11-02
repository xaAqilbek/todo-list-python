with open("../names.txt", "w", encoding="utf-8") as file:
    file.write("Aqil\n")
    file.write("Lala\n")
    file.write("Ata\n")

with open("../names.txt", "a", encoding="utf-8") as file:
    file.write("Mama\n")

with open("../names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())