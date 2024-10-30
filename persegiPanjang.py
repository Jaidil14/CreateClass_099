class PersegiPanjang:    
    def __init__(self, p, l):
        self.p = p
        self.l = l
    
    def keliling(self):
        return 2 * (self.p + self.l)
    
    def luas(self):
        return self.p * self.l
    
    def __str__(self):
        return "(" + str(self.p) + ", " + str(self.l) + ")"

def main():
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        if panjang <= 0 or lebar <= 0:
            print ("Bilangan harus bernilai positif!")
            return
        pp = PersegiPanjang (panjang, lebar)    
        print (pp)
        print ("keliling: ", pp.keliling())
        print ("luas: ", pp.luas())
    except ValueError: 
        print("Nilai harus sesuai!")
        
main()

