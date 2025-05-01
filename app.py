import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('./model.pkl')

# Fitur penting
important_features = [
    'Curricular_units_2nd_sem_approved',
    'Tuition_fees_up_to_date',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Admission_grade',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_evaluations',
    'Application_mode',
    'Mothers_occupation',
    'Previous_qualification_grade'
]

# Mapping kategorikal (label -> value numerik)
application_mode_map = {
    '1st phase - general contingent': 1,
    'Ordinance No. 612/93': 2,
    '1st phase - special contingent (Azores Island)': 5,
    'Holders of other higher courses': 7,
    'Ordinance No. 854-B/99': 10,
    'International student (bachelor)': 15,
    '1st phase - special contingent (Madeira Island)': 16,
    '2nd phase - general contingent': 17,
    '3rd phase - general contingent': 18,
    'Ordinance No. 533-A/99, item b2) (Different Plan)': 26,
    'Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
    'Over 23 years old': 39,
    'Transfer': 42,
    'Change of course': 43,
    'Technological specialization diploma holders': 44,
    'Change of institution/course': 51,
    'Short cycle diploma holders': 53,
    'Change of institution/course (International)': 57
}

mothers_occupation_map = {
    'Student': 0,
    'Legislative/Executive/Managers': 1,
    'Intellectual and Scientific Activities': 2,
    'Technicians and Intermediate Professions': 3,
    'Administrative staff': 4,
    'Personal Services, Security, Sellers': 5,
    'Farmers/Fisheries/Forestry': 6,
    'Industry/Construction/Craftsmen': 7,
    'Machine Operators and Assemblers': 8,
    'Unskilled Workers': 9,
    'Armed Forces Professions': 10,
    'Other Situation': 90,
    '(blank)': 99,
    'Health professionals': 122,
    'Teachers': 123,
    'ICT Specialists': 125,
    'Science/Engineering Technicians': 131,
    'Health Technicians': 132,
    'Legal/Social/Sports/Cultural Technicians': 134,
    'Office/Data Processing Workers': 141,
    'Finance/Accounting Services': 143,
    'Other Admin Support': 144,
    'Personal Service Workers': 151,
    'Sellers': 152,
    'Personal Care Workers': 153,
    'Skilled Construction Workers': 171,
    'Jewelers/Artisans/etc.': 173,
    'Food/Wood/Clothing Workers': 175,
    'Cleaning Workers': 191,
    'Unskilled Agriculture/Forestry': 192,
    'Unskilled Construction/Transport': 193,
    'Meal Prep Assistants': 194
}

# Judul aplikasi
st.title("Prediksi Dropout Mahasiswa")

st.subheader("Masukkan Data Mahasiswa:")

user_input = {}

# Fitur numerik langsung
user_input['Curricular_units_2nd_sem_approved'] = st.number_input("SKS Disetujui (Semester 2)", min_value=0)
user_input['Tuition_fees_up_to_date'] = st.selectbox("Status Pembayaran UKT", [0, 1], format_func=lambda x: "Lunas" if x == 1 else "Belum Lunas")
user_input['Curricular_units_1st_sem_approved'] = st.number_input("SKS Disetujui (Semester 1)", min_value=0)
user_input['Curricular_units_2nd_sem_grade'] = st.number_input("Nilai Rata-rata Semester 2", min_value=0.0, max_value=20.0)
user_input['Admission_grade'] = st.number_input("Nilai Masuk (0-200)", min_value=0, max_value=200)
user_input['Curricular_units_1st_sem_grade'] = st.number_input("Nilai Rata-rata Semester 1", min_value=0.0, max_value=20.0)
user_input['Curricular_units_2nd_sem_evaluations'] = st.number_input("Jumlah Evaluasi Semester 2", min_value=0)
user_input['Previous_qualification_grade'] = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0, max_value=200)

# Fitur kategorikal (ditampilkan sebagai label, disimpan sebagai angka)
app_mode_label = st.selectbox("Mode Aplikasi", list(application_mode_map.keys()))
user_input['Application_mode'] = application_mode_map[app_mode_label]

mothers_occ_label = st.selectbox("Pekerjaan Ibu", list(mothers_occupation_map.keys()))
user_input['Mothers_occupation'] = mothers_occupation_map[mothers_occ_label]

# Prediksi
if st.button("Prediksi Dropout"):
    input_df = pd.DataFrame([user_input])[important_features]
    pred = model.predict(input_df)[0]
    st.success(f"Hasil Prediksi: {'Dropout' if pred == 1 else 'Non-Dropout'}")
