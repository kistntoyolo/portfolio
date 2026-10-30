# Kistanto – Personal Portfolio

Website portfolio dengan konsep Dark Modern Professional.
**Stack:** HTML5 · CSS3 (Tailwind CSS) · JavaScript (vanilla). Tanpa framework runtime, sehingga cepat dimuat dan mudah dipublikasikan.

## Struktur Folder

```
kistanto-portfolio/
├── index.html                 # Home, About, Skills, Projects, Education, Contact
├── project-soleguard.html     # Halaman detail proyek SoleGuard
├── css/style.css              # Hasil build Tailwind (sudah disertakan)
├── js/main.js                 # Hamburger menu, scroll reveal, active nav, fallback foto
├── src/input.css              # Sumber CSS Tailwind + komponen kustom
├── tailwind.config.js         # Warna, font, tema
├── scripts/build_cv.py        # Pembuat CV PDF
├── assets/
│   ├── cv/Kistanto_CV.pdf     # File yang diunduh tombol "Download CV"
│   └── img/                   # Foto profil & screenshot (lihat di bawah)
└── package.json
```

## Menjalankan Secara Lokal

Website sudah ter-build, jadi cukup dibuka lewat server statis:

```bash
npm install          # sekali saja
npm start            # buka http://localhost:3000
```

Alternatif tanpa npm: `python3 -m http.server 3000` lalu buka http://localhost:3000.

### Mengubah tampilan

Jika mengedit class Tailwind atau `src/input.css`, build ulang CSS:

```bash
npm run build        # sekali build
npm run dev          # mode watch saat mengedit
```

## Yang Perlu Anda Lengkapi

1. **Foto profil** – sudah terpasang di `assets/img/profile.png`; timpa file ini untuk menggantinya.
2. **Email** – sudah diisi `kistnto@gmail.com`; LinkedIn tidak ditampilkan. Untuk menambahkannya nanti, salin salah satu baris kontak di section Contact pada `index.html`.
3. **Screenshot SoleGuard** – simpan sebagai `assets/img/screenshot-1.png` dan `screenshot-2.png`; placeholder otomatis tergantikan.
4. **Data evaluasi** – di `project-soleguard.html` bagian *Evaluation Results*, isi Precision, Recall, dan mAP dari hasil pelatihan Anda. Beberapa data (lima kelas, 3.511 citra asli ± 8.000 setelah augmentasi, Google Colab Tesla T4, accuracy 85%) diambil dari informasi yang pernah Anda sampaikan; **mohon cocokkan dengan skripsi**. Teks bertanda `[Placeholder]` / `[Isi]` harus diganti atau dihapus.
5. **Domain & SEO** – ganti `https://example.com/` pada `<link rel="canonical">` di `index.html` dengan URL asli setelah deploy.
6. **CV** – edit data di `scripts/build_cv.py`, lalu `pip install reportlab && python3 scripts/build_cv.py`. Atau timpa langsung `assets/cv/Kistanto_CV.pdf` dengan CV Anda sendiri.

## Publikasi

**Vercel**
1. Push folder ini ke repository GitHub.
2. Di vercel.com pilih *Add New → Project*, impor repository.
3. Framework Preset: *Other*. Build Command kosong (atau `npm run build`), Output Directory `.`
4. Deploy.

**GitHub Pages**
1. Push ke repository GitHub (`css/style.css` harus ikut ter-commit).
2. *Settings → Pages → Build and deployment → Deploy from a branch*, pilih `main` dan folder `/ (root)`.
3. Situs aktif di `https://<username>.github.io/<repo>/`. Semua tautan memakai path relatif sehingga aman di sub-path.

## Fitur

- Responsif (desktop, tablet, smartphone) dengan hamburger menu
- Dark mode sebagai tampilan utama, smooth scrolling, scroll reveal ringan (menghormati `prefers-reduced-motion`)
- Tombol Download CV, tautan GitHub, dan WhatsApp (`https://wa.me/6285227341724`) berfungsi
- SEO metadata, Open Graph, dan JSON-LD
- Accessibility dasar: skip link, label ARIA, fokus terlihat, alt text, struktur heading
