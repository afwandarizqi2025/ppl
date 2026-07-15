package controller;

import model.Warga;
import java.util.ArrayList;
import java.util.List;

public class RtManager {
    private List<Warga> daftarWarga;
    private final String rt = "004B";
    private final String rw = "01";
    private final String desa = "Nagrak";
    private final String kecamatan = "Cileungsi";
    private final String kabupaten = "Bogor";

    public RtManager() {
        this.daftarWarga = new ArrayList<>();
    }

    public void tambahWarga(Warga warga) {
        daftarWarga.add(warga);
        System.out.println("✓ Data " + warga.getNama() + " berhasil ditambahkan.");
    }

    public void tampilkanProfilWilayah() {
        System.out.println("\n========================================");
        System.out.println("  PROFIL WILAYAH ADMINISTRASI RT");
        System.out.println("========================================");
        System.out.println("RT / RW    : " + rt + " / " + rw);
        System.out.println("Desa       : " + desa);
        System.out.println("Kecamatan  : " + kecamatan);
        System.out.println("Kabupaten  : " + kabupaten);
        System.out.println("Total Warga: " + daftarWarga.size() + " orang");
        System.out.println("========================================");
    }

    public void tampilkanDaftarWarga() {
        if (daftarWarga.isEmpty()) {
            System.out.println("\n[!] Belum ada data warga terdaftar.");
            return;
        }

        System.out.println("\n-----------------------------------------------------------------------------");
        System.out.printf("%-18s | %-25s | %-15s | %-15s\n", "NIK", "Nama Lengkap", "Jenis Kelamin", "Status Hubungan");
        System.out.println("-----------------------------------------------------------------------------");
        for (Warga w : daftarWarga) {
            System.out.printf("%-18s | %-25s | %-15s | %-15s\n", 
                w.getNik(), w.getNama(), w.getJenisKelamin(), w.getStatusHubungan());
        }
        System.out.println("-----------------------------------------------------------------------------");
    }
}
