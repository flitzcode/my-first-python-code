"""
Program perulangan membaca buku
"""
jumlah_buku = 10
print('Ibu berkata,"Baca semua bukumu"')
jumlah_buku_yang_sudah_dibaca = 0
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} ")

print('dengan for')
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} ")

#Tanpa For
print('Tanpa For')
print('Buku ke 1 sudah dibaca')
print('Buku ke 2 sudah dibaca')
print('Buku ke 3 sudah dibaca')
print('Buku ke 4 sudah dibaca')
print('Buku ke 5 sudah dibaca')


