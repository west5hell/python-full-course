# Python string methods

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")

# result = len(name)
# result = name.find("X")
# result = name.rfind("e")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")

# print(result)


# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("username is no more than 12 characters")
elif not username.find(" ") == -1:
    print("username must not contain spaces")
elif not username.isalpha():
    print("username must not contain digits")
else:
    print(f"Welcome {username}")
