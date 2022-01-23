# Windows Temel Uygulamalar #

* Yazarlar: Joseph Lee, Derek Riemer ve diğerleri
* [kararlı sürüm][1]ü indir
* [geliştirme sürümü][2]nü indir
* NVDA uyumluluğu: 2021.2 ve üstü

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

* Hesap makinesi
* Cortana
* Posta
* Haritalar
* Microsoft Solitaire Koleksiyonu
* Modern klavye (emoji paneli/dikte/sesle yazma/donanım giriş önerileri/pano
  geçmişi/modern giriş yöntemi düzenleyicileri)
* Notepad (Windows 11)
* Kişiler
* Ayarlar (sistem ayarları, Windows+I)
* Hava durumu
* Başlat Menüsü kutucukları gibi kontroller için çeşitli modüller

Notlar:

* This add-on requires Windows 10 21H1 (build 19043) or later and is
  compatible with Windows 11.
* Ne kadar yüklenebilse de, bu eklenti Windows Enterprise LTSC (Uzun Süreli
  Hizmet Kanalı) ve Windows Server sürümlerini desteklemez.
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

* NVDA, arama ilerledikçe öneri sayısının değiştiği durumlar da dahil olmak
  üzere çoğu durumda bir arama yaparken öneri sayısını bildirebilir. Bu
  artık NVDA 2021.3'ün bir parçasıdır.
* NVDA tarafından sağlanan UIA olay işleyicilerine ek olarak, şu UIA
  olayları tanınır: sürükleme tamamlandı, bırakma hedefi bırakıldı, düzen
  geçersiz kılındı. NVDA'nın günlük seviyesi hata ayıklamaya ayarlandığında,
  bu olaylar izlenecek ve UIA bildirim olayı için, bildirimler o anda etkin
  olan uygulama dışında bir yerden gelirse bir hata ayıklama tonu
  duyulacaktır. Ad değişikliği ve olaylar için denetleyici gibi NVDA'da
  yerleşik olarak bulunan olaylar, Event Tracker adlı bir eklentiden
  izlenir.
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
* In Windows 10, history and memory list items are properly labeled.

## Cortana

* Cortana'dan gelen metin içerikli yanıtlar çoğu durumda bildirilir.
* Cortana ile sesli konuşurken NVDA konuşmayacaktır.

## Posta

* Mesaj listesindeki öğeleri gözden geçirirken, artık mesaj başlıklarını
  gözden geçirmek için tablo gezinme komutlarını kullanabilirsiniz. Satırlar
  (mesajlar) arasında gezinmenin desteklenmediğini unutmayın.

## Haritalar

* NVDA, harita konumları için konum bip sesi çıkarır.
* Sokak yan görünümünü kullanırken ve "klavyeyi kullan" seçeneği
  etkinleştirilirse, haritada gezinmek için ok tuşlarını kullandığınızda
  NVDA sokak adreslerini duyurur.

## Microsoft Solitaire Koleksiyonu

* NVDA kartların ve kart destelerinin adlarını bildirir.

## Modern klavye

Buna emoji paneli, pano geçmişi, dikte, donanım giriş önerileri ve belirli
diller için modern giriş yöntemi düzenleyicileri dahildir. Emojileri
görüntülerken, en iyi deneyim için, NVDA'nın konuşma ayarlarından Unicode
Consortium ayarını etkinleştirin ve imla seslendirme düzeyini  "bazıları"
veya  çoğu olarak ayarlayın. Windows 10'da pano geçmişinden yapıştırırken,
seçilen öğeyi yapıştırmak için Enter tuşu yerine Aralık tuşuna basın. Ayrıca
NVDA, Windows 11'de güncellenmiş giriş deneyimi panelini destekler.

* Windows 10'da bir emoji grubu (kaomoji ve semboller grubu dahil)
  seçildiğinde, NVDA artık nesne sunucusunu belirli emojilere
  taşımayacaktır.
* Windows 11'de güncellenmiş giriş deneyimi paneli (birleşik emoji paneli ve
  pano geçmişi) için destek eklendi.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed.
* NVDA will no longer announce entered text when pressing Enter key from the
  document.

## Kişiler

* Kişileri ararken, özellikle son uygulama sürümleri kullanılıyorsa, ilk
  öneri duyurulacaktır.

## Ayarlar

* Depolama algılama/disk temizleme widget'ı ve Windows Update'ten gelen
  hatalar dahil olmak üzere Windows Update ilerleme durumu gibi belirli
  bilgiler otomatik olarak bildirilir.
* İlerleme çubuğu değerleri ve diğer bilgiler artık iki kez duyurulmaz.
* Bazı Windows kurulumlarında görülen garip kontrol etiketleri düzeltildi.
* NVDA, varsa isteğe bağlı kalite güncelleme kontrolünün adını duyurur
  (Windows 10'da şimdi indir ve kur bağlantısı, Windows 11'de indir
  düğmesi).
* Windows 11'de içerik haritası çubuğu öğeleri düzgün bir şekilde tanınır.

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
