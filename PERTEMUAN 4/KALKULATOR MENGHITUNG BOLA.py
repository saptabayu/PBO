import flet as ft
import math
# Fungsi Utama
def main(page: ft.Page):

    # Warna Background (abu-abu)
    page.bgcolor = "#D3D3D3"

    # Jika tombol 'hasil' ditekan, maka jalankan kode dibawah ini
    def btn_click(e):

        # Jika user tidak menginputkan jari_jari, maka
        if not jari_jari.value:

            # Buat pesan error
            jari_jari.error_text = "Tolong masukkan jari_jari Bola"

            # Halaman di refrash (agar pesan error muncul)
            page.update()

        # Jika user tidak menginputkan tinggi
        elif not tinggi.value:

            # Buat pesan error
            tinggi.error_text = "Tolong masukkan tinggi Bola"

            # Halaman di refrash (agar pesan error muncul)
            page.update()

        # Jika berhasil (user menginputkan semua, jari_jari, lebar dan tinggi)
        else:
            # Hitung luas
            value_luas =  4 * math.pi * float(jari_jari.value) * float(jari_jari.value) + float(tinggi.value)
            
            # Hitung volume
            value_volume =  math.pi * (4/3) * math.pi * jari_jari ** 3
            # Tampilkan luas
            luas.value = value_luas

            # Tampilkan volume
            volume.value = value_volume

            # Page di refresh
            page.update()

    # Buat Elemen TextField (inputan)
    jari_jari = ft.TextField(label="Jari-jari")
    tinggi = ft.TextField(label="Tinggi")
    luas = ft.TextField(label="Luas")
    volume = ft.TextField(label="Volume")

    # Tampilkan elemen tersebut
    page.add(

        # Nav bar, bagian atas / judul. Nama & warna background (biru)
        ft.AppBar(title=ft.Text("Kalkulator Bola"), bgcolor="#BBE1FA"),

        jari_jari,
        tinggi,

        # Tombol Hasil
        ft.ElevatedButton("Hitung!", on_click=btn_click),

        luas,
        volume
    )

# Jalankan aplikasi
ft.app(target=main)
