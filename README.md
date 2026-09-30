# My Portfolio

Website portfolio pribadi yang dibuat menggunakan HTML5, CSS3, dan Django. Website ini berisi informasi profil pribadi, riwayat pendidikan, pengalaman, dan project.

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

### Tugas 4

Pada Tugas 4, saya melanjutkan website portfolio Django dari Tugas 3 dengan menerapkan authentication, authorization, session, cookie, serta fitur interaktif pemberian star pada project.

Beberapa perubahan yang saya implementasikan meliputi:

- Menambahkan role `Editor` menggunakan Django Group melalui Django Admin.

- Menerapkan pembatasan hak akses berdasarkan role pengguna.

- Superuser dapat membuat, mengubah, dan menghapus data portfolio.

- Editor dapat mengubah data portfolio tetapi tidak dapat membuat atau menghapus data.

- Pengguna biasa hanya dapat membaca data portfolio dan memberikan atau membatalkan star pada project.

- Pengunjung yang belum login harus melakukan login sebelum melakukan tindakan yang membutuhkan akun.

- Menerapkan pengecekan hak akses pada sisi server menggunakan `login_required` dan pengecekan role untuk menghasilkan HTTP 403 pada tindakan yang tidak diizinkan.

- Menyembunyikan tombol create, update, dan delete pada template untuk pengguna yang tidak memiliki hak akses.

- Menambahkan relasi `ManyToManyField` antara model `Project` dan model `User` untuk menyimpan pengguna yang memberikan star.

- Mengimplementasikan fitur star dan unstar menggunakan request `POST` dengan `{% csrf_token %}`.

- Menampilkan jumlah total star dan status star pengguna pada setiap project.

- Memastikan endpoint JSON dari tugas sebelumnya tetap berfungsi dan tidak mengembalikan informasi pengguna yang memberikan star.

#### AI Disclosure

Dalam pengerjaan Tugas 4, saya menggunakan ChatGPT sebagai alat bantu untuk memahami konsep authentication dan authorization pada Django, memahami penggunaan Django Group, membantu menganalisis struktur kode, serta membantu melakukan debugging dan pengujian implementasi.

AI digunakan untuk membantu pada bagian:

- Memahami penggunaan Django Group sebagai role `Editor`.

- Membantu menyusun dan memeriksa pengecekan authorization pada `views.py`.

- Membantu menyusun routing untuk fitur update project.

- Membantu menyesuaikan template agar kontrol create, update, dan delete tampil sesuai role pengguna.

- Membantu mengimplementasikan dan memeriksa fitur star dan unstar menggunakan `ManyToManyField`.

- Membantu menganalisis dan memperbaiki endpoint JSON agar tidak membocorkan informasi pengguna yang memberikan star.

- Membantu menyusun dan memperluas unit test untuk menguji authentication, authorization, fitur star, dan endpoint JSON.

- Membantu menganalisis error yang ditemukan selama implementasi dan pengujian.

Setelah mendapatkan bantuan dari AI, saya menerapkan perubahan pada project, menjalankan aplikasi secara langsung, melakukan pengujian melalui browser, memeriksa hasil authorization untuk beberapa jenis pengguna, menjalankan migration, dan menjalankan unit test menggunakan `python manage.py test`.

Saya tetap melakukan penyesuaian manual terhadap kode berdasarkan struktur project yang saya gunakan. Beberapa saran dari AI juga perlu disesuaikan setelah diuji agar sesuai dengan routing, template, model, dan fitur yang sudah ada pada project.

#### Strategi Prompting

Saya menggunakan prompting secara bertahap selama pengerjaan Tugas 4. Saya memberikan konteks berupa kode, screenshot hasil implementasi, pesan error, dan requirement tugas kepada ChatGPT. Setelah itu, saya meminta AI untuk menjelaskan penyebab masalah atau memberikan contoh perubahan kode yang sesuai dengan struktur project.

Saya tidak langsung menerapkan semua saran yang diberikan. Setiap perubahan saya simpan dan uji terlebih dahulu melalui browser, Django development server, serta unit test. Jika hasilnya belum sesuai, saya memberikan kondisi terbaru kepada AI untuk dianalisis kembali dan kemudian melakukan penyesuaian manual.

