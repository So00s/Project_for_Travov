"""
функция которая считывает строки из файла
"""


def read_file(name):
    with open(f"{name}", 'r', encoding="UTF-8") as f:
        list_line = f.readlines()
    return list_line


"""
Разбиение на слова
"""


def read_word(list_lines):
    word = ""
    list_of_word = []
    for row in list_lines:
        row = row.rstrip()
        for _ in row:
            if _ != " ":
                word += _
            else:
                list_of_word.append(word)
                word = ""
        word += "E"
        list_of_word.append(word)
        word = ""
    return list_of_word


"""
перевод в цифры
"""


def convert_to_numbers(string):
    list_of_num = []
    lfi5 = {41: "ё", 2: "1", 3: "2", 15: "tab", 16: "й", 30: "ф", 58: "Caps", 42: "L", 44: "я"}
    lfi4 = {4: "3", 17: "ц", 31: "ы", 45: "ч"}
    lfi3 = {5: "4", 18: "у", 32: "в", 46: "с"}
    lfi2 = {6: "5", 7: "6", 19: "к", 20: "е", 33: "а", 34: "п", 47: "м", 48: "и"}
    rfi5 = {12: "-", 13: "=", 14: "bs", 25: "з", 26: "х", 27: "ъ", 43: "\\", 39: "ж", 40: "э", 28: "E", 53: ".", 54: "\
    R"}
    rfi4 = {11: "0", 24: "щ", 38: "д", 52: "ю"}
    rfi3 = {10: "9", 23: "ш", 37: "л", 51: "б"}
    rfi2 = {8: "7", 9: "8", 21: "н", 22: "г", 35: "р", 36: "о", 49: "т", 50: "ь"}
    fi1 = {57: " "}
    left_upper = ["Й", "Ц", "У", "К", "Е", "П", "А", "В", "Ы", "Ф", "Я", "Ч", "С", "М", "И"]
    for _ in string:
        if _.isupper() or _ == ",":
            if _ in left_upper:
                list_of_num.append(54)
            elif _ == ",":
                list_of_num.append(42)
                list_of_num.append(53)
            elif _ == "E":
                list_of_num.append(28)
            else:
                list_of_num.append(42)
        _ = _.lower()
        for key, value in lfi5.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in lfi4.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in lfi3.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in lfi2.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in rfi5.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in rfi4.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in rfi3.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in rfi2.items():
            if _ == value:
                list_of_num.append(key)
        for key, value in fi1.items():
            if _ == value:
                list_of_num.append(key)

    return list_of_num


def test_dict(num):
    test = {"lfi1": {1: 3, 2: 25}, "lfi2": {1: 1, 3: 2}}
    for i, j in test.items():
        print(i, " ", j)
        for key, value in j.items():
            if num == value:
                print(i, key)
    return 0


"""
счетчик ходов
"""


def count_of_move(list_of_numbers):
    counter = 0
    dict_of_row = {"tr": {"lfi5": {0: 41, 1: 2, 2: 3}, "lfi4": {3: 4}, "lfi3": {4: 5}, "lfi2": {5: 6, 6: 7}, "rfi\
        2": {7: 8, 8: 9}, "rfi3": {9: 10}, "rfi4": {10: 11}, "rfi5": {11: 12, 12: 13, 13: 14}}, "mr": {"lfi\
        5": {0: 15, 1: 16}, "lfi4": {2: 17}, "lfi3": {3: 18}, "lfi2": {4: 19, 5: 20, 6: 21}, "rfi2": {7: 22, 8: 23}, "r\
        fi3": {9: 24}, "rfi4": {10: 25}, "rfi5": {11: 26, 12: 27, 13: 43}}, "hr": {"lfi5": {0: 58, 1: 30, 2: 31}, "lfi\
        4": {3: 32}, "lfi3": {4: 33}, "lfi2": {5: 34, 6: 35}, "rfi2": {7: 36, 8: 37}, "rfi3": {9: 38}, "rfi\
        4": {10: 39}, "rfi5": {11: 40, 12: 28, 13: ""}}, "dr": {"lfi5": {0: 42, 1: 44, 2: 45}, "lfi4": {3: 46}, "lfi\
        3": {4: 47}, "lfi2": {5: 48, 6: 49}, "rfi2": {7: 50, 8: 51}, "rfi3": {9: 52}, "rfi4": {10: 53}, "rfi\
        5": {11: 54, 12: "", 13: ""}}}
    count_moves = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    prev_position = {"lfi5": {"row": 0, "col": 0}, "lfi4": {"row": 0}, "lfi3": {"row": 0}, "lfi2": {"row": 0, "co\
        l": 0}, "rfi2": {"row": 0, "col": 0}, "rfi3": {"row": 0}, "rfi4": {"row": 0}, "rfi5": {"row": 0, "col": 0}}
    for _ in list_of_numbers:
        for k, v in dict_of_row.items():
            for k1, v1 in v.items():
                for k2, v2 in v1.items():
                    if _ == v2:
                        out = [k, k1, k2]
                        print(out)
                        for k3, v3 in count_moves.items():
                            if k2 == k3:
                                v3 += counter
    lfi5_prev = 0
    pos_now = 0
    pos_prev = 0
    return count_moves


if __name__ == '__main__':
    #name = input("Введите название файла: \n")
    name = "test.txt"
    list_of_lines = read_file(name)
    print(list_of_lines)
    list_of_word = read_word(list_of_lines)
    print(list_of_word)
    for _ in list_of_word:
        list_of_num = (convert_to_numbers(_))
        print(list_of_num)
        count_of_move(list_of_num)
'''
    string = input("Введите строку: \n")
    #string = string.lower()
    list1 = convert_to_numbers(string)
    print(list1)
    s = ""
    for i in range(len(list1)):
        if i == len(list1) - 1:
            s += str(list1[i])
        else:
            s += str(list1[i]) + ","
    print(s)
'''
