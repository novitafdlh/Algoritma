#Hajera_F55123047

import time

# Data
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Merge Sort
def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    return merge_sort(left, right)

def merge_sort(left, right):
    sort_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort_arr.append(left[i])
            i += 1
        else:
            sort_arr.append(right[j])
            j += 1

    sort_arr.extend(left[i:])
    sort_arr.extend(right[j:])
    return sort_arr

# Quick Sort
def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick(left) + [pivot] + quick(right)

# Pilihan Sorting
def choose_algorithm():
    print("Pilih algoritma sorting yang akan digunakan:")
    print("1. Merge Sort")
    print("2. Quick Sort")

    while True:
        choice = input("Masukkan pilihan (1/2): ").strip()
        if choice == "1":
            return "merge"
        elif choice == "2":
            return "quick"
        else:
            print("Pilihan tidak valid, coba lagi!")

def run_sorting(algorithm, data):
    if algorithm == "merge":
        return merge(data)
    elif algorithm == "quick":
        return quick(data)
    else:
        raise ValueError("Algoritma tidak dikenal!")

def main():
    algorithm = choose_algorithm()
    print(f"\nMenggunakan {algorithm.capitalize()} Sort untuk mengurutkan data...")

    sorted_data = run_sorting(algorithm, X) 

    print("\nHasil Pengurutan:")
    print(sorted_data) 

    # Analisis 
    print("\nAnalisis :")
    if algorithm == "merge":
        print(" Merge Sort: ")
        print("  - Worst Case (O(n log n)): Merge Sort membagi data menjadi dua bagian")
        print("    dan menggabungkannya kembali, sehingga kompleksitasnya selalu O(n log n),")
        print("    baik data terurut, terbalik, maupun acak.")
        print("  - Best Case (O(n log n)): Sama seperti worst case, karena pembagian dan")
        print("    penggabungan tetap dilakukan, terlepas dari urutan data awal.")
        print("  - Average Case (O(n log n)): Sama seperti worst dan best case karena sifatnya deterministik.")
    elif algorithm == "quick":
        print(" Quick Sort: ")
        print("  - Worst Case (O(n²)): Terjadi ketika pivot yang dipilih buruk, misalnya data")
        print("    sudah terurut (ascending/descending), sehingga pembagian menjadi tidak seimbang.")
        print("  - Best Case (O(n log n)): Jika pivot selalu membagi array menjadi dua bagian")
        print("    yang sama besar, pembagian menjadi optimal.")
        print("  - Average Case (O(n log n)): Dengan data acak, pembagian rata-rata cukup")
        print("    mendekati seimbang sehingga performa mendekati best case.")

if __name__ == "__main__":
    main()
