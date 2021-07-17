# Windows Temel Uygulamalar #

* Yazarlar: Joseph Lee, Derek Riemer ve diğer Windows 10 kullanıcıları
* [kararlı sürüm][1]ü indir
* [geliştirme sürümü][2]nü indir
* NVDA uyumluluğu: 2020.4 ve sonrası

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

* Hesap makinesi (modern)
* Takvim
* Cortana (Konuşmalar)
* Posta
* Haritalar
* Microsoft Solitaire Koleksiyonu
* Microsoft Store
* Modern klavye (emoji paneli/dikte/donanım giriş önerileri/pano
  geçmişi/modern giriş yöntemi düzenleyicileri)
* Kişiler
* Ayarlar (sistem ayarları, Windows+I)
* Hava durumu
* Başlat Menüsü kutucukları gibi kontroller için çeşitli modüller

Notlar:

* Bu eklenti, Windows 10 20H2 (derleme 19042) veya sonraki bir sürümünü
  gerektirir. En iyi deneyim için, en son Windows ve eklenti sürümünü
  kullanın. (Windows 10 21H1/build 19043).
* Ne kadar yüklenebilse de, bu eklenti Windows Enterprise LTSC (Uzun Süreli
  Hizmet Kanalı) ve Windows Server sürümlerini desteklemez.
* Windows 11 desteği deneyseldir ve bazı özellikler çalışmayacaktır
  (ayrıntılar için ilgili bölümlere  bakın).
* Bazı eklenti özellikleri, NVDA ekran okuyucusunun bir parçasıdır veya
  yakında olacaktır.
* Aşağıda listelenmeyen özellikler için,listelenmeyen özelliklerin artık
  NVDA'nın bir parçası olduklarını, eklentinin eski Windows 10 sürümleri
  gibi desteklenmeyen Windows sürümlerini desteklemediğini veya programlarda
  yapılan değişiklerden dolayı özelliklerin Windows'ta artık geçerli
  olmadığını farz edebilirsiniz.
* Bazı uygulamalar, kompakt bindirme modunu destekler (örneğin, Hesap
  Makinesi her zaman en üsttedir) ve bu mod, NVDA'nın taşınabilir sürümüyle
  düzgün çalışmaz.

Her eklenti sürümü arasında yapılan değişikliklerin bir listesi için
[eklenti sürümleri değişiklik değişiklik listesi][3] dosyasına bakın.

## Genel

* NVDA, çoğu durumda arama yaparken öneri sayısını bildirebilir. Bu seçenek,
  NVDA ayarlarında bulunan Nesne sunumu bölümündeki  "Nesne konum bilgisini
  bildir" ile kontrol edilir.
* Windows 10 1909 (Kasım 2019 Güncellemesi) ve sonraki sürümlerinde Başlat
  menüsünde veya Dosya Gezgini'nde arama sırasında sonuçları incelerken
  NVDA'nın arama sonuçlarını iki kez bildirmesi daha az dikkat çeker, bu da
  öğeleri gözden geçirirken braille çıktısını daha tutarlı hale getirir.
* NVDA'nın sağladığı UIA olay işleyicilerine ek olarak, aşağıdaki UIA
  olayları tanınır: sürükleme başlatma, sürükleme iptal etme, sürükleme
  tamamlama, hedef sürükleme girişini bırak, hedef bırak sürükle bırak,
  hedefi bırak. NVDA'nın günlük seviyesi hata ayıklamaya ayarlandığında, bu
  olaylar izlenir ve UIA bildirim olayı için, bildirimler o anda etkin olan
  uygulama dışında bir yerden gelirse bir hata ayıklama tonu
  duyulacaktır. Bazı olaylar, olay için denetleyicideki öğe sayısı, durum
  değişikliği olayı için öğenin durumu ve öğe durumu olayı için öğe metni
  gibi ek bilgiler sağlayacaktır.
* Yalnızca belirli olayları ve/veya belirli uygulamalardan gelen olayları
  izlemek mümkündür.
* NVDA, sanal masaüstlerini açarken, kapatırken, yeniden düzenlerken
  (Windows 11) veya sanal masaüstleri arasında geçiş yaparken etkin sanal
  masaüstü adını duyurur (örneğin, masaüstü 2).
* NVDA, ekran çözünürlüklerini veya yönünü değiştirirken artık Başlat menüsü
  boyutu metnini duyurmayacaktır.
* Artık NVDA, Alt+Shift+ok tuşlarıyla Başlat menüsü kutucuklarını veya İşlem
  Merkezi hızlı eylemlerini düzenlerken,  sürüklenen öğeler veya sürüklenen
  öğenin yeni konumu hakkında bilgi duyuracaktır.
* Dosya Gezgini'ndeki ses/parlaklık değişiklikleri ve Microsoft Store'dan
  gelen uygulama güncelleme bildirimleri gibi duyurular, NVDA'nın nesne
  sunumu ayarlarından Rapor Bildirimleri kapatılarak engellenebilir.

