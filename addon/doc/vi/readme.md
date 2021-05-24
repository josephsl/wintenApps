# Windows 10 App Essentials #

* Tác giả: Joseph Lee, Derek Riemer và những người dùng Windows 10 khác
* Tải về [phiên bản chính thức][1]
* Tải về [phiên bản thử nghiệm][2]
* NVDA tương thích: 2020.3 đến 2020.4

Add-on này là một bộ sưu tập các modules cho nhiều ứng dụng của Windows 10,
đồng thời là các cải tiến và sửa lỗi cho một số điều khiển trong windows 10.

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

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows 10 stable release
  (21H1/build 19043).
* Vài tính năng của add-on đã hoặc sẽ là một phần tính năng của trình đọc
  màn hình NVDA.
* Với những thành phần không được liệt kê bên dưới, bạn có thể xem như các
  tính năng đó đã là một phần tính năng của NVDA, không phải áp dụng như
  add-on không hỗ trợ cho các bản phát hành Windows 10 cũ hay các thay đổi
  đã được thực hiện cho Windows 10 và các ứng dụng này không còn được áp
  dụng.
* Vài ứng dụng hỗ trợ chế độ compact overlay (luon chạy ở trên như
  Calculator), và chế độ này sẽ không hoạt động tốt với các phiên bản chạy
  trực tiếp của NVDA.

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

* NVDA sẽ không còn phát âm báo lỗi hoặc không làm gì nếu add-on này hoạt
  động trên Windows 7, Windows 8.1 và các bản phát hành Windows 10 không
  được hỗ trợ.
* Ngoài các hộp thoại được NVDA nhận ra, nhiều hộp thoại giờ đã được nhận
  diện đúng thuộc tính và thông báo chính xác, bao gồm hộp thoại Insider
  Preview (ứng dụng settings).
* NVDA có thể thông báo số gợi ý đếm được khi thực hiện tìm kiếm trong đa số
  trường họp. Tùy chọn này được điều khiển bởi "Thông báo thông tin vị trí
  đối tượng" trong bảng điều khiển trình bày đối tượng, tìm thấy trong cài
  đặt của NVDA.
* Khi tìm kiếm trên Start menu hoặc File Explorer trong phiên bản 1909 (bản
  cập nhật tháng 11/2019) trở lên, việc NVDA thông báo kết quả tìm kiếm hai
  lần khi duyệt quả chúng sẽ giảm đi. Nó cũng làm coh việc xem các thành
  phần ở đầu ra chữ nổi được thể hiện hợp lý hơn.
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
* Khi mở, đóng, hay chuyển giữa desktop ảo, NVDA sẽ thông báo tên cửa sổ
  desktop hiện tại (desktop 2 chẳng hạn).
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

* Khi bấm ENTER hay Escape, NVDA sẽ thông báo kết quả tính toán.
* Với các phép tính như chuyển đổi đơn vị và tiền tệ, NVDA sẽ thông báo ngay
  khi phép tính được nhập.
* NVDA sẽ thông báo nếu đã đạt số tối đa khi nhập công thức.
* NVDA sẽ không còn đọc hai lần thông điệp trên màn hình tính toán đồ thị.

## Calendar

* NVDA không còn thông báo "có thể nhập" hay "chỉ đọc" trong nội dung thư và
  các trường khác.

## Cortana

Hầu hết các thành phần đều dùng được khi sử dụng Cortana Conversations
(phiên bản 2004 trở lên).

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống.
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.
* Trong phiên bản 1909 (November 2019 Update) trở lên, trải nghiệm tìm kiếm
  mới trong File Explorer quản lý bởi giao diện tìm kiếm người dùng của
  Windows đã được hỗ trợ.

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
* Khi tải các nội dung như ứng dụng và phim, NVDA sẽ thông báo tên sản phẩm
  và tiến trình tải về.

## Modern keyboard

Đã bao gồm bản biểu tượng cảm xúc, lịch sử khay nhớ tạm, nhận dạng, gọi ý
thiết bị đầu vào, và các kiểu nhập hiện đại cho vài ngôn ngữ nhất định. Khi
xem các biểu tượng cảm xúc, để có trải nghiệm tốt nhất, hãy bật tùy chọn
Unicode Consortium trong cài đặt tiếng  nói của NVDA và chọn mức độ đọc kí
hiệu là  "một vài" hay cao hơn. NVDA cũng đã hỗ trợ kiểu nhập được cập nhật
trong  bản dựng 21296 trở lên.

* Khi mở lịch sử khay nhớ tạm, NVDA không còn đọc "clipboard" khi có nội
  dung trong khay nhớ tạm ở vài trường hợp.
* Trên vài hệ thống chạy phiên bản 1903 (May 2019 Update) trở lên, NVDA sẽ
  không còn tình trạng không làm gì khi mở bản biểu tượng cảm xúc.
* Đã thêm hỗ trợ cho các kiểu nhập mới của tiếng Trung,  tiếng Nhật và tiếng
  Hàn (CJK) trên giao diện không chính thức, ra mắt trong phiên bản 2004
  (build 18965 trở lên).
* Khi một nhóm biểu tượng cảm xúc (bao gồm kaomoji và nhóm các kí hiệu trong
  phiên bản 1903 trở lên) được chọn, NVDA sẽ không còn di chuyển đối tượng
  điều hướng tới một biểu tượng nhất định.
* Đã thêm hỗ trợ cho bản các kiểu nhập được cập nhật (gộp chung bản biểu
  tượng cảm xúc và lịch sử khay nhớ tạm) trong bản dựng 21296 trở lên.

## People

* Khi tìm kiếm danh bạ, gợi ý đầu tiên sẽ được thông báo, đặc biệt là với
  các bản phát hành mới của ứng dụng.

## Settings

* Vài thông tin như thanh trạng thái của Windows Update đã được thông báo tự
  động, bao gồm Storage sense/disk cleanup và các lỗi từ Windows Update.
* Giá trị của thanh tiến trình và các thông tin khác không còn bị đọc hai
  lần.
* Hộp thoại Windows Update reminder đã được nha65nn dạng đúng là hộp thoại.
* Nhãn không hợp lý cho các điều khiển trong một số bản cài Windows 10 đã
  được sửa.
* Trong các bản cập nhật gần đây của phiên bản 1803 trở lên, do các thay đổi
  trong thủ tục của Windows Update cho feature updates, liên kết tên
  "download and install now" đã được thêm. NVDA giờ đây sẽ đọc tiêu đề của
  cập nhật mới nếu có.

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
