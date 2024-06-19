#aturcara utama
#menu
print("Senarai menu pilihan operasi")
print("1. Kiraan lilitan bulatan")
print("2. Kiraan luas bulatan")
print("========================")

#input pilihan menu
menu=int(input("Sila pilih menu 1 atau 2:"))

#isytihar pemalar PI
#PI=3.142
jejari=int(input("Sila masukkan nilai jejari (cm):"))
#sub aturcara 1: mengira lilitan bulatan
#input jejari
if menu==1:
    
#proses kiraan lilitan bulatan
    lilitan_bulatan=2*PI*jejari
#output
    print("Lilitan bulatan:", round(lilitan_bulatan,0),"cm")


#sub aturcara 2: mengira luas bulatan
#input jejari
else:
    #proses kiraan luas bulatan
    luas_bulatan=PI*jejari*jejari
#output
    print("Luas bulatan:", round(luas_bulatan,0),"cm persegi")

      
