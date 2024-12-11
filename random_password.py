import string
import random

# Define the function to generate a secure password
LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTUAUTO = string.punctuation


# hàm dùng để kiểm tra độ dài kí tự đã nhập
def check_length_of_string():
    while True:
        length = int(input("Enter the length of the password: "))
        if length < 8:
            print(f"Password length should be at least 8.")
            continue
        else:
            break
    return int(length)
        


def generate_password(length_of_string):
    # Define the character sets
    printable = f'{LETTER}:{NUMBER}:{PUNCTUAUTO}' # nối các kí tự lại với nhau

    printable = list(printable) # đưa các kí tự đã khai báo về dạng list
    random.shuffle(printable) # đảo trộn các kí tự

    random_password = random.choices(printable,k=length_of_string)
    random_password = ''.join(random_password) # để nối lại thành chuỗi kí tự
    return random_password


def main():
    print(f"Asci Letter is {LETTER}")
    print(f"Number Letter is {NUMBER}")
    print(f"Punctuauto Letter is {PUNCTUAUTO}")
    print("\n")
    length = check_length_of_string()
    password = generate_password(length)
    print(password)


if __name__ == "__main__":
    main()