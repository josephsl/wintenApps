# Windows10应用增强 #

* 作者: Joseph Lee, Derek Riemer and other Windows 10 users
* 下载[稳定版][1]
* 下载[开发板][2]
* NVDA兼容版本: 2020.4 或更高

此插件用于各种 Windows 10 应用程序的模块集合，以及针对某些 Windows 10 控件的增强功能和修复程序。

包括以下应用程序的支持模块（有关所包含内容的详细信息，请参阅每个应用程序部分）：

* 计算器（现代）
* 日历
* Cortana（会话）
* 邮件
* 地图
* Microsoft Solitaire Collection（微软纸牌游戏）
* Microsoft Store
* 现代键盘（包括表情符号面板、听写、硬件输入建议、云剪贴板历史记录以及现代输入法编辑器）
* 人脉
* 设置（系统设置，Windows + I）
* 天气
* 开始菜单中瓷贴控件等其他模块

注意:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows release (Windows 10
  Version 21H1/build 19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* 某些插件功能可能将成为NVDA屏幕阅读器的一部分。
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support older Windows
  releases, or changes were made to Windows and apps that makes entries no
  longer applicable.
* 某些应用程序支持紧凑叠加模式（例如，计算器中的始终置顶模式），该模式无法与 NVDA 的便携版正常工作。

有关每个附加发行版之间所做的更改的列表，请参阅[更新日志的附加发布] [3]文档。

## 常规设置

* 在大多数情况下，NVDA 可以在执行搜索时朗读建议计数。此选项由 NVDA “对象提示”设置对话框中的“读出对象的位置信息”复选框控制。
* 在 1909 版（2019年11月更新）及更高版本 Windows 10 中的‘开始’菜单或文件资源管理器中进行搜索时，现在 NVDA
  在浏览结果时两次宣布搜索结果的实例不太明显，这也使盲文输出在浏览项目时更加一致。
* 除了NVDA提供的UIA事件处理程序外，还可以识别以下UIA事件：拖动开始、拖动取消、拖动完成、拖动目标进入、拖动目标离开、拖动目标丢弃。在NVDA的日志级别设置为调试时，这些事件将被跟踪，对于UIA通知事件，如果通知来自当前活动应用以外的其他地方，将听到调试音。有些事件会提供额外的信息，比如事件的控制器中的元素数量，状态变化事件的元素状态，以及项目状态事件的项目文本。
* 可以只跟踪特定事件或来自特定应用程序的事件。
* 打开、关闭、重新排序（内部版本 21337 或更高版本）或切换虚拟桌面时，NVDA将朗读当前桌面名称（例如，桌面2）。
* 当改变屏幕分辨率或方向时，NVDA将不再读出开始菜单的大小文本。
* 当使用 Alt + Shift +光标键托移“开始”菜单磁贴或“操作中心”快速操作按钮时，NVDA 将朗读有关所拖动项目及所拖动项目的新位置的信息。
* 通过在 NVDA 的“对象提示”设置中关闭“读出通知提示”，可以禁止诸如文件资源管理器中的音量、亮度更改和来自 Microsoft Store
  的应用程序更新之类的通知。

## 计算器

* NVDA 将不再两次宣布图形计算器屏幕消息。

## 日历

* NVDA 不再在邮件正文和其他字段中读出“编辑”或“只读”。

## Cortana

大多数项目适用于使用 Cortana 对话（版本 2004 及以后）。

* 现在，在大多数情况下，都会发布来自Cortana的文字回复。
* 通过语音与Cortana交互时，NVDA将保持沉默。
* 在版本1909（2019年11月更新）及更高版本中，现在支持资源管理器的Windows 搜索用户的现代界面。

## 邮件

* 现在查看消息列表中的项目时，您现在可以使用表格导航命令来查看消息标题。请注意，不支持在行（消息）之间导航。
* 在编写信息时，在提建议的状态用声音提示。

## 地图

* NVDA为地图位置播放位置嘟嘟声。
* 在使用街道视图时，如果启用“使用键盘”选项，NVDA将在您使用光标键浏览地图时读出街道地址。

## Microsoft Solitaire Collection（微软纸牌游戏）

* NVDA现在可读出卡片和卡片组的名称。

## Microsoft Store

* 检查应用更新后，应更新的应用列表中的应用名称将被正确标记。
* 下载应用和电影等内容时，NVDA会读出产品名称和下载进度。

## 系统键盘

这包括表情符号面板、剪贴板历史记录、听写、硬件输入建议以及某些语言的现代输入法编辑器。查看表情符号时，为了获得最佳体验，请从 NvDA
的语音设置对话框中选中“处理字符和符号时包含 Unicode 数据（表情符号）”复选框，并将符号级别设置为“少数”或更高。此外，NVDA 在
Windows 10 内部版本 21296 及更高版本中支持更新的输入体验面板。

* 当前，打开剪贴板历史记录时，在某些情况下，剪贴板中有项目时，NVDA将不再读出“剪贴板”。
* 在某些运行版本1903（2019年5月更新）的系统上，当表情符号面板打开时，NVDA将不再显示任何内容。
* 当选择表情符号组（包括版本 1903之后的绘文字）时，NVDA 将不再将导航器对象移动到某些表情符号。
* 在Windows 10 内部版本 21296 及更高版本中，增加了对更新的输入体验面板（组合的表情符号面板和剪贴板历史记录）的支持。

## 人脉

* 搜索联系人时，将首先朗读搜索的建议，特别是在使用最新的应用程序版本时。

## 设置

* 现在将自动读出某些信息，例如 Windows Update 进度，包括存储感知、磁盘清理和 Windows Update中的错误。
* 进度栏值和其他信息不再重复朗读两次。
* Windows 更新提醒对话框被识别为正确的对话框。
* Odd control labels seen in certain Windows installations has been
  corrected.
* 在版本 1803 及更高版本的 Windows 10 中，Windows 更新中的某些更新添加了“立即下载并安装”链接。NVDA
  现在将朗读新更新的标题（如果存在）。

## 天气

* 如“预测”和“地图”之类的选项卡被识别为适当的选项卡（由Derek Riemer打补丁）。
* 阅读预测时，请使用左右光标在项目之间移动。使用上下光标读取单个项目。例如，按右光标可能会报告“星期一：79度，间中多云，...”。按向下光标将显示“星期一”，然后再次按将读取下一项（如温度）。目前，该功能可用于每日和每小时预测。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
