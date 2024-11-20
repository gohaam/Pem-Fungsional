import time
import math

# Decorator untuk mengukur waktu eksekusi
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end_time - start_time:.4f} detik")
        return result
    return wrapper

# 1. Mengubah input menjadi pasangan titik (x, y)
@measure_time
def parse_input(input_string):
    # Mengubah string menjadi list of integers
    data = list(map(int, input_string.split(',')))
    
    # Mengecek jika jumlah elemen ganjil
    if len(data) % 2 != 0:
        raise ValueError("Jumlah elemen harus genap untuk membentuk pasangan (x, y).")
    
    # Membentuk pasangan titik (x, y)
    points = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    return points

# 2. Fungsi Transformasi

# Fungsi translasi
def translate(tx, ty):
    def apply(point):
        x, y = point
        return x + tx, y + ty
    return apply

# Fungsi rotasi
def rotate(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_theta, sin_theta = math.cos(angle_radians), math.sin(angle_radians)
    def apply(point):
        x, y = point
        return x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta
    return apply

# Fungsi dilatasi
def scale(factor):
    def apply(point):
        x, y = point
        return x * factor, y * factor
    return apply

# 3. Melakukan Transformasi dengan HoF
@measure_time
def apply_transformation(points, transformation):
    return list(map(transformation, points))

# 4. Membulatkan hasil ke dua angka di belakang koma
def format_points(points):
    return [(round(x, 2), round(y, 2)) for x, y in points]

# 5. Implementasi Transformasi Berdasarkan Soal
def main():
    # Input user
    input_string = input("Masukkan koordinat (x,y) dipisahkan dengan koma, misalnya '1,2,3,4,5,6': ")
    
    try:
        points = parse_input(input_string)
        print("Titik awal:", points)

        # Transformasi 1: Translasi dengan tx=3 dan ty=7
        translated_points = apply_transformation(points, translate(3, 7))
        print("Setelah translasi (tx=3, ty=7):", format_points(translated_points))

        # Transformasi 2: Rotasi sebesar 60 derajat
        rotated_points = apply_transformation(translated_points, rotate(60))
        print("Setelah rotasi 60 derajat:", format_points(rotated_points))

        # Transformasi 3: Dilatasi dengan faktor skala 1.5
        scaled_points = apply_transformation(rotated_points, scale(1.5))
        print("Setelah dilatasi (skala=1.5):", format_points(scaled_points))

    except ValueError as e:
        print("Error:", e)

# Menjalankan program
if __name__ == "__main__":
    main()
