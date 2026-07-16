<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('alamat_dusuns', function (Blueprint $table) {
            $table->id();
            $table->string('nama_dusun');
            $table->string('rt');
            $table->string('rw');
            $table->string('kecamatan');
            $table->string('kabupaten');
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('alamat_dusuns');
    }
};
