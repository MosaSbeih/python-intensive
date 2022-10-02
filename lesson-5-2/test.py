from my_package.module import slice_string_keep_numbers, coloured_string, filter_string, print_table


if __name__ == "__main__":
    print(slice_string_keep_numbers("row42column333"))

    print(filter_string("H-e-l-l-o Wo0rld", ["-", "0"]))

    print(coloured_string("Hello", "gray"))
    print(coloured_string("Hello", "red"))
    print(coloured_string("Hello", "green"))
    print(coloured_string("Hello", "yellow"))
    print(coloured_string("Hello", "blue"))
    print(coloured_string("Hello", "purple"))
    print(coloured_string("Hello", "cyan"))

    food_type = ["Fruit and vegetables", "Dairy", "Protein"]
    food_example = ["Apple", "Milk", "Tuna"]
    avg_price = ["0.5$", "3$", "2$"]

    print_table(
        food_type,
        food_example,
        avg_price,
        )
