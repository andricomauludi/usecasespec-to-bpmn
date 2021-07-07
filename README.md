# UsespecToBPMN
> Generate dari Use Case Specification to Business Process Modelling Notation (BPMN)

Repository ini merupakan Project milik kelompok 5 Pembangunan Perangkat Lunak Praktikum Kelas I2, dimana Project ini bertujuan dapat melakukan Generate dari Use Case Specification ke Business Process Modelling Notation (BPMN)

# Daftar Isi
* [Deskripsi Proyek](#Deskripsi-Proyek)
  * [Definisi](#definisi)
  * [Sistem Pembangun](#sistem-pembangun)
* [Petunjuk Instalasi](#petunjuk-instalasi)
* [Penjelasan Penggunaan](#penjelasan-penggunaan)
   * [Petunjuk Pengisian Scenario](#petunjuk-pengisian-scenario)
* [Informasi Lainnya](#informasi-lainnya)
  * [Anggota Proyek](#anggota-proyek)
  * [Manajemen Proyek](#manajemen-proyek)
  * [Tanggal Rilis](#tanggal-rilis)
  * [Kontak](#kontak)
* [Lisensi](#lisensi)

<!-- TENTANG PROYEK -->
# Deskripsi Proyek
### Definisi
Proses bisnis saat ini semakin mengutamakan perangkat lunak untuk mendukung aktivitasnya terutama dalam pemodelan proses bisnis. Pemodelan ini bertujuan untuk memberikan pemahaman yang lebih baik tentang proses bisnis di perusahaan. Salah satu cara untuk memodelkan kebutuhan suatu proses adalah penggunaan Use Case, yang menggambarkan interaksi aktor dengan sistem yang diinginkan. Use Case kemudian harus di breakdown untuk menjelaskan bagaimana sistem ini bekerja (Muchtar, et al. 2011), inilah yang kemudian disebut Use Case Specification. Namun, muncul masalah mengenai perbedaan pemahaman antara orang TI dan orang bisnis. Faktanya, tidak semua pelaku bisnis dapat memahami artifak sistem informasi seperti use case yang ditujukan untuk para pelaku IT, begitu juga sebaliknya. Para pelaku bisnis yang non-IT membutuhkan visualisasi yang lebih mudah dalam menganalisis suatu proses dari berbagai artefak perangkat lunak, yaitu dalam bentuk notasi.
Dalam laporan ini kami menjelaskan pembuatan model proses bisnis dalam BPMN dari Use Case Specification dengan mengurutkan Scenario ID-nya. Berikut adalah penjelasan singkat dari masing-masing artefak yang dilibatkan dalam aplikasi ini. 
1. *Use Case Specification* merupakan deskripsi singkat tentang langkah-langkah yang diperlukan untuk menggambarkan use case, lalu langkah-langkahnya dibuat untuk menambahkan lebih detail yang disebut dengan use case specification.
2. BPMN adalah pendekatan berorientasi grafik yang memodelkan aktivitas proses bisnis berdasarkan flow-nya. 

Secara garis besar, komponen pembentuk dari *Use Case Specification* sebagai *input* yang dihasilkan terbentuk melalui komponen input, yaitu :
1. Use Case Name : Nama Use Case berdasarkan keperluan aktor.
2. Actor : Pelaku dalam proses.
3. Pre-condition : Keadaan sistem yang diperlukan sebelum use case specification di mulai.
4. Post-condition : Keadaan sistem yang diperlukan setelah use case specification di akhiri.
5. Main Scenario (task) : Menunjukkan ketika aktor melakukan aktivitas, sistem harus meresponsnya dengan sesuai. Skenario utama menjelaskan successful case dari Use Case.
6. Extension Scenario (conditional) : Pengecualian dan kasus yang unsuccessful dapat ditambahkan di bagian ekstensions, disebut juga dengan Exceptional Scenario.

Secara garis besar, komponen pembentuk dari BPMN sebagai *output* yang dihasilkan terbentuk melalui komponen input, yaitu :
1. Actor : Actor dari inputan use case specification akan ditampilkan pada pool BPMN
2. Event : Event adalah sesuatu yang "terjadi" selama jalannya Proses. Mempengaruhi aliran dari model dan bisanya memiliki penyebab (trigger) atau dampak (postcondition). Event digambarkan dalam lingkaran terbuka untuk membedakan fungsinya. Ada dua jenis event yang digunakan, berdasarkan pengaruh aliran proses: Start dan End
3. Activity : Aktivitas adalah sebuah istilah umum untuk menampilkan sebuah proses bisnis, suatu inputan task berhubungan dengan task yang lain untuk menjelaskan urutan dari activity.
4. Gateway : Gateway digunakan untuk mengambil dua atau lebih jalur alternatif untuk sebuah proses / task. Gateway akan muncul saat memilih Extension  Scenario (conditional)
5. Sequence flow : Sebuah Arus Urutan digunakan untuk menunjukkan urutan kegiatan yang akan dilakukan dalam proses
6. Pool : Tempat dari sebuah proses tunggal, dimana urutan arus tidak boleh melebihi batas dari pool.

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
1. Download dan install XAMPP
   ```sh
   https://www.apachefriends.org/index.html
   ```
2. Lakukan *clone* atau download secara manual aplikasi UseCaseSpecToBPMN dari repository GitHub. Simpan ke dalam folder XAMPP/htdocs/
   ```sh
   git clone https://github.com/AgileRE-2021/UseCaseSpecToBPMN.git
   ```
3. Buka CMD dan masuk ke folder aplikasi
   ```sh
   cd xampp\htdocs\UseCaseSpecToBPMN\UseCaseSpecToBPMN
   ```
4. Masuk ke dalam *virtual environment* 
   ```sh
   env\Scripts\activate
   ```
5. Lakukan instalasi *Django Framework*
   ```sh
   py -m pip install Django
   ```
6. Lakukan instalasi MySQLClient dengan mengikuti link video dibawah
   ```sh
   https://youtu.be/jo9jZ1GKFmw
   ```
7. Nyalakan Server Apache dan MySQL melalui aplikasi XAMPP
8. Buat sebuah database baru bernama django
9. Lakukan migrasi pada database
   ```sh
   python manage.py makemigrations
   ```
   ```sh
   python manage.py migrate
   ```
10. Jalankan aplikasi pada *localhost*
   ```sh
   py manage.py runserver
   ```
11. Akses Aplikasi melalui browser
   ```sh
   http://127.0.0.1:8000/
   ```
   
# Penjelasan Penggunaan
Petunjuk mengenai prosedur penggunaan aplikasi dapat dilihat pada bagian di bawah ini :
1. Pertama, sistem akan menampilkan halaman login, dimana sebelumnya user harus melakukan sign up akun
![sign in](https://user-images.githubusercontent.com/67141922/124756258-76e78d00-df56-11eb-97e2-5972b7de97d9.png)
![sign up](https://user-images.githubusercontent.com/67141922/124757077-6aafff80-df57-11eb-8666-3b6f0cdfb9d4.png)
2. Setelah log in sistem akan berada pada halaman Welcome Page
![welcome page](https://user-images.githubusercontent.com/67141922/124757109-769bc180-df57-11eb-81b2-c332ddbc71b2.png)
3. Untuk memulai project, klik menu "Project List" pada navbar. Disini akan ditampilkan daftar project use case specification yang telah dibuat
![projectlist](https://user-images.githubusercontent.com/67141922/124757145-80252980-df57-11eb-9b14-25ac62e56631.png)
4.	Untuk menambahkan project baru, klik "Add Project". Setelah itu melengkapi form use case yang ada
![addproject](https://user-images.githubusercontent.com/67141922/124761209-c1b7d380-df5b-11eb-8fdf-7e4107987ddc.png)
5.	Lalu untuk menambahkan scenario pada use case kembali ke halaman Project List dan klik "Scenario"
![projectlist](https://user-images.githubusercontent.com/67141922/124757246-916e3600-df57-11eb-910c-f94dccf429df.png)
6.	Pada halaman ini user dapat memasukkan scenario sesuai data use case specification (tutorial pengisian skenario dijelaskan di sub bab selanjutnya)
![addscenario](https://user-images.githubusercontent.com/67141922/124758432-c929ad80-df58-11eb-86ea-a1a18119a8ff.png)
(Contoh scenario yang telah diisi)
![scenario](https://user-images.githubusercontent.com/67141922/124757282-9af79e00-df57-11eb-8d30-513290520572.png)
7. Kemudian, kembali pada halaman "Project List" dan klik "Generate" untuk melihat hasilnya
![hasil](https://user-images.githubusercontent.com/67141922/124757308-a1861580-df57-11eb-9d55-b98c328747a7.png)
![bpmn](https://user-images.githubusercontent.com/67141922/124757315-a34fd900-df57-11eb-83f1-69e976599a21.png)
8.	Hasil semua generate BPMN akan tersimpan pada menu navbar “BPMN List”
![bpmn list](https://user-images.githubusercontent.com/67141922/124757334-a945ba00-df57-11eb-88fd-6b6a1fc4d63b.png)


### Petunjuk Pengisian Scenario
Sebagai contoh, disini akan dilakukan pengisian scenario dari use case spesifikasi yang berjudul “Edit Profile”
![input1](https://user-images.githubusercontent.com/67141922/124758659-fe360000-df58-11eb-85dd-29ecfc9f797d.png)
![input2](https://user-images.githubusercontent.com/67141922/124758670-00985a00-df59-11eb-94a8-33d4ec428168.png)

Sebelum masuk ke tutorial, berikut hal-hal yang perlu diperhatikan pada tabel pengisian scenario:
- Tiap skenario diberi nomor ID sesuai urutannya.
- Ada dua skenario, yaitu Task dan Conditional. **Task Scenario** adalah **Basic Flows**, sedangkan **Conditional Scenario** digunakan untuk mendefinisikan adanya **Alternative Flows**, yang akan ditampilkan dalam notasi "Gateway" pada BPMN.
- Scenario ID Yes dan Scenario ID No, digunakan untuk menentukan jalur dari skenario yang berasal dari Gateway


1.	User memilih nama project yang akan ditambahkan scenario.
2.	Isi ID scenario (urut dimulai dari 1), lalu memilih scenario type "TASK" pada form "scenariotype".
![scenario task](https://user-images.githubusercontent.com/67141922/124761258-ce3c2c00-df5b-11eb-9c5c-820de2d263c5.png)
3.	Pada ID scenario 1 tidak perlu mengisi "postscenarioidyes" dan "postscenarioidno", langsung isikan deskripsi scenario “memilih menu edit”
![1](https://user-images.githubusercontent.com/67141922/124759356-c24f6a80-df59-11eb-9339-a159df269cad.png)
4.	ID scenario 2 serupa dengan ID scenario 1, isi scenario dengan “sistem menampilkan field untuk mengganti profile”
![2](https://user-images.githubusercontent.com/67141922/124759369-c4b1c480-df59-11eb-8406-541f008cecc4.png)
5.	ID scenario 3 serupa dengan ID scenario 1, isi scenario dengan “mengganti profile yang diinginkan”
![3](https://user-images.githubusercontent.com/67141922/124759387-c8dde200-df59-11eb-8933-09ad74326b4c.png)
6.	Pada data use case specification, terdapat tanda bahwa scenario ID scenario 3 memiliki alternative flows, maka dari itu, sebelum lanjut ke langkah selanjutnya kita perlu mendefinisikan alternative flows yang dilalui.

![3 1](https://user-images.githubusercontent.com/67141922/124759398-caa7a580-df59-11eb-81f0-2074703e92fc.png)

7.	Untuk membuat conditional scenario, kita hanya perlu memilih "Conditional" scenariotype pada form
![3 2](https://user-images.githubusercontent.com/67141922/124761250-cd0aff00-df5b-11eb-89be-5ed57c3f6a1a.png)
8.	Sehingga, ID scenario 4 adalah conditional scenario berupa kalimat pertanyan "Apakah Actor memasukkan field yang diperlukan dengan tepat?"
![4](https://user-images.githubusercontent.com/67141922/124776978-16624b00-df6a-11eb-9812-b9083be860ff.png)
9.	Setelah conditional scenario, pasti ada dua cabang jalur scenario yaitu jawaban "Yes" atau "No".
10.	ID scenario 5 mendefinisikan jalur ke arah Jawaban "Yes" dari pertanyaan ID scenario ke 4
![5](https://user-images.githubusercontent.com/67141922/124776987-17937800-df6a-11eb-9423-72f542de8d84.png)
11.	ID scenario 6 mendefinisikan scenario yang dilanjutkan dari jawaban "Yes", yaitu “profile berhasil terganti dan tersimpan ke dalam database”
![6](https://user-images.githubusercontent.com/67141922/124776995-195d3b80-df6a-11eb-87c2-61cf5aad4f83.png)
12.	Sementara itu, ID scenario 7 mendefinisikan jalur ke arah Jawaban "No" dari pertanyaan ID scenario ke 4
![7](https://user-images.githubusercontent.com/67141922/124777002-19f5d200-df6a-11eb-804b-3586e14ab81a.png)
13.	ID scenario 8 mendefinisikan scenario yang dilanjutkan dari jawaban "No", yaitu “sistem memberikan peringatan keada actor”
![8](https://user-images.githubusercontent.com/67141922/124777008-1b26ff00-df6a-11eb-98ba-42fc194d25ed.png)
14.	ID scenario 9 kembali melanjutkan scenario dari jawaban "No", yaitu “sistem akan mempersilahkan aktor untuk mengisi field dengan tepat”
![9](https://user-images.githubusercontent.com/67141922/124777024-1cf0c280-df6a-11eb-8a93-e069db761617.png)
15.	Sebelum proses diakhiri dengan end event, dalam BPMN perlu menyediakan satu task penghubung antara kedua jalur "Yes" dan "No", yaitu ID scenario 10 yang menyatakan “End of the process”
![10](https://user-images.githubusercontent.com/67141922/124777041-1eba8600-df6a-11eb-95c7-83b0f387c412.png)
17.	Hasil generatenya adalah seperti berikut

![bpmn2](https://user-images.githubusercontent.com/67141922/124759515-e743dd80-df59-11eb-8a18-38fcfca71ec8.png)


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

### Manajemen Proyek
Dalam pelaksanaan proyek, digunakan pengelolaan proyek berbasis Agile yaitu SCRUM.
- Link pengaturan Sprint Board : [Trello Board](https://trello.com/b/yajsJQGM/usepec-to-bpmn)
- Link hasil tester dataset : [Dataset Result](https://drive.google.com/file/d/1wd1QIzrmChM0YwXYnG5mf-fQaUhE-mR1/view?usp=sharing)

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