## Hesap makinesi

* NVDA artık grafik hesap makinesi ekran mesajını iki kez bildirmeyecek.

## Takvim

* NVDA artık Mesaj kutularında ve diğer alanlarda "düzenle" veya "salt
  okunur" ifadesini bildirmeyecek.

## Cortana

Çoğu öğe Cortana  Konuşmalar (Windows 10 2004 ve sonrası) kullanılırken
geçerlidir.

* Cortana'dan gelen metin içerikli yanıtlar çoğu durumda bildirilir.
* Cortana ile sesli konuşurken NVDA konuşmayacaktır.
* Windows 10 1909 (Kasım 2019 Güncelleştirmesi) ve sonraki sürümlerinde,
  Windows Aarama kullanıcı arabirimi tarafından desteklenen Dosya
  Gezgini'ndeki modern arama deneyimi desteklenir.

## Posta

* Mesaj listesindeki öğeleri gözden geçirirken, artık mesaj başlıklarını
  gözden geçirmek için tablo gezinme komutlarını kullanabilirsiniz. Satırlar
  (mesajlar) arasında gezinmenin desteklenmediğini unutmayın.
* Mesaj yazarken, söz konusu önerilerin görünümü seslerle belirtilir.

## Haritalar

* NVDA, harita konumları için konum bip sesi çıkarır.
* Sokak yan görünümünü kullanırken ve "klavyeyi kullan" seçeneği
  etkinleştirilirse, haritada gezinmek için ok tuşlarını kullandığınızda
  NVDA sokak adreslerini duyurur.

## Microsoft Solitaire Koleksiyonu

* NVDA kartların ve kart destelerinin adlarını bildirir.

## Microsoft Store

* Uygulama güncellemelerini kontrol ettikten sonra, güncellenecek
  uygulamalar listesindeki uygulama adları doğru şekilde etiketlenir.
* Uygulamalar ve filmler gibi içerikleri indirirken, NVDA ürün adını ve
  indirme ilerlemesini bildirecektir (Windows 11'de güncellenmiş Microsoft
  Store'da düzgün çalışmıyor).

## Modern klavye

Buna emoji paneli, pano geçmişi, dikte, donanım giriş önerileri ve belirli
diller için modern giriş yöntemi düzenleyicileri dahildir. Emojileri
görüntülerken, en iyi deneyim için, NVDA'nın konuşma ayarlarından Unicode
Consortium ayarını etkinleştirin ve imla seslendirme düzeyini  "bazıları"
veya  çoğu olarak ayarlayın. Ayrıca NVDA, Windows 11'de güncellenmiş giriş
deneyimi panelini destekler.

* Pano geçmişini açarken, bazı durumlarda panoda öğeler olduğunda NVDA artık
  "pano" duyurusu yapmayacaktır.
* Windows 10 1903 (Mayıs 2019 Güncellemesi) ve sonraki sürümleri çalıştıran
  bazı sistemlerde emoji paneli açıldığında NVDA artık hiçbir şey
  yapmıyormuş gibi görünmeyecektir.
* Bir emoji grubu (Windows 10 1903 veya sonraki sürümlerde kaomoji ve
  semboller grubu dahil) seçildiğinde, NVDA artık   nesne sunucusunu belirli
  emojilere taşımayacaktır.
* Windows 11'de güncellenmiş giriş deneyimi paneli (birleşik emoji paneli ve
  pano geçmişi) için destek eklendi.

## Kişiler

* Kişileri ararken, özellikle son uygulama sürümleri kullanılıyorsa, ilk
  öneri duyurulacaktır.

## Ayarlar

* Depolama algılama/disk temizleme widget'ı ve Windows Update'ten gelen
  hatalar dahil olmak üzere Windows Update ilerleme durumu gibi belirli
  bilgiler otomatik olarak bildirilir.
* İlerleme çubuğu değerleri ve diğer bilgiler artık iki kez duyurulmaz.
* Windows Update hatırlatıcı iletişim kutusu, uygun bir iletişim kutusu
  olarak tanınır.
* Bazı Windows kurulumlarında görülen garip kontrol etiketleri düzeltildi.
* NVDA, varsa, genellikle "şimdi indir ve kur" olarak adlandırılan isteğe
  bağlı kalite güncelleme bağlantısının adını duyurur.

## Hava durumu

* "Hava Durumu Tahmini" ve "haritalar" gibi sekmeler, uygun sekmeler olarak
  tanınır (Derek Riemer tarafından yamalanmıştır).
* Bir hava durumu tahminini okurken, öğeler arasında hareket etmek için sol
  ve sağ okları kullanın. Tek tek öğeleri okumak için yukarı ve aşağı okları
  kullanın. Örneğin, sağ oka basıldığında "Pazartesi: 79 derece, parçalı
  bulutlu, ..." bildirilebilir. Bu şu anda günlük ve saatlik tahminler için
  çalışıyor.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog