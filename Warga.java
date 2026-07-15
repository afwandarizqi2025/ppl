package model;

public class Warga {
    private String nik;
    private String nama;
    private String jenisKelamin;
    private String statusHubungan; // Contoh: Kepala Keluarga, Istri, Anak

    public Warga(String nik, String nama, String jenisKelamin, String statusHubungan) {
        this.nik = nik;
        this.nama = nama;
        this.jenisKelamin = jenisKelamin;
        this.statusHubungan = statusHubungan;
    }

    // Getter dan Setter
    public String getNik() { return nik; }
    public void setNik(String nik) { this.nik = nik; }

    public String getNama() { return nama; }
    public void setNama(String nama) { this.nama = nama; }

    public String getJenisKelamin() { return jenisKelamin; }
    public void setJenisKelamin(String jenisKelamin) { this.jenisKelamin = jenisKelamin; }

    public String getStatusHubungan() { return statusHubungan; }
    public void setStatusHubungan(String statusHubungan) { this.statusHubungan = statusHubungan; }
}
