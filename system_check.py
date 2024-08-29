def login(username, password):
    
    if username == "dennis" and password == "alumas123":
        return True
    else:
        return False

def main():
    print("Welcome to the Secure System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login(username, password):
        print("Login successful! System secure!, {}!".format(username))
        
    else:
        print("Login failed. Invalid username or password.")
        # In a real system, you'd want to compare against a database of usernames and hashed passwords
if __name__ == "__main__":
    main()





