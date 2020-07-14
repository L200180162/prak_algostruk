###############################No.1###############################
class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

        
c0 = Mahasiswa('Ika',10,'Sukoharjo')
c1 = Mahasiswa('Budi',51,'Sragen')
c2 = Mahasiswa('Ahmad',2,'Surakarta')
c3 = Mahasiswa('Chandra',18,'Surakarta')
c4 = Mahasiswa('Eka',4,'Boyolali')
c5 = Mahasiswa('Fandi',31,'Salatiga')
c6 = Mahasiswa('Deni',13,'Klaten')
c7 = Mahasiswa('Galuh',5,'Wonogiri')
c8 = Mahasiswa('Janto',23,'Klaten')
c9 = Mahasiswa('Hasan',64,'Karanganyar')
c10 = Mahasiswa('Khalid',29,'Purwodadi')

DaftarAngka = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
BubbleSort(DaftarAngka)
print(DaftarAngka)