#### Log Prompting

Beberapa contoh prompt yang saya gunakan selama pengerjaan Tugas 4:

1. Meminta penjelasan mengenai cara menerapkan role `Editor` menggunakan Django Group.

2. Meminta bantuan membatasi akses create, update, dan delete berdasarkan role pengguna.

3. Meminta bantuan memperbaiki routing dan form agar halaman edit project tidak diarahkan ke endpoint create.

4. Meminta bantuan memeriksa fitur star dan relasi `ManyToManyField` dengan model `User`.

5. Meminta bantuan menganalisis endpoint JSON yang masih mengembalikan informasi `starred_by`.

6. Meminta bantuan menyusun dan memeriksa unit test untuk authentication, authorization, star, dan API.

7. Memberikan screenshot hasil pengujian seperti HTTP 403 dan redirect ke halaman login untuk memastikan implementasi sesuai requirement.

#### Keterbatasan dan Evaluasi Penggunaan AI

Penggunaan AI membantu saya memahami konsep authorization dan debugging dengan lebih cepat, tetapi solusi yang diberikan tidak selalu dapat langsung diterapkan. Saya perlu memeriksa kembali apakah perubahan yang disarankan sesuai dengan struktur project dan requirement tugas.

Saya melakukan verifikasi melalui pengujian langsung. Sebagai contoh, saya menguji perbedaan hak akses antara superuser, editor, pengguna biasa, dan pengunjung yang belum login. Saya juga menjalankan unit test untuk memastikan fitur yang ditambahkan tidak merusak implementasi sebelumnya.

### Tugas 5

1. **Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**

   Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan suatu aktivitas selama waktu tertentu. Pada fitur pencarian AJAX, debouncing digunakan agar request ke server tidak dikirim setiap kali pengguna mengetik satu karakter. Dengan memberikan jeda, misalnya 300 milidetik, request hanya dikirim setelah pengguna berhenti mengetik. Hal ini dapat mengurangi jumlah request ke server dan membuat penggunaan fitur pencarian menjadi lebih efisien.

2. **Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**

   `await` digunakan untuk menunggu sampai Promise yang dihasilkan oleh `fetch()` selesai sebelum kode berikutnya dijalankan. Dengan menggunakan `await`, hasil dari `fetch()` dapat digunakan secara langsung sebagai sebuah nilai sehingga alur program lebih mudah dibaca dan dipahami. Jika `await` tidak digunakan, `fetch()` akan mengembalikan Promise dan kode berikutnya dapat berjalan sebelum response dari server selesai diterima. Jika ingin mengambil hasilnya, Promise tersebut perlu ditangani menggunakan `.then()` atau mekanisme asynchronous lainnya.

3. **Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!**

   XSS (Cross-Site Scripting) adalah serangan ketika data yang mengandung kode HTML atau JavaScript berbahaya berhasil dimasukkan ke dalam halaman dan kemudian dijalankan oleh browser pengguna. Data yang ditampilkan melalui AJAX/JavaScript lebih berisiko ketika langsung dimasukkan ke dalam `innerHTML` karena proses tersebut tidak otomatis mendapatkan auto-escaping dari template Django. Oleh karena itu, data yang berasal dari server perlu di-escape terlebih dahulu, misalnya menggunakan fungsi `escapeHtml()`, sehingga karakter HTML tidak diperlakukan sebagai kode yang dapat dieksekusi.

#### AI Disclosure

Dalam pengerjaan Tugas 5, saya menggunakan ChatGPT sebagai alat bantu pembelajaran, debugging, pemahaman konsep JavaScript dan AJAX, serta membantu memeriksa implementasi pada project portfolio Django.

AI digunakan untuk membantu pada bagian:

- Memahami konsep AJAX dan Fetch API.

- Memahami implementasi pencarian data menggunakan `fetch()`.

- Menerapkan pencarian berdasarkan field `title` pada halaman Experience.

