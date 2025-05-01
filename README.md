# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga dengan saat ini, institusi tersebut telah memiliki banyak lulusan dengan kualitas yang baik. Akan tetapi, terdapat siswa yang tidak menyelesaikan pendidikannya atau dropout. 
Jumlah dropout yang tinggi akan menjadi tanda tanya yang besar pada institusi pendidikan tersebut. Oleh sebab itu, institusi ini ingin menganalisa dan mendeteksi sedini mungkin siswa yang berpotensi besar akan Dropout. 

### Permasalahan Bisnis
**Jaya Jaya Institute** menghadapi masalah serius dengan tingginya angka dropout. Dikhawatirkan dari tingginya angka dropout tersebut, institusi ini akan berksesan gagal dalam mencetak lulusan yang berkualitas. 

### Cakupan Proyek
- Pengumpulan dan persiapan data: Mengumpulkan dan menyiapkan data dari sumber yang diberikan, serta memastikan data tersebut siap untuk digunakan. 
- Eksplorasi Data: Menganalisa pola pola dan pengaruh terkait status Dropout.
- Pengembangan Model Prediksi: Menggunakan teknik machine learning untuk membangun model prediksi apakah siswa berpotensi Dropout atau tidak 

### Persiapan

Sumber data : [data](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_dropout python=3.9
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_dropout
    ```
4. Instal semua library yang dibutuhkan menggunakan perintah berikut.
    ```
   pip install -r requirements.txt
    ```
5. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```
## Business Dashboard
Dashboard ini digunakan untuk memberikan gambaran visual terkait analisis data Dropout pada institusi Jaya Jaya. Tujuan utamanya adalah memberikan informasi yang mudah dipahami oleh stakeholder dalam mengidentifikasi siswa yang berpotensi dropout. 

**link** [Looker] (https://lookerstudio.google.com/reporting/c021c6b0-25c1-4d91-ad2f-98f25e826adf)

## Menjalankan Sistem Machine Learning

1. **Pastikan Python terinstal**
   - Pastikan Python versi 3.x terinstal di sistem . Anda dapat mengunduh dan menginstalnya dari [python.org](https://www.python.org/).

2. **Buat lingkungan virtual**
   - Buat lingkungan virtual untuk mengisolasi dependensi proyek. Jalankan perintah berikut di terminal Anda:
     ```bash
     python -m venv env
     ```
     
3. **Aktifkan lingkungan virtual**
   - Untuk Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Untuk macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Pasang dependensi menggunakan `requirements.txt`**
   - Pastikan Anda berada di direktori proyek yang sama dengan file `requirements.txt`, lalu jalankan perintah berikut:
     ```bash
     pip install -r requirements.txt
     ```

5. Running Streamlit
```
streamlit run app.py
```
**link** [Streamlite](https://student-dropout-tcal6grcnfkzbbqdexoifv.streamlit.app/)

## Conclusion
Berdasarkan permasalahan diatas dapat disimpulkan bawah ada beberapa faktor yang mempengaruhi mahasiswa di dropout yaitu :
- Jurusan manajemen baik siang maupun malam memiliki jumlah dropout tertinggi. Hal ini dapat menjadi tanda tanya dengan jurusan tersebut. Apa yang terjadi pada jurusan tersebut menjadi tugas lanjutan setelah analisis ini. 
- Siswa yang mendapat nilai rendah pada semester pertama cenderung memiliki kemungkinan dropout yang tinggi.
- Siswa yang memiliki hutang cenderung memiliki resiko dropout yang tinggi. Hal ini mengindikasikan faktor ekonomi siswa menjadi salah satu penyebab tingginya faktor dropout. Ditambah lagi dengan latar belakang orang tua yang berlatar belakng pendidikan yang tidak terlalu tinggi menambah kemungkinan faktor latar belakang keluarga menjadi salah satu pilar penyebab Dropout yang tinggi. 

### Rekomendasi Action Items
Berikut beberapa rekomendasi action items yang harus dilakukan guna menyelesaikan permasalahan :

1. Melakukan penyelidikan terhadap jurusan yang memiliki angka Dropout tertinggi.
2. Memberikan bantuan beasiswa/keuangan agar dapat membantu perekonomian siswa. 
3. Memberikan motivasi kepada siswa agar dapat menjadi kebanggaan keluarga. 
4. Memberikan bimbingan pembelajaran lebih intensive sejak semester pertama. 
