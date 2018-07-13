# Windows 10 App Essentials #

* Tác giả: Joseph Lee, Derek Riemer và những người dùng Windows 10 khác
* Tải về [phiên bản stable][1]
* Tải về [phiên bản development][2]

Add-on này là một bộ sưu tập các modules cho nhiều ứng dụng của Windows 10,
đồng thời là các cải tiến và sửa lỗi cho một số điều khiển trong windows 10.

Các module cho các ứng dụng sau đây đã đơc5 tích hợp (xem phần thông tin chi
tiết của mỗi ứng dụng để biết thêm chi tiết):

* Alarms and Clock.
* Calendar
* Calculator (bản mới).
* Cortana
* Feedback Hub
* Game Bar
* Mail
* Maps
* Microsoft Edge
* Bàn phím hiện đại (bản biểu tượng cảm xúc / gợi ý thiết bị đầu vào / các
  thành phần bộ nhớ tạm đám mây trong phiên bản 1709 trở lên)
* People
* Settings (system settings, Windows+I)
* Skype (universal app)
* Store
* Weather.
* Các module tổng hợp cho các điều khiển như Start Menu tiles.

Lưu ý:

* Add-on này yêu cầu Windows 10 phiên bản 1709 (build 16299) trở lên và NVDA
  2018.2 trở lên. Tốt nhất, là dùng add-on với bản Windows 10 mới nhất
  (build 17134) và stable bản mới nhất của NVDA.
* Vài tính năng của add-on đã hoặc sẽ là một phần tính năng của trình đọc
  màn hình NVDA.
* Với những thành phần không được liệt kê bên dưới, bạn có thể xem như các
  tính năng đó đã là một phần của NVDA, không phải áp dụng như add-on không
  hỗ trợ Windows 10 phiên bản cũ or các thay đổi của các ứng dụng làm cho
  chúng không còn tác dụng.

Để biết các thay đổi giữa các lần phát hành của add-on, xem phần [changelogs
for add-on releases][3] .

## Chung

* Trong trình đơn ngữ cảnh của Start Menu tiles, các trình đơn con đã được
  nhận diện chính xác.
* Một số hộp thoại giờ đã được nhận diện đúng thuộc tính và thông báo chính
  xác, bao gồm hộp thoại Insider Preview (ứng dụng settings).
* NVDA có thể thông báo số gợi ý đếm được khi thực hiện tìm kiếm trong một
  số trường họp. Tùy chọn này được điều khiển bởi "Thông báo thông tin vị
  trí đối tượng" trong hộp thoại trình bày đối tượng.
* Trong một số trình đơn ngữ cảnh (như của Edge), thông tin vị trí (như 1
  trên 2) không còn được đọc nữa.
* Các sự kiện UIA sau đây đã được nhận dạng: active text position change
  (Redstone 5), controller for, drag start, drag cancel, drag complete,
  element selected, live region change, notification, system alert, tooltip
  opened, window opened. Với NVDA được thiết lập để chạy với chế độ bản ghi
  dò lỗi được bật, các sự kiện này sẽ được theo dõi, và cho thông báo sự
  kiện UIA, bạn sẽ nghe âm báo gỡ lỗi.
* Thêm khả năng kiểm tra cập nhật add-on (tự động hoặc thủ công) thông qua
  hộp thoại Windows 10 App Essentials được tìm thấy trong trình đơn tùy chọn
  của NvDA . Mặc định, các phiên bản stable và development sẽ được tự động
  kiểm tra cập nhật hàng ngày hoặc hàng tuần.
* Trong một số ứng dụng, live region text đã được thông báo. Bao gồm các
  thông báo trong Edge, các kết quả trong Calculator và các thông tin
  khác. Lưu ý rằng các kết quả này có thể được đọc hai lần trong vài trường
  hợp.
* Thông báo từ các ứng dụng mới phát hành trên Windows 10 phiên bản 1709
  (build 16299) trở lên đã được đọc.
* Thông báo trên đối tượng từ Edge và các ứng dụng tương tự đã được nhận
  dạng và sẽ được thông báo.
* Trong build 17627 trở lên, khi mở một bộ tab mới (Control+Windows+T), NVDA
  sẽ thông báo kết quả tìm kiếm khi tìm các thành phần trong cửa sổ Cortana
  đã được nhún vào.
* Khi chuyển giữa các bộ tab, NvDA sẽ thông báo tên và vị trí của tab bạn
  đang chuyển đến.
* Khi mở, đóng, hay chuyển giữa desktop ảo, NVDA sẽ thông báo desktop ID
  hiện tại (desktop 2 chẳng hạn).
* NVDA sẽ không thông báo kích thước văn bản của Start menu khi thay đổi độ
  phân giải hay hướng màn hình.

## Alarms and clock

* giá trị của bộ chọn thời gian giờ đã được đọc, đặc biệt là khi chuyển con
  trỏ đến điều khiển để chọn. điều này cũng có tác dụng với điều khiển đã
  dùng để chọn thời gian khởi động lại máy để hoàn tất việc cài đặt cập nhật
  Windows.

## Calculator

* Khi bấm ENTER hay Escape, NVDA sẽ thông báo kết quả tính toán.
* Với các phép tính như chuyển đổi đơn vị và tiền tệ, NVDA sẽ thông báo ngay
  khi phép tính được nhập.

## calendar

* NVDA không còn thông báo "có thể nhập" hay "chỉ đọc" trong nội dung thư và
  các trường khác.

## Cortana

