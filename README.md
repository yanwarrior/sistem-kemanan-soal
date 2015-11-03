## Sistem Keamanan Soal

Sistem Keamanan Soal Untuk Sekolah, menggunakan `Algoritma RC4` pada `Django` dan `Python 2.7`, 
dikarenkan Python 3 bentrok di bagian `Library Native RC4` yang ada di sini untuk membaca File.

## Fitur Utama
fitur utama yang tersedia di dalam web apps ini terdiri dari :
* Enkripsi dan Dekripsi cepat dengan `Algoritma RC4` untuk mengamankan soal-soal ujian.
* User `Administrator` dan User `Tata Usaha` serta peranan masing-masing dalam pengelolaan soal.
* User `Guru` dan halaman khusus untuk screen guru.
* `Kirim Soal` fitur yang tersedia untuk guru untuk mengirim Soal secara aman ke bagian user `Tata Usaha`.
* `Login` dan `Logout` semua user (Guru, Administrator dan Tata Usaha) ke dalam sistem. 
* Setiap User memiliki batas permissionnya masing-masing dari apa yang boleh ia lakukan di dalam sistem.
* `Penghapusan Soal` yang diberikan wewenang terhadap guru di halaman dashboardnya. 
* `Pencarian` dan `Pagination`.
* Look And Feel serta mudah dioperasikan. 
* Free
* Kapasitas ukuran soal yang dikirim secara default 5 MiB.
* Kapasitas ukuran soal yang dikirm bisa di atur batasnya. 
* Pengecekan dan Validasi Tipe file soal berdasarkan `content type`. 
* Bisa mengatur file apa saja yang boleh di upload dan file apa saja yang tidak boleh. 
* Setup dan Pengaturan Mudah. 
* Terdedia sistem manajemen pengelolaan password yang diberikan untuk `Administrator` dan `Tata Usaha`.

## Required
* Python 2.7
* Django => 1.6

## Database Settings
Anda bisa mengaturn database anda sendiri sesuai kebutuhan anda di bagian `settings.py`. 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    }
}
```

## Thanks To
> All My Friends In Kabel Konslet, Morpyn Behind The Canteen, I love u all.

## MIT Licence
> Copyright (c) 2015 Yanwar Solahudin

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.