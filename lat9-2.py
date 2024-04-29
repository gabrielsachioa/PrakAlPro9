def minta_input():
    hasil = []
    penyelesaian = False

    while penyelesaian == False:
        n = input("Masukkan bilangan (ketik 'done' untuk menyelesaikan): ")

        if n.isdigit() == True:
            hasil.append(int(n))
            hasil.sort()

            nilai_minimum = min(hasil)
            nilai_maksimum = max(hasil)
        elif n.lower() == "done":
            print(hasil)
            print(f"Nilai minimum: {nilai_minimum}")
            print(f"Nilai maksimum: {nilai_maksimum}")
            penyelesaian = True  
        else:
            print("Input tidak valid")

minta_input()