- Menerapkan debouncing dengan jeda 300 milidetik agar request pencarian tidak dikirim untuk setiap karakter.

- Menggunakan `AbortController` untuk membatalkan request pencarian sebelumnya yang belum selesai.

- Menyusun fungsi JavaScript untuk mengambil data Experience dari endpoint JSON dan merender data secara dinamis.

- Membuat fungsi `escapeHtml()` untuk melakukan escaping terhadap data yang dimasukkan melalui `innerHTML`.

- Menerapkan modal menggunakan Popover API.

- Membuat submit form tambah Experience menggunakan AJAX tanpa reload halaman.

- Menambahkan pengiriman CSRF token melalui header `X-CSRFToken`.

- Menangani response HTTP `201`, `400`, dan `403` pada endpoint AJAX.

- Mengintegrasikan toast notification untuk kondisi berhasil dan gagal.

- Menambahkan sanitasi server-side menggunakan `strip_tags` melalui method `clean_title`, `clean_description`, dan `clean_category` pada `ExperienceForm`.

- Membantu menganalisis dan memperbaiki error pada `views.py`, `urls.py`, `forms.py`, `experience.html`, `experience_form.html`, `experience_form_modal.html`, dan `experience.js`.

Setelah mendapatkan bantuan dari AI, saya menerapkan perubahan pada project dan menguji hasilnya secara langsung melalui browser dan Django development server.

#### Strategi Prompting

Saya menggunakan prompting secara bertahap selama pengerjaan Tugas 5. Saya memberikan konteks berupa kode yang sedang digunakan, screenshot halaman, hasil pengujian, dan pesan error kepada ChatGPT. Kemudian saya meminta AI untuk menjelaskan penyebab masalah dan memberikan perubahan kode yang sesuai dengan struktur project.

Ketika solusi awal belum menghasilkan perilaku yang sesuai, saya memberikan kondisi terbaru atau screenshot hasil pengujian kepada AI dan meminta analisis kembali. Dengan cara tersebut, saya menggunakan AI sebagai pendamping debugging dan pembelajaran, bukan hanya untuk menghasilkan kode.

#### Bagian yang Dibantu AI

Bagian yang dibantu AI pada Tugas 5 meliputi:

- Implementasi endpoint JSON untuk Experience.

- Implementasi pencarian Experience berdasarkan `title`.

- Implementasi debouncing dan `AbortController`.

- Implementasi rendering Experience menggunakan JavaScript.

- Implementasi modal tambah Experience menggunakan Popover API.

- Implementasi submit Experience melalui AJAX.

- Implementasi CSRF pada request POST.

- Implementasi toast notification untuk response berhasil dan gagal.

- Implementasi escaping menggunakan `escapeHtml()`.

- Implementasi sanitasi server-side menggunakan `strip_tags`.

- Debugging integrasi antara template Django, JavaScript, view, form, dan URL.

#### Log Prompting

Beberapa contoh prompt yang saya gunakan selama pengerjaan Tugas 5:

1. Meminta bantuan menerapkan AJAX pada halaman Experience agar data tidak perlu dimuat melalui render template secara langsung.

2. Meminta bantuan membuat pencarian Experience berdasarkan judul menggunakan `fetch()`.

3. Meminta bantuan menerapkan debouncing pada pencarian agar request hanya dikirim setelah pengguna berhenti mengetik.

4. Meminta bantuan memperbaiki penggunaan `AbortController` pada request pencarian.

5. Meminta bantuan membuat modal tambah Experience menggunakan Popover API dengan struktur yang konsisten dengan modal Project.

6. Meminta bantuan membuat submit form tambah Experience menggunakan AJAX dan `FormData`.

7. Meminta bantuan memperbaiki pemanggilan `showToast()` agar toast sukses menggunakan tipe `success` dan toast error menggunakan tipe `error`.

8. Meminta bantuan menerapkan sanitasi server-side pada `ExperienceForm`.

9. Meminta bantuan melakukan pengujian XSS dan memastikan payload HTML tidak dieksekusi.

10. Meminta bantuan memeriksa request AJAX melalui Chrome DevTools pada tab Network, termasuk status HTTP `201` dan header `X-CSRFToken`.

