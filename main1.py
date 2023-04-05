"""
Функция, которая считывает строки из файла
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


"""
счетчик ходов
"""


def count_of_move(list_of_numbers):
    counter = 0
    dict_of_row = {"tr": {"lfi5": {0: 41, 1: 2, 2: 3}, "lfi4": {3: 4}, "lfi3": {4: 5}, "lfi2": {5: 6, 6: 7}, "rfi\
2": {7: 8, 8: 9}, "rfi3": {9: 10}, "rfi4": {10: 11}, "rfi5": {11: 12, 12: 13, 13: 14}}, "mr": {"lfi\
5": {0: 15, 1: 16}, "lfi4": {2: 17}, "lfi3": {3: 18}, "lfi2": {4: 19, 5: 20}, "rfi2": {6: 21, 7: 22}, "r\
fi3": {8: 23}, "rfi4": {9: 24}, "rfi5": {10: 25, 11: 26, 12: 27, 13: 43}}, "hr": {"lfi5": {0: 58, 1: 30}, "lfi\
4": {2: 31}, "lfi3": {3: 32}, "lfi2": {4: 33, 5: 34}, "rfi2": {6: 35, 7: 36}, "rfi3": {8: 37}, "rfi\
4": {9: 38}, "rfi5": {10: 39, 11: 40, 12: 28, 13: ""}}, "dr": {"lfi5": {0: 42, 1: 44}, "lfi4": {2: 45}, "lfi\
3": {3: 46}, "lfi2": {4: 47, 5: 48}, "rfi2": {6: 49, 7: 50}, "rfi3": {8: 51}, "rfi4": {9: 52}, "rfi\
5": {10: 53, 11: 54, 12: "", 13: ""}}}
    count_moves = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    prev_position = {"lfi5": {"row": 2, "col": 1}, "lfi4": {"row": 2, "col": 2}, "lfi3": {"row": 2, "col": 3}, "lfi\
2": {"row": 2, "col": 4}, "rfi2": {"row": 2, "col": 7}, "rfi3": {"row": 2, "col": 8}, "rfi4": {"row": 2, "col": 9}, "rf\
i5": {"row": 2, "col": 10}}
    for _ in list_of_numbers:
        for k, v in dict_of_row.items():
            for k1, v1 in v.items():
                for k2, v2 in v1.items():
                    if _ == v2:
                        out = [k, k1, k2]
                        if out[0] == "tr":
                            for key, value in prev_position.items():
                                if k1 == key:
                                    count_moves[k1] += abs(value["row"] - 0)
                                    value["row"] = 0
                                    count_moves[k1] += abs(value["col"] - k2)
                                    value["col"] = k2
                        elif out[0] == "mr":
                            for key, value in prev_position.items():
                                if k1 == key:
                                    count_moves[k1] += abs(value["row"] - 1)
                                    value["row"] = 1
                                    count_moves[k1] += abs(value["col"] - k2)
                                    value["col"] = k2
                        elif out[0] == "hr":
                            for key, value in prev_position.items():
                                if k1 == key:
                                    count_moves[k1] += abs(value["row"] - 2)
                                    value["row"] = 2
                                    count_moves[k1] += abs(value["col"] - k2)
                                    value["col"] = k2
                        elif out[0] == "dr":
                            for key, value in prev_position.items():
                                if k1 == key:
                                    count_moves[k1] += abs(value["row"] - 3)
                                    value["row"] = 3
                                    count_moves[k1] += abs(value["col"] - k2)
                                    value["col"] = k2
    return count_moves


def main():
    name = "test.txt"
    list_of_lines = read_file(name)
    # print(list_of_lines)
    list_of_word = read_word(list_of_lines)
    # print(list_of_word)
    counter = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    for _ in list_of_word:
        list_of_num = (convert_to_numbers(_))
        # print(list_of_num)
        # print(count_of_move(list_of_num))
        for key, value in count_of_move(list_of_num).items():
            counter[key] += value
    print(counter)


if __name__ == '__main__':
    main()