import numpy as np
# Inisialisasi Matriks A (2x2) dan B (2x2)
n = 2 
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.zeros((n, n))

print("Serial Computation (Sequential Matrix Multiplication)")
# Algoritma Sekuensial: Baris demi baris, satu per satu
for i in range(len(A)): # Loop baris A
    for j in range(len(B[0])): # Loop kolom B
        for k in range(len(B)): # Loop perkalian elemen
            result[i][j] += A[i][k] * B[k][j]
        
        # Mencetak setiap langkah 
        print(f"Step [row {i}, col {j}]: Result = {result[i][j]}")
