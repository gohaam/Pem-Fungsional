import time
from functools import reduce

# Decorator untuk mengukur waktu eksekusi setiap fungsi
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end_time - start_time:.4f} detik")
        return result
    return wrapper

# Fungsi Registrasi dengan dict comprehension dan decorator
@measure_time
def register(profiles, email, name, password):
    if email in profiles:
        return profiles, "Email sudah terdaftar!"
    
    new_id = len(profiles) + 1
    updated_profiles = {**profiles, email: {'id': new_id, 'name': name, 'password': password, 'role': 'user'}}
    return updated_profiles, "Registrasi berhasil!"

# Fungsi Tambah Roti menggunakan list comprehension dan decorator
@measure_time
def add_bread(breads, name, description, price):
    new_id = len(breads) + 1
    new_bread = {'id': new_id, 'name': name, 'description': description, 'price': price, 'available': True}
    updated_breads = [*breads, new_bread]
    return updated_breads, "Roti berhasil ditambahkan!"

# Closure untuk filter roti yang tidak memiliki id tertentu
def bread_not_id(bread_id):
    return lambda bread: bread['id'] != bread_id

# Fungsi Hapus Roti tanpa lambda, menggunakan closure
@measure_time
def delete_bread(breads, bread_id):
    updated_breads = [bread for bread in breads if bread_not_id(bread_id)(bread)]
    if len(updated_breads) == len(breads):
        return breads, "Roti tidak ditemukan!"
    return updated_breads, "Roti berhasil dihapus!"

# Fungsi untuk cek roti yang tersedia dengan closure
def is_available():
    return lambda bread: bread['available']

# Fungsi Lihat Roti Tersedia menggunakan filter dan decorator
@measure_time
def view_bread_items(breads):
    available_breads = list(filter(is_available(), breads))
    return available_breads if available_breads else "Tidak ada roti yang tersedia saat ini."

# Closure untuk update ketersediaan roti
def update_availability(bread_id):
    return lambda bread: {**bread, 'available': False} if bread['id'] == bread_id else bread

# Fungsi Pesan Roti dengan list comprehension dan decorator
@measure_time
def order_bread(email, breads, orders, bread_id):
    ordered_bread = next((b for b in breads if b['id'] == bread_id and b['available']), None)
    if not ordered_bread:
        return breads, orders, "Roti tidak ditemukan atau sudah dipesan!"

    updated_breads = [update_availability(bread_id)(bread) for bread in breads]
    updated_orders = {**orders, email: orders.get(email, []) + [bread_id]}
    return updated_breads, updated_orders, "Roti berhasil dipesan!"

# Fungsi untuk mendapatkan pesanan berdasarkan id roti
@measure_time
def get_bread_by_id(breads, bread_id):
    return next((bread for bread in breads if bread['id'] == bread_id), None)

# Fungsi Lihat Pesanan dengan filter dan map
@measure_time
def view_orders(email, breads, orders):
    if email not in orders:
        return "Anda belum memesan roti."
    
    ordered_breads = [get_bread_by_id(breads, bread_id) for bread_id in orders[email]]
    return list(filter(None, ordered_breads))

# Fungsi Lihat Semua Pengguna dengan dict comprehension
@measure_time
def view_all_users(profiles):
    return [{"id": v['id'], "email": k, "name": v['name']} for k, v in profiles.items()]

# Fungsi Login Pengguna
@measure_time
def login(profiles, email, password):
    user = profiles.get(email)
    if user and user['password'] == password:
        return email, "Login berhasil!"
    return None, "Login gagal! Email atau password salah."

# Fungsi untuk mengupdate profile pengguna menggunakan decorator
@measure_time
def update_user_profile(profiles, email, name=None, password=None, role=None):
    user = profiles.get(email)
    if not user:
        return profiles, "User tidak ditemukan!"
    
    updated_user = {
        'id': user['id'],
        'name': name if name else user['name'],
        'password': password if password else user['password'],
        'role': role if role else user['role']
    }
    profiles[email] = updated_user
    return profiles, f"Profil {email} berhasil diperbarui!"

# Fungsi untuk mendapatkan roti yang sudah dipesan berdasarkan id
def get_ordered_bread(orders, breads, bread_id):
    return next((bread for bread in breads if bread['id'] == bread_id), None)

# Fungsi untuk melihat status ketersediaan roti berdasarkan id
def check_availability_by_id(breads, bread_id):
    return next((bread for bread in breads if bread['id'] == bread_id and bread['available']), None)

# Fungsi Rekursif untuk mencari roti yang tersedia
def recursive_available_breads(breads):
    if not breads:
        return []
    bread = breads[0]
    rest = recursive_available_breads(breads[1:])
    if bread['available']:
        return [bread] + rest
    return rest

# Data awal
profile = {
    'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
    'wafiq@gmail.com': {'id': 2, 'name': 'wafiq', 'password': '1234', 'role': 'user'},
    'hamdan@gmail.com': {'id': 3, 'name': 'hamdan', 'password': '1234', 'role': 'user'},
    'ilham@gmail.com': {'id': 4, 'name': 'ilham', 'password': '1234', 'role': 'user'}
}

bread_items = [
    {'id': 1, 'name': 'Roti Tawar', 'description': 'Roti tawar lembut', 'price': 15000, 'available': True},
    {'id': 2, 'name': 'Croissant', 'description': 'Croissant renyah', 'price': 25000, 'available': True},
    {'id': 3, 'name': 'Donat', 'description': 'Donat manis dengan topping coklat', 'price': 10000, 'available': True}
]

orders = {}

# Testing Fungsi

# Registrasi pengguna baru
profile, message = register(profile, 'testuser@gmail.com', 'Test User', 'password123')
print(message)

# Update profil pengguna
profile, message = update_user_profile(profile, 'testuser@gmail.com', name="Test User Updated", role="user")
print(message)

# Menambahkan roti baru
bread_items, message = add_bread(bread_items, 'Bagel', 'Bagel empuk dengan isian cream cheese', 20000)
print(message)

# Memesan roti
bread_items, orders, message = order_bread('testuser@gmail.com', bread_items, orders, 1)
print(message)

# Melihat pesanan pengguna
user_orders = view_orders('testuser@gmail.com', bread_items, orders)
print("Pesanan:", user_orders)

# Melihat semua pengguna
all_users = view_all_users(profile)
print("Daftar pengguna:", all_users)

# Hapus roti
bread_items, message = delete_bread(bread_items, 2)
print(message)

# Rekursif melihat roti yang tersedia
recursive_breads = recursive_available_breads(bread_items)
print("Roti yang tersedia (rekursif):", recursive_breads)

# Cek ketersediaan roti berdasarkan id
bread = check_availability_by_id(bread_items, 1)
if bread:
    print(f"Roti dengan ID 1 tersedia: {bread['name']}")
else:
    print("Roti dengan ID 1 tidak tersedia.")

# Melihat roti yang tersedia dengan fungsi filter
available_breads = view_bread_items(bread_items)
print("Roti yang tersedia (dengan filter):", available_breads)

# Login pengguna
email, message = login(profile, 'testuser@gmail.com', 'password123')
print(message)

# Melihat pengguna setelah update profil
all_users = view_all_users(profile)
print("Daftar pengguna setelah update:", all_users)
