correct_username = "hello"
correct_password = "123abc"

max_attempts = 3

for attempt in range(1, max_attempts + 1):
    username = input("Enter username:")
    password = input("Enter password:")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password")

        remaining = max_attempts - attempt
        if remaining > 0:
            print("Attempts left:", remaining)
        else:
            print("Account locked! Too many failed attempts.")