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
![addproject](https://user-images.githubusercontent.com/67141922/124757216-8adfbe80-df57-11eb-8ab2-b8aefc7ae534.png)
5.	Lalu untuk menambahkan scenario pada use case kembali ke halaman Project List dan klik "Scenario"
![projectlist](https://user-images.githubusercontent.com/67141922/124757246-916e3600-df57-11eb-910c-f94dccf429df.png)
6.	Pada halaman ini user dapat memasukkan scenario sesuai data use case specification (tutorial pengisian skenario dijelaskan di sub bab selanjutnya)
![addscenario](https://user-images.githubusercontent.com/78306501/124612538-9ae69800-de9c-11eb-856b-f2c34f6e03bc.PNG)
(Contoh scenario yang telah diisi)
![scenario](https://user-images.githubusercontent.com/67141922/124757282-9af79e00-df57-11eb-8d30-513290520572.png)
7. Kemudian, kembali pada halaman "Project List" dan klik "Generate" untuk melihat hasilnya
![hasil](https://user-images.githubusercontent.com/67141922/124757308-a1861580-df57-11eb-9d55-b98c328747a7.png)
![bpmn](https://user-images.githubusercontent.com/67141922/124757315-a34fd900-df57-11eb-83f1-69e976599a21.png)
8.	Hasil semua generate BPMN akan tersimpan pada menu navbar “BPMN List”
![bpmn list](https://user-images.githubusercontent.com/67141922/124757334-a945ba00-df57-11eb-88fd-6b6a1fc4d63b.png)


### Petunjuk Pengisian Scenario
Sebagai contoh akan digunakan project "Student Applies For Thesis"
![scenario](https://user-images.githubusercontent.com/78306501/124612538-9ae69800-de9c-11eb-856b-f2c34f6e03bc.PNG)
Dimana hasil generatenya adalah seperti berikut :
![hasil](https://user-images.githubusercontent.com/78306501/124613729-be5e1280-de9d-11eb-9c16-722914bec570.PNG)

1. Untuk membuat task user dapat mengisi form scenario seperti dibawah
![task](https://user-images.githubusercontent.com/78306501/124615703-b8693100-de9f-11eb-88c0-c2317be2a09a.PNG)
User memilih project mana yang akan ditambahkan scenario, lalu mengisi ID (urut yang dimulai dari 1), lalu memilih scenario type "TASK" pada form "scenariotype", tidak mengisi form "postscenarioidyes" dan "postscenarioidno", dan terakhir mengisi deskripsi task.
2. Untuk membuat conditional
![conditional](https://user-images.githubusercontent.com/78306501/124616666-7a204180-dea0-11eb-93fc-14485f602f3c.PNG)
User memilih project mana yang akan ditambahkan scenario, lalu mengisi ID (urut yang dimulai dari 1), lalu memilih scenario type "CONDITIONAL" pada form "scenariotype", tidak mengisi form "postscenarioidyes" dan "postscenarioidno", dan terakhir mengisi deskripsi conditional dengan kalimat tanya. Namun task setelahnya dapat dibuat dengan pengisian form seperti berikut:
![conditional2](https://user-images.githubusercontent.com/78306501/124617238-f87ce380-dea0-11eb-839e-377b0822c472.png)
Dimana ID 3 dan 4 adalah hasil dari kondisi "Form Fill Correctly" yang telah didefinisikan pada ID 3 dan hasilnya adalah task ID 4 yaitu "Systemacknowledges receipt of data on screen and by e-mail". Lalu ID 5 dan 6 adalah hasil dari kondisi "Wrong answer" yang telah didefinisikan pada ID 5 dan hasilnya adalah task ID 6 yaitu "Form is not filled out completely".
3. Namun untuk kasus seperti berikut :
![kasus2](https://user-images.githubusercontent.com/78306501/124618196-ca4bd380-dea1-11eb-8592-2eddab3c3347.PNG)

Perlu diberikan task "Selsai" untuk menyatukan cabang kondisi yang telah dibuat sebelum end. Berikut scenarionya :
![hasilkasus2](https://user-images.githubusercontent.com/78306501/124618447-fe26f900-dea1-11eb-8537-f391e07a6fe8.PNG)


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
- Link hasil tester dataset : [Dataset Result](https://drive.google.com/file/d/1DgQO7LENr08Ky3M-HFDzjiKq6Id2zIOa/view?usp=sharing)

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
