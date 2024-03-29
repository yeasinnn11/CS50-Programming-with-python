def camel_to_snake_case(camel_case_str):
    words = []
    start_index = 0

    for i in range(1, len(camel_case_str)):
        if camel_case_str[i].isupper():
            words.append(camel_case_str[start_index:i])
            start_index = i

    words.append(camel_case_str[start_index:])
    snake_case_str = '_'.join(words).lower()
    return snake_case_str

def main():
    camel_case_input = input("camelCase: ")
    snake_case_output = camel_to_snake_case(camel_case_input)
    print("snake_case:", snake_case_output)

if __name__ == "__main__":
    main()


