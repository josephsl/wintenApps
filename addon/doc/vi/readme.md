# Windows App Essentials #

* Tác giả: Joseph Lee, Derek Riemer và những người dùng Windows 10 khác
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA tương thích: 2020.4 trở lên

Note: Originally called Windows 10 App Essentials, it was renamed to Windows
App Essentials in 2021 to support Windows 10 and future releases such as
Windows 11. Parts of this add-on will still refer to the original add-on
name.

This add-on is a collection of app modules for various modern Windows apps,
as well as enhancements and fixes for certain controls found in Windows 10
and later.

Các module cho các ứng dụng sau đây đã được tích hợp (xem phần thông tin chi
tiết của mỗi ứng dụng để biết them):

* Calculator (modern)
* Calendar
* Cortana (Conversations)
* Mail
* Maps
* Microsoft Solitaire Collection
* Microsoft Store
* Bàn phím hiện đại (bản biểu tượng cảm xúc / đọc chính tả / gợi ý thiết bị
  đầu vào / các thành phần bộ nhớ tạm)
* People
* Settings (system settings, Windows+I)
* Weather
* Các module tổng hợp cho các điều khiển như Start Menu tiles

Lưu ý:

* This add-on requires Windows 10 20H2 (build 19042) or later. For best
  results, use the add-on with latest Windows release (Windows 10 21H1/build
  19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details).
* Vài tính năng của add-on đã hoặc sẽ là một phần tính năng của trình đọc
  màn hình NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support unsupported
  Windows releases such as old Windows 10 versions, or changes were made to
  Windows and apps that makes entries no longer applicable.
* Vài ứng dụng hỗ trợ chế độ compact overlay (luon chạy ở trên như
  Calculator), và chế độ này sẽ không hoạt động tốt với các phiên bản chạy
  trực tiếp của NVDA.

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

* NVDA có thể thông báo số gợi ý đếm được khi thực hiện tìm kiếm trong đa số
  trường họp. Tùy chọn này được điều khiển bởi "Thông báo thông tin vị trí
  đối tượng" trong bảng điều khiển trình bày đối tượng, tìm thấy trong cài
  đặt của NVDA.
* When searching in Start menu or File Explorer in Windows 10 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* Ngoài UIA event handlers cung cấp bởi NVDA, các sự kiện UIA sau đây được
  nhận dạng: drag start, drag cancel, drag complete, drop target drag enter,
  drop target drag leave, drop target dropped. Với cấp độ log của NVDA là
  sửa lỗi, các sự kiện này sẽ được theo dõi, và với các thông báo sự kiện
  UIA, một âm báo lỗi sẽ được phát nếu thông báo đến từ nơi khác chứ không
  phải ứng dụng đang hoạt động. Vài sự kiện sẽ cung cấp them các thông tin
  như số thành phần đếm được trong điều khiển của sự kiện, trạng thái của
  thành phần hay sự kiện thay đổi trạng thái, và văn bản thành phần cho sự
  kiện trạng thái thành phần.
* Đã có thể chỉ theo dõi một số sự kiện nhất định và / hoặc các sự kiện từ
  một ứng dụng nhất định.
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

## Calendar

* NVDA không còn thông báo "có thể nhập" hay "chỉ đọc" trong nội dung thư và
  các trường khác.

## Cortana

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.
* In Windows 10 1909 (November 2019 Update) and later, modern search
  experience in File Explorer powered by Windows Search user interface is
  supported.

## Mail

* Khi xem các thành phần trong danh sách thư, bạn có thể dùng các phím điều
  hướng trong bảng để xem lại các tiêu để của thư. Lưu ý rằng việc điều
  hướng qua từng dòng (từng thư) chưa được hỗ trợ.
* Khi soạn thư, sự xuất hiện các đề xuất được đề cập được biểu thị bằng âm
  thanh.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.
* Khi dùng  street side view và nếu tùy chọn "use keyboard" được bật, NVDA
  sẽ thông báo địa chỉ của đường khi bạn dùng mũi tên để điều hướng trong
  bản đồ.

## Microsoft Solitaire Collection

* NVDA sẽ đọc tên của các lá bài và bài trên sàn.

## Microsoft Store

* Sau khi kiểm tra cập nhật ứng dụng, tên của các ứng dụng trong danh sách
  chờ cập nhật đã được gán nhãn một cách chính xác.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress (does not work properly in updated
  Microsoft Store in Windows 11).

## Modern keyboard

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in Windows 11.

* Khi mở lịch sử khay nhớ tạm, NVDA không còn đọc "clipboard" khi có nội
  dung trong khay nhớ tạm ở vài trường hợp.
* On some systems running Windows 10 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* When an emoji group (including kaomoji and symbols group in Windows 10
  1903 or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
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
* Hộp thoại Windows Update reminder đã được nha65nn dạng đúng là hộp thoại.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update link if
  present, typically named "download and install now".

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
