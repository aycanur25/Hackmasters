import struct

# MD5'te kullanılan sabitler (sinüs fonksiyonundan türetilmiş)
S = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
K = [int(2**32 * abs(__import__("math").sin(i + 1))) for i in range(64)]

def left_rotate(x, c):
    """32-bit döndürme işlemi"""
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    """MD5 hash hesaplama fonksiyonu"""
    # Başlangıçta kullanılan 4 sabit değer
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    
    # Padding (512-bit'lik bloklara ayırma)
    original_length = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80' + b'\x00' * ((56 - (len(message) + 1) % 64) % 64) + struct.pack('<Q', original_length)
    
    # Her 512-bit (64 byte) blok için işlem yap
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        M = list(struct.unpack('<16I', chunk))
        
        a, b, c, d = A, B, C, D
        
        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            f = (f + a + K[j] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, S[j])) & 0xFFFFFFFF

        A, B, C, D = (A + a) & 0xFFFFFFFF, (B + b) & 0xFFFFFFFF, (C + c) & 0xFFFFFFFF, (D + d) & 0xFFFFFFFF

    return ''.join(format(x, '08x') for x in [A, B, C, D])

# Test
data = input("hashlenecek girdi: ").encode()
print("MD5 Hash:", md5(data))
