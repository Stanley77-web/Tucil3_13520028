# Tugas Kecil 3 IF 2211 Strategi Algoritma
> Aplikasi Algoritma Branch and Bound untuk Membuat Suatu Program _Solver_ dari Permainan Puzzle 15

## Daftar Isi
  - [Tugas Kecil 3 IF 2211 Strategi Algoritma](#tugas-kecil-3-if-2211-strategi-algoritma)
  - [Daftar Isi](#daftar-isi)
  - [Informasi Umum](#informasi-umum)
  - [Teknologi Digunakan](#teknologi-digunakan)
  - [Tampilan Program](#tampilan-program)
  - [Penggunaan](#penggunaan)
  - [Penulis](#penulis)
<!-- * [License](#license) -->

## Informasi Umum
Membuat program _solver_ untuk permainan Puzzle 15 dengan memanfaatkan algoritma branch and bound. 
Spesifikasi program adalah sebagai berikut: 
1. Gui :
   - Program meminta input kepada pengguna untuk men-_generate_ puzzle secara random atau melalui file konfigurasi.
   - Program akan menampilkan kondisi dan informasi awal puzzle (nilai X, list nilai masing-masing fungsi kurang(i),dan Sigma(kurang(i)) + X)
   - Program akan menyelesaikan puzzle setelah pengguna menekan tombol ```Find``` tanpa melakukan visualisasi.
   - Program akan menampilkan pesan puzzle tidak dapat diselesaikan apabila puzzle tidak memenuhi syarat penyelesaian
   - Program akan melakukan visualisasi penyelesaian puzzle setelah pengguna menekan tombol ```Visualize``` dengan kecepatan yang bisa diatur.
   - Program akan menampilkan puzzle yang sudah berhasil diselesaikan beserta dengan informasi akhir puzzle (Total pergerakan, total simpul yang dibangkitkan, dan waktu penyelesaian).
2. CLI
   - Program meminta input kepada pengguna untuk menentukan jenis masukan puzzle, apakah men-_generate_ puzzle secara random atau melalui file konfigurasi atau melalui input langsung.
   - Program akan menampilkan kondisi dan informasi awal puzzle (nilai X, list nilai masing-masing fungsi kurang(i),dan Sigma(kurang(i)) + X)
   - Program akan menyelesaikan puzzle.
   - Program akan menampilkan pesan puzzle tidak dapat diselesaikan apabila puzzle tidak memenuhi syarat penyelesaian
   - Program akan menampilkan langkah-langkah penyelesaian dan move yang diambil.
   - Program akan menampilkan puzzle yang sudah berhasil diselesaikan beserta dengan informasi akhir puzzle (Total pergerakan, total simpul yang dibangkitkan, dan waktu penyelesaian).
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Teknologi Digunakan
- [Python - version 3.10.2](https://id.wikipedia.org/wiki/Python_(bahasa_pemrograman)) 
- [Pip - version 22.0.3](https://en.wikipedia.org/wiki/Pip_(package_manager))
- [Windows OS - version 10+](https://en.wikipedia.org/wiki/Microsoft_Windows) **Disarankan**

## Tampilan Program
Tampilan Program dalam CLI adalah sebagai berikut

  ![image](https://media.discordapp.net/attachments/941288781401698307/960519180787011734/unknown.png?width=1260&height=662)

Tampilan Program dalam GUI adalah sebagai berikut

  ![image](https://media.discordapp.net/attachments/941288781401698307/960518709775061002/unknown.png?width=495&height=663)

## Penggunaan
***[Perhatikan]***
Berikut ini cara menjalankan dan menggunakan program
1. Prerequisite, install _package_ PySimpleGUI pada python dengan memasukkan _command line_ ```pip install PySimpleGUI``` pada terminal ```cmd``` atau ```powershell```
  
2. Buka folder bin pada root yang berisi file executable. 
3. Buka file executable yang ingin digunakan (GUI atau CLI).

  ![image](https://media.discordapp.net/attachments/941288781401698307/960537426516901898/unknown.png)

4. Masukan nama dataset yang ingin dibentuk _convex hull_-nya, seperti gambar dibawah ini:

  ![image](https://cdn.discordapp.com/attachments/941288781401698307/947410226259296256/unknown.png)

Untuk file executable GUI :
5. Tekan tombol ```Generate puzzle``` untuk membuat puzzle random yang akan di selesaikan, seperti gambar dibawah ini:
atau
   Tekan tombol ```Browse``` untuk mengambil file configurasi yang berisi puzzle yang akan di selesaikan, seperti gambar dibawah ini :

  ![image](https://media.discordapp.net/attachments/941288781401698307/960541371578597417/unknown.png)

6. Program akan menampilkan kondisi dan informasi awal puzzle, seperti gambar dibawah ini:

  ![image](https://media.discordapp.net/attachments/941288781401698307/960549212053979136/unknown.png?width=696&height=662)

7. Tekan tombol ```Find ``` untuk memproses pencarian solusi penyelesaian (apabila puzzle tidak dapat diselesaikan akan memunculkan pesan tidak bisa diselesaikan) dan tekan tombol ```Visualize``` untuk melakukan visualisasi, kecepatan animasi dapat diatur menggunakan slider ```Animation Speed```, selama visualisasi pergeseran puzzle move yang diambil akan ditampilkan, seperti gambar dibawah ini:
   
  ![image](https://media.discordapp.net/attachments/941288781401698307/960544434653646888/unknown.png)

8. Program akan menampilkan puzzle yang sudah berhasil diselesaikan beserta dengan informasi akhir puzzle, seperti gambar dibawah ini: 

  ![image](https://media.discordapp.net/attachments/941288781401698307/960549744940294254/unknown.png?width=585&height=662)

9. Untuk mengulangi visualisasi bisa menekan tombol ```Visualize``` atau menekan tombol ```New Game``` yang akan muncul setelah melakukan visualisasi untuk mengulangi program ke state awal

Untuk file executable CLI :
5. Pilih menu untuk memasukkan puzzle yang akan diselesaikan, seperti gambar dibawah ini: 

  ![image](https://media.discordapp.net/attachments/941288781401698307/960553639439659048/unknown.png)

6. Untuk menu ```Input keyboard``` pengguna harus memasukkan matrix puzzle yang akan di solve secara langsung, untuk menu ```Input file``` pengguna harus memasukan nama file .txt yang berisi konfigurasi puzzle, untuk menu ```Generate Random``` program akan langsung menampilkan kondisi dan informasi awal puzzle dan menyelesaikannya

  ![image](https://media.discordapp.net/attachments/941288781401698307/960553773669969930/unknown.png)

  ![image](https://media.discordapp.net/attachments/941288781401698307/960554060497444934/unknown.png)

  ![image](https://media.discordapp.net/attachments/941288781401698307/960554358288838656/unknown.png)

7. Program akan menyelesaikan puzzle dan akan menampilkan kondisi dan informasi akhir puzzle serta langkah penyelesaian apabila puzzle dapat diselesaikan 

  ![image](https://media.discordapp.net/attachments/941288781401698307/960555935397457970/unknown.png)

**Penting!!**
  _untuk file konfigurasi harus file ```.txt``` berisi matrix 4 x 4 berisi angka-angka 1 - 15 dan 16 untuk menunjukan kotak kosong, seperti gambar dibawah ini :_

  ![image](https://media.discordapp.net/attachments/941288781401698307/960543157974626374/unknown.png)

Selamat Mencoba!
  _untuk cli disarankan dijalankan melalui windows terminal dengan memasukan command line ```./"Puzzle15Solver(CLI)"``` karena jika langsung melalui executable akan membuka melalui terminal cmd dan ada beberapa simbol yang tidak muncul di terminal cmd_
  
## Penulis
<table>
    <tr>
      <td><b>Nama</b></td>
      <td><b>NIM</b></td>
    </tr>
    <tr>
      <td><b>Timothy Stanley Setiawan</b></td>
      <td><b>13520028</b></td>
    </tr>
</table