#Nama   : Jasmine Sarah Maqnolia
#NIM    : 20051397078
#Kelas  : 2020B
#Prodi  : Manajemen Informatika

def segitiga():
    a = float(input("\nMasukan Alas  : "))
    t = float(input("Masukan Tinggi: "))
    luas= 0.5 * a * t
    print("Luas Segitiga : ", luas)
    return luas

def segitiga2():
    a=int(input("Masukan sisi 1="))
    b=int(input("Masukan sisi 2="))
    c=int(input("Masukan sisi 3="))
    keliling = a + b + c
    print("Keliling Segitiga : ", keliling)
    return keliling

while True:
    print("MENGHITUNG LUAS DAN KELILING SEGITIGA")
    print("Pilih:")
    print("1. Mencari Luas Segitiga")
    print("2. Mencari Keliling Segitiga")
    print("3. Tutup")
    option = input("Option 1-3 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        segitiga()
    elif option == "2":
        print("Anda Pilih Menu 2")
        segitiga2()
    elif option == "3":
        break
    else:
        print("Input Anda salah coba ulang lagi!!!")

