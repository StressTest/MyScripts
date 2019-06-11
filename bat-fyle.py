# python
import os.path, os
paths = [ r'C:\Users\andrew\PycharmProjects\emi']
for variant in enumerate(paths):
    print(f"{variant[0]+1}: {variant[1]}")
try:
    varian = int(input('Введите номер варианта: ').strip())
except TypeError:
    print('Необходимо ввести число')
if varian > len(paths):
    print('Несуществующий путь')
else:
    start_path = os.path.realpath(paths[varian-1])
    ans = input(f'Запустить виртуальную среду {start_path} Y/N? ').strip().lower()
    if ans != 'y':
        print('Goodbye')
    else:
        start_path = os.path.normpath(start_path)
        os.chdir(start_path)
        full_path = os.path.realpath(os.path.join(os.path.normpath(start_path), os.path.normpath(r'Scripts\activate.bat')))
        os.system(rf'C:\Windows\System32\cmd.exe /K {full_path} ; jupyter-notebook')
