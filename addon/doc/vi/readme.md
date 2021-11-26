# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA compatibility: 2021.2 and beyond

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
* Microsoft Store
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* People
* Settings (system settings, Windows+I)
* Weather
* Các module tổng hợp cho các điều khiển như Start Menu tiles

Lưu ý:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Dù vẫn có thể cài đặt được, add-on này không hỗ trợ Windows 10 Enterprise
  LTSC (Long-Term Servicing Channel) và các bản phát hành của Windows
  Server.
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

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  is now part of NVDA 2021.3.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag complete, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  are tracked from an add-on called Event Tracker.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
* NVDA sẽ không thông báo kích thước văn bản của Start menu khi thay đổi độ
  phân giải hay hướng màn hình.
* Khi sắp xếp Start menu tiles hoặc Action Center quick actions với
  Alt+Shift+các phím mũi tên, NVDA sẽ thông báo các thông tin trên các thành
  phần đã kéo hoặc vị trí mới của thành phần đã kéo.
* Các thông báo như thay đổi âm lượng / độ sáng màn hình trong File Explorer
  và các thông báo cập nhật ứng dụng từ Microsoft Store có thể tắt đi bằng
  cách tắt tùy chọn Đọc các thông báo trong phần trình bày đối tượng của
  NVDA.

## Calculator

* NVDA sẽ không còn đọc hai lần thông điệp trên màn hình tính toán đồ thị.

## Cortana

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.

## Mail

* Khi xem các thành phần trong danh sách thư, bạn có thể dùng các phím điều
  hướng trong bảng để xem lại các tiêu để của thư. Lưu ý rằng việc điều
  hướng qua từng dòng (từng thư) chưa được hỗ trợ.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.
* Khi dùng  street side view và nếu tùy chọn "use keyboard" được bật, NVDA
  sẽ thông báo địa chỉ của đường khi bạn dùng mũi tên để điều hướng trong
  bản đồ.

## Microsoft Solitaire Collection

* NVDA sẽ đọc tên của các lá bài và bài trên sàn.

## Microsoft Store

* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

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
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.

## People

* Khi tìm kiếm danh bạ, gợi ý đầu tiên sẽ được thông báo, đặc biệt là với
  các bản phát hành mới của ứng dụng.

## Settings

* Vài thông tin như thanh trạng thái của Windows Update đã được thông báo tự
  động, bao gồm Storage sense/disk cleanup và các lỗi từ Windows Update.
* Giá trị của thanh tiến trình và các thông tin khác không còn bị đọc hai
  lần.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.

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
