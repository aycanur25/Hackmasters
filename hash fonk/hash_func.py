# Hash fonksiyonu

import random
import struct

def left_rotate(value, shift):
    """32-bit sola döndürme (bitwise rotation)"""
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def custom_strong_hash(data, salt=None, rounds=5):
    """Güçlü özel hash fonksiyonu"""
    
    # Rastgele bir salt ekleyelim (yoksa)
    if salt is None:
        salt = struct.pack("<I", random.randint(0, 0xFFFFFFFF)).hex()

    # Başlangıç hash değeri (sabit bir seed)
    hash_value = 0xA1B2C3D4  

    # Veriyi byte dizisine çevir
    data = (salt + data).encode()

    for _ in range(rounds):  # Birden fazla hashleme turu
        for char in data:
            hash_value = (hash_value ^ ord(char)) & 0xFFFFFFFF  # XOR işlemi
            hash_value = left_rotate(hash_value, 5)  # Bitwise rotation ekleme
            hash_value = (hash_value * 33) & 0xFFFFFFFF  # Sabit bir çarpan ile karıştırma
        
        # Yeni bir tur için string'e çevirerek tekrar işle
        data = hex(hash_value)[2:].encode()

    return hex(hash_value)[2:], salt  # Hash çıktısı ve kullanılan salt

# Test
user_input = input("Lütfen hash'lemek istediğiniz metni girin: ")
hashed_value, used_salt = custom_strong_hash(user_input)

print(f"🔒 Güçlü Hash: {hashed_value}")
print(f"🧂 Kullanılan Salt: {used_salt}")