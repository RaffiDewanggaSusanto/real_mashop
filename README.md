https://raffi-dewangga-realmashop.pbp.cs.ui.ac.id/

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
Saya mengerjakan setiap bagiman checklist dengan mengingat kembali bagaimana saya menyelesaikan tutorial-tutorial sebelumnya, jika saya lupa cara untuk melakukan sesuatu maka saya akan kembali ke halaman tutorial atau bertanya kepada teman-teman saya.

Saya memulai dengan membuat project Django. Pertama saya membuat direktori baru yang akan digunakan untuk menambahkan project ke github. Direktori ini dihubungkan ke github menggunakan git remote add (dengan link git). Selanjutnya jika ada perubahan pada code saya dapat menambahkannya ke github dengan commit dan push. Selanjutnya saya melakukan instalasi Django dengan membuat requirements berisi al-hal yang diperlukan untuk instalasi Django. Lalu pada terminal saya menjalankan django-admin startproject real_mashop (nama file) . untuk membuat project django ini.

Kemudian saya membuat file .env untuk menyimpan informasi konfigurasi seperti credential database, API keys, atau pengaturan environment. File ini digunakan agar code ini dapat berjalan di environment tanpa perlu mengupdate codenya. Saya juga membuat file .env.prod dengan production = true, aplikasi akan menggunakan database PostGre SQL. Kemudian isi dari settings.py perlu diubah agar env bisa diload dari env filenya.

Lalu saya menambahkan project ke dalam git dengan git add ., git commit -m "pesan", dan git push origin master.Kemudian saya menghubungkan PWS dengan menambahkan kode URL deployment PWS pada list ALLOWED_HOST pada settings.py sehingga PWS menjadi host.

Setelah melakukan hal-hal tersebut, saya mulia membuat aplikasi dengan nama "main" dan nama toko "real_mashop". Aplikasi ini adalah aplikasi mengenai sportswear, maka model-model di models.py perlu diubah sesuai dengan ketentuan pada tugas. Pada bagian ini terdapat tipe-tipe data tertentu yang digunakan:
CharField --> untuk menyimpan teks pendek
TextField --> untuk menyimpan teks panjang
IntegerField --> untuk menyimpan angka bulat
URLField --> untuk menyimpan url
BooleanField --> untuk true or false

Kemudian saya membuat template HTML dengan nama main.html. Page ini berisi konten seperti nama toko, nama, dan kelas yang kemudian akan ditampilkan menggunakan routing. Routing dilakukan menggunakan file views.py dan urls.py. Views.py untuk memproses permintaan dan mengirimkan respons (context) dan urls.py untuk menentukan URL yang digunakan. Di dalam main.html digunakan sintaks Django seperti {{ aplikasi }}, {{ name }}, {{ class }}, yang disebut template variables untuk menampilkan nilai dari variabel dalam context.

Setelah proses routing, selanjutnya project akan dideploy pada PWS menggunakan git add ., git commit -m "pesan", git push origin master, git push pws master. Proses pembuatan aplikasi main sudah selesai. 


# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](image.png) https://www.biznetgio.com/news/django (bagan terdapat pada link)
Client akan melakukan request yang diterima oleh URL. Kemudian akan dipilih views yang sesuai. Kemudian views akan berinteraksi dengan model untuk mengelola data di database, yang kemudian akan memilih template yang sesuai untuk memberikan halaman web kepada client. urls.py digunakan utnuk memetakan pola URL ke fungsi, views.py menangani permintaan (memproses input), models.py digunakan untuk membaca atau menulis ke database, dan berkas html digunakan sebagai template tampilan.

# Jelaskan peran settings.py dalam proyek Django!
settings.py memiliki peran penting dalam proyek Django ini. Pada settings.py dapat ditambahkan allowed_host, Konfigurasi Database, Pengaturan Template. Intinya settings.py dapat digunakan untuk memodifikasi perilaku dari proyek Django ini.

# Bagaimana cara kerja migrasi database di Django?
Migrasi database pada Django digunakan untuk memperbarui database agar sesuai dengan perubahan pada model Django dengan membuat dan menerapkan migrasi. Migrasi di Django adalah jembatan code dengan database. Alurnya adalah mendefinisikan model, buat file migrasi, jalankan migrasi ke database.

# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dipilih untuk permulaan pembelajaran pengembangan perangkat lunak karena framework Django memiliki semua yang developer butuhkan untuk membuat suatu aplikasi web. Django memiliki struktur yang jelas yaitu MVT, Django sudah memiliki fitur-fitur bawaan, dari segi keamanan Django memiliki keamanan yang lebih baik jika dibandingkan dengan PHP.

# Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Untuk tutorial menurut saya cukup mudah dimengerti, setiap langkah dijelaskan dengan cukup rinci dan diberikan contoh image pada beberapa step untuk mempermudah pengerjaan tutorial.

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasikan sebuah platform karena data delivery memungkinkan pertukaran informasi antara server dan client. Data perlu dikirim dari satu stack ke stack lainnya, perlu dipastikan bagian-bagian dari sistem dapat saling berkomunikasi. Data delivery dapat dilakukan dengan format html, json, dan xml.

# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dan lebih populer dari XML karena JSON lebih mudah untuk dibaca oleh manusia. Sintaks pada JSON lebih sederhana dibandingkan XML. JSON menggunakan format key: value sedangkan XML dibutuhkan tag pembuka dan penutup untuk setiap element data. JSON juga memiliki ukuran data yang lebih kecil dan lebih mudah diproses oleh JavaScript.

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid pada views.py adalah untuk melakukan validasi data yang dikirim oleh user ke dalam form valid atau tidak. Method ini akan memeriksa apakah semua field form sudah terisi dengan benar sesuai dengan aturannya dan sesuai dengan kebutuhan, sehingga dapat mencegah error. Kita membutuhkan method ini karena is_valid() dapat meningkatkan keamanan dan digunakan untuk automasi validasi sehingga tidak perlu dilakukan validasi manual.

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi yang dibuat dari serangan CSRF (Cross Site Request Forgery) dimana penyerang akan memanfaatkan sesi user yang sedang login untuk beraksi tanpa pengetahuan user. csrf_token digunakan untuk memberikan akses ke url yang dideploy.

Jika csrf_token tidak digunakan pada form Django,aplikasi akan rentan terhadap serangan CSRF. Penyerang bisa membuat form palsu yang kemudian akan mengirim request ke aplikasi menggunakan sesi user yang sedang melakukan login sehingga data dapat diubah.

Penyerang dapat memanfaatkan hal ini untuk merubah password, mengirim uang ke rekening tak dikenal mengatasnamakan user, dan menghapus data. csrf_token dapat mencegah hal ini dengan memverifikasi setiap request form sehingga yang diproses hanyalah request yang sah.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama, saya mengaktifkan virtual environment agar versi dari code yang kita gunakan sesuai dengan proyek yang sedang dibuat.
- Kemudian saya mengisi DIRS pada file settings.py dengan BASE_DIR / 'templates' agar terhubung dengan proyek dan mengubah APP_DIRS menjadi true agar templates milik app diprioritaskan.
- Lalu saya menambahkan 
{% extends 'base.html' %}
{% block content %}
{% endblock content %}
pada file main.html pada direktori templates.
- Lalu saya membuat forms.py sebagai form untuk menerima data product yang ditambahkan yang akan ditampilkan pada halaman utama.
- Lalu pada file views.py ditambahkan import baru untuk menambahkan function-function baru seperti create_product dan show_product.
- Lalu pada main.html ditambahkan code untuk tombol "Add Product", thumbnails, dan description product. 
- Pada direktori templates ditambahkan file create_product.html dan product_detail.html. create_product.html digunakan untuk menambahkan produk-produk baru. product_detail.html digunakan untuk menampilkan kategori, harga, gambar, dan deskripsi dari produk ketika pengguna mengklik tombol read more.
- Lalu pada views.py saya mengimport seralizers dan httpresponse untuk menambahkan function-function lagi agar data dapat dikembalikan dalam bentuk XML dan JSON.
- Pada urls.py ditambahkan import function-function yang telah dibuat dan menambahkan pathnya. Hal ini dilakukan untuk XML, JSON, XML by id, dan JSON by id.
- Terakhir saya mengecek apakah semuanya sudah sesuai dengan menjalankan localhost dan menambahkan product baru dan menggunakan postman untuk mengecek hasil dari step-step sebelumnya.
- Terakhir saya melakukan commit pada github dan pws.

# Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Menurut saya tutorial yang diberikan sudah cukup baik dan jelas. Asdos juga sangat responsif dalam membantu kami ketika ada masalah dalam pengerjaan tugas.