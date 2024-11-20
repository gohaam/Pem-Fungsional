from functools import reduce

def baris_aritmetika_geometri(a, d, r, n):
    if n == 1:
        return [a]
    else:
        # Menghasilkan baris hingga suku ke-n secara rekursif
        deret = baris_aritmetika_geometri(a, d, r, n - 1)
        # Menghitung suku ke-n berdasarkan rumus
        suku_ke_n = (a + (n - 1) * d) * (r ** (n - 1))
        deret.append(suku_ke_n)
        return deret

# Meminta input dari pengguna
a = int(input("Masukkan suku pertama (a): "))
d = int(input("Masukkan beda aritmetika (d): "))
r = int(input("Masukkan rasio geometri (r): "))
n = int(input("Masukkan jumlah suku (n): "))

# Menghasilkan deret
hasil = baris_aritmetika_geometri(a, d, r, n)
print("Deret aritmetika-geometri:", hasil)

jumlah_deret = sum(hasil)
print("Jumlah deret:", jumlah_deret)
