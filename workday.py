
# Mencari hari kerja dalam range tanggal
# Menggunakan timedelta() + sum() + weekday()
from datetime import datetime, timedelta

# Input Date dari user (string)
input_date1 = str(input('Masukkan Tanggal awal (yyyy-mm-dd): '))
input_date2 = str(input('Masukkan Tanggal akhir (yyyy-mm-dd): '))

# Merubah string ke format date
date1 = datetime.strptime(input_date1, "%Y-%m-%d")
date2 = datetime.strptime(input_date2, "%Y-%m-%d")

# Cetak range tanggal
print("Range Tanggal : " + str(date1) + " --- " + str(date2))

# Hari diekstrak menggunakan timedelta(): Selisih hari di increment sampai hari terakhir
dates = (date1 + timedelta(i + 1) for i in range((date2 - date1).days))

# Hari kerja difilter menggunakan weekdays(),   
res = sum(1 for day in dates if day.weekday() < 5)

# printing
print("Total hari kerja dalam range : " + str(res))
