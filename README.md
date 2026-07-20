Sistem Pakar Rekomendasi Kandungan Aktif Skincare Berdasarkan Gejala Kulit Menggunakan Metode Certainty Factor
Deskripsi

Sistem Pakar Rekomendasi Kandungan Aktif Skincare merupakan aplikasi berbasis web yang dirancang untuk membantu pengguna menentukan kandungan aktif skincare yang sesuai berdasarkan gejala kulit yang dialami. Sistem ini menggunakan metode Certainty Factor (CF) untuk menghitung tingkat keyakinan terhadap setiap rekomendasi berdasarkan gejala yang dipilih pengguna.

Knowledge base (basis pengetahuan) pada sistem disusun berdasarkan referensi ilmiah berupa jurnal dan panduan dermatologi terpercaya sehingga rekomendasi yang diberikan memiliki dasar ilmiah.

Latar Belakang

Banyak masyarakat mengalami kesulitan dalam memilih kandungan aktif skincare yang sesuai dengan kondisi kulitnya. Kesalahan memilih kandungan aktif dapat menyebabkan iritasi, breakout, maupun hasil perawatan yang kurang optimal.

Melalui sistem pakar ini, pengguna dapat memperoleh rekomendasi kandungan aktif berdasarkan gejala kulit yang dipilih sehingga proses pemilihan kandungan aktif menjadi lebih mudah, cepat, dan terarah.

Tujuan
Membantu pengguna memilih kandungan aktif skincare yang sesuai dengan kondisi kulit.
Mengimplementasikan metode Certainty Factor pada sistem pakar.
Menyediakan rekomendasi berdasarkan basis pengetahuan yang berasal dari sumber ilmiah terpercaya.
Metode yang Digunakan
Rule Base

Sistem menggunakan kumpulan aturan (Rule Base) yang menghubungkan gejala kulit dengan kandungan aktif skincare.

Contoh aturan:

IF kulit berminyak AND berjerawat THEN Salicylic Acid
IF kulit kering AND skin barrier rusak THEN Ceramide
IF terdapat bekas jerawat THEN Niacinamide
Certainty Factor (CF)

Metode Certainty Factor digunakan untuk menghitung tingkat keyakinan terhadap setiap rekomendasi kandungan aktif berdasarkan gejala yang dipilih oleh pengguna.

Output sistem berupa:

Nama kandungan aktif yang direkomendasikan
Nilai Certainty Factor
Persentase tingkat keyakinan
Fitur Sistem
Input gejala kulit.
Pemrosesan menggunakan Rule Base.
Perhitungan menggunakan metode Certainty Factor.
Menampilkan rekomendasi kandungan aktif skincare.
Menampilkan nilai dan persentase keyakinan hasil diagnosis.
Alur Sistem
Pengguna Memilih Gejala
            │
            ▼
     Rule Base Matching
            │
            ▼
 Perhitungan Certainty Factor
            │
            ▼
 Menentukan Nilai Keyakinan
            │
            ▼
Rekomendasi Kandungan Aktif
Teknologi yang Digunakan
Python
Flask
HTML
CSS
JavaScript
Certainty Factor Method
Struktur Folder
project/
│
├── app.py
├── certainty_factor.py
├── inference.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── gejala.py
│   ├── rules.py
│   └── kandungan.py
│
├── templates/
│
├── static/
│
└── assets/

Catatan: Struktur folder dapat disesuaikan dengan repository yang digunakan.

Cara Menjalankan Program
1. Clone Repository
git clone https://github.com/username/nama-repository.git
2. Masuk ke Folder Project
cd nama-repository
3. Install Dependency
pip install -r requirements.txt
4. Jalankan Program
python app.py
5. Buka Browser
http://127.0.0.1:5000
Contoh Penggunaan
Pilih gejala kulit yang dialami.
Klik tombol Proses Diagnosa.
Sistem akan menghitung nilai Certainty Factor.
Sistem menampilkan kandungan aktif yang direkomendasikan beserta tingkat keyakinannya.
Tampilan Sistem

Tambahkan screenshot berikut pada folder assets/ kemudian tampilkan di README.

Halaman Beranda
Halaman Input Gejala
Halaman Hasil Diagnosa
Halaman Rekomendasi Kandungan Aktif
Referensi

Knowledge base pada sistem disusun berdasarkan referensi ilmiah, di antaranya:

Guidelines of Care for the Management of Acne Vulgaris.
Efficacy of Ceramides and Niacinamide-Containing Moisturizer in Skin Barrier Repair.
Literatur dan jurnal dermatologi yang membahas penggunaan kandungan aktif skincare sesuai indikasi klinis.
Anggota Kelompok
Nama Lengkap – NIM
Nama Lengkap – NIM
Nama Lengkap – NIM
Lisensi

Project ini dibuat untuk memenuhi tugas Ujian Akhir Semester (UAS) Mata Kuliah Sistem Pakar dan digunakan untuk keperluan akademik.