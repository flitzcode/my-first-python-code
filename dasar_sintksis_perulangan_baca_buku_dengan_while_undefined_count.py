"""
Program Perulangan memmbaca buku dengan while
"""
book_count = 10
print('ibu berkata,"Baca semua bukumu"')
read_count = 0

understood_count = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {understood_count} ")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

print(f"jumlah buku yang sudah dibaca dan dipahami {understood_count}")
if understood_count == book_count:
    print('Bu,semua buku sudah dibaca dan dipahami')
else:
    print(f'Bu,tidak semua buku bisa dipahami. Budi hanya bisa memahami {understood_count} buku')

print(f"jumlah buku yang sudah dibaca {understood_count} ")