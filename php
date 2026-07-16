<?php

class AlamatDusun {
    // Properti terenkapsulasi (Encapsulation)
    private $namaDusun;
    private $rt;
    private $rw;
    private $kecamatan;
    private $kabupaten;

    // Constructor untuk menginisialisasi data objek
    public function __construct($dusun, $rt, $rw, $kecamatan, $kabupaten) {
        $this->namaDusun = $dusun;
        $this->rt = $rt;
        $this->rw = $rw;
        $this->kecamatan = $kecamatan;
        $this->kabupaten = $kabupaten;
    }

    // Method untuk mengambil cetak alamat rapi (Getter/Behavior)
    public function getFormatBaris() {
        return "Dusun {$this->namaDusun}, RT {$this->rt}/RW {$this->rw}, Kec. {$this->kecamatan}, Kab. {$this->kabupaten}";
    }

    // Method untuk menampilkan cetak kartu data
    public function tampilkanKartuAlamat() {
        echo "=========================================\n";
        echo "             DATA ALAMAT DUSUN           \n";
        echo "=========================================\n";
        echo "Dusun     : " . $this->namaDusun . "\n";
        echo "RT / RW   : RT " . $this->rt . " / RW " . $this->rw . "\n";
        echo "Kecamatan : " . $this->kecamatan . "\n";
        echo "Kabupaten : " . $this->kabupaten . "\n";
        echo "=========================================\n";
    }
}

// Instansiasi Objek berdasarkan data Dusun Nagrak
$alamatNagrak = new AlamatDusun("Nagrak", "004b", "001", "Cileungsi", "Bogor");

// Memanggil method objek
$alamatNagrak->tampilkanKartuAlamat();
echo "Format Teks: " . $alamatNagrak->getFormatBaris() . "\n";

?>
