from ast import arg


number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# string: h42l -> [h, 42, l]
def slice_string_keep_numbers(string: str) -> list:
    char_list = []

    saved_num = ""

    for char in string:
        if char in number_list:
            saved_num += char
        else:
            if saved_num:
                char_list.append(saved_num)
            char_list.append(char)
            saved_num = ""

    if saved_num:
        char_list.append(saved_num)

    return char_list


def filter_string(string: str, removable_list: list = [str]) -> str:
    string_list = [*string]

    filtered_string_list = filter(lambda char: char not in removable_list, string_list)

    return "".join(filtered_string_list)


# colours availabe are (gray, red, green, yellow, blue, purple, cyan)
def coloured_string(string: str, colour: str) -> str:
    colour_dict = {
        "gray": "\33[90m",
        "red": "\33[91m",
        "green": "\33[92m",
        "yellow": "\33[93m",
        "blue": "\33[94m",
        "purple": "\33[95m",
        "cyan": "\33[96m",
    }

    return f"{colour_dict[colour]}{string}\33[0m"


# all lists must be same length
def print_table(*args: list) -> None:
    print(50 * "-")

    for item_index in range(len(args[0])):
        for list_index in range(len(args)):
            print(args[list_index][item_index], " | ", end="")
        print(f"\n{50 * '-'}")






    

