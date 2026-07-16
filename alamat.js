class AlamatDusun {
    // Constructor untuk inisialisasi data
    constructor(dusun, rt, rw, kecamatan, kabupaten) {
        this.namaDusun = dusun;
        this.rt = rt;
        this.rw = rw;
        this.kecamatan = kecamatan;
        this.kabupaten = kabupaten;
    }

    // Method untuk menampilkan alamat secara lengkap
    tampilkanAlamat() {
        console.log("=========================================");
        console.log("             DATA ALAMAT DUSUN           ");
        console.log("=========================================");
        console.log(`Dusun     : ${this.namaDusun}`);
        console.log(`RT / RW   : RT ${this.rt} / RW ${this.rw}`);
        console.log(`Kecamatan : ${this.kecamatan}`);
        console.log(`Kabupaten : ${this.kabupaten}`);
        console.log("=========================================");
        console.log(`Format Baris: ${this.namaDusun}, RT ${this.rt}/RW ${this.rw}, Kec. ${this.kecamatan}, Kab. ${this.kabupaten}`);
    }
}

// Membuat objek alamat sesuai data yang Anda berikan
const alamat1 = new AlamatDusun("Nagrak", "004b", "001", "Cileungsi", "Bogor");

// Menampilkan data alamat ke konsol
alamat1.tampilkanAlamat();
