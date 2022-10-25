from tabulate import tabulate


from module import generate_products, product_avg_price


if __name__ == "__main__":
    products_prices = product_avg_price(generate_products(75000))

    products_prices.insert(0, ("Product", "AveragePrice"))

    print(tabulate(products_prices, headers="firstrow", tablefmt="fancy_grid"))
