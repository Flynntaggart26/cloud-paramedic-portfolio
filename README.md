# ☁️ CloudMed

**Cloud Computing: Paranaşütcü Gözünden** — bulut bilişimi, bulut türleri, bulut istifleri,
öğrenme yolları, dersler ve paraşütcüler için güvenlik/risk yönetimi.

Bu proje, acil servis, ambulans/kampüs ve sağlık teknolojileri çalışanları için
**Türkçe ana içerik + İngilizce terimler**yle bir ortak dönüşüm rehberi sunar.

---

## 🚀 Canlı Site

[⚡ Canlı Siteyi Görüntüle](https://flynntaggart26.github.io/cloud-paramedic-portfolio/)

Site tek dosyalı, tarayıcıda açılır ve mobil uyumlu durur.

---

## 📖 Dokümanlar

- [Bulut Bilişimi Temelleri](docs/cloud-basics.md)
- [Bulut Servis Modelleri](docs/cloud-services.md)
- [Bulut Dağıtım Modelleri](docs/cloud-deployment.md)
- [Bulut Sağlayıcıları ve Yerllere Göre İstifler](docs/cloud-providers-locations.md)
- [Paraşütcüler İçin Riskler](docs/cloud-risks-paramedic.md)
- [Glosaryo](docs/glossary.md)

---

## 💡 İçerik Özeti

1. [Bulut Bilişimi Nedir?](#1-bulut-bilişimi-nedir)
2. [Bulut Türleri](#2-bulut-türleri)
3. [Servis Modelleri](#3-servis-modelleri)
4. [Nerede Çalışır?](#4-nerede-çalışır)
5. [İngilizce GitHub’da Bulutları Bulmak](#5-ıngilizce-githubda-bulutları-bulmak)
6. [Dersler](#6-dersler)
7. [Paraşütcüler İçin Riskler](#7-ıııı-ıııı)
8. [Glosaryo](#8-ıglosaryo)

---

## 1. Bulut Bilişimi Nedir?

**Cloud computing**, ağın üzerindeki çok sayıda kişiye depolama, işlem, ağ, veritabanı, sunucu, yazılım, analiz ve
yapay zeka gibi kaynakları sağlayan bir modeldir.

Kısaca bir **“sanal depo ve sanal bina”** diyebiliriz. Sağlık hizmetlerinde hastalık kayıtları, e-posta, görsel görüntü,
telefon aramaları ve acil yönetim sistemleri bu uzak depolama ve işlem mimarilerine dayanabilir.

⚠️ **“Cloud” ile ne kastediliyor?**

Internet üzerindeki hiçbir fiziksel bulut değil; yazılım ve altyapının **görülmeyen (abstraction)** sunumudur.
Sizin bilgisayarınızdan dışarıya çıkan verilerin nerededir, o verinin **“bulutta”** olduğunu söylemek,
ona **“bu hizmetin sağlayıcısının sunucusunda”** demektir.

---

## 2. Bulut Türleri

- **Public Cloud** — AWS, Azure, Google Cloud gibi sağlayıcının herkese açık ortamı.
- **Private Cloud** — Tek kurum içinde çalıştırılan, kapatılmış ve izlenen ortam.
- **Hybrid Cloud** — Aynı işletmede hem kuralı hem genel bulut kullanımı.
- **Community Cloud** — Bir genel topluluk (ör. sağlık, sigorta, kamu) için ortak ortam.
- **Multi-Cloud** — Birden fazla sağlayıcı kullanarak sisteminizi şekillendirmek.

---

## 3. Servis Modelleri

| Model | Kısaca Ne Alıyorsunuz? | Örnek Kullanım |
|---|---|---|
| **IaaS** | Sanal sunucu, disk, ağ, sanal ağı | Sunucuyu çalıştırmak, veritabanı kopyası alın |
| **PaaS** | Geliştirme çerçevesi ve operasyonel altyapı | Uygulama kodu yazmak, dağıtmak |
| **SaaS** | Kullanabileceğiniz bitişik yazılımlar | E-posta, puanlama, telefon, sağlık uygulamaları |
| **FaaS** | İstek üzerine çalışan fonksiyonlar | Yeni kayıt olduğunda bildirim gönder |
| **DaaS** | Uzak masaüstü ortamı | Ortak ekiple çalışma alanı |
| **DBaaS** | Yönetilen veritabanı | Hasta kayıtları, izleme raporları için kullanılabilir |

---

## 4. Nerede Çalışır?

Bulut kavramları yalnızca İngilizce terimlerle değil; fiziksel ve işleyiş kavramlarına da sahiptir:
`region`, `availability zone`, `edge`, `datacenter`.

- **AWS**: `aws.amazon.com/regions`
- **Microsoft Azure**: `azure.microsoft.com/explore/global-infrastructure/`
- **Google Cloud**: `cloud.google.com/compute/docs/regions-zones`

Sağlık alanında kullanımda şunları mutlaka kontrol edin:

1. Veri konumu / ülke sınırları
2. Uyum ve yetkilendirme seçenekleri
3. İş birliği protokolleri (ör. BAA/AIA)
4. Loglama, şifreleme ve erişim kontrolleri
## 5. İngilizce GitHub’da Bulutları Nasıl Bulunur?

Git’te “bulut” çoğu zaman `cloud`, `cloud-computing`, `cloud-integration`, `cloud-security`,
`cloud-infrastructure` gibi gövde veya etiketlerde görünür.

Örnek arama terimlerinin karşılıkları:

| Türkçe ne diyorsunuz? | İngilizce arama |
|---|---|
| Daha esnek/uyarlanabilir | `scalable cloud` / `elastic cloud` |
| Tüketici odaklı | `broker cloud` / `marketplace cloud` |
| Yerleşik önbellek | `edge cache` / `CDN` |
| Esneklik | `elasticity` / `autoscaling` |
| Güvenlik | `cloud security` / `IAM` / `zero trust` |
| Kurtarılabilirlik | `backup` / `recovery` / `disaster recovery` |

Önerilen kaynaklar:

- AWS: `aws.amazon.com/cloud-computing/`
- Microsoft Learn: “Introduction to cloud computing”
- Google Cloud: `cloud.google.com/learn/what-is-cloud-computing`
- Khan Academy: Computer Science pathway
- Wikipedia: `Cloud computing`
- NIST SP 800-145

---

## 6. Dersler

- **Görünmeyen mimarinin gerçeklik vardır**: Arka planda fiziksel cihazlar, ısınma, koruma ve izleme vardır.
- **Çok fazla kontrol, çok fazla sorumluluk**: Sağlayıcı, alana bazı varsayılan güvenlik kontrolü verir.
- **Esneklik, aciliyeti anlamaz**: Yanlış ayar, gecikme, fiyat artışı veya performans sorunlarına yol açabilir.
- **Veri koruyucu en üst tefekle birliktelikte çalışmalıdır**: Şifreleme, erişim denetimi, günlük tutma, çok faktörlü kimlik.
- **Felaket sonrası önce kurtarılıyor**: `RTO` ve `RPO` sınırları tanımlanmalı, yedekler test edilmelidir.

---

## 7. Paraşütcüler İçin Bulut Riskleri

- 🔒 **Hasta verisi sızıntısı**
- ⚖️ **Uyumluluk yükü (HIPAA, GDPR, KVKK vb.)**
- 📶 **Platform downtimesi**
- 🎣 **Vendor lock-in**
- 🔑 **Kimlik ve bilgisel sızıntı**
- 🛡️ **Veri konumlandırma ve özerklik**
- 🔄 **Ransomware ve yedek arızası**
- 🌡️ **Çevresel faktörler**
- 🧠 **İnsan faktörü / bilinçsiz paylaşım**

### Altın kurallar

- Şifreleme (giden veri ve duran veri)
- En az yetkili erişim
- Çok faktörlü doğrulama
- 3-2-1 yedek stratejisi
- `RTO`/`RPO` testleri
- Günlük tutma ve uyarılar
- Oturum sonlandırma / geçici erişim
- Bağlantı kopmak üzere offline/manual iş akışı

---

## 8. Glosaryo

| Türkçe | İngilizce | Kısa Anlam |
|---|---|---|
| Bulut bilişimi | Cloud computing | İnternet üzerinden kaynak sunumu |
| Bulut | Cloud / The Cloud | Görünmeyen sanal altyapı |
| Bölge | Region | Coğrafi bulut alanı |
| Bulum noktası | Availability zone | İzole kaynak grup |
| Depo | Datacenter / Storage | Fiziksel veri deposu |
| Süreklilik | Continuity / Disaster Recovery | Kısmeli işlemler |
| Erişim kontrolüğü | Access control / IAM | Kimlere neyin izin verilir |
| Şifreleme | Encryption | Verinin kısaltılması |
| Yedekleme | Backup / Snapshot | Veri kopyası alın |
| Geri kazanım süresi | RTO / RPO | Süre / veri kaybı sınırı |

---

## 🛠 Çalışma Alanı

Açık `index.html` tarayıcıda çalışır:

```bash
# Örnek: yerel statik sunucu
python3 -m http.server 8000
# https://localhost:8000
```

Mac/Linux/MacOS için:

```bash
python3 -m http.server 8000
```

Windows için:

```powershell
python -m http.server 8000
```

---

## 🤝 Katkıda Bulunma

1. Fork gönder
2. Yeni bir bölüm veya dil ekle
3. `index.html` HTML doğruluğu ve `README.md` güncellenmeli
4. Pull request aç

---

## 📜 Lisans

[MIT](LICENSE)