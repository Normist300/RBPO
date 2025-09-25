# 2. Работа  с файлами

import os, time, sys

#Создать файл
file_name = "file.txt"
with open(file_name, 'w') as file:
    print(file_name, "создан.")

#Записать в файл строку, введённую пользователем
user_input = input('''          
                  .----.
      .---------. | == |
      |.-"""""-.| |----|
      ||       || | == |
      ||       || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\\" _  "
    /:::=======:::\`\`\\
    `"""""""""""""`  '-'
    Введите строку, компьютер ждёт Вас:''')

print("Компьютер обрабатывает ваш запрос")
for i in range(5):
    time.sleep(0.5)
    sys.stdout.write('.') # Через принты не работает
    sys.stdout.flush()
print('.')

with open(file_name, 'w') as file:
    file.write(user_input)
    print(f"Строка '{user_input}' записана в файл.")

#Прочитать файл в консоль
with open(file_name, 'r') as file:
    file_content = file.read()
    print(f"Содержимое файла '{file_name}':")
    print(file_content)

#Удалить файл
os.remove(file_name)
print(f"Файл '{file_name}' удалён.")
