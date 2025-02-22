# Proje hashli değeri kullanıcıdan alıp bir wordlist brute force atıcaksınız.

import hashlib

def hash_sha256(data):
    """SHA-256 hash hesaplama"""
    return hashlib.sha256(data.encode()).hexdigest()

def hash_md5(data):
    """MD5 hash hesaplama"""
    return hashlib.md5(data.encode()).hexdigest()

def brute_force(hash_value, hash_type, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
            for word in wordlist:
                word = word.strip()  #Satırdaki boşlukları temizle
                
                #Hash fonksiyonunu seç
                if hash_type == "sha256":
                    hashed_word = hash_sha256(word)
                elif hash_type == "md5":
                    hashed_word = hash_md5(word)
                else:
                    print("Geçersiz hash türü!")
                    return
                # Eşleşme kontrolü
                if hashed_word == hash_value:
                    print(f"\n Şifre Çözüldü: {word}")
                    return
        print("\n Şifre wordlist içinde bulunamadı!")
    
    except FileNotFoundError:
        print(" Wordlist dosyası bulunamadı!")

if __name__ == "__main__":
    hash_value = input("Lütfen çözmeye çalıştığınız hash değerini girin: ").strip()
    hash_type = input("Hash türünü seçin (sha256 / md5): ").strip().lower()
    wordlist_path = "C:\\Users\\AYÇANUR\\Desktop\\hash fonk\\rockyou.txt"
    
    brute_force(hash_value, hash_type, wordlist_path)