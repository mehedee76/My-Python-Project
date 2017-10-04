password = ''
while password != 'python123':
    password = input("Enter your password: ")
    if password == 'python123':
        print("Login Successful")
    else:
        print("Password incorrect.. retry")
