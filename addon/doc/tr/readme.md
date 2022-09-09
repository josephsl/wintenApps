# Windows Temel Uygulamalar #

* Yazarlar: Joseph Lee, Derek Riemer ve diğerleri
* [kararlı sürüm][1]ü indir
* [geliştirme sürümü][2]nü indir
* NVDA compatibility: 2022.2 and later

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

* Cortana
* Haritalar
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Kişiler
* Ayarlar (sistem ayarları, Windows+I)
* Voice access (Windows 11 22H2)
* Hava durumu
* Başlat Menüsü kutucukları gibi kontroller için çeşitli modüller

Notlar:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Ne kadar yüklenebilse de, bu eklenti Windows Enterprise LTSC (Uzun Süreli
  Hizmet Kanalı) ve Windows Server sürümlerini desteklemez.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported.
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
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Her eklenti sürümü arasında yapılan değişikliklerin bir listesi için
[eklenti sürümleri değişiklik değişiklik listesi][3] dosyasına bakın.

## Genel

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect. With NVDA's log level set to debug, these
  events will be tracked and logged.
* NVDA, sanal masaüstlerini açarken, kapatırken, yeniden düzenlerken
  (Windows 11) veya sanal masaüstleri arasında geçiş yaparken etkin sanal
  masaüstü adını duyurur (örneğin, masaüstü 2).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. This is now part of
  NVDA 2022.4.
* Dosya Gezgini'ndeki ses/parlaklık değişiklikleri ve Microsoft Store'dan
  gelen uygulama güncelleme bildirimleri gibi duyurular, NVDA'nın nesne
  sunumu ayarlarından Rapor Bildirimleri kapatılarak engellenebilir.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* Item status changes are announced in more apps including Visual Studio
  Community 2022. This is now part of NVDA 2022.4.

## Cortana

* Cortana'dan gelen metin içerikli yanıtlar çoğu durumda bildirilir.
* Cortana ile sesli konuşurken NVDA konuşmayacaktır.

## Haritalar

* NVDA, harita konumları için konum bip sesi çıkarır.

## Modern klavye

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* Windows 10'da bir emoji grubu (kaomoji ve semboller grubu dahil)
  seçildiğinde, NVDA artık nesne sunucusunu belirli emojilere
  taşımayacaktır.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## Kişiler

* Kişileri ararken, özellikle son uygulama sürümleri kullanılıyorsa, ilk
  öneri duyurulacaktır.

## Ayarlar

* NVDA, varsa isteğe bağlı kalite güncelleme kontrolünün adını duyurur
  (Windows 10'da şimdi indir ve kur bağlantısı, Windows 11'de indir
  düğmesi).
* Windows 11'de içerik haritası çubuğu öğeleri düzgün bir şekilde tanınır.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice
  access interface.

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
