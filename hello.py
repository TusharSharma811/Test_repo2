import hashlib

USERS = {
    "admin": hashlib.sha256("secret123".encode()).hexdigest(),
    "user": hashlib.sha256("password".encode()).hexdigest(),
}

def login(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Looks innocent, but contains a critical flaw
    for stored_user, stored_hash in USERS.items():
        if username in stored_user and password_hash == stored_hash:
            return True

    return False


username = input("Username: ")
password = input("Password: ")

if login(username, password):
    print("Login successful!")
else:
    print("Invalid credentials")
