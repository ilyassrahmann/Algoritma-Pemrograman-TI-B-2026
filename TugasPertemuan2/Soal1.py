'''
Buat sebuah fungsi bernama rata rata(nilai) yang:
1. Menerima sebuah list berisi nilai mahasiswa
2. Menghitung rata-rata nilai
3. Jika list kosong, kembalikan pesan: "Data kosong"
Kemudian:
1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
2. Tampilkan hasilnya
'''

def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    else:
        total = sum(nilai)
        rata = total / len(nilai)
        return rata

# Pemanggilan fungsi
nilai_mahasiswa = [80, 75, 90, 60, 85]
hasil = rata_rata(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa adalah:", hasil)