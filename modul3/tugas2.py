from functools import reduce

# Fungsi Registrasi menggunakan update dict comprehension
def register(profiles, email, name, password):
    if email in profiles:
        return profiles, "Email sudah terdaftar!"
    
    new_id = len(profiles) + 1
    updated_profiles = {**profiles, email: {'id': new_id, 'name': name, 'password': password, 'role': 'user'}}
    return updated_profiles, "Registrasi berhasil!"

# Fungsi Tambah Roti menggunakan list comprehension
def add_bread(breads, name, description, price):
    new_id = len(breads) + 1
    new_bread = {'id': new_id, 'name': name, 'description': description, 'price': price, 'available': True}
    updated_breads = [*breads, new_bread]
    return updated_breads, "Roti berhasil ditambahkan!"

# Fungsi untuk filter roti yang tidak memiliki id tertentu
def bread_not_id(bread, bread_id):
    return bread['id'] != bread_id

# Fungsi Hapus Roti tanpa lambda
def delete_bread(breads, bread_id):
    updated_breads = [bread for bread in breads if bread_not_id(bread, bread_id)]  # Menggunakan list comprehension
    if len(updated_breads) == len(breads):
        return breads, "Roti tidak ditemukan!"
    return updated_breads, "Roti berhasil dihapus!"

# Fungsi untuk cek roti yang tersedia
def is_available(bread):
    return bread['available']

# Fungsi Lihat Roti Tersedia menggunakan filter
def view_bread_items(breads):
    available_breads = list(filter(is_available, breads))
    return available_breads if available_breads else "Tidak ada roti yang tersedia saat ini."

# Fungsi update ketersediaan roti
def update_availability(bread, bread_id):
    return {**bread, 'available': False} if bread['id'] == bread_id else bread

# Fungsi Pesan Roti tanpa lambda
def order_bread(email, breads, orders, bread_id):
    ordered_bread = next((b for b in breads if b['id'] == bread_id and b['available']), None)
    if not ordered_bread:
        return breads, orders, "Roti tidak ditemukan atau sudah dipesan!"

    updated_breads = [update_availability(bread, bread_id) for bread in breads]  # Menggunakan list comprehension
    updated_orders = {**orders, email: orders.get(email, []) + [bread_id]}
    return updated_breads, updated_orders, "Roti berhasil dipesan!"

# Fungsi untuk mendapatkan pesanan berdasarkan id roti
def get_bread_by_id(breads, bread_id):
    return next((bread for bread in breads if bread['id'] == bread_id), None)

# Fungsi Lihat Pesanan menggunakan map
def view_orders(email, breads, orders):
    if email not in orders:
        return "Anda belum memesan roti."
    
    ordered_breads = [get_bread_by_id(breads, bread_id) for bread_id in orders[email]]
    return list(filter(None, ordered_breads))

# Fungsi Lihat Semua Pengguna menggunakan dict comprehension
def view_all_users(profiles):
    return [{"id": v['id'], "email": k, "name": v['name']} for k, v in profiles.items()]

# Fungsi Login Pengguna
def login(profiles, email, password):
    user = profiles.get(email)
    if user and user['password'] == password:
        return email, "Login berhasil!"
    return None, "Login gagal! Email atau password salah."

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

# Program utama
def main():
    current_profiles = profile
    current_breads = bread_items
    current_orders = orders

    while True:
        print("\n========================")
        print("WELLCOME TOTOKO ROTI APP SIMULATOR")
        print("========================")
        print("1. Registrasi")
        print("2. Login")
        print("3. Lihat Roti")
        print("4. Keluar")
        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            email = input("Email: ")
            name = input("Nama: ")
            password = input("Password: ")
            current_profiles, message = register(current_profiles, email, name, password)
            print(message)

        elif choice == '2':
            email = input("Email: ")
            password = input("Password: ")
            user_email, message = login(current_profiles, email, password)
            print(message)

            if user_email:
                user_role = current_profiles[user_email]['role']
                if user_role == 'admin':
                    while True:
                        print("\nMenu Admin:")
                        print("1. Lihat Semua Pengguna")
                        print("2. Tambah Roti")
                        print("3. Hapus Roti")
                        print("4. Logout")
                        admin_choice = input("Pilih opsi (1-4): ")

                        if admin_choice == '1':
                            users = view_all_users(current_profiles)
                            for user in users:
                                print(f"ID: {user['id']}, Email: {user['email']}, Nama: {user['name']}")

                        elif admin_choice == '2':
                            name = input("Nama Roti: ")
                            description = input("Deskripsi: ")
                            price = int(input("Harga: "))
                            current_breads, message = add_bread(current_breads, name, description, price)
                            print(message)

                        elif admin_choice == '3':
                            bread_id = int(input("ID Roti: "))
                            current_breads, message = delete_bread(current_breads, bread_id)
                            print(message)

                        elif admin_choice == '4':
                            print("Logout berhasil.")
                            break

                else:  # Menu untuk user biasa
                    while True:
                        print("\nMenu Pengguna:")
                        print("1. Lihat Roti")
                        print("2. Pesan Roti")
                        print("3. Lihat Pesanan")
                        print("4. Logout")
                        user_choice = input("Pilih opsi (1-4): ")

                        if user_choice == '1':
                            breads = recursive_available_breads(current_breads)
                            if not breads:
                                print("Tidak ada roti yang tersedia saat ini.")
                            else:
                                for bread in breads:
                                    print(f"ID: {bread['id']}, Nama: {bread['name']}, Harga: {bread['price']}")

                        elif user_choice == '2':
                            bread_id = int(input("ID Roti: "))
                            current_breads, current_orders, message = order_bread(user_email, current_breads, current_orders, bread_id)
                            print(message)

                        elif user_choice == '3':
                            orders_list = view_orders(user_email, current_breads, current_orders)
                            if isinstance(orders_list, str):
                                print(orders_list)
                            else:
                                for order in orders_list:
                                    print(f"ID: {order['id']}, Nama: {order['name']}, Harga: {order['price']}")

                        elif user_choice == '4':
                            print("Logout berhasil.")
                            break

        elif choice == '3':
            breads = recursive_available_breads(current_breads)
            if not breads:
                print("Tidak ada roti yang tersedia saat ini.")
            else:
                for bread in breads:
                    print(f"ID: {bread['id']}, Nama: {bread['name']}, Harga: {bread['price']}")

        elif choice == '4':
            print("Keluar dari program.")
            break

if __name__ == "__main__":
    main()
