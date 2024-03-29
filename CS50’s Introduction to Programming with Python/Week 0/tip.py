def main():
    dollars = dollars_to_float(input("How much was the meal: "))
    percent = percent_to_float(input("What percentage would you like to tip: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
def dollars_to_float(d):
    amount_str = d.replace('$', '')
    return float(amount_str)
def percent_to_float(p):
    percent_str = p.replace('%', '')
    return float(percent_str) / 100
main()
