#  Proje hash fonksiyonlarını kullanarak girdileri hashleyeceksiniz.

import hashlib

def hash_sha256(data):
    """SHA-256 hash hesaplama fonksiyonu"""
    return hashlib.sha256(data.encode()).hexdigest()

def hash_md5(data):
    """MD5 hash hesaplama fonksiyonu"""
    return hashlib.md5(data.encode()).hexdigest()

if __name__ == "__main__":
    user_input = input("Lütfen hash'lemek istediğiniz metni girin: ")
    
    sha256_hash = hash_sha256(user_input)
    md5_hash = hash_md5(user_input)

    print(f"\nSHA-256 Hash: {sha256_hash}")
    print(f"MD5 Hash: {md5_hash}")