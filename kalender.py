import streamlit as st
from datetime import datetime

# Fungsi untuk menghitung durasi hingga batas akhir 31 Desember 2024
def calculate_duration(start_year, start_month):
    start_date = datetime(start_year, start_month, 1)
    end_date = datetime(2024, 12, 31)  # Batas akhir di 31 Desember 2024
    duration_in_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    years, months = divmod(duration_in_months, 12)
    return years, months

# Judul dan deskripsi aplikasi
st.title("Perhitungan Durasi dan Predikat Kelulusan Kuliah")
st.write("Masukkan tahun dan bulan Anda memulai kuliah di Jurusan Teknik Informatika Bilingual Universitas Sriwijaya dan IPK Anda.")

# Input dari user
year = st.number_input("Masukkan tahun masuk kuliah (misal: 2021)", min_value=2000, max_value=datetime.now().year, value=2021)
month = st.number_input("Masukkan bulan masuk kuliah (1-12)", min_value=1, max_value=12, value=8)
ipk = st.number_input("Masukkan IPK (misal: 3.5)", min_value=0.0, max_value=4.0, value=3.5, format="%.2f")

# Hitung durasi
years, months = calculate_duration(year, month)

# Menampilkan hasil dan predikat
st.write(f"Anda berkuliah selama {years} tahun {months} bulan.")
if ipk < 3.8 and years <= 4 and months <= 3:
    st.write("Predikat: Dengan Pujian")
elif years > 4 or (years == 4 and months > 3):
    st.write("Predikat: Sangat Memuaskan")
else:
    st.write("Predikat: Dengan Pujian")

# Memasukkan informasi tambahan tentang logika predikat
st.write("Predikat kelulusan dihitung berdasarkan durasi kuliah dan IPK hingga batas akhir tahun 2024.")
