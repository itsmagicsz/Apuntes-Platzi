def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname":"Daniel", "lastname": "Angel"}

    super_list = [
        {"firstname":"Daniel", "lastname": "Angel"},
        {"firstname":"David", "lastname": "Garcia"},
        {"firstname":"Juan", "lastname": "Rodriguez"},
        {"firstname":"Pepe", "lastname": "Lopez"},
        {"firstname":"Jose", "lastname": "Rojas"}
    ]

    super_dict = {
        "Natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.7, 9.9]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i["firstname"],"-",i["lastname"])



if __name__ == '__main__':
    run()