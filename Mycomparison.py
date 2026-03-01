import subprocess
import time

def run_script(script_name):
    print(f"--- Menjalankan {script_name} ---")
    start = time.time()
    
    # Mengeksekusi file python eksternal
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    
    end = time.time()
    print(result.stdout) # Menampilkan output dari slide 22-27 atau 35-38
    return end - start

if __name__ == "__main__":
    print("ANALISIS PERBANDINGAN KOMPUTASI (Slide 20 vs Slide 34)\n")

    # 1. Jalankan Serial (SISD)
    time_serial = run_script('MySequentialProgram.py')
    print(f"Waktu Eksekusi Serial: {time_serial:.4f} detik\n")

    # 2. Jalankan Paralel (MIMD)
    time_parallel = run_script('MyParallelProgram.py')
    print(f"Waktu Eksekusi Paralel: {time_parallel:.4f} detik\n")

    # Kesimpulan Analisis berdasarkan PPT
    print("--- KESIMPULAN ---")
    if time_parallel < time_serial:
        print("Komputasi Paralel berhasil membagi tugas (splitting the work).")
    else:
        print("Serial lebih cepat karena 'overhead' sistem saat membuat proses baru untuk tugas kecil.")