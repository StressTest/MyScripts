# Эксперименты с регулярными выражениями
# Можно удалить не задумываясь
import re
import requests
from fpdf import FPDF
last_adr = input('''Введите строку с адресом картинки с последнего слайда.
______________________________________________________

Примерный вид:
https://webinar.nocvko.ru/presentation/105d62400580fa7e383653e01bcbf89011248cf5-1552402648080/presentation/816cafcb9472cdf3d0595f3807b4acf6f896a743-1552404909746/slide-13.png

: ''')
tmp_adr = re.sub(r'\.png$', '', last_adr)
num = int(re.search(r'\d+$', tmp_adr).group(0))
prefix_adr = re.sub(r'\d+$', '', tmp_adr)
file_list = []
print('_'*59)
for i in range(1, num + 1):
    adr = prefix_adr + str(i) + '.png'
    r = requests.get(adr)
    print('Получен файл ' + adr)
    filename = str(i) + '.png'
    with open(filename, 'wb') as f:
        f.write(r.content)
    file_list.append(filename)
print('Созданы файл слайдов ')

pdf = FPDF(orientation = 'L', unit = 'mm', format='A4')
for image in file_list:
    pdf.add_page()
    pdf.image(image, x=29, y=15, w=238, h=179)
pdf.output('output.pdf', 'F')
print('\n' + '_'*59)
input('Создан файл output.pdf. Для выхода нажмите Enter')

