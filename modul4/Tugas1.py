import time

# Decorator untuk mengukur waktu eksekusi setiap fungsi
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end_time - start_time:.4f} detik")
        return result
    return wrapper

# Closure untuk menghitung harga roti dengan diskon
def discount_calculator(discount_rate):
    def apply_discount(price):
        return price - (price * discount_rate)
    return apply_discount

# Fungsi registrasi pengguna dengan First-Class Function
@measure_time
def register(profiles, email, name, password):
    if email in profiles:
        return profiles, "Email sudah terdaftar!"
    new_id = len(profiles) + 1
    updated_profiles = {**profiles, email: {'id': new_id, 'name': name, 'password': password, 'role': 'user'}}
    return updated_profiles, "Registrasi berhasil!"

# Fungsi menambah roti menggunakan First-Class Function dan Lambda Expression
@measure_time
def add_bread(breads, name, description, price):
    # Lambda untuk membuat ID roti baru
    new_id = (lambda: len(breads) + 1)()  # Menggunakan lambda untuk ID baru
    new_bread = {'id': new_id, 'name': name, 'description': description, 'price': price, 'available': True}
    updated_breads = [*breads, new_bread]
    return updated_breads, "Roti berhasil ditambahkan!"

# Higher-Order Function: Fungsi yang menggunakan filter dan lambda untuk cek roti yang tersedia
@measure_time
def view_available_breads(breads):
    # filter() adalah built-in higher-order function yang menggunakan lambda untuk mengecek ketersediaan roti
    available_breads = list(filter(lambda bread: bread['available'], breads))
    return available_breads if available_breads else "Tidak ada roti yang tersedia."

# Higher-Order Function: Fungsi yang menggunakan map dan lambda untuk mengupdate harga roti
@measure_time
def update_bread_prices(breads, price_increase):
    # map() adalah built-in higher-order function yang menggunakan lambda untuk menambah harga roti
    updated_breads = list(map(lambda bread: {**bread, 'price': bread['price'] + price_increase}, breads))
    return updated_breads

# Fungsi untuk memesan roti dengan First-Class Function dan Higher-Order Function
@measure_time
def order_bread(email, breads, orders, bread_id):
    ordered_bread = next((bread for bread in breads if bread['id'] == bread_id and bread['available']), None)
    if not ordered_bread:
        return breads, orders, "Roti tidak ditemukan atau sudah dipesan!"
    
    # Higher-Order Function: Menggunakan lambda untuk mengubah status roti
    updated_breads = list(map(lambda bread: {**bread, 'available': False} if bread['id'] == bread_id else bread, breads))
    updated_orders = {**orders, email: orders.get(email, []) + [bread_id]}
    return updated_breads, updated_orders, "Roti berhasil dipesan!"

# Fungsi tambahan untuk menghitung harga dengan diskon menggunakan closure
@measure_time
def apply_discount_to_breads(breads, discount_rate):
    discount_func = discount_calculator(discount_rate)
    updated_breads = [
        {**bread, 'price': discount_func(bread['price'])} for bread in breads
    ]
    return updated_breads, f"Diskon {discount_rate * 100}% telah diterapkan!"

# Data awal (hanya 3 pengguna dan 3 roti untuk kesederhanaan)
profile = {
    'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
    'user1@gmail.com': {'id': 2, 'name': 'User One', 'password': 'userpass', 'role': 'user'},
    'user2@gmail.com': {'id': 3, 'name': 'User Two', 'password': 'userpass', 'role': 'user'}
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

# Menambahkan roti baru
bread_items, message = add_bread(bread_items, 'Bagel', 'Bagel empuk dengan isian cream cheese', 20000)
print(message)

# Melihat roti yang tersedia
available_breads = view_available_breads(bread_items)
print("Roti yang tersedia:", available_breads)

# Memesan roti
bread_items, orders, message = order_bread('testuser@gmail.com', bread_items, orders, 1)
print(message)

# Melihat pesanan pengguna
user_orders = orders.get('testuser@gmail.com', [])
print("Pesanan pengguna:", user_orders)

# Mengupdate harga roti
bread_items = update_bread_prices(bread_items, 5000)
print("Harga roti setelah update:", bread_items)

# Menghitung harga roti setelah diskon
bread_items, discount_message = apply_discount_to_breads(bread_items, 0.1)
print(discount_message)
print("Harga roti setelah diskon:", bread_items)
