def isKabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

tahun_input = int(input("Masukkan tahun: "))

hasil = isKabisat(tahun_input)

if hasil:
    print(f"Hasil: {hasil}. Tahun {tahun_input} adalah tahun kabisat.")
else:
    print(f"Hasil: {hasil}. Tahun {tahun_input} bukan tahun kabisat.")