def check_input(input_str):
    if input_str == '42':
        return 'Yes'
    elif input_str.lower() == 'forty two' or input_str.lower() == 'forty-two':
        return 'Yes'
    else:
        return 'No'

user_input = input("Enter a number or its textual representation: ").strip()
result = check_input(user_input)
print(result)
