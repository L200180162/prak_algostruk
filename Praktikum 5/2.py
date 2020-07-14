###############################No.2###############################
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)

a = DaftarAngka
DaftarAngka1 = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka1)

b = DaftarAngka1
DaftarAngka2 = (a+b)
BubbleSort(DaftarAngka2)

c = DaftarAngka2
print(c)
