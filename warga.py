class Warga:
    def __init__(self, nik: str, nama: str, jenis_kelamin: str, status_keluarga: str):
        self.nik = nik
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.status_keluarga = status_keluarga  # Contoh: Kepala Keluarga, Istri, Anak

    def to_dict(self):
        """Mengubah data objek menjadi dictionary agar mudah dibaca/dikelola"""
        return {
            "NIK": self.nik,
            "Nama": self.nama,
            "Jenis Kelamin": self.jenis_kelamin,
            "Status": self.status_keluarga
        }
