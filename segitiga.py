# Fungsi segitiga bintang
def segitiga(n):
	
	# Jumlah spasi
	k = n - 1

	# loop luar sebagai jumlah baris
	for i in range(0, n):
	
		# loop dalam sebagai jumlah spasi
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k tiap selesai loop
		k = k - 1
	
		# loop dalam sebagai jumlah kolom
		for j in range(0, i+1):
		
			# cetak bintang
			print("* ", end="")
	
		# ganti baris
		print("\r") 

# Input
input_num = int(input("Masukkan angka:"))
n = input_num
segitiga(n)
