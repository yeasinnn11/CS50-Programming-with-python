fruits = {"apple": 130,
          "Avocado": 50,
          "pear": 100,
          "Kiwifruit":90,
          "Sweet Cherries": 100}

fruits_asked = str(input("Item: "))

for key in fruits:
    if key == fruits_asked:
        print(f"Calories: {fruits[key]}")

