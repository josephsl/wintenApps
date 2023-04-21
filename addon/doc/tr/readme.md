# Windows Temel Uygulamalar #

* Yazarlar: Joseph Lee, Derek Riemer ve diğerleri
* [kararlı sürüm][1]ü indir
* Download [beta version][2]
* Download [development version][3]
* NVDA uyumluluğu: 2022.4 ve üstü

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
* Modern keyboard (emoji panel/touch keyboard/dictation/voice
  typing/hardware input suggestions/clipboard history/Suggested
  Actions/modern input method editors)
* Ayarlar (sistem ayarları, Windows+I)
* Voice access (Windows 11 22H2)
* Hava durumu
* Miscellaneous modules for controls and features such as virtual desktops
  announcements

Notlar:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Ne kadar yüklenebilse de, bu eklenti Windows Enterprise LTSC (Uzun Süreli
  Hizmet Kanalı) ve Windows Server sürümlerini desteklemez.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in canary
  and dev channels.
* Add-on dev channel will include changes including experimental content
  that may or may not be included in beta and stable releases, and beta
  channel will come with changes planned for future stable releases.
* Bazı eklenti özellikleri, NVDA ekran okuyucusunun bir parçasıdır veya
  yakında olacaktır.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][4] document.

## Genel

* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, mouse and/or touch interaction can be used
  to interact with redesigned system tray overflow window and Open With
  dialog. This is now part of NVDA 2023.1.
* NVDA will record processor architecture for the current Windows
  installation (x86/32-bit, AMD64, ARM64) when it starts. This is now part
  of NVDA 2023.1.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11 prior to build 25267) and reporting item position when moving
  through taskbar icons (Windows 10 and 11 prior to build 25281).
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them. This is now part of NVDA 2023.2.

## Cortana

* Cortana'dan gelen metin içerikli yanıtlar çoğu durumda bildirilir.

## Haritalar

* NVDA will no longer interrupt speech when focused on items other than the
  map control in some cases.

## Modern klavye

This includes emoji panel, clipboard history, touch keyboard,
dictation/voice typing, hardware input suggestions, suggested actions, and
modern input method editors for certain languages across Windows 10 and
11. When viewing emojis, for best experience, enable Unicode Consortium
setting from NVDA's speech settings and set symbol level to "some" or
higher. When pasting from clipboard history in Windows 10, press Space key
instead of Enter key to paste the selected item.

* Windows 10'da bir emoji grubu (kaomoji ve semboller grubu dahil)
  seçildiğinde, NVDA artık nesne sunucusunu belirli emojilere
  taşımayacaktır.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu
  items. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
