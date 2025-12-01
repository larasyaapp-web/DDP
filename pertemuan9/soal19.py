#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens

def bilangan(bil):
    for i in range(1, bil+1):
        if i % 2 != 0:
            print(i)

bilangan(22)