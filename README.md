# CloudMed

**Cloud Computing: Paranaşütcü Gözünden** — bulut bilişimi, bulut türleri, bulut istifleri,
öğrenme yolları, dersler ve paraşütcüler için güvenlik/risk yönetimi.

Bu proje, acil servis, ambulans/kampüs ve sağlık teknolojileri çalışanları için
**Türkçe ana içerik + İngilizce terimler**yle bir ortak dönüşüm rehberi sunar.

---

## Nasıl çalışır?

1. `index.html` sayfasını tarayıcınızda açın.
2. Sunucuya ihtiyaç duymaz; statik ve tarayıcıda çalışır.
3. İsterseniz `docs/` içindeki markdown dosyaları örnek belgeler olarak inceleyebilirsiniz.

### GitHub Pages ile yayın

1. Bu dizini GitHub'a `git push` edin.
2. Reponun **Settings &rarr; Pages** bölümünden **Deploy from a branch** &rarr; `main` / `master` seçin.
3. `/ (root)` seçeneğini işaretleyip **Save** yapın.
4. Linkiniz `https://<kullanıcı>.github.io/<repo>/` olur.

`(Bu rehberde, ben bir yaratıcı olarak gerçek bir GitHub hesabına push yapılmadı; kullanıcı
repository’yi kendi GitHub hesabına taşıdıktan sonra yukarıdaki adımları uygulamalıdır.)`

---

## Proje yapısı

```text
.
├── index.html                  # Ana web sitesi
├── css/
│   └── styles.css              # Tek karmaşık CSS
├── js/
│   └── main.js                 # Mobil menü toggle ve yumuşak git
├── docs/                       # Sanal dokümanlar
│   ├── cloud-basics.md
│   ├── cloud-services.md
│   ├── cloud-deployment.md
│   ├── cloud-providers-locations.md
│   ├── cloud-risks-paramedic.md
│   └── glossary.md
├── LICENSE
├── .gitignore
└── .nojekyll                   # GitHub Pages’te Jekyll işlemeyi kırar
```

---

## İlk adım: görsel olarak kontrol

- Açık `index.html`
- `css/` ve `js/` yollarının doğru bağlandığından emin olun
- Mobil dar görüşte menünün açılıp kapanmasını test edin

## Katkıda bulunma

1. Pull request aç
2. Yeni bir bölüm veya dil eklemesi ekleyin
3. `index.html` doğruluğu, HTML yapısını ve `README.md` içeriğini güncelleyin

## Lisans

MIT (dosyada `LICENSE`).
