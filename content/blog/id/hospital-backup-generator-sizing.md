---
title: "Genset diesel untuk daya cadangan rumah sakit: panduan penentuan kapasitas"
date: "2026-10-28"
excerpt: "Cara menentukan kapasitas genset diesel untuk cadangan daya rumah sakit: daftar beban, perhitungan kVA, starting motor, ketahanan bahan bakar, redundansi dan uji load bank."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Genset diesel berperedam suara untuk daya cadangan rumah sakit di pabrik kami di Yangzhou](/images/blog/hospital-generator-sizing.jpg)

Pemadaman listrik di rumah sakit bukan sekadar gangguan. Dalam hitungan detik, kamar operasi kehilangan penerangan, ventilator di ICU beralih ke baterai yang bertahan menit bukan jam, lemari bank darah mulai melewati 6 °C, lift berhenti di antara lantai dengan pasien di dalamnya, dan sistem panggilan perawat padam.

Karena itu **genset diesel untuk daya cadangan rumah sakit** ditentukan berbeda dari genset pabrik atau lokasi proyek. Bukan “unit terbesar yang masuk anggaran”, melainkan mesin keselamatan jiwa yang kapasitas, perilaku starting, ketahanan bahan bakar, akustik, dan catatan ujinya harus dapat dipertanggungjawabkan di hadapan auditor akreditasi.

Panduan ini mengikuti urutan perhitungan yang kami pakai pada proyek rumah sakit: menyusun daftar beban, mengonversi ke kVA dengan koreksi yang tepat, memeriksa starting motor, lalu menetapkan bahan bakar, redundansi, kebisingan, dan cakupan uji. Angkanya berasal dari lembar data seri KC kami, termasuk dua unit nyata kelas rumah sakit.

## 1. Apa yang sebenarnya disuplai genset di rumah sakit

Instalasi listrik rumah sakit umumnya dibagi menjadi suplai normal dan satu atau beberapa bus esensial. Hanya bus esensial yang masuk ke genset. Menetapkan batas ini dengan benar adalah separuh pekerjaan.

| Kelompok beban | Isi tipikal | Artinya untuk perhitungan |
|---|---|---|
| Keselamatan jiwa | Penerangan kamar operasi dan ICU, alarm kebakaran, penghisap asap, penerangan evakuasi, alarm gas medis | Pindah dalam sekitar 10 detik, tidak boleh dilepas |
| Kritis | Peralatan ICU dan neonatus, dialisis, pendingin bank darah, rantai dingin farmasi, inkubator laboratorium, TI dan panggilan perawat | Stabilitas tegangan lebih penting daripada kapasitas kasar |
| Peralatan | Lift, pompa air, pompa kebakaran, tata udara, sterilisasi, sebagian dapur dan laundry | Starting motor yang menentukan, bukan daya jalan |
| Opsional | Stopkontak bangsal, AC standar, sebagian dapur | Biasanya tidak disuplai atau dilepas saat overload |

Dari situ muncul dua aturan praktis. Pertama: jangan suplai seluruh rumah sakit dari genset bila anggaran dan tangki bahan bakar tidak mendukung — sebagian besar proyek menaruh 40–60 % beban terpasang di bus esensial. Kedua: perlakukan beban motor sebagai masalah starting, bukan daya jalan; motor lift 15 kW bisa menarik lima sampai tujuh kali arus nominalnya selama satu dua detik.

Kerangka regulasi berbeda per negara — NFPA 99 dan NFPA 110 di Amerika Serikat, HTM 06-01 di Inggris, IEC 60364-7-710 untuk lokasi medis di Eropa dan banyak pasar ekspor. Berbeda detail tetapi sepakat pada intinya: bus esensial tertentu, waktu pindah tertentu, durasi bahan bakar tertentu, dan uji berkala terdokumentasi. Pastikan versi lokal sebelum menetapkan kVA.

## 2. Daftar beban dulu, kVA kemudian

Setiap perdebatan kapasitas genset rumah sakit sebenarnya perdebatan daftar beban. Susun di spreadsheet, sirkuit per sirkuit.

Untuk tiap item catat empat data: kW papan nama, faktor daya, faktor kebutuhan (berapa yang benar-benar jalan bersamaan), dan metode starting (langsung, bintang-segitiga, soft starter, inverter).

Contoh rumah sakit umum 200 tempat tidur dengan chiller, dapur, dan laundry di bus esensial. Ini angka perencanaan, bukan pengganti diagram satu garis proyek:

| Beban | kW tersambung | Faktor kebutuhan | kW saat jalan |
|---|---|---|---|
| Kamar operasi, ICU, penerangan darurat, sistem kebakaran | 120 | 1,0 | 120 |
| Peralatan ICU, bank darah, farmasi, TI | 90 | 1,0 | 90 |
| Lift (4 × 15 kW) | 60 | 0,6 | 36 |
| Chiller (satu di bus esensial) | 90 | 1,0 | 90 |
| Pompa, pengolahan air, pompa kebakaran | 55 | 1,0 | 55 |
| Dapur dan laundry, sebagian | 60 | 1,0 | 60 |
| **Total saat jalan** | | | **451** |

Faktor keragaman 0,9 memberi sekitar **406 kW**. Tambah cadangan pertumbuhan — rumah sakit menambah pencitraan, tempat tidur, pendingin — sehingga 20 % adalah cadangan realistis: **487 kW**. Unit standar terdekat adalah **500 kW / 625 kVA**.

Lalu periksa kasus starting. Jika chiller start langsung dengan arus enam kali sementara kamar operasi sudah berbeban, genset harus menyerap langkah itu tanpa penurunan tegangan yang mematikan alat medis. Bila tidak lolos, jawabannya bukan otomatis genset lebih besar: soft starter atau inverter pada chiller, biasanya lebih murah daripada 200 kW alternator tambahan.

## 3. Rumus dan empat koreksi

Konversi dasarnya sederhana:

**kVA = kW ÷ faktor daya**

Dengan faktor daya standar 0,8 tertinggal pada unit 50 Hz kami, beban jalan 400 kW memerlukan 500 kVA alternator sebelum koreksi. Empat koreksi lalu berlaku.

**Cadangan pertumbuhan.** 15–25 % untuk rumah sakit baru, karena tidak ada yang mendesain untuk jumlah tempat tidur hari ini.

**Starting motor dan beban bertahap.** Penurunan tegangan transien harus tetap dalam batas yang ditoleransi alat medis. Lembar data seri KC kami menetapkan: deviasi tegangan transien ≤ 15 %, regulasi tegangan kondisi tunak ≤ 0,5 %, deviasi frekuensi transien ≤ 0,5 %, dan waktu pulih tegangan serta frekuensi ≤ 3 detik. Itulah yang benar-benar dialami monitor ICU saat transfer.

**Derating lokasi.** Unit berating 40 °C kehilangan kapasitas pada 45 °C, dan lebih banyak di ketinggian. Bila ruang mesin panas karena radiator membuang udara ke sudut, entah turunkan rating atau perbaiki aliran udara.

**Mode kerja.** Rating cadangan (jam terbatas, tanpa overload) dibanding rating utama (kontinu, overload 10 % satu jam). Rumah sakit yang menjalankan genset delapan jam selama perbaikan jaringan berada pada mode cadangan; rumah sakit dengan pemadaman harian berada pada mode utama dan harus ditentukan demikian.

## 4. Dua titik acuan nyata

Panduan abstrak mudah ditulis dan sulit dipakai. Ini dua unit yang kami buat untuk layanan rumah sakit, angka langsung dari lembar teknis KC.

| Parameter | KC-YC200 | KC-YC1600 |
|---|---|---|
| Daya rating / cadangan | 200 kW / 220 kW | 1.600 kW / 1.760 kW |
| Tegangan / arus | 380/220 V, 360 A | 380/220 V, 2.880 A |
| Frekuensi, faktor daya | 50 Hz, 0,8 tertinggal | 50 Hz, 0,8 tertinggal |
| Mesin | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1.805 / 1.985 kW |
| Silinder / kapasitas | Inline 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Turbo / governor | Turbo intercooler, elektronik | Turbo intercooler, elektronik |
| Konsumsi bahan bakar | 200 g/kWh | 200 g/kWh |
| Alternator | KCI-200, brushless, AVR, IP23, kelas H, tembaga | KCI-1600, brushless, AVR, IP23, kelas H, tembaga |
| Dimensi (P × L × T) | 3.000 × 1.100 × 1.750 mm | 5.500 × 2.200 × 2.700 mm |
| Berat | 2.800 kg | 15.800 kg (referensi) |
| Kebisingan (LP7M) | 102 dB(A) | 102 dB(A) |

