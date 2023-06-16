# Windows Temel Uygulamalar #

* Yazarlar: Joseph Lee, Derek Riemer ve diğerleri
* [Kararlı sürümü indirin][1]
* [Beta sürümünü indirin][2]
* [Geliştirme sürümünü indirin][3]
* NVDA uyumluluğu: 2023.1 ve üstü

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
* Modern klavye (emoji paneli/dokunmatik klavye/dikte/sesle yazma/donanım
  giriş önerileri/pano geçmişi/Önerilen Eylemler/modern giriş yöntemi
  düzenleyicileri)
* Ayarlar (sistem ayarları, Windows+I)
* Sesli erişim (Windows 11 22H2)
* Hava durumu
* Sanal masaüstleri duyuruları gibi kontroller ve özellikler için çeşitli
  modüller

Notlar:

* Bu eklenti, Windows 10 22H2 (yapı 19045), 11 21H2 (yapı 22000) veya
  sonraki sürümleri gerektirir.
* Özellik güncelleme destek süresi, tüketici destek süresine (Ev, Pro, Pro
  Education, Pro for Workstations sürümleri) bağlıdır ve eklenti, tüketici
  desteği sona ermeden önce özellik güncellemesi desteğini
  sonlandırabilir. Daha fazla bilgi ve destek tarihleri ​​için
  aka.ms/WindowsTargetVersioninfo adresine bakın.
* Ne kadar yüklenebilse de, bu eklenti Windows Enterprise LTSC (Uzun Süreli
  Hizmet Kanalı) ve Windows Server sürümlerini desteklemez.
* Eklenti Güncelleyici kuruluysa ve arka planda eklenti güncellemeleri
  etkinleştirildiyse, Windows App Essentials, desteklenmeyen Windows
  sürümlerine hiç yüklenmez.
* Windows Insider Önizleme yapılarındaki tüm özellikler desteklenmeyecek,
  özellikle canary ve dev kanallarında Windows Insiders alt kümesine sunulan
  özellikler için.
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
[eklenti sürümleri için değişiklik günlükleri][4] belgesine bakın.

## Genel

* Sanal masaüstlerini açarken, kapatırken veya aralarında geçiş yaparken,
  NVDA aktif sanal masaüstü adını (örneğin masaüstü 2) duyurur. Bu artık
  NVDA 2023.2'nin bir parçasıdır.
* Alt+Shift+sol/sağ ok tuşlarına basıldığında simgelerin yeniden
  düzenlenmesinin sonuçlarının duyurulması (Windows 11) ve görev çubuğu
  simgeleri arasında gezinirken öğe konumunun bildirilmesi (Windows 10 ve
  11) dahil olmak üzere iyileştirilmiş Windows 10 ve 11 görev çubuğu
  deneyimi.
* Sekmeli pencerelerin desteklendiği Windows 11 22H2 Dosya Gezgini ve Not
  Defteri gibi uygulamalarda NVDA, bunlar arasında geçiş yaparken sekmelerin
  adını ve konumunu duyurur. Bu artık NVDA 2023.2'nin bir parçasıdır.

## Cortana

* Cortana'dan gelen metin içerikli yanıtlar çoğu durumda bildirilir.

## Modern klavye

Buna emoji paneli, pano geçmişi, dokunmatik klavye, dikte/sesle yazma,
donanım giriş önerileri, önerilen eylemler ve Windows 10 ve 11'deki belirli
diller için modern giriş yöntemi düzenleyicileri dahildir. Emojileri
görüntülerken, en iyi deneyim için Unicode Konsorsiyum ayarını şu adresten
etkinleştirin: NVDA'nın konuşma ayarları ve sembol seviyesini "bazı" veya
daha yükseğe ayarlayın. Windows 10'da pano geçmişinden yapıştırırken, seçili
öğeyi yapıştırmak için Enter tuşu yerine Boşluk Çubuğuna tuşuna basın.

* Windows 11 22H2 ve sonrasında, telefon numaraları gibi uyumlu veriler
  panoya kopyalandığında NVDA önerilen eylemleri duyurur.

## Ayarlar

* NVDA, varsa isteğe bağlı kalite güncelleme kontrolünün adını duyurur
  (Windows 10'da şimdi indir ve kur bağlantısı, Windows 11'de indir
  düğmesi).
* Windows 11'de içerik haritası çubuğu öğeleri düzgün bir şekilde tanınır.
* NVDA, indirme ve yükleme ilerledikçe Windows Update durumuyla ilgili
  güncellemeleri bildirir. Bu, güncellemeler indirilirken ve yüklenirken
  Ayarlar uygulamasında gezinirken konuşmanın kesilmesine neden
  olabilir. Windows 11 kullanıyorsanız ve UIA etkinlik kaydı NVDA gelişmiş
  ayarlar panelinden seçmeli olarak ayarlanmışsa, NVDA'nın güncelleme
  ilerlemesini duyurabilmesi için göründükleri anda odağı güncellemeler
  listesine taşımalısınız.

## Sesli erişim

Bu, Windows 11 22H2'de tanıtılan Sesli erişim özelliğini ifade eder.

* NVDA, Ses erişim arayüzünden mikrofonu değiştirirken mikrofon durumunu
  duyurur.

## Hava durumu

* "Hava Durumu Tahmini" ve "haritalar" gibi sekmeler, uygun sekmeler olarak
  tanınır (Derek Riemer tarafından yamalanmıştır).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
