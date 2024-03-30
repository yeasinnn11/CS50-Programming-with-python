def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)


def convert(fraction):
    while True:
        try:
            divided_number, division_number = fraction.split("/")
            result_one =int(divided_number)
            result_tow = int(division_number)
            f = result_one / result_tow
            if f<=1:
                p = int(f * 100)
                return p
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
          return "E"
    elif percentage >=99:
       return "F"
    else:
       return str(percentage) + "%"

if __name__ == "__main__":
    main()