**Kapan kelas 200 kW cocok.** Klinik, pusat bedah sehari, rumah sakit kecil, dan bangunan pencitraan yang bus esensialnya terbatas pada penerangan kamar operasi, peralatan ICU, sistem kebakaran, TI, dan dua lift, dengan chiller di suplai normal. Dengan 2.800 kg dan panjang 3 m, unit bisa masuk ruang mesin basement dengan hand pallet — penting saat renovasi dengan pintu 1,2 m.

**Kapan kelas 1.600 kW cocok.** Rumah sakit regional dan pendidikan yang bus esensialnya benar-benar mencakup chiller sentral, dapur, laundry, pencitraan, dan 10–20 lift. Dengan 15.800 kg dan 5,5 m dibutuhkan ruang mesin nyata, slab beton atau area level tanah, rencana pengangkatan crane, dan biasanya dua unit paralel bukan satu.

Di antara keduanya ada tingkatan antara; intinya lembar data harus cukup lengkap agar insinyur perencana dapat memindahkan angka langsung ke model kelistrikan.

## 5. Ketahanan bahan bakar: pertanyaan 72 jam

Bahan bakar adalah titik paling sering gagal dalam spesifikasi rumah sakit, karena konsumsi dicantumkan per kWh dan konversinya terlupa.

Dengan 200 g/kWh dan solar sekitar 0,84 kg/L:

**Liter per jam = kW rating × 0,2 ÷ 0,84**

| Beban (KC-YC200) | Bahan bakar per jam | Per 24 jam | Per 72 jam |
|---|---|---|---|
| 100 % (200 kW) | 47,6 L/jam | 1.143 L | 3.429 L |
| 50 % rata-rata (100 kW) | 23,8 L/jam | 571 L | 1.714 L |
| 25 % rata-rata (50 kW) | 11,9 L/jam | 286 L | 857 L |

Jadi unit 200 kW dengan rata-rata realistis setengah beban memerlukan sekitar **1.700 L untuk 72 jam**. Tetapkan tangki utama 2.000 L dan tersisa margin plus volume tak terpakai. Untuk unit 1.600 kW pada setengah beban sekitar **4.570 L per 24 jam**, karena itu rumah sakit besar memakai tangki terpendam atau bertanggul plus kontrak pembersihan bahan bakar, bukan tangki di rangka.

Tiga detail yang diperiksa auditor: **tangki harian** untuk 8 jam operasi (agar masalah tangki utama tidak langsung menghentikan unit), **tanggul 110 %** volume, dan **alarm level tinggi/rendah** yang terhubung ke building management system. Pada jalur bahan bakar, pasang katup isolasi tahan api di outlet tangki, dan jangan pernah merutekan lewat tangga darurat.

## 6. Redundansi, paralel, dan transfer

Satu genset adalah satu titik kegagalan. Rumah sakit jarang menerima itu pada bangunan baru.

| Skema | Artinya | Pemakaian tipikal |
|---|---|---|
| N | Satu unit sesuai beban esensial | Klinik, rumah sakit kecil |
| N+1 | Unit tambahan yang dapat memikul beban bila salah satu gagal | Rumah sakit umum, 3 × 500 kW untuk beban 1.000 kW |
| 2N | Dua suplai lengkap dan independen dengan ruang terpisah | Rumah sakit pendidikan, kampus besar |

Paralel memberi lebih dari redundansi: dua unit pada 60 % alih-alih satu pada 100 % menurunkan konsumsi dan kebisingan malam, dan satu unit bisa dirawat sementara yang lain memikul beban. Kontroler kami mendukung pembagian beban, pembagian isokron, dan sinkronisasi otomatis, dengan bus tie untuk mengisolasi satu unit.

Pada transfer, tetapkan lama perpindahan sejak awal. Sirkuit keselamatan jiwa umumnya diharapkan mendapat daya dalam sekitar 10 detik; kamar operasi dan ICU menjembatani celah itu dengan UPS atau static transfer switch, bukan mengharapkan genset seketika. Uji seluruh urutan — jaringan hilang, sinyal ATS, engkol, pembentukan tegangan, penutupan breaker, penerimaan beban — di meja uji, bukan pada malam pemadaman.

