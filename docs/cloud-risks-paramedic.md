# Paramedikler ve Saha Sağlık Ekipleri için Riskler

## Özet

Bulut teknolojisi hız, paylaşım ve süreklilik sağlar. Ancak yanlış tasarlanmış bir bulut kurulumu hasta verisini açığa çıkarabilir, kesinti sırasında akışı durdurabilir veya uyumluluk ihlaline yol açabilir.

## Ana risk alanları

- **Veri açığı** — Yanlış yapılandırılmış depolama, loglar veya paylaşım bağlantıları hasta verisini sızdırabilir.
- **Uyumluluk** — HIPAA, GDPR, KVKK ve yerel sağlık mevzuatı aynı anda geçerli olabilir.
- **Kesinti** — Sağlayıcı arızası kayıt, e-posta ve izleme sistemlerini etkiler.
- **Yedekler** — Silinmiş veya şifrelenmiş yedekler sürekliliği kesintiye uğratır.
- **Kimlik ve kimlik bilgileri** — Zayıf parola veya sızmış anahtar yetkisiz erişime yol açar.
- **Satıcıya bağımlılık** — Geçiş maliyeti yükseldikçe sağlayıcı değiştirmek zorlaşır.
- **Veri ikametgahı** — Verinin belirli bir ülke veya bölgede kalması gerekebilir.
- **Fiziksel ve çevresel etkenler** — Güç, soğutma ve fiziksel güvenlik hâlâ önemlidir.
- **İnsan faktörü** — Oltalama, hatalı yapılandırma ve hasta görüntüsünün kişisel telefonla paylaşılması.

## Tercih edilen kontroller

- Veriyi **aktarımda** ve **durgun halde** şifreleyin.
- En az yetki ilkesi ve çok faktörlü kimlik doğrulama kullanın.
- **3-2-1** yedek kuralını uygulayın: 3 kopya, 2 farklı ortam, 1 çevrimdışı veya değiştirilemez kopya.
- Geri yükleme ve kesinti prosedürlerini düzenli olarak test edin.
- Araç ve olay yerinde kullanılmak üzere çevrimdışı/manuel dokümantasyon modu bulundurun.
- Satıcı sözleşmelerini (BAA/DPA) ve veri ikametgahı maddelerini inceleyin.
- Saha personelini eğitin ve olay tatbikatları yapın.

## Sahada en sık görülen üç hata

1. Paylaşım bağlantısını "süresiz ve herkese açık" bırakmak.
2. Test ortamını üretim verisiyle doldurup sonra kapatmayı unutmak.
3. Yedeği almak ama geri yüklemeyi hiç denememek.
