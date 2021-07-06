# UserStoryScenToUseCaseSpec
> Generate dari Use Case Specification to Business Process Modelling Notation (BPMN)

Repository ini merupakan Project milik kelompok 5 Pembangunan Perangkat Lunak Praktikum Kelas I2, dimana Project ini bertujuan dapat melakukan Generate dari Use Case Specification ke Business Process Modelling Notation (BPMN)

# Daftar Isi
* [Deskripsi Proyek](#Deskripsi-Proyek)
  * [Definisi](#definisi)
  * [Sistem Pembangun](#sistem-pembangun)
* [Petunjuk Instalasi](#petunjuk-instalasi)
* [Penjelasan Penggunaan](#penjelasan-penggunaan)
* [Informasi Lainnya](#informasi-lainnya)
  * [Anggota Proyek](#anggota-proyek)
  * [Tanggal Rilis](#tanggal-rilis)
  * [Kontak](#kontak)
* [Lisensi](#lisensi)

<!-- TENTANG PROYEK -->
# Deskripsi Proyek
### Definisi
Proyek perangkat lunak terus berkembang dari waktu ke waktu oleh karena itu spesifikasi kebutuhan perangkat lunak juga berkembang. Salah satu cara untuk mendokumentasikan kebutuhan adalah penggunaan Use Case, yang menggambarkan interaksi seorang aktor dengan sistem yang diinginkan. Use Case kemudian harus di breakdown untuk menjelaskan bagaimana sistem ini bekerja (Muchtar, et al. 2011), inilah yang kemudian disebut Use Case Specification. Dalam laporan ini kami menjelaskan pembuatan model proses bisnis dalam BPMN dari Use Case Specification dengan mengurutkan Scenario ID-nya. Berikut adalah penjelasan dari masing-masing artefak yang dilibatkan dalam aplikasi ini. 
1. *Use Case Specification* merupakan deskripsi singkat tentang langkah-langkah yang diperlukan untuk menggambarkan use case, lalu langkah-langkahnya dibuat untuk menambahkan lebih detail yang disebut dengan use case specification.
2. BPMN adalah pendekatan berorientasi grafik yang memodelkan aktivitas proses bisnis berdasarkan flow-nya. 

Secara garis besar, komponen pembentuk dari *Use Case Specification* sebagai *output* yang dihasilkan terbentuk melalui komponen input, yaitu :
1. Use Case Name : Nama Use Case berdasarkan keperluan aktor.
2. Trigger : Tujuan aktor melakukan aktivitas tersebut dalam sistem.
3. Main Scenario : Menunjukkan ketika aktor melakukan aktivitas, sistem harus meresponsnya dengan sesuai. Skenario utama menjelaskan successful case dari Use Case. 
4. Pre-condition : Keadaan sistem yang diperlukan sebelum use case specification di mulai.
5. Extension : Pengecualian dan kasus yang unsuccessful dapat ditambahkan di bagian ekstensions, disebut juga dengan Exceptional Scenario.
6. Post-condition : Keadaan sistem yang diperlukan setelah use case specification di akhiri.

### Sistem Pembangun
Aplikasi Use Case Specification Generator dibangun dengan memanfaatkan *software*, *framework*, dan beberapa bahasa pemrograman, diantaranya adalah sebagai berikut :
- [VsCode Editor](https://code.visualstudio.com/)
- [MySQL](https://www.mysql.com/)
- [GitHub](https://github.com/)
- [Django Framework](https://www.djangoproject.com/) 
- [Bootstrap Framework](https://getbootstrap.com/)
- [Python](https://www.python.org/)
- [Javascript](javascript.com)

# Petunjuk Instalasi 
Petunjuk mengenai prosedur instalasi untuk aplikasi dilakukan pada sesi terminal, berikut prosedur yang dapat dilakukan :
1. Lakukan *clone* pada repositori
   ```sh
   git clone https://github.com/AgileRE-2021/UseCaseSpecToBPMN.git
   ```
2. Membuat *virtual environment* pada *python*
   ```sh
   py -m venv env
   ```
3. Masuk ke dalam *virtual environment* 
   ```sh
   venv\Scripts\activate.bat
   ```
4. Lakukan instalasi *Django Framework*
   ```sh
   py -m pip install Django
   ```
5. Masuk ke dalam folder aplikasi CDG
   ```sh
   cd UseCaseSpecToBPMN
   ```
6. Lakukan instalasi *Bootstrap Framework* 
   ```sh
   pip install django-bootstrap-v5
   ```
7. Lakukan instalasi MySQL dengan mengikuti link video dibawah
   ```sh
   https://youtu.be/jo9jZ1GKFmw
   ```
8. Jalankan aplikasi pada *localhost*
   ```sh
   py manage.py runserver
   ```
# Penjelasan Penggunaan
Petunjuk mengenai prosedur penggunaan aplikasi dapat dilihat pada bagian di bawah ini :
1. Pada halaman awal sistem user akan diperlihatkan pada halaman login dimana user harus melakukan sign up
2. Setelah sign in sistem akan berada pada halaman welcome page
3. Untuk memulai project klik menu "Project List" pada navbar
<img src="https://github.com/AgileRE-2021/UseCaseSpecToBPMN/assets_readme/projectlist.PNG">
4. 

# Informasi Lainnya
### Anggota Proyek
Anggota pada proyek pengerjaan aplikasi *Use Case Specification Generator* terdiri dari 7 orang, meliputi :
1. Intan Noer Fatimah
2. Munawaroh
3. Muhammad Abdul Gani
4. Rayhan Naufal Altavin
5. Andrico Mauludi Junianto
6. Muhammad Raihan Nady K.
7. Albert Samuel Pangihutan

### Tanggal Rilis 
Tanggal 9 Juli 2021

### Kontak 
Informasi kontak setiap anggota lebih detail dapat dilihat di bawah ini. 
1. Intan Noer Fatimah         : intan.noer.fatimah-2018@fst.unair.ac.id
2. Munawaroh                  : munawaroh-2018@fst.unair.ac.id
3. Muhammad Abdul Gani        : muhammad.abdul.gani-2018@fst.unair.ac.id
4. Rayhan Naufal Altavin      : rayhan.naufal.a-2018@fst.unair.ac.id
5. Andrico Mauludi Junianto   : andrico.mauludi.junianto-2018@fst.unair.ac.id
6. Muhammad Raihan Nady K.    : muhammad.raihan.nady.khairullah-2018@fst.unair.ac.id
7. Albert Samuel Pangihutan   : albert.samuel.pangihutan-2018@fst.unair.ac.id

# Lisensi

Copyright © 2021 Universitas Airlangga

---
<br/>
