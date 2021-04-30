# Windows 10 App Essentials #

* Tác giả: Joseph Lee, Derek Riemer và những người dùng Windows 10 khác
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA compatibility: 2020.3 to 2020.4

Add-on này là một bộ sưu tập các modules cho nhiều ứng dụng của Windows 10,
đồng thời là các cải tiến và sửa lỗi cho một số điều khiển trong windows 10.

Các module cho các ứng dụng sau đây đã được tích hợp (xem phần thông tin chi
tiết của mỗi ứng dụng để biết thêm chi tiết):

* Calculator (bản mới).
* Calendar
* Cortana (Conversations)
* Mail
* Maps
* Microsoft Solitaire Collection
* Microsoft Store
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* People
* Thiết lập (thiết lập hệ thống, Windows+I)
* Weather.
* Các module tổng hợp cho các điều khiển như Start Menu tiles.

Lưu ý:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows 10 stable release
  (20H2/build 19042).
* Vài tính năng của add-on đã hoặc sẽ là một phần tính năng của trình đọc
  màn hình NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to Windows 10 and apps that makes entries
  no longer applicable.

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

* NVDA will no longer play error tones or do nothing if this add-on becomes
  active from Windows 7, Windows 8.1, and unsupported releases of Windows
  10.
* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drag target
  enter, drag target leave, drag target dropped. With NVDA's log level set
  to debug, these events will be tracked, and for UIA notification event, a
  debug tone will be heard if notifications come from somewhere other than
  the currently active app. Some events will provide additional information
  such as element count in controller for event, state of the element for
  state change event, and item text for item status event.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop name (desktop 2, for example).
* NVDA sẽ không thông báo kích thước văn bản của Start menu khi thay đổi độ
  phân giải hay hướng màn hình.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.

## Calculator

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* Với các phép tính như chuyển đổi đơn vị và tiền tệ, NVDA sẽ thông báo ngay
  khi phép tính được nhập.
* NVDA will notify if maximum digit count has been reached while entering
  expressions.

## Calendar

* NVDA không còn thông báo "có thể nhập" hay "chỉ đọc" trong nội dung thư và
  các trường khác.

## Cortana

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## Mail

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* Khi viết một tin nhắn, sự xuất hiện các đề xuất được đề cập được biểu thị
  bằng âm thanh.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.
* Khi dùng  street side view và nếu tùy chọn "use keyboard" được bật, NVDA
  sẽ thông báo địa chỉ của đường khi bạn dùng mũi tên để điều hướng trong
  bản đồ.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* Sau khi kiểm tra cập nhật ứng dụng, tên của các ứng dụng trong danh sách
  chờ cập nhật đã được gán nhãn một cách chính xác.
* Khi tải các nội dung như ứng dụng và phim, NVDA sẽ thông báo tên sản phẩm
  và tiến trình tải về.

## Modern keyboard

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in build 21296 and later.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in build 21296 and later.

## People

* Khi tìm kiếm danh bạ, gợi ý đầu tiên sẽ được thông báo, đặc biệt là với
  các bản phát hành mới của ứng dụng.

## Thiết lập

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Giá trị của thanh tiến trình và các thông tin khác không còn bị đọc hai
  lần.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## Weather

* Các thẻ như "dự báo" và "bản đồ" đã được nhận dạng chính xác (vá lỗi bởi
  Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
