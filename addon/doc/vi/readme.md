# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA compatibility: 2021.3 and later

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Các module cho các ứng dụng sau đây đã được tích hợp (xem phần thông tin chi
tiết của mỗi ứng dụng để biết them):

* Calculator
* Cortana
* Mail
* Maps
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Notepad (Windows 11)
* People
* Settings (system settings, Windows+I)
* Voice access (Windows 11)
* Weather
* Các module tổng hợp cho các điều khiển như Start Menu tiles

Lưu ý:

* This add-on requires Windows 10 21H1 (build 19043), Windows 11 21H2 (build
  22000) or later.
* Dù vẫn có thể cài đặt được, add-on này không hỗ trợ Windows 10 Enterprise
  LTSC (Long-Term Servicing Channel) và các bản phát hành của Windows
  Server.
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
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* When arranging pinned entries (tiles in Windows 10) in Start menu or
  Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce
  information on dragged items or new position of the dragged item.
* Các thông báo như thay đổi âm lượng / độ sáng màn hình trong File Explorer
  và các thông báo cập nhật ứng dụng từ Microsoft Store có thể tắt đi bằng
  cách tắt tùy chọn Đọc các thông báo trong phần trình bày đối tượng của
  NVDA.
* In Windows 11 Insider Preview builds, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and
  later. This is now part of NVDA 2022.1.
* NVDA will once again announce search result details in Start menu. This is
  now part of NVDA 2022.2.
* In Windows 11, Taskbar items and other user interface controls can be
  detected properly when using mouse and/or touch interaction.

## Calculator

* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will announce calculator display content when performing scientific
  mode commands such as trigonometry operations. This is now part of NVDA
  2022.2.

## Cortana

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.

## Mail

* Khi xem các thành phần trong danh sách thư, bạn có thể dùng các phím điều
  hướng trong bảng để xem lại các tiêu để của thư. Lưu ý rằng việc điều
  hướng qua từng dòng (từng thư) chưa được hỗ trợ.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.

## Microsoft Solitaire Collection

* NVDA sẽ đọc tên của các lá bài và bài trên sàn.

## Modern keyboard

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.

## Notepad

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed.

## People

* Khi tìm kiếm danh bạ, gợi ý đầu tiên sẽ được thông báo, đặc biệt là với
  các bản phát hành mới của ứng dụng.

## Settings

* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* In Windows 10, NVDA will interupt speech and report updates to Windows
  Update status as download and install progresses. This may result in
  speech interruption when navigating Settings app while updates are being
  downloaded and installed.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2 preview.

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
