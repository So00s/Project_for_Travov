"""
Основной файл
"""
from utils import *


def main():
    name = "text.txt"
    counter = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    counter_vyzov = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    # чтение файла построчно и его обработка
    with open(f"{name}", 'r', encoding="UTF-8") as f:
        while True:
            # считываем строку
            line = f.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            list_of_word = read_word(line)
            # print(list_of_word)
            for _ in list_of_word:
                list_of_num = (convert_to_numbers(_))
                # print(list_of_num)
                # print(count_of_move(list_of_num))
                for key, value in count_of_move(list_of_num).items():
                    counter[key] += value
            for _ in list_of_word:
                list_of_num = (convert_vyzov_to_numbers(_))
                # print(list_of_num)
                # print(count_of_move(list_of_num))
                for key, value in count_of_move(list_of_num).items():
                    counter_vyzov[key] += value
        print(counter)
        print(counter_vyzov)


if __name__ == '__main__':
    main()
    
