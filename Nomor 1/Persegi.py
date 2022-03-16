#Nama   : Jasmine Sarah Maqnolia
#NIM    : 20051397078
#Kelas  : 2020B
#Prodi  : Manajemen Informatika


def persegi():
    s = float(input("\nMasukan Panjang Sisi: "))
    luas = s**2
    print("Luas Persegi : ", luas)
    return luas

def persegi2():
    s = float(input("\nMasukan Panjang Sisi: "))
    keliling = 4 * s
    print("Keliling Persegi : ", keliling)
    return keliling

while True:
    print("MENGHITUNG LUAS DAN KELILING PERSEGI")
    print("Pilih:")
    print("1. Mencari Luas Persegi")
    print("2. Mencari Keliling Persegi")
    print("3. Tutup")
    option = input("Option 1-3 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        persegi()
    elif option == "2":
        print("Anda Pilih Menu 2")
        persegi2()
    elif option == "3":
        break
    else:
        print("Input Anda salah coba ulang lagi!!!")