* Phản hồi văn bản từ Cortana được thông báo trong hầu hết tình huống (nếu
  không, thử mở lại Start menu và tìm kiếm lại).
* NVDA sẽ im lặng khi điều khiển Cortana bằng giọng nói.
* NVDA giờ đây sẽ thông báo nhắc nhở cuộc trò chuyện nếu bạn thiết lập.

## Feedback Hub

* Từ các ứng dụng mới ra, NVDA không còn thông báo hai lần loại phản hồi.

## Game Bar

* NVDA sẽ thông báo sự xuất hiện của cửa sổ Game Bar. vì giới hạn kĩ thuật,
  NVDA không thể tương tác hoàn toàn với Game Bar.

## Mail

* Khi xem các thành phần trong danh sách tin nhắn, bạn có thể dùng các phím
  điều hướng trong bảng để xem lại các tiêu để của tin nhắn.
* Khi viết một tin nhắn, sự xuất hiện các đề xuất được đề cập được biểu thị
  bằng âm thanh.

## Maps

* NVDA phát tiếng beep cho vị trí trên bản đồ.
* Khi dùng  street side view và nếu tùy chọn "use keyboard" được bật, NVDA
  sẽ thông báo địa chỉ của đường khi bạn dùng mũi tên để điều hướng trong
  bản đồ.

## Microsoft Edge

* Các thông báo như tải tập tin và nhiều thông báo khác trên web, và khả
  năng của chế độ xem (nếu dùng phiên bản 1709 trở lên) đã được đọc.

## Modern keyboard

* Hỗ trợ bản đầu vào cho Emoji trong phiên bản 1709 (Fall Creators Update)
  trở lên, bao gồm bản thiết kế lại trong build 17661 trở lên. để có trải
  nghiệm tốt nhất khi đọc các biểu tượng, hãy sử dụng bộ đọc Windows
  OneCore.
* Hỗ trợ cho gợi ý thiết bị đầu vào  trong phiên bản 1803 (April 2018
  Update) trở lên.
* Trong post-1709 builds, NVDA sẽ thông báo biểu tượng được chọn đầu tiên
  khi mở bản biểu tượng cảm xúc.
* Hỗ trợ thông báo thành phần của bộ nhớ tạm đám mây trong build 17666
  (Redstone 5) trở lên.
* Bỏ những cấp độ không cần thiết khi làm việc với modern keyboard và tính
  năng của nó. Bao gồm không còn thông báo "Microsoft Candidate UI" khi mở
  gợi ý thiết bị bàn phím đầu vào và giữ im lặng khi một số phím trên bàn
  phím cảm ứng tăng sự kiện đổi tên trên một số hệ thống.

## People

* Khi tìm kiếm danh bạ, âm thanh sẽ được phát lên khi tìm thấy kết quả.

## Thiết lập

* Vài thông tin như thanh tiến trình của Windows Update đã được thông báo tự
  động.
* Giá trị của thanh tiến trình và các thông tin khác không còn bị đọc hai
  lần.
* Các nhóm thiết lập đã được nhận dạng khi dùng điều hướng đối tượng để di
  chuyển giữa các điều khiển.
* Với vài hộp xổ, NVDA không còn lỗi không nhận dạng được nhãn hay các thay
  đổi giá trị.
* Không còn nghe tiếng beep của thanh tiến trình âm lượng audio trong phiên
  bản 1803 trở lên.
* Nhiều thông tin về trạng thái cập nhật Windows đã được thông báo, đặc biệt
  là khi việc cập nhật Windows xảy ra lỗi.

## Skype

* Thông báo nhập văn bản chỉ được đọc giống như Skype for Desktop client.
* Control+NvDA+phím số, dùng để đọc lịch sử chat gần đây và di chuyển đối
  tượng điều hướng đến nội dung chat trong Skype for Desktop, cũng có luôn
  trong Skype UWP.
* Bạn có thể bấm Alt+phím số để xác định và chuyển đến các cuộc đàm thoại
  (1), danh bạ (2), bots (3) và trường nhập liệu chat nếu có (4). Lưu ý rằng
  các lệnh này sẽ hoạt động tốt nếu được cài bản Skype cập nhật tháng
  3/2017.
* NVDA không còn đọc "Skype Message" khi xem lại tin nhắn trong nhiều trường
  hợp.
* Từ danh sách lịch sử tin nhắn, bấm NVDA+D tại một tin nhắn sẽ cho phép
  NVDA đọc các thông tin chi tiết của tin nhắn như loại kênh, ngày giờ gửi,
  vân vân.

## Store

* Sau khi kiểm tra cập nhật ứng dụng, tên của các ứng dụng trong danh sách
  chờ cập nhật đã được gán nhãn một cách chính xác.
* Khi tải các nội dung như ứng dụng và phim, NVDA sẽ thông báo tên sản phẩm
  và tiến trình tải về.

## Weather

* Các tab như "dự báo" và "bản đồ" đã được nhận dạng chính xác (vá lỗi bởi
  Derek Riemer).
* Khi đọc một dự báo, dùng mũi tên trái phải để chuyển giữa các thành
  phần. Dùng mũi tên lên xuống để đọc từng thành phần. Ví dụ, Bấm mũi tên
  phải có thể thông báo "Thứ hai: 26 độ, có mây, ..." Bấm mũi tên xuống sẽ
  đọc "Thứ hai" và bấm lần nữa sẽ đọc thành phần tiếp theo (nhiệt độ chẳng
  hạn). Tính năng này hiện hoạt động với dự báo theo ngày và theo giờ.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
