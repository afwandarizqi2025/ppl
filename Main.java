import controller.RtManager;
import model.Warga;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        RtManager manager = new RtManager();
        Scanner scanner = new Scanner(System.in);
        boolean berjalan = true;

        // Data Awal (Dummy Data) untuk simulasi
        manager.tambahWarga(new Warga("3201021234560001", "Ahmad Subagja", "Laki-laki", "Kepala Keluarga"));
        manager.tambahWarga(new Warga("3201021234560002", "Siti Aminah", "Perempuan", "Istri"));

        while (berjalan) {
            manager.tampilkanProfilWilayah();
            System.out.println("Menu Aplikasi RT:");
            System.out.println("1. Tambah Data Warga");
            System.out.println("2. Lihat Semua Data Warga");
            System.out.println("3. Keluar");
            System.out.print("Pilih menu (1-3): ");
            
            int pilihan = scanner.nextInt();
            scanner.nextLine(); // Membersihkan buffer row

            switch (pilihan) {
                case 1:
                    System.out.print("\nMasukkan NIK: ");
                    String nik = scanner.nextLine();
                    System.out.print("Masukkan Nama Lengkap: ");
                    String nama = scanner.nextLine();
                    System.out.print("Masukkan Jenis Kelamin: ");
                    String jk = scanner.nextLine();
                    System.out.print("Masukkan Status Hubungan Keluarga: ");
                    String status = scanner.nextLine();

                    Warga wargaBaru = new Warga(nik, nama, jk, status);
                    manager.tambahWarga(wargaBaru);
                    break;
                case 2:
                    manager.tampilkanDaftarWarga();
                    break;
                case 3:
                    berjalan = false;
                    System.out.println("\nTerima kasih. Program selesai.");
                    break;
                default:
                    System.out.println("\n[!] Pilihan tidak valid. Silakan coba lagi.");
            }
        }
        scanner.close();
    }
}
