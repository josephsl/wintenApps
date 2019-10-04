# Windows10应用增强 #

* 作者: Joseph Lee, Derek Riemer and other Windows 10 users
* 下载[稳定版][1]
* 下载[开发板][2]
* NVDA兼容版本: 2019.1至2019.2

此附加组件用于各种Windows 10应用程序的模块集合，以及针对某些Windows 10控件的增强功能和修复程序。

以下应用程序模块或用于某些应用程序的支持已包含在内（请参阅每个应用程序部分以了解包含的内容）：

* 计算器（现代）。
* 日历
* Cortana (Classic and Conversations)
* 反馈中心
* 邮件
* 地图
* 斯巴达浏览器
* Microsoft Store
* 系统键盘（版本1709及更高版本中的表情符号面板/听写/硬件输入建议/云剪贴板项目）
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

* 此插件需要Windows 10版本1809（版本17763）或更高版本以及NVDA 2019.1或更高版本。为获得最佳体验，请使用最新Windows
  10稳定版（build 18362）和最新稳定版NVDA插件。
* 一些插件功能可能将成为NVDA屏幕阅读器的一部分。
* 对于未在下面列出的条目，您可以假定功能是NVDA的一部分，不再适用，因为插件不支持旧版本的Windows
  10，或者对应用程序进行了更改，使条目不再适用。

有关每个附加发行版之间所做的更改的列表，请参阅[更新日志的附加发布] [3]文档。

## 常规设置

* 如果此插件在Windows 7和8.1或者是超过支持周期的旧版Windows10上面启用，NVDA将不再播放错误音效。
* 现在子菜单项在各种应用程序中都可以正确识别，包括“开始”菜单磁贴的上下文菜单和Microsoft Edge的应用程序菜单（Redstone 5）。
* 某些对话框现在被识别为正确的对话框并按此朗读，包括“内幕预览”对话框（设置应用程序）。
* 在大多数情况下，NVDA可以在执行搜索时朗读建议计数。此选项由NVDA设置中的对象显示面板中的“朗读对象位置信息”控制。
* 在某些上下文菜单中（例如在Edge中），位置信息（例如，1、2）不再被朗读。
* 现在识别以下UIA事件：控制器，拖动开始，拖动取消，拖动完成，元素选择，项目状态，实时区域更改，通知，系统警报，文本更改，工具提示打开，窗口打开。将NVDA设置为启用调试日志记录运行时，将跟踪这些事件，对于UIA通知事件，如果通知来自当前活动应用程序以外的某个位置，则会听到调试音。
* 现在，可以仅传送来自特定应用的特定事件和/或事件。
* 来自Edge和通用应用程序的工具提示已被识别并将被朗读。现在这是NVDA 2019.3的一部分。
* 在虚拟桌面之间打开，关闭或切换时，NVDA将朗读当前桌面名称（例如，桌面2）。
* 在更改屏幕分辨率或方向时，NVDA将不再公布“开始”菜单大小文本。
* 在版本1903（2019年5月更新）中，如果专注于文件资源管理器，NVDA将朗读音量和亮度变化。这是NVDA 2019.2的一部分。
* App name and version for various Microsoft Store apps are now shown
  correctly. This will be part of NVDA 2019.3.

## 计算器

* When ENTER or Escape is pressed, NVDA will announce calculation results.
* 对于计算，如单位换算，汇率转换器，NVDA将在输入计算后立即读出结果。
* NVDA将不再朗读计算器结果的“标题级别”。
* 如果在输入表达式时达到最大统计值，NVDA现在将读出。
* 添加了对未来计算器版本中始终启用模式的支持。

## 日历

* NVDA不再在邮件正文和其他字段中读出“编辑”或“只读”。

## 小娜

Most items are no longer applicable on Version 1903 and later. Classic
Cortana refers to older Cortana interface which was part of Start menu.

* Textual responses from Cortana (both Classic and Conversations UI) are
  announced in most situations (if using Classic Cortana, reopen Start menu
  and try searching again if responses are not announced).
* 通过语音与Cortana交互时，NVDA将保持沉默。
* In Classic Cortana, NVDA will announce reminder confirmation after you set
  one.
* 在构建18945及更高版本中，现在支持由Cortana用户界面的文件浏览器中的现代搜索界面。

## 反馈中心

* 对于新的应用程序版本，NVDA将不再对反馈类别重复朗读两次。

## 邮件

* 现在查看消息列表中的项目时，您现在可以使用表格导航命令来查看消息标题。请注意，不支持在行（消息）之间导航。
* 在编写信息时，在提建议的状态用声音提示。
* 关闭此应用程序后，NVDA将不再执行任何操作或播放错误音。这是NVDA 2019.2的一部分。

## 地图

* NVDA为地图位置播放位置嘟嘟声。
* 在使用街道视图时，如果启用“使用键盘”选项，NVDA将在您使用箭头键导航地图时读出街道地址。

## 斯巴达浏览器

This refers to classic EdgeHTML-based Microsoft Edge.

* Text auto-complete will be tracked and announced in address omnibar. This
  will be part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This will be part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This will be part
  of NVDA 2019.3.

## Microsoft Store

* 检查应用程序更新后，应更新的应用程序列表中的应用程序名称将被正确标记。
* 下载应用程序和电影等内容时，NVDA会读出产品名称和下载进度。

## 系统键盘

Most features below are now part of NVDA 2018.3 or later.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in build
  18963 and later as the app has been renamed. If using NVDA releases
  earlier than 2018.4, for best experience when reading emojis, use Windows
  OneCore speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* 在某些情况下，当剪贴板中有项目时，NVDA将不再朗读“剪贴板”。
* 在某些运行版本1903（2019年5月更新）的系统上，当表情符号面板打开时，NVDA将不再显示任何内容。
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in 20H1 build 18965 and later.

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
* 在版本1803和更高版本中不再听到音量进度条蜂鸣声。
* 如果在某些情况下使用对象导航命令，NVDA将不再显示任何内容或播放错误音。
* Windows Update提醒对话框被识别为正确的对话框。
* 在某些Windows10安装中看到的奇怪的控件标签已被更正。
* 在版本1803及更高版本中，Windows Update功能更新过程发生了更改，因此添加了“立即下载并安装”链接。
  NVDA现在将朗读新更新的标题（如果存在）。

## 天气

* 如“预测”和“地图”之类的选项卡被识别为适当的选项卡（由Derek Riemer打补丁）。
* 在阅读预测时，使用左右箭头在项目之间移动。 使用向上和向下箭头阅读各个项目。
  例如，按向右箭头可能会报告“星期一：79度，部分阴天，...”，按向下箭头将会显示“星期一”。然后再次按下将读取下一项（如温度）。
  目前这适用于每日和每小时的预测。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
