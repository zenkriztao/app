import streamlit as st
from datetime import datetime

# Fungsi untuk menghitung durasi
def calculate_duration(start_year, start_month):
    start_date = datetime(start_year, start_month, 1)
    current_date = datetime.now()
    duration_in_months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
    years, months = divmod(duration_in_months, 12)
    return years, months

# Judul dan deskripsi aplikasi
st.title("Perhitungan Durasi Kuliah")
st.write("Masukkan tahun dan bulan Anda memulai kuliah di Jurusan Teknik Informatika Bilingual Universitas Sriwijaya.")

# Input dari user
year = st.number_input("Masukkan tahun masuk kuliah (misal: 2021)", min_value=2000, max_value=datetime.now().year, value=2021)
month = st.number_input("Masukkan bulan masuk kuliah (1-12)", min_value=1, max_value=12, value=8)

# Hitung durasi
years, months = calculate_duration(year, month)

# Menampilkan hasil
st.write(f"Anda berkuliah selama {years} tahun {months} bulan.")
if years > 4 or (years == 4 and months > 3):
    st.write("Predikat: Dengan Memuaskan")
elif years > 3 or (years == 3 and months > 5):
    st.write("Predikat: Summa Cum Laude atau Dengan Pujian")
else:
    st.write("Predikat: Belum memenuhi syarat untuk predikat spesial.")

# Memasukkan informasi tambahan
st.write("Predikat dihitung berdasarkan durasi kuliah sampai saat ini.")
