'''
Buat sebuah fungsi rekursif bernama jumlah digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10
'''

def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlah_digit(n // 10)

# Pemanggilan fungsi
n = 1234
hasil = jumlah_digit(n)
print("Jumlah digit dari", n, "adalah:", hasil)