from csv import reader
import os
import random


def open_table():
    try:
        with open('books.csv', 'r', encoding='cp1251') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            # print(table[0])
            return table[1:]
    except FileNotFoundError:
        print('Файл не найден!')
        return 0


def filter_name(table, len_name=30): 
    return list(filter(lambda x: len(x[1]) > len_name, table))


def search_autor(table, autor, lim_price=200):
    if autor == '': autor = 'Людмила Петрановская' 
    f_table = filter(lambda x: float(x[7]) < lim_price and x[3] == autor, table)
    return [x[1] for x in f_table]


def generator_links(table):
    table = random.sample(table, 20)
    return [f'{x[3]}. {x[1]} - {x[6].split()[0].split('.')[-1]}' for x in table]


if __name__ == '__main__':
    table = open_table()
    if table == 0:
        exit() 
    while True:
        os.system('clear')
        print('Меню:\n1 - Число записей, им. Название более 30 симв.\n2 - Поиск по автору (ограничение до 200р)\n3 - Генератор библиографических ссылок (20 записей)\n0 - Выход')
        menu = input('Выберите пункт меню: ')
        match menu:
            case '1':
                print(len(filter_name(table)))
            case '2':
                autor = input('Введите автора (по умолч. Людмила Петрановская)')
                print(*search_autor(table, autor), sep='\n')
            case '3':
                links = generator_links(table)
                print(*links, sep='\n')
                with open('result.txt', 'w', encoding='utf8') as t: 
                    for i, link in enumerate(links):
                        t.write(f'{i + 1}. {link}\n')
                print('\nВывод произведён в файл result.txt')
            case '0':
                break
            case _:
                print('Нет пункта меню, нажмите Enter')
        input()

