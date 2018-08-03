# Windows10应用增强 #

* 作者: Joseph Lee, Derek Riemer and other Windows 10 users
* 下载[稳定版][1]
* 下载[开发板][2]

此附加组件用于各种Windows 10应用程序的模块集合，以及针对某些Windows 10控件的增强功能和修复程序。

以下应用程序模块或用于某些应用程序的支持已包含在内（请参阅每个应用程序部分以了解包含的内容）：

* 时锺和闹钟。
* 日历
* 计算器（现代）。
* 小娜
* 反馈中心
* 游戏栏
* 邮件
* 地图
* 斯巴达浏览器
* 系统键盘（在版本1709及以上版本中的表情符号面板/硬件输入建议/云剪贴板的项目）
* {longName} ({name})
  版本: {version}
  网址: {url}
  {copyright}
  
{name} 遵循 GNU 通用公共授权协议第二版， 您可以自由分享或者以任何方式修改本软件， 但在重新发布时必须包含本协议，
  同时必须公开原版和修改版的源代码， 并附上任何用本软件的源代码所产生的软件。
  关于授权协议的详情,您可以通过“帮助”菜单的“授权信息”访问。
  您也可参看以下网页： http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
  
{name} 是由非赢利组织“NV Access”开发的一个用于协助视障用户的免费且开放源代码的解决方案。
  若您觉的 NVDA 很实用，并希望他可以继续发展，请赞助“NV Access”。您可以通过选择位于 NVDA 主菜单的“捐赠”菜单打开捐赠页面
* 设置（系统设置，Windows + I）
* Skype（通用应用程序）
* 商店
* 天气。
* 开始菜单中瓷贴控件等其他模块。

笔记:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA.
* 一些插件功能可能将成为NVDA屏幕阅读器的一部分。
* 对于未在下面列出的条目，您可以假定功能是NVDA的一部分，不再适用，因为附加组件不支持旧版本的Windows
  10，或者对应用程序进行了更改，使条目不再适用。

有关每个附加发行版之间所做的更改的列表，请参阅[更新日志的附加发布] [3]文档。

## 常规设置

* 现在子菜单项在各种应用程序中都可以正确识别，包括“开始”菜单磁贴的上下文菜单和Microsoft Edge的应用程序菜单（Redstone 5）。
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app).
* NVDA可以在大多数情况下执行搜索时朗读建议计数。 此选项由对象查看对话框/面板中的“读出对象位置信息”控制。
* 在某些上下文菜单中（例如在Edge中），位置信息（例如，1、2）不再被朗读。
* The following UIA events are recognized: active text position change,
  controller for, drag start, drag cancel, drag complete, element selected,
  live region change, notification, system alert, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* 增加可通过NVDA选项菜单中的Windows 10 应用增强对话框的检查插件更新（自动或手动）的功能。
  默认情况下，稳定版和开发版将分别按每周或每天自动检查新更新。
* In some apps, live region text is announced. This includes alerts in Edge
  (including elements marked with aria-role=alert), results in Calculator
  and others. Note that this may result in double-speaking in some cases.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced.
* 来自Edge和通用应用程序的工具提示已被识别并将被朗读。
* With Sets turned on (builds 17627 through 17692 for some insiders), when
  opening a new Sets tab (Control+Windows+T), NVDA will announce search
  results when searching for items in the embedded Cortana window.
* With Sets turned on, when switching between Sets tabs, NvDA will announce
  name and position of the tab you are switching to.
* 在虚拟桌面之间打开，关闭或切换时，NVDA会读出当前的桌面ID（例如，桌面2）。
* 在更改屏幕分辨率或方向时，NVDA将不再公布“开始”菜单大小文本。

## 时锺和闹钟

* 更改使用时段对话框可朗读，在将焦点移至选择活动时间选取器可显示。 这也影响用于选择何时重新启动以完成安装Windows更新。

## 计算器

* 按下ENTER或Escape后，NVDA会读出计算结果。
* 对于计算，如单位换算，汇率转换器，NVDA将在输入计算后立即读出结果。
* NVDA will no longer announce "heading level" for calculator results.

## 日历

* NVDA不再在邮件正文和其他字段中读出“编辑”或“只读”。

