def hitung_ganjil(angka_list):
    jumlah_ganjil = 0
    total_ganjil = 0
    banyak_ganjil = 0

    for angka in angka_list:
        if angka % 2 == 0:
            continue
        jumlah_ganjil += angka
        total_ganjil += 1
        banyak_ganjil += 1

    if total_ganjil == 0:
        return None, None, 0
    rata_rata = jumlah_ganjil / total_ganjil
    return jumlah_ganjil, rata_rata, banyak_ganjil

angka_list = [2, 3, 5, 7, 10]

jumlah, rata_rata, banyak_ganjil = hitung_ganjil(angka_list)

if jumlah is None and rata_rata is None:
    print("Tidak ada bilangan ganjil")
else:
    print("Jumlah angka ganjil: ", jumlah)
    print("Rata-rata angka ganjil: ", rata_rata)
    print("Total bilangan ganjil: ", banyak_ganjil)