#Nama   : Jasmine Sarah Maqnolia
#NIM    : 20051397078
#Kelas  : 2020B
#Prodi  : Manajemen Informatika

def jajargenjang():
    alas = float(input("Masukan alas jajargenjang: "))
    tinggi = float(input("Masukan tinggi jajargenjang: "))
    luas = alas * tinggi
    print("Luas Jajargenjang : ", luas)
    return luas

def jajargenjang2():
    sisi1 = float(input("Masukan sisi 1 jajargenjang: "))
    sisi2 = float(input("Masukan sisi 2 jajargenjang: "))
    keliling = sisi1 + sisi2 + sisi1 + sisi2
    print("Keliling JajarGenjang : ", keliling)
    return keliling

while True:
    print("MENGHITUNG LUAS DAN KELILING JAJAR GENJANG")
    print("Pilih:")
    print("1. Mencari Luas Jajar genjang")
    print("2. Mencari Keliling Jajar Genjang")
    print("3. Tutup")
    option = input("Option 1-3 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        jajargenjang()
    elif option == "2":
        print("Anda Pilih Menu 2")
        jajargenjang2()
    elif option == "3":
        break
    else:
        print("Input Anda salah coba ulang lagi!!!")