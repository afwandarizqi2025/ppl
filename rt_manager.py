from warga import Warga

class RtManager:
    def __init__(self):
        self.daftar_warga = []
        # Informasi Wilayah Administratif
        self.rt = "004B"
        self.rw = "001"
        self.desa = "Nagrak"
        self.kecamatan = "Cileungsi"
        self.kabupaten = "Bogor"

    def tambah_warga(self, warga: Warga):
        self.daftar_warga.append(warga)
        print(f"\n✓ Data Warga atas nama '{warga.nama}' berhasil ditambahkan!")

    def tampilkan_profil_wilayah(self):
        print("\n" + "="*40)
        print("     PROFIL ADMINISTRASI WILAYAH RT")
        print("="*40)
        print(f"RT / RW     : {self.rt} / {self.rw}")
        print(f"Desa        : {self.desa}")
        print(f"Kecamatan   : {self.kecamatan}")
        print(f"Kabupaten   : {self.kabupaten}")
        print(f"Total Warga : {len(self.daftar_warga)} Orang")
        print("="*40)

    def tampilkan_semua_warga(self):
        if not self.daftar_warga:
            print("\n[!] Belum ada data warga terdaftar di wilayah ini.")
            return

        print("\n" + "-"*80)
        print(f"{'NIK':<18} | {'Nama Lengkap':<25} | {'Jenis Kelamin':<15} | {'Status Keluarga':<15}")
        print("-"*80)
        for w in self.daftar_warga:
            print(f"{w.nik:<18} | {w.nama:<25} | {w.jenis_kelamin:<15} | {w.status_keluarga:<15}")
        print("-"*80)
