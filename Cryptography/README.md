# Kriptografi Giriş

## Temel Kavramlar

Kriptografi, üçüncü tarafların varlığında güvenli iletişim tekniklerinin incelenmesi ve uygulanmasıdır.

Temel güvenlik ilkeleri:
- **Gizlilik**: Bilginin belirli kişilerle veya yerlerle sınırlı olmasını sağlayan belirli kurallar
- **Veri bütünlüğü**: Verilerin tüm yaşam döngüsü boyunca doğru ve tutarlı kalması
- **Kimlik doğrulama**: Kullanıcının talep ettiği verinin ona ait olduğundan emin olma süreci
- **İnkar edilemezlik**: Bir belgenin üzerindeki imzasının veya bir mesajın gönderilmesinin gerçekliğini inkar edememesi

### Şifreleme Süreci

Alice (Gönderen) → Bob (Alıcı)  
C = E (m, k) → m = D (C, k)

Burada:
- C: Şifreli metin
- E ve D: Şifreleme ve Şifre Çözme algoritmaları
- m: Orijinal mesaj
- k: Anahtar

## Kriptografi Türleri

1. **Simetrik anahtarlı şifreleme**: Verileri şifrelemek ve şifresini çözmek için tek bir anahtarın kullanılmasını içerir.

2. **Asimetrik anahtar şifrelemesi**: Verileri şifrelemek ve şifresini çözmek için bir anahtar çifti kullanır. Genel anahtar herkes tarafından kullanılabilirken, özel anahtar sahibi tarafından gizli tutulur.

3. **Karma işlevleri**: Herhangi bir boyuttaki verileri sabit boyutlu bir çıktıya dönüştüren matematiksel bir algoritmadır.

## Uygulama Alanları

Kriptografi şu alanlarda yaygın olarak kullanılmaktadır:
- Bankacılık
- E-ticaret
- Dijital imzalar
- Parolalar
- Askeri ve istihbarat uygulamaları

## Public Key Infrastructure (PKI)

Açık anahtar altyapısı, dijital sertifikaların verilmesinin arkasındaki yönetim organıdır. Anahtar çifti kullanır: açık anahtar ve özel anahtar. Saldırılara açıktır, bu nedenle sağlam bir altyapıya ihtiyacı vardır.

## Kriptosistemdeki Anahtarların Yönetimi

Kripto sisteminin güvenliği anahtarlarına dayanır. Kriptografik anahtar, güvenli bir yönetim tarafından yönetilmesi gereken bir veri parçasıdır.

### Anahtar Yaşam Döngüsü

Anahtar yaşam döngüsünün yönetilmesi şunları içerir:

1. **Generation of key (Anahtar Oluşturma)**: Anahtarın oluşturulması işlemi. Bu aşamada güvenli bir anahtar oluşturulması için gerekli algoritmalar kullanılır.

2. **Establishment of key (Anahtarın Belirlenmesi)**: Oluşturulan anahtarın güvenli bir şekilde dağıtılması ve kullanıma hazır hale getirilmesi.

3. **Storage of key (Anahtarın Saklanması)**: Anahtarın güvenli bir ortamda saklanması. Bu aşama, anahtarın yetkisiz erişimlerden korunmasını sağlar.

4. **Usage of key (Anahtarın Kullanımı)**: Anahtarın şifreleme veya diğer güvenlik işlemleri için aktif olarak kullanıldığı aşama.

5. **Archival (Arşivleme)**: Kullanılan anahtarın gerektiğinde geri yüklenebilmesi için güvenli bir şekilde arşivlenmesi. Bu aşamada anahtarın uygun süre boyunca saklanması önemlidir.

6. **Destruction of key (Anahtarın Yok Edilmesi)**: Anahtarın kullanılmasının sona ermesi durumunda, anahtarın güvenli bir şekilde imha edilmesi.

Bu döngü, anahtar yönetimi sürecinin her aşamasında güvenliği ve veri bütünlüğünü sağlamak için dikkatli bir şekilde uygulanmalıdır. Anahtar yaşam döngüsü yönetimi, şifreleme ve veri koruma stratejilerinin etkili olabilmesi için kritik bir bileşendir.

### Anahtar Güvenliği

- **Özel anahtarı gizli tutmak**: Özel anahtarı sadece sahibi kullanabilir.
- **Genel anahtarın güvence altına alınması**: Genel anahtarlar açık alandadır. Bu düzeyde genel erişilebilirlik olduğunda, bir anahtarın doğruluğu ve ne için kullanılacağını bilmek zorlaşır.

## Açık Anahtar Altyapısı (PKI) Bileşenleri

- Dijital Sertifika
- Özel Anahtar Belirteçleri
- Kayıt Yetkisi
- Sertifika Yetkisi
- CMS veya Sertifikasyon yönetim sistemi

## PKI Çalışma Prensibi

PKI ve Şifreleme kökü kriptografi ve şifreleme tekniklerinin kullanımını içerir. Temel zorluk: Genel anahtarın doğru kişiye mi yoksa ait olduğunu düşündüğümüz kişiye mi ait olduğunu nasıl bileceğiz? Her zaman bir MITM (Ortadaki Adam) riski vardır. Bu sorun, dijital sertifikalar kullanan PKI tarafından çözülür. PKI, sahiplerin doğrulanması için anahtarlara kimlikler verir.

### Açık Anahtar Sertifikası veya Dijital Sertifika

Dijital dünyada benzersiz bir şekilde dağıtmak için verilir. Sertifika Yetkilisi (CA), bir kullanıcının genel anahtarının özelliklerini diğer bilgilerle birlikte dijital sertifikada depolar ve dijital imza ekler. Sertifika Yetkilisinin açık anahtarı kullanılarak imzanın doğrulanmasıyla çalıştırılabilir.

### Sertifika Yetkilileri (CA)

CA sertifikaları düzenler ve doğrular. Doğruluğundan emin olur ve dijital olarak imzalar. Temel rolleri:

- Anahtar çiftlerini oluşturma
- Dijital sertifikaların bildirimi
- Sertifikaların yayınlanması
- Sertifikanın doğrulanması
- İptal

## Dijital Sertifikanın Sınıfları

- **Sınıf 1**: Yalnızca e-posta adresini kullanarak alınır.
- **Sınıf 2**: Daha fazla kişisel performansa ihtiyaç duyulur.
- **Sınıf 3**: Öncelikle istekte bulunan kişinin çalışmalarını kontrol eder.
- **Sınıf 4**: Kurumlar ve hükümetler tarafından kullanılır.

## Sertifika Oluşum Süreci

1. Özel ve genel anahtar oluşturulur.
2. CA, özel anahtarın sahibinin tanımlayıcı özelliklerini ister.
3. Açık anahtar ve nitelikler bir CSR (Sertifika İmzalama İsteği) formatında kodlanır.
4. Anahtar sahibi, özel anahtara sahip olduğunu kanıtlamak için CSR'yi imzalar.
5. CA, gerekli incelemelerden sonra sertifikayı imzalar.