## 7. Kebisingan, penempatan, dan tetangga

Dua unit di tabel adalah tipe rangka terbuka 102 dB(A) pada 7 meter di titik acuan LP7M. Ini keras, sekitar level gergaji mesin. Dapat diterima di ruang mesin berperedam baik atau lokasi terpencil, dan tidak dapat diterima 30 meter dari jendela bangsal.

Opsi menurut biaya:

- **Kanopi peredam suara** — umumnya menurunkan unit ke kisaran 70–75 dB(A) pada 7 m.
- **Perlakuan akustik ruang** — lapisan penyerap, pintu rapat, lantai terapung, dan peredam udara masuk serta keluar yang dihitung benar. Untuk unit besar, ruang biasanya jalur lebih murah mencapai batas tapak yang ketat.
- **Penempatan** — arahkan buang radiator dan cerobong asap jauh dari fasad bangsal, dan periksa tinggi cerobong terhadap jendela yang dapat dibuka terdekat.

Periksa batas tapak setempat sebelum memilih karena sangat bervariasi; banyak yurisdiksi menerapkan kisaran 45–55 dB(A) pada penerima sensitif terdekat di malam hari. Jangan menganggap kanopi saja cukup pada mesin 1,6 MW — tidak cukup.

## 8. Detail pemasangan yang menentukan hasil

Inilah yang mengubah lembar data yang benar menjadi instalasi yang bekerja:

- **Udara pendingin.** Radiator perlu inlet bersih dan outlet tersalur ke udara luar. Ruang dengan kisi seukuran kotak surat akan menurunkan rating dan memanaskan alternator.
- **Tekanan balik gas buang.** Jalur panjang, belokan tajam, dan peredam kecil menaikkan tekanan balik dan memakan daya. Rancang dengan tekanan balik maksimum yang diizinkan pemasok.
- **Isolasi getaran.** Dudukan pegas atau karet di bawah rangka, sambungan fleksibel gas buang, dan koneksi bahan bakar fleksibel. Tanpanya kebisingan merambat lewat slab ke bangsal di atas.
- **Ukuran kabel.** Hitung dari arus rating pada suhu nyata, dan pisahkan kabel daya dan kontrol dalam tray berbeda.
- **Pembumian dan netral.** Konfirmasi sistem pembumian dengan insinyur listrik rumah sakit: perlakuan netral genset harus sesuai instalasi, bukan sebaliknya.
- **Sekat kebakaran.** Ruang genset adalah kompartemen kebakaran dengan deteksi sendiri dan biasanya pemadam sendiri.
- **Akses.** Sisakan akses ke ujung alternator dan kedua sisi mesin: unit yang tak bisa dirawat akan gagal lebih cepat.

## 9. Pengujian: bagian yang paling sering dilewati pemasok

Genset rumah sakit dinilai pada malam ia dibutuhkan. Karena itu setiap unit yang keluar dari pabrik Yangzhou kami masuk load bank digital sebelum pengiriman, dengan urutan tetap:

| Tahap | Durasi tahan | Yang diverifikasi |
|---|---|---|
| Tanpa beban | — | Pemanasan, tekanan oli, tegangan pengisian |
| Beban 25 % | 30 menit | Stabilitas tegangan dan frekuensi, suhu gas buang |
| Beban 50 % | 30 menit | Respons governor, konsumsi, kebisingan |
| Beban 75 % | 60 menit | Sistem pendingin, suhu cairan pendingin, ketegangan belt |
| Beban 100 % | 60 menit | Daya rating penuh, regulasi tegangan dalam ±1,5 % |
| Overload 110 % | 1 menit | Trip proteksi dan verifikasi alarm |

Setelah uji kami memeriksa tahanan isolasi dan kontinuitas pembumian setelah siklus termal, memverifikasi seluruh fungsi proteksi (overspeed, suhu air tinggi, tekanan oli rendah, arus lebih, stop darurat), dan menguji urutan ATS dari awal sampai akhir di meja uji. Laporan uji menyertai unit.

Bila proyek memerlukan uji dengan saksi, laporan inspeksi pihak ketiga (BV, SGS, atau TUV), atau protokol FAT khusus lokasi, itu harus dipesan sebelum unit masuk produksi, bukan seminggu sebelum pengiriman.

