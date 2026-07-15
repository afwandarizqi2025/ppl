from warga import Warga
from rt_manager import RtManager

def main():
    manager = RtManager()

    # Data awal (Dummy Data) untuk simulasi awal
    manager.tambah_warga(Warga("3201021234560001", "tajudin", "Laki-laki", "Kepala Keluarga"))
    manager.tambah_warga(Warga("3201021234560002", "Siti Aminah", "Perempuan", "Istri"))

    while True:
        manager.tampilkan_profil_wilayah()
        print("Menu Sistem Informasi RT:")
        print("1. Tambah Data Warga Baru")
        print("2. Lihat Semua Data Warga")
        print("3. Keluar Sistem")
        
        pilihan = input("\nPilih menu (1-3): ").strip()

        if pilihan == "1":
            print("\n--- Input Data Warga Baru ---")
            nik = input("Masukkan NIK                   : ")
            nama = input("Masukkan Nama Lengkap          : ")
            jk = input("Masukkan Jenis Kelamin (L/P)   : ")
            status = input("Masukkan Status Kependudukan   : ")

            warga_baru = Warga(nik, nama, jk, status)
            manager.tambah_warga(warga_baru)

        elif pilihan == "2":
            manager.tampilkan_semua_warga()
            input("\nTekan Enter untuk kembali ke menu utama...")

        elif pilihan == "3":
            print("\nSistem dimatikan. Terima kasih telah menggunakan aplikasi administrasi RT.")
            break
        else:
            print("\n[!] Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")

if __name__ == "__main__":
    main()
