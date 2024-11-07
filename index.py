class Ruangan:
    def _init_(self, nama, luas):
        self.nama = nama
        self.luas = luas

    def info(self):
        return f"Ruangan: {self.nama}, Luas: {self.luas} m²"


class Rumah:
    def _init_(self, alamat):
        self.alamat = alamat
        self.ruangan = []

    def tambah_ruangan(self, ruangan):
        self.ruangan.append(ruangan)

    def info_rumah(self):
        info = f"Rumah beralamat: {self.alamat}\n"
        info += "Daftar Ruangan:\n"
        for r in self.ruangan:
            info += r.info() + "\n"
        return info


# Membuat objek rumah
rumah_saya = Rumah("Jl. Kebon Jeruk No. 5")

# Membuat beberapa ruangan
ruang_tamu = Ruangan("Ruang Tamu", 25)
kamar_tidur = Ruangan("Kamar Tidur", 15)
dapur = Ruangan("Dapur", 10)

# Menambahkan ruangan ke rumah
rumah_saya.tambah_ruangan(ruang_tamu)
rumah_saya.tambah_ruangan(kamar_tidur)
rumah_saya.tambah_ruangan(dapur)

# Menampilkan informasi rumah
print(rumah_saya.info_rumah())