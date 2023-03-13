def read_file():

    return 0


def count_of_press(string):
    listOfNum = []
    lfi5 = {41: "ё", 2: "1", 3: "2", 15: "tab", 16: "й", 30: "ф", 58: "Caps", 42: "LShift", 44: "я"}
    lfi4 = {4: "3", 17: "ц", 31: "ы", 45: "ч"}
    lfi3 = {5: "4", 18: "у", 32: "в", 46: "с"}
    lfi2 = {6: "5", 7: "6", 19: "к", 20: "е", 33: "а", 34: "п", 47: "м", 48: "и"}
    rfi5 = {12: "-", 13: "=", 14: "bs", 25: "з", 26: "х", 27: "ъ", 43: "\\", 39: "ж", 40: "э", 28: "Enter", 53: ".", 54: "RShift"}
    rfi4 = {11: "0", 24: "щ", 38: "д", 52: "ю"}
    rfi3 = {10: "9", 23: "ш", 37: "л", 51: "б"}
    rfi2 = {8: "7", 9: "8", 21: "н", 22: "г", 35: "р", 36: "о", 49: "т", 50: "ь"}
    fi1 = {57: " "}
    for i in string:
        for key, value in lfi5.items():
            if i == value:
                listOfNum.append(key)
        for key, value in lfi4.items():
            if i == value:
                listOfNum.append(key)
        for key, value in lfi3.items():
            if i == value:
                listOfNum.append(key)
        for key, value in lfi2.items():
            if i == value:
                listOfNum.append(key)
        for key, value in rfi5.items():
            if i == value:
                listOfNum.append(key)
        for key, value in rfi4.items():
            if i == value:
                listOfNum.append(key)
        for key, value in rfi3.items():
            if i == value:
                listOfNum.append(key)
        for key, value in rfi2.items():
            if i == value:
                listOfNum.append(key)
        for key, value in fi1.items():
            if i == value:
                listOfNum.append(key)
    return listOfNum


if __name__ == '__main__':
    string = input("Введите строку: \n")
    string = string.lower()
    list1 = count_of_press(string)
    s = ""
    for i in range(len(list1)):
        if i == len(list1) - 1:
            s += str(list1[i])
        else:
            s += str(list1[i]) + ","
    print(s)
