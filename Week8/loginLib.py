import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hash_password(password: str) -> str:
    """Hash a password with MD5 and return hex digest."""
    return hashlib.md5(password.encode()).hexdigest()

def register(username: str, password: str) -> None:
    """Register a new user and append to the credentials file."""
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            lines = f.readlines()
            user_id = len(lines)
    except FileNotFoundError:
        lines = []
        user_id = 0

    hashed = hash_password(password)
    with open(CREDENTIALS_FILE, "a") as f:
        f.write(f"{user_id}{DELIMITER}{username}{DELIMITER}{hashed}\n")

def login(username: str, password: str) -> bool:
    """Check if username and password match."""
    hashed = hash_password(password)
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(DELIMITER)
                if len(parts) != 3:
                    continue
                _, user, pwd = parts
                if username == user and hashed == pwd:
                    return True
    except FileNotFoundError:
        return False
    return False

def viewProfile(username: str):
    """Return [user_id, username] for the given username."""
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(DELIMITER)
                if len(parts) != 3:
                    continue
                user_id, user, _ = parts
                if username == user:
                    return [user_id, user]
    except FileNotFoundError:
        return None
    return None

def change_password(username: str, new_password: str) -> None:
    """Update the password for a user."""
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    new_hashed = hash_password(new_password)
    updated = []
    for line in lines:
        parts = line.strip().split(DELIMITER)
        if len(parts) != 3:
            continue
        user_id, user, pwd = parts
        if user == username:
            updated.append(f"{user_id}{DELIMITER}{user}{DELIMITER}{new_hashed}\n")
        else:
            updated.append(line)

    with open(CREDENTIALS_FILE, "w") as f:
        f.writelines(updated)
