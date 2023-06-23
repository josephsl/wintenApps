# Windows 应用增强 #

* 作者：Joseph Lee、Derek Riemer 等
* 下载[稳定版][1]
* 下载[测试版][2]
* 下载[开发板][3]
* NVDA 兼容性：2023.1 及更高版本

注意：此插件最初称为 Windows 10 应用增强，在 2021 年更名为 Windows 应用增强，以支持 Windows 10 和 Windows
11 等后续版本。此插件的部分内容仍将引用原始插件名称。

此插件是用于各种现代 Windows 应用的应用模块集合，以及对 Windows 10 及更高版本中某些控件的增强和修复。

包括以下应用程序的支持模块（有关所包含内容的详细信息，请参阅每个应用程序部分）：

* Cortana
* 现代键盘（表情符号面板/触摸键盘/听写/语音输入/硬件输入建议/剪贴板历史/建议操作/现代输入法编辑器）
* 设置（Windows + I系统设置）
* 语音访问（Windows 11 22H2）
* 天气
* 用于控件和功能的其他模块，例如读出虚拟桌面名称

注意:

* 此插件需要 Windows 10 22H2（内部版本 19045）、11 21H2（内部版本 22000）或更高版本。
* 功能更新支持期限与消费者支持期限（家庭版、专业版、专业教育版、工作站专业版）相关联，并且插件可能会在消费者支持结束之前终止对功能更新的支持。有关更多信息和支持日期，请参阅
  aka.ms/WindowsTargetVersioninfo。
* 尽管可以安装，但此插件不支持 Windows Enterprise LTSC（长期服务版）和 Windows Server 版本。
* 如果安装了插件更新器并启用了后台插件更新， 在不受支持的操作系统上 Windows App Essentials 不会被安装。
* 并非支持所有的 Windows Insider Preview 版本，更偏向于支持由开发或金丝雀通道引入 Windows Insider 的功能。
* The add-on may emulate fixes included in Insider Preview builds which are
  subsequently removed, and for these changes, the add-on may remove them in
  future releases.
* 插件的 Dev 通道将包括可能包含或不包含在测试版和稳定版中的实验性内容，而Beta 通道将会包含为未来稳定版计划的更改。
* 插件中的某些功能或将成为NVDA屏幕阅读器的一部分。
* 为了获得内嵌 Web 试图（例如开始菜单及其上下文菜单）的应用程序的最佳体验，请在 NVDA
  的浏览模式设置面板启用“输入焦点移动时的自动焦点模式支持”。

有关每个版本之间所做的具体更改，请参阅[另外发布的更新日志][4]文档。

## 常规增强

* 当打开、关闭或在虚拟桌面之间切换时，NVDA 会读出当前的虚拟桌面名称（例如桌面 2）。该特性已经包含在 NVDA2023.2 中。
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11) and reporting item position when moving through taskbar icons
  (Windows 10 and 11). Note that these are emulated workarounds for features
  introduced and then subsequently removed in Insider Preview builds and may
  be removed from the add-on in the future.
* In aps such as Windows 11 22H2 File Explorer and Notepad where tabbed
  windows are supported, NVDA will announce the name and the position of
  tabs when switching between them. This is now part of NVDA 2023.2.

## Cortana

* 现在，在大多数情况下，都会发布来自Cortana的文字回复。

## 系统键盘

包括表情符号面板、剪贴板历史记录、触摸键盘、听写/语音输入、硬件输入建议、建议的操作（预览）、适用于 Windows10 /
Windows11的某些语言的现代输入法编辑器。查看表情符号时，为了获得最佳体验，请从 NvDA 的语音设置对话框中选中“处理字符和符号时包含
Unicode 数据（表情符号）”复选框，并将符号级别设置为“少数”或更高。在 Windows 10
中从云剪贴板历史记录粘贴时，请按空格键而非回车键来粘贴所选项目。

* 在 Windows 11 22H2 及更高版本中，当电话号码等兼容的数据复制到剪贴板时，NVDA 会读出建议的操作。

## 设置

* NVDA 会读出可选质量更新控件的名称（如果存在）（Windows 10 中的立即下载和安装链接，Windows 11 中的下载按钮）。
* 在 Windows 11 中，可以正确识别 breadcrumb 栏项目。
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

## 语音访问

这是指 Windows 11 22H2 中加入的语音访问功能。

* 在语音访问界面切换麦克风时，NVDA 会读出麦克风的状态。

## 天气

* 诸如“预测”和“地图”之类的选项卡被识别为适当的选项卡（来自Derek Riemer的补充修复）。

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
