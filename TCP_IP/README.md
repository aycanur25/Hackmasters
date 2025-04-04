# TCP/IP, RFC, Network ve HTTP Authentication

Bu belge, TCP/IP protokolü, RFC'ler, ağ türleri ve HTTP kimlik doğrulama yöntemleri hakkında temel bilgiler sunmaktadır. Ayrıca, HTTP yöntemlerine ve güvenlik protokollerine dair açıklamalar içermektedir.

## TCP/IP

**TCP/IP** (Transmission Control Protocol/Internet Protocol), internet ve diğer bilgisayar ağlarının temelini oluşturan bir iletişim protokolü setidir. Bu protokol, verilerin kaynak cihazdan hedef cihaza güvenilir bir şekilde aktarılmasını sağlar. TCP/IP, dört katmandan oluşur:

- **Uygulama Katmanı**: HTTP, FTP, SMTP gibi protokoller içerir.
- **Taşıma Katmanı**: TCP ve UDP gibi protokollerle veri aktarımı güvenilirliği sağlanır.
- **Ağ Katmanı**: IP adresleme ve paket yönlendirme işlemlerini gerçekleştirir.
- **Bağlantı Katmanı**: Fiziksel veri aktarımını ve cihazlar arasındaki bağlantıyı sağlar.

## RFC (Request for Comments)

**RFC** (Yorum Talebi), internet standartlarını ve protokollerini tanımlayan belge serisidir. İnternet Mühendisliği Görev Gücü (IETF) tarafından yayınlanır. Örnekler:

- **RFC 791**: IP protokolü standardını tanımlar.
- **RFC 2616**: HTTP 1.1 protokolünü tanımlar.

## Network (Ağ)

Bir **network** (ağ), birbirine bağlı cihazlar ve bu cihazlar arasında veri paylaşımını sağlayan altyapıdır. Temel ağ türleri:

- **LAN (Local Area Network)**: Küçük bir alanda (ofis, ev) kullanılan ağ.
- **WAN (Wide Area Network)**: Büyük bir alanda (şehirler, ülkeler) kurulan ağ.
- **VLAN (Virtual LAN)**: Sanal olarak bölümlenmiş ağlar.

## HTTP Authentication

HTTP, kullanıcıların bir web kaynağına erişimini kontrol etmek için çeşitli kimlik doğrulama yöntemleri sunar.

### Basic Authentication

Kullanıcı adı ve parola, Base64 ile kodlanarak "Authorization" başlığı içinde gönderilir. Güvenli değildir, şifreleme (örn. HTTPS) olmadan kullanılmamalıdır.

```plaintext
Basic dXNlcm5hbWU6cGFzc3dvcmQ=
