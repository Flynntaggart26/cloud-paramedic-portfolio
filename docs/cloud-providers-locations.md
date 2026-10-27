# Bulut Sağlayıcıları ve Konum

## Ana sağlayıcılar

- **AWS** — `aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- **Microsoft Azure** — `azure.microsoft.com/explore/global-infrastructure/`
- **Google Cloud** — `cloud.google.com/compute/docs/regions-zones`

Bölge listeleri ve hizmet kapsamı sık değişir. Bir bölgenin varlığı, o bölgede ihtiyacınız olan tüm hizmetlerin ve uyumluluk kapsamının bulunduğu anlamına gelmez; güncel doküman ve sözleşme esas alınmalıdır.

## Temel terimler

- **Region (bölge)** — Bir veya daha fazla veri merkezini kapsayan coğrafi alan. Veri ikametgahı kararı burada verilir.
- **Availability zone / zone (kullanılabilirlik bölgesi)** — Bölge içinde bağımsız güç ve ağa sahip izole kaynak grubu.
- **Edge (uç nokta)** — Kullanıcıya yakın önbellek ve dağıtım noktası; gecikmeyi düşürür, kalıcı veri saklama yeri değildir.
- **Datacenter (veri merkezi)** — Sunucu ve depolama barındıran fiziksel bina.

## Sağlıkla ilgili not

Hasta verisi, e-reçete, hastane entegrasyonu veya kamu kayıtları söz konusu olduğunda şunları doğrulayın:

1. Bölge ve veri ikametgahı gereksinimleri.
2. Uyumluluk ve akreditasyon seçenekleri (HIPAA, GDPR, KVKK, ISO 27001, SOC 2).
3. Sağlık verisi için işleme sözleşmesi (BAA) veya eşdeğeri.
4. Denetim kaydı, şifreleme ve erişim kontrolleri.
5. Veri çıkışı (egress) maliyeti ve sağlayıcı değiştirme koşulları.

Sağlayıcının pazarlama sayfası değil, güncel konsol, hizmet kapsamı dokümanı ve imzalanacak sözleşme kanıt sayılır.
