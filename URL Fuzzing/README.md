# WEB FUZZING

Web fuzzing, çeşitli girdileri test ederek güvenlik açıklarını belirlemek için web uygulaması güvenliğinde kritik bir tekniktir. Saldırganların istismar edebileceği potansiyel kusurları tespit etmek için beklenmeyen veya rastgele veriler sağlayarak web uygulamalarının otomatik olarak test edilmesini içerir.

## Fuzzing ve Brute Forcing

- **Fuzzing** daha geniş bir ağ atar. Fuzzing araçları genellikle çeşitli yükler kümesi oluşturmak için ortak desenler, mevcut parametrelerin mutasyonları veya hatta rastgele karakter dizileri içeren kelime listelerinden yararlanır.
- **Brute-forcing** daha hedefli bir yaklaşımdır. Belirli bir değer için, örneğin bir parola için birçok olasılığı sistematik olarak denemeye odaklanır.

## Web Fuzzing'in Faydaları

- **Gizli Güvenlik Açıklarını Ortaya Çıkarma**: Fuzzing, geleneksel güvenlik test yöntemlerinin gözden kaçırabileceği güvenlik açıklarını ortaya çıkarabilir.
- **Güvenlik Testini Otomatikleştirme**: Bulanıklaştırma, test girdilerinin oluşturulmasını ve gönderilmesini otomatikleştirerek değerli zaman ve kaynak tasarrufu sağlar.
- **Gerçek Dünya Saldırılarını Simüle Etme**: Fuzzer'lar saldırganların tekniklerini taklit ederek kötü niyetli aktörler bunları istismar etmeden önce zayıflıkları belirlemenize yardımcı olabilir.
- **Girdi Doğrulamayı Güçlendirme**: Bulanıklaştırma, SQL injection ve cross-site scripting gibi yaygın güvenlik açıklarını önlemek için kritik öneme sahip olan girdi doğrulama mekanizmalarındaki zayıflıkları belirlemeye yardımcı olur.
- **Kod Kalitesini İyileştirme**: Bulanıklaştırma, hataları ve yanlışları ortaya çıkararak genel kod kalitesini iyileştirir.
- **Sürekli Güvenlik**: Bulanıklaştırma, boru hatlarının bir parçası olarak software development lifecycle'a entegre edilebilir.

## Temel Kavramlar

### Wordlist
Bulanıklaştırma sırasında girdi olarak kullanılan sözcüklerin, ifadelerin, dosya adlarının, dizin adlarının veya parametre değerlerinin bir sözlüğü veya listesi.
- **Genel**: admin, login, password, backup, config
- **Uygulamaya özgü**: productID, addToCart, checkout

### Payload
Bulanıklaştırma sırasında web uygulamasına gönderilen gerçek veriler. Basit bir dize, sayısal değer veya karmaşık veri yapısı olabilir.
- Örnek: `' OR 1=1 --` (SQL enjeksiyonu için)

### Response Analysis
Bulanıklaştırıcının yüklerine yönelik web uygulamasının yanıtlarını (örneğin yanıt kodları, hata mesajları) inceleyerek güvenlik açıklarına işaret edebilecek anormallikleri tespit etmek.
- **Normal**: 200 OK
- **Hata** (olası SQLi): 500 Veritabanı hata mesajıyla Dahili Sunucu Hatası

### Fuzzer
Bir web uygulamasına yüklerin oluşturulmasını ve gönderilmesini ve yanıtların analiz edilmesini otomatikleştiren bir yazılım aracıdır.
- Örnek araçlar: ffuf, wfuzz, Burp Suite Intruder

## Fuzzing Araçları

### FFUF (Fuzz Faster U Fool)

Go'da yazılmış hızlı bir web bulanıklaştırıcıdır. Web uygulamalarında dizin keşfi, parametre fuzzing'i, gizli dosyaları bulma, alt domain keşfi ve zafiyet testleri için kullanılır. Özellikle pentest ve bug bounty (ödüllü güvenlik testleri) yapanlar tarafından tercih edilir.

#### Kurulum:

**Linux/macOS**:
```bash
sudo apt install ffuf   # Debian/Ubuntu için
brew install ffuf       # macOS için
go install github.com/ffuf/ffuf@latest
```

**Windows**:
```bash
# Go kurulumu yapın, sonra:
go install github.com/ffuf/ffuf@latest
```

#### Kullanım Örnekleri:

**Web Dizini Keşfi**:
```bash
ffuf -u http://hedefsite.com/FUZZ -w wordlist.txt
```

**Dosya ve Uzantı Keşfi**:
```bash
ffuf -u http://hedefsite.com/FUZZ -w wordlist.txt -e .php,.html,.txt
```

**Alt Domain Fuzzing**:
```bash
ffuf -u http://FUZZ.hedefsite.com -w subdomains.txt -H "Host: FUZZ.hedefsite.com"
```

**POST Verisi ile Fuzzing**:
```bash
ffuf -u http://hedefsite.com/login -w passwords.txt -X POST -d "username=admin&password=FUZZ"
```

**Status Code Filtreleme**:
```bash
ffuf -u http://hedefsite.com/FUZZ -w wordlist.txt -mc 200
```

**JSON API Fuzzing**:
```bash
ffuf -u http://hedefsite.com/api/FUZZ -w api-endpoints.txt -H "Content-Type: application/json"
```

### Gobuster

Bir diğer popüler web dizini ve dosya bulanıklaştırıcısıdır. Hızı ve basitliğiyle bilinir, bu da onu hem yeni başlayanlar hem de deneyimli kullanıcılar için harika bir seçim haline getirir. Özellikle web dizin keşfi, DNS alt domain keşfi ve VHost (Virtual Host) keşfi yapmak için kullanılır. Go diliyle yazıldığı için çok hızlıdır ve büyük wordlist'lerle bile etkili çalışır.

#### Kurulum:

**Linux/macOS**:
```bash
sudo apt install gobuster   # Debian/Ubuntu için
brew install gobuster       # macOS için
go install github.com/OJ/gobuster/v3@latest
```

**Windows**:
```bash
# Go kurulumu yapın, sonra:
go install github.com/OJ/gobuster/v3@latest
```

#### Kullanım Örnekleri:

**Web Dizini Keşfi**:
```bash
gobuster dir -u http://hedefsite.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

**Alt Domain Keşfi (DNS Fuzzing)**:
```bash
gobuster dns -d hedefsite.com -w subdomains.txt
```

**Virtual Host Keşfi (VHost Fuzzing)**:
```bash
gobuster vhost -u http://hedefsite.com -w vhosts.txt
```

**AWS S3 Bucket Keşfi**:
```bash
gobuster s3 -w s3_wordlist.txt
```

**Sonuçları Filtreleme**:
```bash
gobuster dir -u http://hedefsite.com -w wordlist.txt --status-codes-blacklist 403 -o result.txt
```

### FeroxBuster

Rust'ta yazılmış hızlı, yinelemeli bir içerik keşif aracıdır. Web uygulamalarında bağlantısız içeriklerin kaba kuvvetle keşfi için tasarlanmıştır.

### Araç Karşılaştırması

- Gobuster DNS ve VHost keşfinde daha güçlü
- FFUF parametre fuzzing ve HTTP isteklerini özelleştirme konusunda daha iyi