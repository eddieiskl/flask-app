with open('words.txt', 'w', encoding='utf-8') as file:
    file.write("שלום")

with open('words.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)