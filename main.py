from utils import *


def main():
    name = "test.txt"
    list_of_lines = read_file(name)
    print(list_of_lines)
    list_of_word = read_word(list_of_lines)
    print(list_of_word)
    counter = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    for _ in list_of_word:
        list_of_num = (convert_to_numbers(_))
        print(list_of_num)
        print(count_of_move(list_of_num))
        for key, value in count_of_move(list_of_num).items():
            counter[key] += value
    print(counter)
    counter = {"lfi5": 0, "lfi4": 0, "lfi3": 0, "lfi2": 0, "rfi2": 0, "rfi3": 0, "rfi4": 0, "rfi5": 0}
    for _ in list_of_word:
        list_of_num = (convert_vyzov_to_numbers(_))
        print(list_of_num)
        print(count_of_move(list_of_num))
        for key, value in count_of_move(list_of_num).items():
            counter[key] += value
    print(counter)


if __name__ == '__main__':
    main()
    
