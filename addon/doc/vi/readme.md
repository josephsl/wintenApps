# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA compatibility: 2022.2 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Các module cho các ứng dụng sau đây đã được tích hợp (xem phần thông tin chi
tiết của mỗi ứng dụng để biết them):

* Cortana
* Maps
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* People
* Settings (system settings, Windows+I)
* Voice access (Windows 11 22H2)
* Weather
* Các module tổng hợp cho các điều khiển như Start Menu tiles

Lưu ý:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Dù vẫn có thể cài đặt được, add-on này không hỗ trợ Windows 10 Enterprise
  LTSC (Long-Term Servicing Channel) và các bản phát hành của Windows
  Server.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported.
* Vài tính năng của add-on đã hoặc sẽ là một phần tính năng của trình đọc
  màn hình NVDA.
* Với những thành phần không được liệt kê bên dưới, bạn có thể xem như các
  tính năng đó đã là một phần tính năng của NVDA, không phải áp dụng như
  add-on không hỗ trợ cho các bản phát hành Windows cũ như Windows 10 bản cũ
  hay các thay đổi đã được thực hiện cho Windows và các ứng dụng này không
  còn được áp dụng.
* Vài ứng dụng hỗ trợ chế độ compact overlay (luon chạy ở trên như
  Calculator), và chế độ này sẽ không hoạt động tốt với các phiên bản chạy
  trực tiếp của NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. This is now part of
  NVDA 2022.4.
* Các thông báo như thay đổi âm lượng / độ sáng màn hình trong File Explorer
  và các thông báo cập nhật ứng dụng từ Microsoft Store có thể tắt đi bằng
  cách tắt tùy chọn Đọc các thông báo trong phần trình bày đối tượng của
  NVDA.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.

## Cortana

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.

## Modern keyboard

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## People

* When searching for contacts, first suggestion will be announced.

## Settings

* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
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

## Weather

* Các thẻ như "dự báo" và "bản đồ" đã được nhận dạng chính xác (vá lỗi bởi
  Derek Riemer).
* khi đọc một dự báo, dùng mũi tên trái / phải để chuyển giữa các thành
  phần. Dùng mũi tên lên / xuống để đọc từng thành phần. Ví dụ, Bấm mũi tên
  phải có thể thông báo "Thứ hai: 79 độ, có mây, ..." Bấm mũi tên xuống sẽ
  đọc "Thứ hai" và bấm lần nữa sẽ đọc thành phần tiếp theo (nhiệt độ chẳng
  hạn). Tính năng này hiện hoạt động với dự báo theo ngày và theo giờ.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
