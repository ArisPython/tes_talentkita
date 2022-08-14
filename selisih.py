# Selisih angka minimal dan maximal dari sebuah array

# Install library numpy: pip install numpy 

# import library numpy
import numpy as np

# Deklarasi array
x = np.array([1, 3, 4, 5, 6, 9, 10, 15])

print("Data array:\n", x)

# Mendapatkan nilai maksimum
nilai_max = np.amax(x)

# Mendapatkan nilai minimum
nilai_min = np.amin(x)

# Menghitung selisih
selisih = nilai_max - nilai_min
print("Selisih nilai Max dan nilai Min dari array adalah:\n", selisih)
