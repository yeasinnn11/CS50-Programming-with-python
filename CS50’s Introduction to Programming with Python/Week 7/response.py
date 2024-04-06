from validator_collection import validators # type: ignore

def main():
    user_email=input("What's your email address? ")
    try:
        emailIsValid = validators.email(user_email)
        print("Valid")
    except:
        print("Invalid")

if __name__=='__main__':
    main()
