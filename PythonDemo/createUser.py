import random
import subprocess


def check_password(password: str) -> bool:
    contains_char = False
    contains_number = False
    contains_special_char = False
    for letter in password:
        if letter.isdigit():
            if contains_char * contains_special_char:
                return True
            contains_number = True
        elif letter.isalpha():
            if contains_number * contains_special_char:
                return True
            contains_char = True
        else:
            if contains_number * contains_char:
                return True
            contains_special_char = True
    return False


def generate_password():
    min_password_length = 8
    ascii_min = 33
    ascii_max = 126
    password = "".join(
        [chr(random.randint(ascii_min, ascii_max)) for _ in range(min_password_length)]
    )
    while not check_password(password):
        password += chr(random.randint(ascii_min, ascii_max))
    return password


password = generate_password()
user_name = input("Please input a username for the new user.\n")
subprocess.run(["sudo", "useradd", "-m", user_name ,"-p", password])
print(password)
delete_user = input("Delete User?.\n")
if delete_user:
    subprocess.run(["sudo", "userdel", "-fr", user_name])


print("Done")
