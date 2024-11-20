# Data penjualan barang dengan informasi ID produk, nama produk, harga, jumlah terjual, dan tanggal penjualan
data_penjualan = [
    {"product_id": "GN101", "product_name": "Laptop", "price": 7000000, "quantity": 2, "date": "2024-08-01"},
    {"product_id": "GN102", "product_name": "Mouse", "price": 150000, "quantity": 5, "date": "2024-08-01"},
    {"product_id": "GN103", "product_name": "Keyboard", "price": 300000, "quantity": 3, "date": "2024-08-01"},
    {"product_id": "GN201", "product_name": "Monitor", "price": 2000000, "quantity": 1, "date": "2024-08-02"},
    {"product_id": "GN202", "product_name": "Flash Drive", "price": 50000, "quantity": 10, "date": "2024-08-02"},
    {"product_id": "GN203", "product_name": "Printer", "price": 1000000, "quantity": 2, "date": "2024-08-02"},
    {"product_id": "GN301", "product_name": "Desk Chair", "price": 850000, "quantity": 4, "date": "2024-08-03"},
    {"product_id": "GN302", "product_name": "Desk", "price": 2000000, "quantity": 1, "date": "2024-08-03"},
    {"product_id": "GN303", "product_name": "Lamp", "price": 300000, "quantity": 6, "date": "2024-08-03"},
    {"product_id": "GN401", "product_name": "Phone", "price": 5000000, "quantity": 1, "date": "2024-08-04"},
    {"product_id": "GN402", "product_name": "Headphones", "price": 800000, "quantity": 2, "date": "2024-08-04"},
    {"product_id": "GN403", "product_name": "Smartwatch", "price": 1500000, "quantity": 3, "date": "2024-08-04"}
]

# Fungsi pure untuk menghitung pendapatan
def hitung_pendapatan(data):
    try:
        return [
            {**entry, "total_income": entry["price"] * entry["quantity"]}
            for entry in data
        ]
    except Exception as e:
        return str(e)

# Fungsi pure untuk menghitung rata-rata penjualan
def average_penjualan(data, tanggal):
    try:
        sales_on_date = [item["quantity"] for item in data if item["date"] == tanggal]
        if not sales_on_date:
            raise ValueError(f"Tanggal '{tanggal}' tidak ditemukan atau format tidak sesuai.")
        avg_sales = sum(sales_on_date) / len(sales_on_date)
        return round(avg_sales, 2)
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)

# Fungsi generator untuk menghasilkan total penjualan
def total_penjualan(data):
    for item in data:
        try:
            total = item["price"] * item["quantity"]
            yield {
                "date": item["date"],
                "product_id": item["product_id"],
                "product_name": item["product_name"],
                "total_income": total
            }
        except Exception as e:
            yield str(e)

# Fungsi pembantu untuk menampilkan hasil dari generator
def print_total_penjualan(generator):
    for item in generator:
        print(item)

# Sistem Menu
def menu():
    data_pendapatan = hitung_pendapatan(data_penjualan)
    while True:
        print("\nSistem Pengelolaan Data Penjualan")
        print("1. Hitung Pendapatan")
        print("2. Rata-rata Penjualan")
        print("3. Total Penjualan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            for item in data_pendapatan:
                print(item)
        elif pilihan == "2":
            tanggal_input = input("Masukkan tanggal (format: YYYY-MM-DD): ")
            hasil = average_penjualan(data_penjualan, tanggal_input)
            print(f"\nRata-rata penjualan pada tanggal {tanggal_input}: {hasil}")
        elif pilihan == "3":
            print("\nTotal Penjualan per Produk:")
            print_total_penjualan(total_penjualan(data_pendapatan))
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.\n")

# Menjalankan Menu
menu()