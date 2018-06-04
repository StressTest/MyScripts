#!/usr/bin/env python3
import json
import os
import subprocess

pip_list = subprocess.getoutput('pip3 list -o --format=json')
results = json.loads(pip_list)
names = []
if results:
    print('''Устаревшие пакеты\n****************''')
    for row in results:
        name = row['name']
        names.append(name)
        print('\t' + name)
    print("****************")

    decision = input('Обновить пакеты Y/N? ').strip().upper()
    counter = 0
    while decision != "Y" and decision != "N":
        if counter >= 3:
            print('4 неправильные попытки. Операция будет прекращена')
            break
        decision = input('Введите Y для установки и N чтобы прервать ').strip().upper()
        counter = counter + 1
    if decision == 'Y':
        output = []
        for name in names:
            res = subprocess.run([f"sudo -H pip3 install -U {name}"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            # print("++++++++++++")
            # print(res.stderr)
            # print("------------")
            if res.stderr:
                output.append(name)
            # if os.system(f"sudo -H pip3 install -U {name}") != 0:
            #     output.append(name)
        if len(output) == 0:
            print('Все пакеты установлены')
        else:
            print('Следующие пакеты не были установлены:')
            print(', '.join(output))
else:
    print("Нет устаревших пакетов")
input('Конец. Нажмите Enter для выхода')
