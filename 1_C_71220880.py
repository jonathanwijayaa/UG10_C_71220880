print("========== Pilih menu ==========")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
bilpertama=int(input("Masukkan angka pertama:"))
bilkedua=int(input("Masukkan angka kedua:"))
Menu=input("Pilihan Anda:")
if Menu=="1" :
    Tambah=bilpertama+bilkedua
    print("Hasil:",Tambah)
elif Menu=="2" :
    Kurang=bilpertama-bilkedua
    print("Hasil:",Kurang)
elif Menu=="3" :
    Kali=bilpertama*bilkedua
    print("Hasil:",Kali)
elif Menu=="4" :
    Bagi=bilpertama/bilkedua
    print("Hasil:",Bagi)
