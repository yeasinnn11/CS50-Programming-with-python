Grocery_list = {}

while True:
    try:
        item = input().lower()
        if item in Grocery_list:
            Grocery_list[item] += 1
        else:
            Grocery_list[item] = 1
    except EOFError:
        for key in sorted(Grocery_list.keys()):
            print(Grocery_list[key], key.upper())
        break
