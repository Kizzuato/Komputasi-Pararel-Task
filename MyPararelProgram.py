import multiprocessing
import numpy as np

def multiply_row(row_idx, A, B, result_queue):
    # Menghitung hasil satu baris matriks
    row_result = np.dot(A[row_idx], B)
    print(f"Proses {row_idx}: Menghitung baris ke-{row_idx}")
    result_queue.put((row_idx, row_result))

if __name__ == "__main__":
    # Inisialisasi Matriks A (2x2) dan B (2x2)
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    result_queue = multiprocessing.Queue()
    processes = []
    
    # Menjalankan proses paralel untuk setiap baris (MIMD Architecture)
    for i in range(len(A)):
        p = multiprocessing.Process(target=multiply_row, args=(i, A, B, result_queue))
        processes.append(p)
        p.start() # Menjalankan proses secara simultan

    # Menunggu semua proses selesai
    for p in processes:
        p.join() 

    # Mengambil hasil dari Queue dan menyusunnya kembali
    final_matrix = np.zeros((2, 2))
    for _ in range(len(A)):
        idx, row_val = result_queue.get()
        final_matrix[idx] = row_val

    print("\nMatriks A:\n", A)
    print("Matriks B:\n", B)
    print("Hasil Perkalian Matriks (Paralel):\n", final_matrix)