#### Keterbatasan dan Evaluasi Penggunaan AI

Saya menemukan bahwa solusi dari AI tidak selalu dapat langsung diterapkan pada project. Beberapa bagian harus disesuaikan dengan struktur project yang sudah ada, terutama hubungan antara view, URL, template, form, dan JavaScript.

Sebagai contoh, pada implementasi awal terdapat masalah pada pemanggilan fungsi `showToast()` karena urutan parameter yang digunakan tidak sesuai dengan struktur fungsi toast yang ada. Setelah diuji melalui browser, saya memperbaiki pemanggilan tersebut agar parameter title, message, dan type dikirim dengan benar.

Saya juga melakukan pengujian manual terhadap validasi server dan XSS. Saya menguji input judul berupa tag HTML berbahaya pada local project dan memastikan server menolaknya, toast error muncul, dan tidak ada JavaScript yang dieksekusi. Selain itu, saya memeriksa request AJAX melalui Chrome DevTools untuk memastikan request `POST` berhasil dengan status `201`, diikuti request `GET` ke endpoint Experience, serta memastikan header `X-CSRFToken` ikut dikirim.

AI membantu mempercepat proses memahami konsep dan menemukan kemungkinan penyebab masalah, tetapi hasil akhir tetap saya verifikasi dengan menjalankan aplikasi dan menguji fitur secara langsung.

#### Progress Pengerjaan

Pada Tugas 5, saya melanjutkan halaman Experience dari Tugas 3 dan Tugas 4 dengan menerapkan interaktivitas menggunakan JavaScript dan AJAX.

Pertama, saya membuat endpoint JSON untuk mengambil data Experience dan menambahkan pencarian berdasarkan judul. Setelah itu saya menerapkan debouncing dan `AbortController` agar pencarian berjalan lebih efisien dan request sebelumnya dapat dibatalkan ketika diperlukan.

Selanjutnya saya mengubah proses rendering Experience agar data diambil secara dinamis melalui JavaScript. Karena data AJAX dimasukkan menggunakan `innerHTML`, saya menambahkan fungsi `escapeHtml()` untuk melakukan escaping pada data yang ditampilkan.

Saya kemudian membuat modal tambah Experience menggunakan Popover API. Form di dalam modal dikirim menggunakan AJAX sehingga Experience baru dapat ditambahkan tanpa melakukan reload halaman. Response server ditangani berdasarkan status HTTP dan hasilnya ditampilkan menggunakan toast notification.

Sebagai bagian dari keamanan, saya menambahkan sanitasi input pada sisi server menggunakan `strip_tags` melalui method `clean_<field>` pada `ExperienceForm`. Saya juga melakukan pengujian XSS pada local project untuk memastikan input HTML berbahaya tidak dieksekusi.

Setelah seluruh fitur selesai, saya melakukan pengujian melalui browser dan Chrome DevTools. Request `POST` ke endpoint AJAX berhasil menghasilkan status `201`, kemudian halaman melakukan request `GET` ke endpoint Experience untuk memperbarui daftar data tanpa reload. Header `X-CSRFToken` juga diperiksa melalui tab Network untuk memastikan token CSRF ikut terkirim.

### AI Disclosure - General

Dalam seluruh pengerjaan project portfolio selama semester, saya menggunakan ChatGPT sebagai alat bantu pembelajaran, debugging, pemahaman konsep, dan dokumentasi. Saya tetap melakukan implementasi, pengujian, penyesuaian kode, dan verifikasi hasil secara langsung pada project.

AI tidak saya gunakan sebagai pengganti proses pengujian. Setiap perubahan yang dibantu AI diperiksa kembali melalui kode sumber, Django development server, browser, DevTools, dan pengujian lain yang relevan dengan tugas.

Saya memahami bahwa output AI dapat mengandung kesalahan atau tidak sesuai dengan struktur project yang sedang digunakan. Oleh karena itu, saya melakukan evaluasi terhadap setiap saran dan menyesuaikannya secara manual sebelum digunakan sebagai bagian dari implementasi akhir.