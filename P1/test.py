import sys
import time

message = "Компьютер обрабатывает ваш запрос"
dots = "..."

# Печать начального сообщения
sys.stdout.write(message)

# Постепенное добавление точек
for i in range(3):
    sys.stdout.write(dots[i])
    sys.stdout.flush()  # Обновление вывода
    time.sleep(0.5)  # Задержка между точками

print()  # Переход на новую строку