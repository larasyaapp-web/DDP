usia = int(input("Usia : "))

if usia <= 4 and usia == 1 :
    print("Balita")
elif usia <= 0:
    print("Umur tidak valid")
    
elif usia >= 4 and usia <= 12 :
    print("Anak anak")
    
elif usia >= 13 and usia <= 17 :
    print("Remaja")
elif usia >= 18 and usia <= 59 :
    print("Dewasa")



else :
    print("Lansia")