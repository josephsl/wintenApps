# Windows 应用增强 #

* 作者：Joseph Lee、Derek Riemer 等
* 下载[稳定版][1]
* 下载[开发板][2]
* NVDA 兼容性：2022.2 及更高版本

注意：此插件最初称为 Windows 10 应用增强，在 2021 年更名为 Windows 应用增强，以支持 Windows 10 和 Windows
11 等后续版本。此插件的部分内容仍将引用原始插件名称。

此插件是用于各种现代 Windows 应用的应用模块集合，以及对 Windows 10 及更高版本中某些控件的增强和修复。

包括以下应用程序的支持模块（有关所包含内容的详细信息，请参阅每个应用程序部分）：

* Cortana
* 地图
* 现代键盘（包括表情符号面板、听写、语音输入、硬件输入建议、云剪贴板历史记录、建议操作（预览）、现代输入法编辑器）
* 设置（Windows + I系统设置）
* 语音访问（Windows 11 22H2）
* 天气
* 用于控件和功能的杂项模块，例如读出虚拟桌面名称。

注意:

* 此插件需要 Windows 10 21H2（内部版本 19044）、11 21H2（内部版本 22000）或更高版本。
* 功能更新支持期限与消费者支持期限（家庭版、专业版、专业教育版、工作站专业版）相关联，并且插件可能会在消费者支持结束之前终止对功能更新的支持。有关更多信息和支持日期，请参阅
  aka.ms/WindowsTargetVersioninfo。
* 尽管可以安装，但此插件不支持 Windows Enterprise LTSC（长期服务版）和 Windows Server 版本。
* 如果安装了插件更新器并启用了后台插件更新， 在不受支持的操作系统上 Windows App Essentials 不会被安装。
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in dev
  channel. For beta channel, only the latest build (22623) is supported.
* 插件中的某些功能或将成为NVDA屏幕阅读器的一部分。
* 某些应用程序支持紧凑叠加模式（例如，计算器中的始终置顶模式），该模式无法在 NVDA 的便携版中使用。
* 为了获得内嵌 Web 试图（例如开始菜单及其上下文菜单）的应用程序的最佳体验，请在 NVDA
  的浏览模式设置面板启用“输入焦点移动时的自动焦点模式支持”。

有关每个发行版之间所做的更改的详细信息，请参阅[更新日志的附加发布] [3]文档。

## 常规增强

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect. These events are now part of NVDA 2022.4.
* 在新建、关闭、或切换虚拟桌面时，NVDA会读出当前桌面名称（例如，桌面2）。
* 当使用 Alt+Shift+箭头键在“开始”菜单（Windows 10 中的磁贴）或操作中心快速操作中排列固定条目时，NVDA
  会读出已拖动项目的信息或已拖动项目的新位置。该特性已经包含在 NVDA2022.4 中。
* 在 Windows 11 中，NVDA 支持在打开“开始”菜单时读出显示的搜索高亮。该特性已经包含在 NVDA2023.1 中。

## Cortana

* 现在，在大多数情况下，都会发布来自Cortana的文字回复。
* 通过语音与Cortana互动时，NVDA会暂停朗读。

## 地图

* NVDA为地图上的位置播放位置嘟嘟声。

## 系统键盘

这包括表情符号面板、剪贴板历史记录、听写/语音输入、硬件输入建议、建议的操作（预览）、适用于 Windows10 /
Windows11的某些语言的现代输入法编辑器。查看表情符号时，为了获得最佳体验，请从 NvDA 的语音设置对话框中选中“处理字符和符号时包含
Unicode 数据（表情符号）”复选框，并将符号级别设置为“少数”或更高。在 Windows 10
中从云剪贴板历史记录粘贴时，请按空格键而非回车键来粘贴所选项目。

* 在 Windows 10 中，选择 Emoji 组（包括Kaomoji和符号组）时，NVDA 不会将导航对象移动到某些EMOJI上。
* 在 Windows 11 剪贴板历史记录中，为了让 NVDA 宣布剪贴板历史记录条目菜单项，浏览模式将默认关闭。
* 在 Windows 11 22H2 Moment 1 及更高版本中，当电话号码等兼容的数据复制到剪贴板时，NVDA 会读出建议的操作。

## 设置

* NVDA 将公布可选质量更新控件的名称（如果存在）（Windows 10 中的立即下载和安装链接，Windows 11 中的下载按钮）。
* 在 Windows 11 中，可以正确识别 breadcrumb 栏项目。
* 在 Windows 10 和 11 22H2 及更高版本中，在 Windows 下载和安装更新过程中 NVDA的朗读会被打断并读出下载或安装进度。
  如果使用 Windows 11 22H2 及更高版本，且“启用选择性注册 UIA
  事件和属性改变”的选项处于开启状态，则必须在更新列表出现时立即将焦点移至更新列表，以便 NVDA 可以读出更新进度。

## 语音访问

这是指 Windows 11 22H2 中加入的语音访问功能。

* 在语音访问界面切换麦克风时，NVDA 会读出麦克风的状态。

## 天气

* 诸如“预测”和“地图”之类的选项卡被识别为适当的选项卡（来自Derek Riemer的补充修复）。
* 阅读预测时，请使用左右光标在项目之间移动。使用上下光标读取单个项目。例如，按右光标可能会报告“星期一：79度，间中多云，...”。按向下光标将显示“星期一”，然后再次按将读取下一项（如温度）。目前，该功能可用于每日和每小时预测。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
