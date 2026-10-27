# CloudMed — Paramedikler için Bulut Bilişim Rehberi

Saha sağlık ekipleri ve paramedikler için hazırlanmış, tek sayfalık Türkçe bulut bilişim başvuru sitesi. Bulut kavramlarını sahadaki kararlarla ilişkilendirir: hangi servis modeli, veri nerede durur, kesinti olursa ne olur, maliyet nasıl kontrol edilir.

**Canlı site:** https://flynntaggart26.github.io/cloud-paramedic-portfolio/

## Kapsam

| Bölüm | İçerik |
|---|---|
| Ana Sayfa | Ambulans → bulut → hastane veri akışı ve hızlı giriş kartları |
| Temeller | NIST SP 800-145’in beş temel özelliği, saha faydaları ve riskleri |
| Servisler | IaaS, PaaS, SaaS, FaaS, DBaaS, DaaS ve ortak sorumluluk dağılımı |
| Dağıtım | Public, private, hybrid, community, multi-cloud + karar simülatörü |
| Sağlayıcılar | AWS, Azure, Google Cloud; region/AZ/edge; sözleşme kontrol listesi |
| Güvenlik | IAM, şifreleme, gözlemlenebilirlik, HIPAA/GDPR/KVKK/SOC 2/ISO 27001 |
| Dayanıklılık | RTO/RPO, 3-2-1 yedek kuralı, kurtarma desenleri, saha sürekliliği |
| Maliyet | FinOps döngüsü, sürpriz maliyet kalemleri, bütçe kontrol listesi |
| Sözlük | 19 terimin Türkçe/İngilizce karşılığı ve birincil kaynaklar |

## Teknik yapı

- **Tek dosya:** Tüm stil ve davranış `index.html` içinde; harici CSS/JS dosyası ve derleme adımı yok.
- **Bağımlılık:** Yalnızca Google Fonts (Inter). Site JavaScript kapalıyken de tüm bölümleri gösterir.
- **Sekmeler:** ARIA `tablist`/`tab`/`tabpanel` rolleri, ok tuşlarıyla gezinme, `#servisler` gibi kalıcı bağlantılar (hash yönlendirmesi) ve tarayıcı geri/ileri desteği.
- **Karar simülatörü:** Veri hassasiyeti, kesinti toleransı ve operasyon kapasitesine göre dört dağıtım modelini puanlar; öneriyi gerekçe ve uyarı ile birlikte gösterir.
- **Erişilebilirlik:** Atlama bağlantısı, görünür odak halkaları, `aria-live` sonuç alanı, `prefers-reduced-motion` desteği, tablo başlıklarında `scope`.
- **SEO/paylaşım:** Meta açıklama, canonical, Open Graph ve Twitter kartı, `og.png` (1200×630), SVG favicon.

## Yerelde çalıştırma

```bash
python -m http.server 8000
```

Ardından `http://localhost:8000` adresini açın. Dosyayı doğrudan açmak da çalışır; yalnızca hash yönlendirmesi için yerel sunucu daha tutarlıdır.

## Yayınlama

Site GitHub Pages üzerinde `main` dalının kök dizininden yayınlanır. `.nojekyll` dosyası Jekyll işlemesini kapatır. Değişiklik yayına almak için:

```bash
git add -A
git commit -m "Açıklayıcı mesaj"
git push origin main
```

## Depo yapısı

```
index.html      Site (HTML + CSS + JS)
favicon.svg     Tarayıcı simgesi
og.png          Sosyal medya kartı (1200×630)
docs/           Konu bazlı kaynak notlar (Türkçe)
LICENSE         MIT
```

## İçerik ilkeleri

- Terimler Türkçe açıklanır, İngilizce karşılığı korunur; sözleşmelerde geçen haliyle eşleşmesi amaçlanır.
- Sağlayıcıya özel iddialar (bölge sayısı, sertifika kapsamı, fiyat) tarih ve kaynak belirtilmeden yazılmaz; güncel konsol ve sözleşme esas alınır.
- Site eğitim amaçlıdır; tıbbi veya hukuki tavsiye değildir.

## Kaynaklar

- NIST SP 800-145 — The NIST Definition of Cloud Computing
- AWS, Microsoft Learn, Google Cloud dokümantasyonu
- HHS / HIPAA, KVKK mevzuat metinleri
- Konu bazlı notlar: [`docs/`](docs/)

## Lisans

MIT — ayrıntı için [LICENSE](LICENSE).

---

### English summary

A single-page Turkish reference site on cloud computing for paramedics and field health teams: service and deployment models, data residency, HIPAA/GDPR/KVKK compliance, resilience (RTO/RPO, 3-2-1 backups) and FinOps. No build step, no framework — one `index.html` with accessible tabs, hash routing and an interactive deployment-decision simulator. Educational content only, not medical or legal advice.
