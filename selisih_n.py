# Mengambil data input dari user, memasukannya sebagai data array
# tiap item/angka dipisahkan dengan spasi
list1 =  []
list1 = [int(item) for item in input("Enter the list items : ").split()]

maxi = max(list1) # Mencari nilai maksimal dari array
mini = min(list1) # Mencari nilai minimal dari array
selisih = maxi - mini # Menghitung nilai selisih

print('Data array:',list1)
print('Nilai array Maksimal:',maxi)
print('Nilai array Minimal:',mini)
print('Selisih Nilai maximal dan minimal:',selisih)