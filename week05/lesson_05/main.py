import platform
import sys

print(sys.platform)
print(sys.executable)
print(sys.version)

print("Информация о системе:")
ops, name, oper_ver, build, proc, proc_fam = platform.uname()
print(f"Операционная система: {ops}")
print(f"Архитектура: {platform.architecture()}")
print(f"Платформа: {sys.platform}")
print(f"Версия операционной системы: {oper_ver}")
print(f"Релиз операционной системы: {build}")
print(f"Пользователь системы: {name}")
print()
print(f"Архитектура процессора: {proc}")
print(f"Модель процессора: {proc_fam}")
print()
print(f"Версия Python: {' от '.join(platform.python_build())}")
print(f"Версия компилятора Python: {platform.python_compiler()}")
print(f"Реализация Python: {platform.python_implementation()}")
print(f"Папка установки интерпретатора Python: {sys.prefix}")
