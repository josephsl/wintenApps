# Windows Temel Uygulamalar #

* Yazarlar: Joseph Lee, Derek Riemer ve diğerleri

Not: Eklenti başlangıçta Windows 10 Temel Uygulamalar olarak
adlandırılırken, Windows 10 ve Windows 11 gibi gelecekteki windows
sürümlerini desteklemek için 2021'de Windows Temel Uygulamalar olarak
yeniden adlandırıldı. Bu eklentinin bazı kısımları yine de orijinal eklenti
adına atıfta bulunacaktır.

Bu eklenti, çeşitli modern Windows uygulamaları için bir uygulama modül
koleksiyonunun yanı sıra Windows 10 ve sonraki sürümlerde bulunan belirli
kontroller için geliştirmeler ve düzeltmeler içerir.

Bazı uygulamalar için aşağıdaki uygulama veya destek modülleri  mevcuttur
(nelerin dahil olduğuyla ilgili ayrıntılar için her bir uygulama bölümüne
bakın):

* Modern klavye
* Ayarlar (Windows+I)

Notlar:

* Bu eklenti için 64 bit Windows 10 22H2 (derleme 19045), 11 22H2 (derleme
  22621) veya sonraki sürümler gerekir.
* Özellik güncelleme destek süresi, tüketici destek süresine (Ev, Pro, Pro
  Education, Pro for Workstations sürümleri) bağlıdır ve eklenti, tüketici
  desteği sona ermeden önce özellik güncellemesi desteğini
  sonlandırabilir. Daha fazla bilgi ve destek tarihleri ​​için
  <https://aka.ms/WindowsTargetVersioninfo> adresine bakın.
* Ne kadar yüklenebilse de, bu eklenti Windows Enterprise LTSC (Uzun Süreli
  Hizmet Kanalı) ve Windows Server sürümlerini desteklemez.
* Windows Insider Önizleme yapılarındaki tüm özellikler desteklenmeyecek,
  özellikle canary ve dev kanallarında Windows Insiders alt kümesine sunulan
  özellikler için.
* Eklenti, Insider Preview derlemelerine dahil edilen ve daha sonra
  kaldırılan değişiklikleri taklit edebilir ve bu değişiklikler için eklenti
  bunları gelecekteki sürümlerde kaldırabilir.
* Eklenti geliştirme kanalı, beta ve kararlı sürümlere dahil edilebilecek
  veya edilmeyebilecek deneysel içerik de dahil olmak üzere değişiklikleri
  içerecek ve beta kanalı, gelecekteki kararlı sürümler için planlanan
  değişikliklerle birlikte gelecek.
* Bazı eklenti özellikleri, NVDA ekran okuyucusunun bir parçasıdır veya
  yakında olacaktır.
* Başlat menüsü ve içerik menüsü gibi web teknolojilerini ve içeriği içeren
  uygulamalarla en iyi deneyimi elde etmek için, NVDA'nın göz atma modu
  ayarları panelinden "Odak değişiklikleri için otomatik odak modu" ayarını
  etkinleştirin.

Her bir eklenti sürümü arasında yapılan değişikliklerin listesi için
[eklenti sürümleri için değişiklik günlükleri][1] belgesine bakın.

## Modern klavye

Buna emoji paneli, pano geçmişi, dokunmatik klavye, dikte/sesle yazma,
donanım giriş önerileri, önerilen eylemler ve Windows 10 ve 11'deki belirli
diller için modern giriş yöntemi düzenleyicileri dahildir. Emojileri
görüntülerken, en iyi deneyim için Unicode Konsorsiyum ayarını şu adresten
etkinleştirin: NVDA'nın konuşma ayarları ve sembol seviyesini "bazı" veya
daha yükseğe ayarlayın. Windows 10'da pano geçmişinden yapıştırırken, seçili
öğeyi yapıştırmak için Enter tuşu yerine Boşluk Çubuğuna tuşuna basın.

* Windows 11'de, telefon numaraları gibi uyumlu veriler panoya
  kopyalandığında NVDA önerilen eylemleri duyuracaktır. Bu artık NVDA
  2024.2'nin bir parçasıdır.

## Ayarlar (Windows+I)

* NVDA, indirme ve yükleme işlemleri ilerledikçe Windows Update durumuna
  yönelik güncellemeleri bildirecektir. Windows 10'da bu, güncellemeler
  indirilirken ve yüklenirken Ayarlar uygulamasında gezinirken konuşmanın
  kesilmesine neden olabilir. Windows 11'de, tek tek girişlerin güncelleme
  durumunu gözden geçirmek için güncellemeler listesinde nesne dolaşımı
  kullanılabilir.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
