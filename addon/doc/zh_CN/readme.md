# Windows10应用增强 #

* 作者: Joseph Lee, Derek Riemer and other Windows 10 users
* 下载[稳定版][1]
* 下载[开发板][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][4] compatible with NVDA 2019.2.1 and earlier

此附加组件用于各种Windows 10应用程序的模块集合，以及针对某些Windows 10控件的增强功能和修复程序。

以下应用程序模块或用于某些应用程序的支持已包含在内（请参阅每个应用程序部分以了解包含的内容）：

* 计算器（现代）。
* 日历
* Cortana (Conversations)
* 邮件
* 地图
* 微软商店
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* {longName} ({name})
  版本: {version}
  网址: {url}
  {copyright}
  
{name} 遵循 GNU 通用公共授权协议第二版， 您可以自由分享或者以任何方式修改本软件， 但在重新发布时必须包含本协议，
  同时必须公开原版和修改版的源代码， 并附上任何用本软件的源代码所产生的软件。
  关于授权协议的详情,您可以通过“帮助”菜单的“授权信息”访问。
  您也可参看以下网页： https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
  
{name} 是由非赢利组织“NV Access”开发的一个用于协助视障用户的免费且开放源代码的解决方案。
  若您觉的 NVDA 很实用，并希望他可以继续发展，请赞助“NV Access”。您可以通过选择位于 NVDA 主菜单的“捐赠”菜单打开捐赠页面
* 设置（系统设置，Windows + I）
* 天气。
* 开始菜单中瓷贴控件等其他模块。

注意:

* This add-on requires Windows 10 Version 1903 (build 18362) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  18363).
* 一些插件功能可能将成为NVDA屏幕阅读器的一部分。
* 对于未在下面列出的条目，您可以假定功能是NVDA的一部分，不再适用，因为插件不支持旧版本的Windows
  10，或者对应用程序进行了更改，使条目不再适用。

有关每个附加发行版之间所做的更改的列表，请参阅[更新日志的附加发布] [3]文档。

## 常规设置

* 如果此插件在Windows 7和8.1或者是超过支持周期的旧版Windows10上面启用，NVDA将不再播放错误音效。
* 某些对话框现在被识别为正确的对话框并按此朗读，包括“内幕预览”对话框（设置应用程序）。
* 在大多数情况下，NVDA可以在执行搜索时朗读建议计数。此选项由NVDA设置中的对象显示面板中的“朗读对象位置信息”控制。
* 在1909版（2019年11月更新）及更高版本中的``开始''菜单或``文件资源管理器''中进行搜索时，现在NVDA在浏览结果时两次宣布搜索结果的实例不太明显，这也使盲文输出在浏览项目时更加一致。
* 可以识别以下UIA事件：控制器，拖动开始，拖动取消，拖动完成，拖动目标进入，拖动目标离开，拖动目标掉落，所选元素，项目状态，活动区域更改，通知，系统警报，文本更改，工具提示打开，窗口打开。将NVDA设置为在启用调试日志记录的情况下运行时，将跟踪这些事件，对于UIA通知事件，如果通知来自当前活动应用程序以外的其他位置，则会听到调试音。
* 现在，可以仅传送来自特定应用的特定事件和/或事件。
* 在虚拟桌面之间打开，关闭或切换时，NVDA将朗读当前桌面名称（例如，桌面2）。
* 在更改屏幕分辨率或方向时，NVDA将不再公布“开始”菜单大小文本。
* 当使用Alt + Shift +箭头键托移“开始”菜单图块或“操作中心”快速操作时，NVDA将朗读有关所拖动项目或所拖动项目的新位置的信息。

## 计算器

* 当按ENTER或Escape键时，NVDA将读出计算结果。
* 对于计算，如单位换算，汇率转换器，NVDA将在输入计算后立即读出结果。
* NVDA将不再朗读计算器结果的“标题级别”。
* 如果在输入表达式时达到最大统计值，NVDA现在将读出。
* 在计算器版本10.1908及更高版本中增加了对始终打开模式的支持。

## 日历

* NVDA不再在邮件正文和其他字段中读出“编辑”或“只读”。

## 小娜

Most items are no longer applicable on Version 1903 and later unless Cortana
Conversations (Version 2004 and later) is in use.

* Textual responses from Cortana are announced in most situations.
* 通过语音与Cortana交互时，NVDA将保持沉默。
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## 邮件

* 现在查看消息列表中的项目时，您现在可以使用表格导航命令来查看消息标题。请注意，不支持在行（消息）之间导航。
* 在编写信息时，在提建议的状态用声音提示。

## 地图

* NVDA为地图位置播放位置嘟嘟声。
* 在使用街道视图时，如果启用“使用键盘”选项，NVDA将在您使用箭头键导航地图时读出街道地址。

## 微软商店

* 检查应用程序更新后，应更新的应用程序列表中的应用程序名称将被正确标记。
* 下载应用程序和电影等内容时，NVDA会读出产品名称和下载进度。

## 系统键盘

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* 在某些运行版本1903（2019年5月更新）的系统上，当表情符号面板打开时，NVDA将不再显示任何内容。
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

## {longName} ({name})
版本: {version}
网址: {url}
{copyright}

{name} 遵循 GNU 通用公共授权协议第二版， 您可以自由分享或者以任何方式修改本软件， 但在重新发布时必须包含本协议， 同时必须公开原版和修改版的源代码， 并附上任何用本软件的源代码所产生的软件。
关于授权协议的详情,您可以通过“帮助”菜单的“授权信息”访问。
您也可参看以下网页： https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

{name} 是由非赢利组织“NV Access”开发的一个用于协助视障用户的免费且开放源代码的解决方案。
若您觉的 NVDA 很实用，并希望他可以继续发展，请赞助“NV Access”。您可以通过选择位于 NVDA 主菜单的“捐赠”菜单打开捐赠页面

* 搜索联系人时，将首先朗读搜索的建议，特别是在使用最新的应用程序版本时。

## 设置

* 现在将自动报告某些信息，例如Windows Update进度，包括存储感知/磁盘清理小部件和Windows Update中的错误。
* 进度栏值和其他信息不再重复朗读两次。
* 对于某些组合框和单选按钮，NVDA将不再无法识别标签和/或读出更改值。
* 如果在某些情况下使用对象导航命令，NVDA将不再显示任何内容或播放错误音。
* Windows Update提醒对话框被识别为正确的对话框。
* 在某些Windows10安装中看到的奇怪的控件标签已被更正。
* 在版本1803及更高版本中，Windows Update功能更新过程发生了更改，因此添加了“立即下载并安装”链接。
  NVDA现在将朗读新更新的标题（如果存在）。

## 天气

* 如“预测”和“地图”之类的选项卡被识别为适当的选项卡（由Derek Riemer打补丁）。
* 阅读预测时，请使用左右箭头在项目之间移动。使用上下箭头读取单个项目。例如，按向右箭头可能会报告“星期一：79度，间中多云，...”。按向下箭头将显示“星期一”，然后再次按将读取下一项（如温度）。目前，该功能可用于每日和每小时预测。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
