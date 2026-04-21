from validator_collection import validators
from hashlib import sha256
from random import randint
from datetime import date
import csv
import sys
import os
import re

def main():
    print("\nSafe Box Password Manager\n")
    while True:
        write_read = input("Enter S to save your safeboxes passwords or V to see your saved safeboxes passwords: ").strip().lower()
        if write_read == "s" or write_read == "v":
            break
        else:
            print("Invalid Input!\nTry again!\n")

    if write_read == "s":
        save()
    if write_read == "v":
        view()

def save():
    while True:
        email = input("Email: ").strip().lower()
        if email_format(email):
            break
        else:
            print("Invalid Email!\nTry again!\n")

    file_name, _ = email.split("@")
    full_name = input("Full Name: ").strip().lower()
    while True:
        birth_date = input("Date of Birth: ").strip()
        if birth_date_format(birth_date):
            break
        else:
            print("Invalid Date: Your date should be in YYYY-MM-DD format.\nTry again!\n")

    father_name = input("Father's Name: ").strip().lower()
    with open(f"{file_name}.csv", "w") as file:
        file.write(f"{email},{full_name},{birth_date},{father_name}\n")

    while True:
        try:
            safeboxes = int(input("How many safeboxes do you have? ").strip())
            break
        except:
            print("Invalid Input: Enter an integer.\nTry again!\n")

    print("\nEnter their passwords.")
    for i in range(safeboxes):
        while True:
            password = input(f"Safebox {i+1}: ").strip()
            if password_format(password):
                break
            else:
                print("Invalid Password: Your password should be 4 digits.\nTry again!\n")

        with open(f"{file_name}.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["safebox", "password"])
                writer.writerow({"safebox": i+1, "password": sha256(password.encode('utf-8')).hexdigest()})

    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit("Passwords saved in high security format!")

def view():
    while True:
        email = input("Email: ").strip().lower()
        if email_format(email):
            file_name, _ = email.split("@")
            if os.path.isfile(f"{file_name}.csv"):
                with open(f"{file_name}.csv", "r") as file:
                    reader = csv.reader(file)
                    row1 = next(reader)
                    saved_email = row1[0]
                    saved_full_name = row1[1]
                    saved_birth_date = row1[2]
                    saved_father_name = row1[3]
                if email == saved_email:
                    break
                else:
                    print("Wrong Email!\nTry again!\n")
            else:
                print("Your email does not exist!\nTry again!\n")
                save_input = input("Did you save your safeboxes passwords before?(yes/no) ").strip().lower()
                if save_input == "no":
                    save()
                    break
        else:
            print("Invalid Email!\nTry again!\n")

    while True:
        full_name = input("Full Name: ").strip().lower()
        if full_name == saved_full_name:
            break
        else:
            print("Wrong Name!\nTry again!\n")

    while True:
        birth_date = input("Date of Birth: ").strip()
        if birth_date_format(birth_date):
            if birth_date == saved_birth_date:
                break
            else:
                print("Wrong Date!\nTry again!\n")
        else:
            print("Invalid Date: Your date should be in YYYY-MM-DD format.\nTry again!\n")

    while True:
        father_name = input("Father's Name: ").strip().lower()
        if father_name == saved_father_name:
            break
        else:
            print("Wrong Name!\nTry again!\n")

    print("\nHuman Test")
    while True:
        try:
            x = randint(0, 9)
            y = randint(0, 9)
            answer = int(input(f"{x} + {y} = "))
            if answer == y + x:
                break
            else:
                print("Wrong Answer!\nTry again!\n")
        except:
            print("Invalid Input: Enter an integer.\nTry again!\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    first_name, _ = full_name.split(" ")
    print(f"Hello {first_name.title()}!")
    safeboxes = []
    passwords = []
    with open(f"{file_name}.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["safebox", "password"])
        for row in reader:
            safeboxes.append(row["safebox"])
            passwords.append(row["password"])

    del safeboxes[0]
    del passwords[0]
    safeboxes = [int(x) for x in safeboxes]
    view_input = "y"
    while view_input == "y" or view_input == "yes":
        try:
            safebox = int(input("Which safebox password do you want? "))
            if safebox in safeboxes:
                hash_to_password = {}
                for p in range(1,10000):
                    hashing_number = sha256(b'%i'% p).hexdigest()
                    hash_to_password[hashing_number] = p

                print(f"Safebox {safebox}: {hash_to_password[passwords[safebox-1]]}\n")
                view_input = input("Do you want another safebox password?(yes/no) ").strip().lower()
            else:
                raise ValueError
        except:
            print("Wrong Input: Enter the number of your needed safebox.\nTry again!\n")

    sys.exit()

def email_format(email):
    try:
        if validators.email(email):
            return True
    except:
        return False

def birth_date_format(birth_date):
    try:
        if date.fromisoformat(birth_date):
            return True
    except:
        return False

def password_format(password):
    try:
        if re.search(r"^[0-9]{4}$", password):
            return True
        else:
            raise ValueError
    except:
        return False

if __name__ == "__main__":
    main()