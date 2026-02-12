import hashlib
import os

def hash_password(password):
    """Securely hashes a password for storage."""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

print("--- SecureVault CLI Tool ---")
pwd = input("Enter a password to secure: ")
print(f"Hashed version for GitHub: {hash_password(pwd).hex()[:50]}...")
