class PersegiPanjang:
    def __init__(self, panjang, lebar):
        """Konstruktor untuk inisialisasi panjang dan lebar."""
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        """Fungsi untuk menghitung keliling persegi panjang."""
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        """Fungsi untuk menghitung luas persegi panjang."""
        return self.panjang * self.lebar

    def __str__(self):
        """Fungsi untuk menampilkan string representasi objek."""
        return f'Persegi Panjang(panjang={self.panjang}, lebar={self.lebar})'


if __name__ == "__main__":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    
    persegi_panjang = PersegiPanjang(panjang, lebar)
    

    print(persegi_panjang)
    
    print("Keliling:", persegi_panjang.hitung_keliling())
    print("Luas:", persegi_panjang.hitung_luas())