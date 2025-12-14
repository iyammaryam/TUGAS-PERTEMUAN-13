nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_data = 0

for n in nilai:
    try:
        # Coba menjumlahkan nilai
        total += n
        jumlah_data += 1
    except TypeError:
        # Lewati data yang bukan angka
        print(f"Data '{n}' bukan angka, dilewati.")

# Hitung dan tampilkan rata-rata
if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print("Rata-rata nilai valid:", rata_rata)
else:
    print("Tidak ada data nilai yang valid.")