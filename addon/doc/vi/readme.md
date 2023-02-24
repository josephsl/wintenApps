# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA compatibility: 2022.4 and later

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
* Modern keyboard (emoji panel/touch keyboard/dictation/voice
  typing/hardware input suggestions/clipboard history/Suggested
  Actions/modern input method editors)
* Settings (system settings, Windows+I)
* Voice access (Windows 11 22H2)
* Weather
* Miscellaneous modules for controls and features such as virtual desktops
  announcements

Lưu ý:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Dù vẫn có thể cài đặt được, add-on này không hỗ trợ Windows 10 Enterprise
  LTSC (Long-Term Servicing Channel) và các bản phát hành của Windows
  Server.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel.
* Vài tính năng của add-on đã hoặc sẽ là một phần tính năng của trình đọc
  màn hình NVDA.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with the portable version
  of NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

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
* NVDA will announce empty folder text inside an empty folder in File
  Explorer.
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them.

## Cortana

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.
* NVDA will no longer interrupt speech when focused on items other than the
  map control in some cases.

## Modern keyboard

This includes emoji panel, clipboard history, touch keyboard,
dictation/voice typing, hardware input suggestions, suggested actions, and
modern input method editors for certain languages across Windows 10 and
11. When viewing emojis, for best experience, enable Unicode Consortium
setting from NVDA's speech settings and set symbol level to "some" or
higher. When pasting from clipboard history in Windows 10, press Space key
instead of Enter key to paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu
  items. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

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
