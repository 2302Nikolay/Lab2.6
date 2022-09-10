#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

if __name__ == '__main__':
    school = {'1А': 24, '1Б': 32, '1В': 16, '2А': 21, '2Б': 15, '3А': 10}

    while True:
        command = input(">> ").lower()

        if command == 'exit':
            break
        # Добавление класса в словарь
        elif command == 'add':
            cl_add = input("Класс: ")
            count_add = input("Количество учеников: ")

            school[cl_add] = count_add
        # Вывод списка комманд
        elif command == 'help':
            print(
                "Список команд: \n",
                "add - добавить класс\n",
                "delite - удалить класс\n",
                "disp - вывести классы\n",
                "help - список команд\n",
                "summ - общее количество учащихся в школе\n",
                "exit - выход из программы"
                  )
        # Удаление класса из словаря
        elif command == 'delite':
            key = input("Класс, который необходмо удалить: ")
            school.pop(key)
        # Вывод словаря
        elif command == 'displ':
            print(school)
        #Вывод общего количества учащихся
        elif command == 'summ':
            count = sum(school.values())
            print("Количество учеников в школе: ", count)
        # Вывод ошибки в случае ввода неправильной команды
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
