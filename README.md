# My Portfolio

Website portfolio pribadi yang dibuat menggunakan HTML5, CSS3, dan Django. Website ini berisi informasi profil pribadi dan riwayat pendidikan.

## Identitas

- Nama: I Komang Arka Darma Laksana
- NPM: 2506656791
- Kelas: PBP D

## Teknologi yang Digunakan

- HTML5
- CSS3
- Django
- Git dan GitHub

### Tugas 1

1. Pada website portfolio saya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<main>`, `<section>`, `<article>`, dan `<footer>`. Saya menggunakan `<section>` untuk memisahkan bagian Profile dan Education karena kedua bagian tersebut memiliki jenis informasi yang berbeda. Saya juga menggunakan `<article>` untuk setiap riwayat pendidikan karena setiap riwayat dapat dianggap sebagai satu informasi yang berdiri sendiri. Penggunaan elemen semantik membantu membuat struktur HTML lebih terorganisir dan mudah dipahami. Selain itu, struktur tersebut membuat kode lebih mudah dibaca dan memudahkan pengembangan ketika website nantinya memiliki bagian atau konten tambahan.

2. Tantangan utama yang saya temukan ketika membuat CSS responsive adalah mempertahankan struktur dan keterbacaan halaman ketika ukuran layar berubah dari desktop ke mobile. Pada tampilan desktop, beberapa informasi dapat ditempatkan secara berdampingan karena tersedia ruang yang lebih luas. Namun, pada mobile, layout tersebut dapat menjadi terlalu sempit sehingga susunan elemen perlu disesuaikan. Saya mengevaluasi setiap elemen berdasarkan ukuran dan kepentingannya pada halaman. Elemen yang berisi informasi utama saya prioritaskan agar tetap mudah dibaca, sedangkan layout yang sebelumnya horizontal saya ubah menjadi lebih sederhana dan vertikal menggunakan media query. Dari proses ini saya memahami bahwa responsive design tidak hanya mengubah ukuran elemen, tetapi juga menyesuaikan posisi dan struktur layout dengan ukuran layar.

3. Karena website yang dibuat masih berupa static web, salah satu keterbatasannya adalah informasi portfolio masih ditulis secara langsung di dalam kode. Jika saya ingin mengubah data pendidikan atau menambahkan informasi baru, saya perlu mengubah file HTML atau template secara manual. Website juga belum memiliki database dan fitur pengelolaan data sehingga konten belum dapat diperbarui secara dinamis. Pada iterasi berikutnya, saya ingin menggunakan database Django untuk menyimpan informasi portfolio seperti pendidikan dan project. Dengan begitu, data dapat dikelola secara lebih terstruktur dan ditampilkan secara dinamis tanpa harus mengubah template setiap kali terdapat perubahan informasi.

## AI Disclosure

Dalam pengerjaan Tugas 1 ini, saya menggunakan ChatGPT sebagai alat bantu pembelajaran, debugging, dan pemahaman konsep.

AI saya gunakan untuk membantu:

- memahami struktur HTML5 dan penggunaan elemen semantik;
- memahami konsep CSS responsive design;
- menganalisis masalah pada tampilan website;
- memahami struktur project Django;
- memahami penggunaan Git, branch, commit, dan remote;
- membantu proses deployment project ke PWS;
- memahami instruksi dan rubrik tugas;
- membantu menyusun dan memperbaiki dokumentasi README.

AI tidak saya gunakan sebagai pengganti proses pengujian. Setelah mendapatkan penjelasan atau saran, saya menerapkannya pada project dan melakukan pengujian secara langsung pada browser, GitHub, dan PWS. Jika hasilnya belum sesuai dengan yang diinginkan, saya melakukan penyesuaian kembali terhadap kode.

### Strategi Prompting

Saya menggunakan prompting secara bertahap sesuai dengan masalah yang saya temukan selama pengerjaan. Ketika mengalami kesulitan, saya memberikan konteks berupa kode, screenshot, atau penjelasan mengenai kondisi yang terjadi, kemudian meminta AI untuk menjelaskan penyebab masalah dan memberikan langkah penyelesaian.

Jika solusi yang diberikan belum berhasil, saya memberikan hasil terbaru kepada AI dan meminta analisis lebih lanjut. Dengan cara tersebut, saya menggunakan AI sebagai alat bantu untuk memahami proses pemecahan masalah, bukan hanya meminta AI menghasilkan keseluruhan project.

### Bagian yang Dibantu AI

Bagian yang dibantu AI meliputi pemahaman struktur kode HTML, CSS, dan Django, debugging layout responsive, penggunaan Git dan branching, serta proses deployment ke PWS.

Dalam proses Git, AI membantu saya memahami cara memisahkan pekerjaan Tugas 1 dari Tutorial 1 menggunakan branch `tugas-1`. Dalam proses deployment, AI membantu saya memahami cara mengirim branch tersebut ke repository PWS dan melakukan deployment melalui PWS.

### Log Prompting
Beberapa contoh prompt yang saya gunakan selama pengerjaan :

1. Meminta penjelasan mengenai struktur kode dan hubungan antar file pada project.
2. Meminta penjelasan mengenai penggunaan elemen semantik HTML5 seperti `<section>` dan `<article>`.
3. Meminta bantuan memahami dan memperbaiki layout responsive menggunakan CSS.
4. Meminta bantuan ketika tampilan website belum sesuai dengan desain yang diinginkan.
5. Meminta penjelasan mengenai penggunaan branch Git untuk memisahkan Tugas 1 dari Tutorial 1.
6. Meminta bantuan melakukan deployment branch `tugas-1` ke PWS.
7. Meminta bantuan memahami instruksi dan rubrik tugas serta memperbaiki dokumentasi README.

Percakapan dengan AI digunakan sebagai referensi selama proses pengerjaan, sedangkan implementasi akhir tetap saya terapkan, jalankan, dan uji sendiri pada project.

### Keterbatasan dan Evaluasi Penggunaan AI

Saya menyadari bahwa jawaban dari AI tidak selalu dapat langsung diterapkan ke dalam project. Beberapa solusi yang diberikan perlu disesuaikan dengan struktur kode dan kondisi project yang saya gunakan. Karena itu, saya tidak langsung menganggap solusi dari AI sebagai solusi akhir.

Saya melakukan pengecekan secara manual dengan menjalankan website, melihat hasil perubahan pada browser, dan memeriksa kembali kode yang digunakan. Ketika solusi AI belum menghasilkan tampilan atau perilaku yang sesuai, saya melakukan perubahan pada kode dan mencoba kembali sampai mendapatkan hasil yang sesuai dengan kebutuhan tugas.

Menurut saya, penggunaan AI paling membantu ketika digunakan untuk menjelaskan konsep dan membantu menemukan kemungkinan penyebab masalah. Namun, pemahaman terhadap kode dan pengujian tetap diperlukan agar solusi yang digunakan benar-benar sesuai dengan project.

### Progress Pengerjaan

Pengerjaan Tugas 1 dilakukan secara bertahap. Saya mulai dengan memahami struktur project dari Tutorial 01, kemudian menambahkan bagian Education dan menyesuaikan struktur HTML menggunakan elemen semantik. Setelah itu saya mengembangkan tampilan menggunakan CSS dan menyesuaikannya agar responsive pada ukuran layar yang berbeda.

Setelah implementasi selesai, saya melakukan pengujian pada browser dan melakukan perbaikan terhadap tampilan. Saya kemudian menggunakan Git untuk memisahkan pekerjaan Tugas 1 ke branch `tugas-1`, melakukan commit, dan melakukan deployment hasil akhir ke PWS.

Penggunaan branch `tugas-1` juga membantu menjaga hasil Tutorial 01 tetap terpisah dari perubahan yang dibuat untuk Tugas 1.

### Tugas 2

1. Ketika pengguna membuka halaman portfolio baru, browser mengirimkan request ke URL `/projects/`. Request tersebut diterima oleh `urls.py` pada level project dan diteruskan ke `urls.py` pada aplikasi `main`. Pada `main/urls.py`, URL `/projects/` diarahkan ke view `show_projects`. View tersebut mengambil data dari model `Project` menggunakan `Project.objects.all()`, kemudian memasukkannya ke dalam context dengan nama `project_list`. Context tersebut diteruskan ke template `projects.html`. Template menggunakan Django Template Language untuk melakukan perulangan terhadap data Project dan menampilkan setiap object. Jika tidak terdapat data, template menampilkan pesan kondisi kosong. Setelah template selesai dirender, HTML dikirim kembali ke browser.

2. Data bagian portfolio baru sebaiknya disimpan pada model karena model menyediakan struktur data yang tersimpan secara terorganisir di database. Jika data ditulis langsung di dalam template, perubahan data mengharuskan pengubahan kode HTML. Dengan menggunakan model, data dapat ditambah, diubah, atau dihapus tanpa mengubah template. Pendekatan ini membuat aplikasi lebih mudah dipelihara dan dikembangkan ketika jumlah data bertambah atau data perlu digunakan oleh bagian aplikasi lainnya.

3. `makemigrations` digunakan untuk membuat file migration berdasarkan perubahan pada model, sedangkan `migrate` digunakan untuk menerapkan migration tersebut ke database. Pada tugas ini, saya menambahkan model `Project` dengan field `name`, `description`, dan `technology`. Saya kemudian menjalankan `python manage.py makemigrations` untuk membuat migration `0002_project.py`, lalu menjalankan `python manage.py migrate` untuk menerapkan perubahan struktur database tersebut.

#### AI Disclosure

Dalam pengerjaan Tugas 2, saya menggunakan ChatGPT sebagai alat bantu untuk memahami instruksi tugas, memahami alur Model-View-Template (MVT) pada Django, serta membantu memeriksa dan memperbaiki implementasi kode.

Bagian yang dibantu oleh AI meliputi:
- Menentukan struktur model `Project` dengan minimal tiga field selain primary key.
- Membantu menyusun view `show_projects` yang mengambil data dari model dan meneruskannya melalui context.
- Membantu menyusun routing untuk halaman `/projects/`.
- Membantu menyusun template `projects.html` dengan Django Template Language, termasuk perulangan data dan kondisi ketika database kosong.
- Membantu menyusun unit test untuk menguji akses URL, tampilan data Project, dan kondisi ketika belum ada data.
- Membantu memeriksa error dan memastikan seluruh unit test berhasil dijalankan.

Saya tetap menjalankan kode, memeriksa hasil pada browser, menjalankan migration, menjalankan unit test, dan memverifikasi hasil implementasi secara langsung.

Strategi prompting yang digunakan adalah memberikan konteks kode yang sedang dikerjakan, meminta bantuan secara bertahap pada setiap bagian MVT, kemudian memeriksa hasil setiap perubahan sebelum melanjutkan ke tahap berikutnya. AI digunakan sebagai pendamping untuk memahami dan memeriksa implementasi, bukan sebagai pengganti proses pengujian dan verifikasi kode.

Riwayat percakapan dengan AI digunakan sebagai log proses bantuan selama pengerjaan tugas.

### Tugas 3

1. `ModelForm` digunakan pada Django karena dapat membuat form berdasarkan model yang sudah didefinisikan sehingga proses pembuatan form menjadi lebih praktis dan konsisten dengan struktur data pada database. `ModelForm` juga membantu melakukan validasi data sebelum data disimpan ke database. Dibandingkan membuat form HTML secara manual, penggunaan `ModelForm` mengurangi kode yang harus ditulis dan mempermudah proses create maupun update data. Sementara itu, `{% csrf_token %}` wajib ditambahkan pada form yang melakukan request `POST` untuk memberikan perlindungan terhadap serangan Cross-Site Request Forgery (CSRF). Token tersebut memastikan request berasal dari form yang valid pada aplikasi.

2. JSON lebih banyak digunakan dalam pengembangan aplikasi web modern karena formatnya lebih sederhana, ringan, dan mudah dibaca oleh manusia maupun mesin. Struktur JSON juga dekat dengan struktur data yang digunakan dalam banyak bahasa pemrograman, sehingga cocok digunakan untuk komunikasi antara frontend dan backend melalui API. Dibandingkan XML, JSON umumnya membutuhkan lebih sedikit karakter untuk merepresentasikan data sehingga lebih ringkas dan lebih praktis untuk pertukaran data pada aplikasi web.

3. Saat data portfolio dikembalikan dalam bentuk JSON, data dari model Django terlebih dahulu diambil dari database menggunakan query terhadap model. Setelah itu, data tersebut dilakukan `serialization` menggunakan serializer Django agar objek model dapat diubah menjadi format JSON. JSON tersebut kemudian dikembalikan melalui `HttpResponse` dengan `content_type="application/json"`. Proses serialization diperlukan karena objek model Django tidak dapat langsung dikirim sebagai JSON. Serialization mengubah objek dan field-field pada model menjadi representasi data yang dapat dikirim dan diproses sebagai JSON. Pada halaman Experience, JSON tersebut kemudian dilakukan `deserialization` kembali menjadi objek Python agar datanya dapat digunakan dan ditampilkan pada template HTML.

### AI Disclosure

Dalam pengerjaan Tugas 3, saya menggunakan ChatGPT sebagai alat bantu untuk memahami requirement tugas, menjelaskan konsep Django seperti `ModelForm`, serialization/deserialization JSON, template inheritance, serta membantu menyusun dan melakukan debugging pada beberapa bagian implementasi.

AI digunakan untuk membantu pada bagian:
- Perancangan `ExperienceForm` pada `forms.py`.
- Penambahan fungsi create, update, delete, serialization, dan deserialization pada `views.py`.
- Penambahan routing pada `urls.py`.
- Refactoring template menggunakan `{% extends "base.html" %}`.
- Penyusunan dan perbaikan tampilan form serta modal konfirmasi delete pada HTML dan CSS.
- Membantu menganalisis error dan memeriksa hasil implementasi selama pengujian.

Seluruh implementasi tetap diuji secara manual pada project Django melalui browser dan `python manage.py check`. Saya juga melakukan penyesuaian manual terhadap kode, struktur template, CSS, dan alur fitur setelah hasil pengujian.