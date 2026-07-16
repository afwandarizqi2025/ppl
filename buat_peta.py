import folium

# Koordinat perkiraan untuk wilayah Desa Nagrak, Cileungsi, Bogor
# Catatan: Ini adalah koordinat area Nagrak secara umum. Anda bisa menggantinya 
# dengan koordinat spesifik RT/RW jika memiliki titik GPS yang lebih akurat.
latitude = -6.4011
longitude = 106.9467

# 1. Membuat objek peta dasar
peta_nagrak = folium.Map(
    location=[latitude, longitude], 
    zoom_start=17,  # Zoom cukup dekat untuk melihat area RT/RW
    tiles="OpenStreetMap"
)

# 2. Menambahkan Marker (Penanda) untuk lokasi RT 004B RW 001
popup_text = """
<b>Dusun Nagrak</b><br>
RT 004B / RW 001<br>
Kecamatan Cileungsi<br>
Kabupaten Bogor
"""

folium.Marker(
    location=[latitude, longitude],
    popup=folium.Popup(popup_text, max_width=300),
    tooltip="Klik untuk detail wilayah",
    icon=folium.Icon(color="red", icon="home", prefix="fa")
).add_to(peta_nagrak)

# 3. Menambahkan lingkaran radius perkiraan wilayah RT (misal 100 meter)
folium.Circle(
    location=[latitude, longitude],
    radius=100,  # Radius dalam meter
    color="blue",
    fill=True,
    fill_color="blue",
    fill_opacity=0.1,
    popup="Perkiraan Cakupan Wilayah RT"
).add_to(peta_nagrak)

# 4. Menyimpan peta ke dalam file HTML
nama_file = "peta_dusun_nagrak_rt004b.html"
peta_nagrak.save(nama_file)

print(f"Peta berhasil dibuat! Silakan buka file '{nama_file}' di browser Anda.")
