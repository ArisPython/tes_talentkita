
# Transpose matriks adalah matriks baru yang diperoleh dengan cara menukar elemen-elemen baris menjadi elemen kolom atau sebaliknya
# Fungsi Transpose
def transpose(l1, l2):
 
    # looping l1 sampai sepanjang item
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            # Menambahkan nilai (item) dengan indexnya (i) kedalam list baru 
            row.append(item[i])
        l2.append(row)
    return l2
 
# Array 2d
l1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
l2 = []
print(transpose(l1, l2))
