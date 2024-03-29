def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
def main():
    user=input("How are you felling right now?: ")
    convert_text=convert(user)
    print(f"Your felling right now {convert_text}")

main()