## 小娜

* 来自Cortana的文字回应在大多数情况下都会朗读（如果没有，请重新打开“开始”菜单并再次尝试搜索）。
* 通过语音与Cortana交互时，NVDA将保持沉默。
* NVDA现在会在您设置后提醒您确认。

## 反馈中心

* 对于新的应用程序版本，NVDA将不再对反馈类别重复朗读两次。

## 游戏栏

* NVDA will announce appearance of Game Bar window. Due to technical
  limitations, NVDA cannot interact fully with Game Bar prior to build
  17723.

## 邮件

* 查看邮件列表中的项目时，现在可以使用表格导航命令查看消息标题。
* 在编写信息时，在提建议的状态用声音提示。

## 地图

* NVDA为地图位置播放位置嘟嘟声。
* 在使用街道视图时，如果启用“使用键盘”选项，NVDA将在您使用箭头键导航地图时读出街道地址。

## 斯巴达浏览器

* Notifications such as file downloads and various webpage alerts, as well
  as availability of Reading View (if using Version 1709 and later) are
  announced.

## 系统键盘

* 支持版本1709（RealCudior
  Update）中的EMOJI输入面板，并包括在构建17661和以后的重新设计的面板。在阅读表情符号时，最好使用Windows
  OneCore语言合成器。
* 支持版本1803（2018年4月更新）及更高版本中的硬件键盘输入建议。
* 在1709后的版本中，当表情符号面板打开时，NVDA会读出第一个选定的表情符号。
* 支持在17666版本（Redstone 5）及更高版本中朗读云端剪贴板项目。
* 使用现代键盘及其功能时减少不必要的冗长。这些包括在打开硬件键盘输入建议时不再公布“Microsoft Candidate
  UI”，并且某些触摸键盘键在某些系统上引发名称更改事件时不再保持沉默。

## {longName} ({name})
版本: {version}
网址: {url}
{copyright}

{name} 遵循 GNU 通用公共授权协议第二版， 您可以自由分享或者以任何方式修改本软件， 但在重新发布时必须包含本协议， 同时必须公开原版和修改版的源代码， 并附上任何用本软件的源代码所产生的软件。
关于授权协议的详情,您可以通过“帮助”菜单的“授权信息”访问。
您也可参看以下网页： http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

{name} 是由非赢利组织“NV Access”开发的一个用于协助视障用户的免费且开放源代码的解决方案。
若您觉的 NVDA 很实用，并希望他可以继续发展，请赞助“NV Access”。您可以通过选择位于 NVDA 主菜单的“捐赠”菜单打开捐赠页面

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## 设置

* 某些信息（如Windows Update进度）会自动朗读。
* 进度栏值和其他信息不再重复朗读两次。
* 当使用对象导航在控件之间导航时，可以识别设置组。
* 对于某些组合框，NVDA将不再无法识别标签/读出更改值。
* 在版本1803和更高版本中不再听到音量进度条蜂鸣声。
* 有关Windows Update状态的更多消息将会公布，特别是如果Windows Update遇到错误的时候。

## Skype

* 打字上屏文本朗读，就像Skype的桌面客户端。
* Control+NvDA+number row commands, used to read recent chat history and to
  move navigator object to chat entries in Skype for Desktop, is also
  available in Skype UWP.
* You can press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* NVDA在浏览多数案件的讯息时将不再读出“Skype讯息”。
* From message history list, pressing NVDA+D on a message item will allow
  NVDA to announce detailed information about a message such as channel
  type, sent date and time and so on.

## 商店

* 检查应用程序更新后，应更新的应用程序列表中的应用程序名称将被正确标记。
* 下载应用程序和电影等内容时，NVDA会读出产品名称和下载进度。

## 天气

* 如“预测”和“地图”之类的选项卡被识别为适当的选项卡（由Derek Riemer打补丁）。
* 在阅读预测时，使用左右箭头在项目之间移动。 使用向上和向下箭头阅读各个项目。
  例如，按向右箭头可能会报告“星期一：79度，部分阴天，...”，按向下箭头将会显示“星期一”。然后再次按下将读取下一项（如温度）。
  目前这适用于每日和每小时的预测。

[[!tag dev 稳定]


[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
