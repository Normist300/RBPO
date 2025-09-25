# 1. Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.
import psutil

parts = psutil.disk_partitions()
print('-' * 40)

for part in parts:
    usage = psutil.disk_usage(part.mountpoint)
    label = part.device
    print(f"Монтирован: {part.mountpoint}")
    print(f"Тип файловой системы: {part.fstype}")
    print(f"Размер: {usage.total / (1024 ** 3):.2f} GB")  # В гигбайтах
    print(f"Метка тома: {label}")
    print('-' * 40)
