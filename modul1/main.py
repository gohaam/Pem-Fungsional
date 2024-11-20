# Data profil pengguna (email -> {name, password, role})
profile = {
    'admin@gmail.com': {'id': 1, 'name': 'Admin', 'password': 'adminpass', 'role': 'admin'},
    'wafiq@gmail.com' : {'id': 2, 'name': 'wafiq', 'password': '1234', 'role': 'user'},
    'hamdan@gmail.com' : {'id': 3, 'name': 'hamdan', 'password': '1234', 'role': 'user'},
    'ilham@gmail.com' : {'id': 4, 'name': 'ilham', 'password': '1234', 'role': 'user'}
}

# Data roti yang tersedia (list of dictionaries)
bread_items = [
    {'id': 1, 'name': 'Roti Tawar', 'description': 'Roti tawar lembut', 'price': 15000, 'available': True},
    {'id': 2, 'name': 'Croissant', 'description': 'Croissant renyah', 'price': 25000, 'available': True},
    {'id': 3, 'name': 'Donat', 'description': 'Donat manis dengan topping coklat', 'price': 10000, 'available': True},
]

# Data kategori roti (tuple)    
bread_categories = ('Manis', 'Gurih', 'Roti Tawar')

# Data pemesanan (dictionary: email -> list of bread item ids)
orders = {}

def register():
    email = input("Masukkan email: ")
    if email in profile:
        print("Email sudah terdaftar! Silakan login.")
        return None
    name = input("Masukkan nama: ")
    password = input("Masukkan Password: ")

    new_id = len(profile) + 1  # Membuat ID unik berdasarkan jumlah akun yang ada
    profile[email] = {'id': new_id, 'name': name, 'password': password, 'role': 'user'}
    
    print("Registrasi berhasil!")
    return email

def view_bread_categories():
    print("\nKategori Roti:")
    for category in bread_categories:
        print(f"- {category}")

# Fungsi untuk menambah roti (hanya untuk admin)
def add_bread():
    name = input("Masukkan nama roti: ")
    description = input("Masukkan deskripsi roti: ")
    price = int(input("Masukkan harga roti: "))
    new_id = len(bread_items) + 1
    bread_items.append({'id': new_id, 'name': name, 'description': description, 'price': price, 'available': True})
    print("Roti berhasil ditambahkan!")

# Fungsi untuk menghapus roti (hanya untuk admin)
def delete_bread():
    bread_id = int(input("Masukkan ID roti yang ingin dihapus: "))
    for bread in bread_items:
        if bread['id'] == bread_id:
            bread_items.remove(bread)
            print("Roti berhasil dihapus!")
            return
    print("Roti tidak ditemukan!")

# Fungsi untuk melihat semua akun (untuk admin)
def view_all_users():
    print("\nDaftar Akun:")
    for email, details in profile.items():
        print(f"ID: {details['id']}, Email: {email}, Nama: {details['name']}")

# Fungsi login menggunakan profile data
def login():
    email = input("Masukkan email: ")
    password = input("Masukkan Password: ")
    if email in profile and profile[email]['password'] == password:
        print("Login berhasil!")
        return email
    else:
        print("Login gagal! Email atau password salah.")
        return None

# Fungsi untuk melihat profil (hanya admin)
def view_profile(email):
    if email in profile and profile[email]['role'] == 'admin':
        print("\nProfil Anda:")
        for user_email in profile:
            print(f"Email: {user_email}, Nama: {profile[user_email]['name']}")
    else:
        print("Anda tidak memiliki izin untuk melihat profil.")

# Fungsi untuk mengedit profil (hanya admin)
def edit_profile():
    email = input("Masukkan email pengguna yang ingin diedit: ")
    if email in profile:
        name = input("Masukkan nama baru: ")
        profile[email]['name'] = name
        print("Profil berhasil diupdate!")
    else:
        print("Profil tidak ditemukan!")

# Fungsi untuk menampilkan semua roti yang tersedia
def view_bread_items():
    print("\nDaftar Roti:")
    available_breads = [bread for bread in bread_items if bread['available']]
    if available_breads:
        for bread in available_breads:
            print(f"ID: {bread['id']}, Nama: {bread['name']}, Deskripsi: {bread['description']}, Harga: {bread['price']}")
    else:
        print("Tidak ada roti yang tersedia saat ini.")

# Fungsi untuk memesan roti
def order_bread(email):
    view_bread_items()
    bread_id = int(input("Masukkan ID roti yang ingin dipesan: "))
    for bread in bread_items:
        if bread['id'] == bread_id and bread['available']:
            bread['available'] = False  # Tandai roti sebagai sudah dipesan
            if email not in orders:
                orders[email] = []
            orders[email].append(bread_id)
            print("Roti berhasil dipesan!")
            return
    print("Roti tidak ditemukan atau sudah dipesan!")

# Fungsi untuk melihat roti yang sudah dipesan
def view_orders(email):
    if email in orders:
        print("\nDaftar roti yang dipesan:")
        for bread_id in orders[email]:
            bread = next((b for b in bread_items if b['id'] == bread_id), None)
            if bread:
                print(f"ID: {bread['id']}, Nama: {bread['name']}, Deskripsi: {bread['description']}, Harga: {bread['price']}")
    else:
        print("Anda belum memesan roti.")

# Menu utama
def main():
    while True:
        print("\n========================")
        print("WELLCOME TOTOKO ROTI APP SIMULATOR")
        print("========================")
        print("1. Registrasi")
        print("2. Login")
        print("3. Lihat Kategori Roti")
        print("4. Keluar")
        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            register()
        elif choice == '2':
            user_email = login()
            if user_email:
                if profile[user_email]['role'] == 'admin':
                    while True:
                        print("\nMenu Admin:")
                        print("1. Lihat Profil Semua Pengguna")
                        print("2. Edit Profil Pengguna")
                        print("3. Lihat Roti")
                        print("4. Tambah Roti")
                        print("5. Hapus Roti")
                        print("6. Logout")
                        admin_choice = input("Pilih opsi (1-6): ")

                        if admin_choice == '1':
                            view_profile(user_email)
                        elif admin_choice == '2':
                            edit_profile()
                        elif admin_choice == '3':
                            view_bread_items()
                        elif admin_choice == '4':
                            add_bread()
                        elif admin_choice == '5':
                            delete_bread()
                        elif admin_choice == '6':
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid! Silakan pilih lagi.")
                else:
                    while True:
                        print("\nMenu Pengguna:")
                        print("1. Lihat Daftar Semua Pengguna")
                        print("2. Lihat Roti")
                        print("3. Pesan Roti")
                        print("4. Lihat Pesanan")
                        print("5. Logout")
                        user_choice = input("Pilih opsi (1-5): ")

                        if user_choice == '1':
                            view_all_users()
                        elif user_choice == '2':
                            view_bread_items()
                        elif user_choice == '3':
                            order_bread(user_email)
                        elif user_choice == '4':
                            view_orders(user_email)
                        elif user_choice == '5':
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid! Silakan pilih lagi.")
        elif choice == '3':
            view_bread_categories()
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih lagi.")

if __name__ == "__main__":
    main()