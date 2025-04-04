# Information Disclosure Vulnerabilities

## İçerik

- [Genel Bakış](#genel-bakış)
- [Information Disclosure Türleri](#information-disclosure-türleri)
- [Açıklar Nasıl Ortaya Çıkıyor?](#bilgi-ifşasındaki-açıklar-nasıl-ortaya-çıkıyor)
- [Güvenlik Açıklarının Etkisi](#bilgi-ifşasındaki-güvenlik-açıklarının-etkisi)
- [Önleme Yöntemleri](#bilgi-ifşa-güvenlik-açıkları-nasıl-önlenir)
- [Lab Örnekleri](#lab-örnekleri)
  - [Lab 1: Error Messages](#lab-1-information-disclosure-in-error-messages)
  - [Lab 2: Debug Page](#lab-2-information-disclosure-on-debug-page)
  - [Lab 3: Backup Files](#lab-3-source-code-disclosure-via-backup-files)
  - [Lab 4: Authentication Bypass](#lab-4-authentication-bypass-via-information-disclosure)
  - [Lab 5: Version Control History](#lab-5-information-disclosure-in-version-control-history)

## Genel Bakış

Information Disclosure (Bilgi Sızıntısı), bir web sitesinin kullanıcılarına istemeden hassas bilgileri ifşa etmesidir. Bu zafiyet, saldırganların sistem hakkında bilgi toplamasına, daha derin güvenlik açıkları keşfetmesine ve potansiyel saldırılar düzenlemesine olanak tanır.

**Örnekler:**
- Gizli dizinlerin adlarını, yapılarını ve içeriklerini bir robots.txt dosya veya dizin listesi aracılığıyla ortaya çıkarmak.
- Geçici yedeklemeler aracılığıyla kaynak kod dosyalarına erişim sağlanması.
- Hata mesajlarında veritabanı tablosu veya sütun adlarının açıkça belirtilmesi.
- Kredi kartı bilgileri gibi son derece hassas bilgileri gereksiz yere ifşa etmek.
- Kaynak kodunda API anahtarlarını, IP adreslerini, veritabanı kimlik bilgilerini vb. sabit kodlama.

## Information Disclosure Türleri

### Error Messages
Web uygulamalarında yanlış yapılandırılmış hata mesajları, sistemin iç yapısı, veritabanı sorguları veya kullanılan teknolojiler hakkında bilgi verebilir.
- **Örnek:** SQL hataları, dosya yolları veya stack trace bilgileri.

### Source Code Disclosure
Yanlış yapılandırmalar veya yanlışlıkla paylaşılan dosyalar, sistemin kaynak kodunun sızmasına neden olabilir.
- **Örnek:** .git klasörünün açık bırakılması, PHP dosyalarının doğrudan erişilebilir olması.

### HTTP Response Headers
Sunucu, X-Powered-By, Server ve diğer başlıkları gereksiz şekilde paylaşarak kullanılan altyapıyı açığa çıkarabilir.
- **Örnek:** `Server: Apache/2.4.29 (Ubuntu)` başlığı ile sunucu yazılımının ve sürümünün ifşa edilmesi.

### Database & Content Leakage
Yanlış yapılandırılmış API'ler veya açık dizin listelemeleri ile sistemdeki veriler açığa çıkabilir.
- **Örnek:** robots.txt dosyasında hassas dizinlerin listelenmesi.

### Sensitive Files & Directories
Güvenlik açıkları nedeniyle .env, config.php gibi dosyalar herkese açık hale gelebilir.
- **Örnek:** .gitignore veya backup.zip gibi dosyaların herkese açık olması.

### Metadata Disclosure
Belge ve medya dosyalarının metadata bilgileri içinde kullanıcı adları, sistem bilgileri veya IP adresleri bulunabilir.
- **Örnek:** Bir Word belgesinin metadata'sında belgenin oluşturulduğu bilgisayarın kullanıcı adı bulunması.

### Log Files
Yanlış yapılandırılmış log dosyaları, saldırganlara sistem içi hareketler hakkında bilgi verebilir.
- **Örnek:** /var/log/apache2/access.log dosyasının dışarıya açık olması.

## Bilgi İfşasındaki Açıklar Nasıl Ortaya Çıkıyor?

1. **Dahili içeriğin genel içerikten kaldırılamaması**
   - Geliştirici yorumları üretimdeki kullanıcılar görebilir.

2. **Web sitesinin ve ilgili teknolojilerin güvenli olmayan yapılandırması**
   - Hata ayıklama ve tanılama özelliklerini devre dışı bırakmamak bazen saldırganlara hassas bilgileri elde etmelerine yardımcı olabilir.

3. **Uygulamanın kusurlu tasarımı ve davranışı**
   - Farklı hata durumlarında farklı yanıtlar döndürüyorsa, bu durum saldırganın hassas verileri saymasına da olanak tanıyabilir.

## Bilgi İfşasındaki Güvenlik Açıklarının Etkisi

Bu tür açıklar hem doğrudan hem dolaylı yoldan etki edebilir:
- Bazen hassas bilgileri ifşa etme eylemi tek başına etkilenen taraflar üzerinde yüksek etkiye sahiptir. Örneğin online satış mağazasının müşterinin kredi kart bilgilerini sızdırması gibi.
- Etki seviyesi, saldırganın bu bilgiyle neler yapabileceğine bağlıdır.

## Bilgi İfşa Güvenlik Açıkları Nasıl Önlenir?

1. **Farkındalık Oluşturma**
   - Herkesin hangi bilgilerin hassas olarak kabul edildiğinin tamamen farkında olduğundan emin olun.
   - .htaccess veya nginx.conf kullanarak kritik dosyalara erişimi kısıtlayın.

2. **Kod İncelemesi**
   - Süreçlerin bir parçası olan bilgi ifşası için kodu denetleyin.
   - Geliştirici yorumlarını kaldırmak gibi ilişkili görevlerden bazılarını otomatikleştirin.

3. **Hata Mesajlarını Kontrol Edin**
   - Genel hata mesajları kullanın, gereksiz ipuçları vermeyin.
   - Özel hata sayfaları kullanarak hassas bilgileri filtreleyin.
   - `display_errors = Off` ayarını yaparak PHP gibi dillerde hata mesajlarını engelleyin.

4. **Debug Modunu Kapatın**
   - Hata ayıklama veya tanılama özelliğinin üretim ortamında devre dışı bırakıldığından emin olun.

5. **Üçüncü Parti Teknolojileri Analiz Edin**
   - Uyguladığınız herhangi bir üçüncü taraf teknolojisinin yapılandırma ayarlarını ve güvenlik etkilerini tam olarak anlayın.
   - Gerçekten ihtiyaç duymadığınız özellikleri ve ayarları araştırıp devre dışı bırakın.

## Lab Örnekleri

### Lab 1: Information Disclosure in Error Messages

1. Ürün sayfasına girilir: `GET /product?productId=1`
2. `productId` değeri dize gibi tamsayı olmayan bir veri türüne değiştirilir: `GET /product?productId="example"`
3. Dönen hata mesajında framework bilgisi görülür: `Apache Struts 2 2.3.31`
4. Bu bilgi submit solution kısmına girilir ve lab çözülür.

### Lab 2: Information Disclosure on Debug Page

1. Sayfa kaynağı görüntülenir ve debug veya geliştirici yorum satırları aranır.
2. `<!-- Debug: /cgi-bin/phpinfo.php -->` gibi bir satır bulunur.
3. Bu URL ziyaret edilir: `https://example.web-security-academy.net/cgi-bin/phpinfo.php`
4. `SECRET_KEY` değeri bulunur ve submit solution kısmına girilir.

### Lab 3: Source Code Disclosure via Backup Files

1. `http://hedef-site.com/robots.txt` dosyasının içeriği kontrol edilir.
2. `/backup` dizini tespit edilir ve `http://hedef-site.com/backup/` adresindeki dosyalar incelenir.
3. `ProductTemplate.java.bak` dosyasının içeriğinde, `connectionBuilder` nesnesinde veritabanı şifresi bulunur.

### Lab 4: Authentication Bypass via Information Disclosure

1. `GET /admin` isteği gönderilir. Yanıt, yönetici panelinin yalnızca bir yönetici olarak oturum açıldığında veya yerel bir IP'den talep edildiğinde erişilebilir olduğunu açıklar.
2. `TRACE /admin` isteği gönderilir, yanıt incelenir. Yanıtta `X-Custom-IP-Authorization` header'ı olduğu görülür.
3. Burp Proxy > Match and Replace kısmında yeni bir kural eklenir:
   - Match: boş
   - Type: Request header
   - Replace: `X-Custom-IP-Authorization: 127.0.0.1`
4. Ana sayfaya gidildiğinde admin paneli görülür, carlos kullanıcısı silinir ve lab çözülür.

### Lab 5: Information Disclosure in Version Control History

1. `.git` dizinin varlığı kontrol edilir: `http://hedef-site.com/.git`
2. Bu dizinin içeriği indirilir: `wget -r https://hedef-site.com/.git/`
3. Yerel git kurulumu kullanılarak commit geçmişi incelenir.
4. "Remove admin password from config." mesajı olan commit bulunur.
5. Bu committe değişen dosyalar incelenir ve diff'e bakılır.
6. Sabit kodlanmış yönetici parolasının ortam değişkeniyle değiştirildiği görülür, ancak eski parola diff'te hala görülebilir.
7. Bu parola kullanılarak admin hesabına giriş yapılır ve carlos kullanıcısı silinir.