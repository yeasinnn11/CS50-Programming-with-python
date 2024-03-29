while True:
    fuel = input("Fraction: ")
    try:
        divided_number , division_number = fuel.split("/")
        result_one =int(divided_number)
        result_tow = int(division_number)
        f = result_one / result_tow
        if f<=1:
            break
    except (ValueError, ZeroDivisionError):
            pass
p = int(f * 100)
s = round(p)
if s <= 1:
    print("E")
elif s >=99:
    print("F")
else:
    print(f"{s}%")