## 10. Mengapa rumah sakit bekerja dengan Kaichen

Kami membuat genset di Yangzhou, Tiongkok, dari 20 kVA sampai 3.000 kVA, dan segmen rumah sakit adalah bagian penting pekerjaan kami. Tiga hal lebih penting di segmen ini.

**Kami membuat alternator sendiri.** Seri KCI dililit tembaga, isolasi kelas H, proteksi IP23, kendali AVR, dan dibuat di lokasi yang sama dengan lini perakitan. Ketika rumah sakit butuh respons transien tertentu, kami mengganti alternator alih-alih mencarinya di luar.

**Kami menguji beban penuh di rumah sendiri.** Load bank digital 2 MW memungkinkan unit 1.600 kW dibuktikan pada 110 % sebelum dikirim, bukan hanya tanpa beban di halaman.

**Kami mendokumentasikan dalam bahasa pelanggan.** Lembar data, manual operasi dan pemeliharaan, deskripsi logika kontrol, dan papan nama dapat disediakan dalam bahasa yang kami terbitkan, yang memperpendek commissioning saat tim lapangan tidak berbahasa Inggris.

Referensi rumah sakit kami berkisar dari unit 200 kW untuk rumah sakit kota hingga instalasi kelas 1.600–1.800 kW untuk kampus rumah sakit regional, termasuk mesin yang bertugas cadangan bertahun-tahun dengan uji beban terjadwal. Setiap pengiriman menyertakan dokumen CE dan ISO 9001, kit suku cadang untuk interval servis pertama, dan dukungan teknis 24/7 selama commissioning.

## Pertanyaan umum

**Berapa kapasitas genset yang dibutuhkan rumah sakit?**
Tergantung bus esensial, bukan jumlah tempat tidur. Klinik dengan penerangan kamar operasi, peralatan ICU, dan dua lift biasanya perlu 150–250 kW. Rumah sakit umum 200 tempat tidur dengan chiller di bus esensial umumnya berada antara 400 dan 600 kW. Kampus regional dengan dapur, laundry, pencitraan, dan lebih dari 15 lift sering perlu 1.200–2.000 kW, biasanya dua unit atau lebih secara paralel.

**Berapa lama bahan bakar harus bertahan?**
Spesifikasi umum meminta 72 jam pada beban tertentu, kadang 96 jam untuk fasilitas kritis. Hitung tangki dari konsumsi nyata g/kWh pada beban rata-rata yang diharapkan: untuk unit 200 kW setengah beban, sekitar 1.700 L menutup 72 jam.

**Bisakah genset diesel menyuplai kamar operasi?**
Bisa, tetapi tidak langsung. Kamar operasi biasanya disuplai melalui UPS atau static transfer switch yang menjembatani 10–30 detik sampai genset menerima beban; tugas genset adalah menjaga tegangan dan frekuensi dalam batas yang ditoleransi alat medis setelah itu.

**Kanopi peredam atau rangka terbuka untuk rumah sakit?**
Peredam untuk semua yang terdengar dari bangsal, staf, atau batas tapak. Rangka terbuka hanya praktis di ruang mesin berperedam baik atau area terpencil.

**Seberapa sering genset rumah sakit diuji?**
Jalan tanpa beban atau beban rendah bulanan plus uji beban penuh tahunan di load bank adalah dasar umum; banyak skema akreditasi meminta uji bulanan terdokumentasi dan uji beban tahunan pada daya rating. Uji ATS bersamaan, bukan terpisah.

## Langkah berikutnya

Bila Anda menentukan unit untuk rumah sakit, kirimkan daftar beban bus esensial dan kondisi lokasi — ketinggian, suhu ambien, batas kebisingan tapak, durasi bahan bakar yang diminta — dan kami akan menentukan kapasitas berdasarkan kasus starting nyata, bukan aturan praktis. Lihat kelas mesin yang kami buat di halaman [genset Cummins 200 kW berperedam](/id/products/cummins-200kw-silent-diesel-generator/), [genset Yuchai 300 kW berperedam](/id/products/yuchai-300kw-silent-diesel-generator/), dan [genset Mitsubishi 1000 kW rangka terbuka](/id/products/mitsubishi-1000kw-open-diesel-generator/), atau [hubungi kami](/id/contact/) dengan diagram satu garis Anda.
