# Bulut Dağıtım Modelleri

## Public cloud (herkese açık bulut)

Hızlı, düşük sabit maliyetli ve öğrenmesi kolaydır. AWS, Azure veya Google Cloud birden fazla müşteriye aynı altyapı havuzundan hizmet verir. Küçük projeler, eğitim ortamları ve standart iş yükleri için uygundur.

Hasta verisi işlenecekse sağlayıcıyla veri işleme sözleşmesi (BAA/DPA) imzalanmalı, bölge seçimi ve şifreleme ayarları yazılı olarak doğrulanmalıdır.

## Private cloud (özel bulut)

Tek bir kuruma ayrılmış ortamdır. Daha yüksek maliyet, daha yüksek kontrol sağlar. Hassas hasta verisi veya katı iç uyumluluk gereksinimleri olduğunda değerlendirilir.

Özel bulut, fiziksel olarak kurum içinde olmak zorunda değildir; önemli olan kaynağın tek kiracıya ayrılmış olmasıdır.

## Hybrid cloud (hibrit bulut)

Kurum içi (on-premises) altyapı ile public cloud'u birlikte kullanır. Bazı işler yerelde kalmak zorundayken ağır işlem gücü dışarıdan alınabilir. Sağlıkta en yaygın desendir; entegrasyon ve kimlik yönetimi karmaşıklığı artar.

## Community cloud (topluluk bulutu)

Benzer ihtiyaçları olan kurumların (afet sağlık ağı, 112 yapısı, kamu hastaneleri) paylaştığı ortamdır. Maliyet paylaşılır, yönetişim ve sorumluluklar ortak kurulur.

## Multi-cloud (çoklu bulut)

İki veya daha fazla sağlayıcı kullanılır. Tek sağlayıcıya bağımlılığı azaltır; yönetim, uyumluluk kanıtı ve veri transferi maliyetini artırır.

## Saha ekipleri için pratik kural

- Günlük araçlar (e-posta, takvim, dokümantasyon): SaaS + public cloud.
- Hassas iş akışları: sözleşme ve risk değerlendirmesi tamamlanana kadar veriyi yerelde tutun.
- Yedeklilik ve süreklilik: platform seçmeden önce yedekleme, devreye alma ve geri dönüş senaryosunu yazılı olarak doğrulayın.
