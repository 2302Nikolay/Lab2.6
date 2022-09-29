#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import datetime

if __name__ == '__main__':
    # Список .
    manslist = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            name = input("Имя:  ")
            number = input("Номер телефона ")
            date = input("Дата рождения  ")

            # Создать словарь.
            man = {
                'name': name,
                'number': number,
                'date': date,
            }

            # Добавить словарь в список.
            manslist.append(man)
            # Отсортировать список.
            if len(manslist) > 1:
                manslist.sort(key=lambda item: datetime.datetime.strptime(item.get('date', ''), '%d.%m.%Y'))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о человеке.
            for idx, man in enumerate(manslist, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        man.get('name', ''),
                        man.get('number', ''),
                        man.get('date', '')
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            sel = parts[1]

            count = 0
            for man in manslist:
                if man.get('number') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, man.get('name', ''))
                    )
                    print('Номер телефона:', man.get('number', ''))
                    print('Дата рождения:', man.get('date', ''))

            # Если счетчик равен 0, то человек не найден.
            if count == 0:
                print("Человек не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <товар> - информация о человеке;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)
