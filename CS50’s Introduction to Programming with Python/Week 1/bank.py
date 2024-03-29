def bank():
    greething = input("Enter a Greething: ").strip().lower()
    if greething.startswith("hello"):
        print("$0")
    elif greething.startswith("h"):
        print("$20")
    else:
        print("$100")
bank()
