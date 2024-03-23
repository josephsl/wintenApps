# Windows 应用增强 #

* 作者：Joseph Lee、Derek Riemer 等

注意：此插件最初称为 Windows 10 应用增强，在 2021 年更名为 Windows 应用增强，以支持 Windows 10 和 Windows
11 等后续版本。此插件的部分内容仍将引用原始插件名称。

此插件是用于各种现代 Windows 应用的应用模块集合，以及对 Windows 10 及更高版本中某些控件的增强和修复。

包括以下应用程序的支持模块（有关所包含内容的详细信息，请参阅每个应用程序部分）：

* 系统键盘
* Settings (Windows+I)

注意:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* 功能更新支持期限与消费者支持期限（家庭版、专业版、专业教育版、工作站专业版）相关联，并且插件可能会在消费者支持结束之前终止对功能更新的支持。有关更多信息和支持日期，请参阅
  <https://aka.ms/WindowsTargetVersioninfo>。
* 尽管可以安装，但此插件不支持 Windows Enterprise LTSC（长期服务版）和 Windows Server 版本。
* 并非支持所有的 Windows Insider Preview 版本，更偏向于支持由开发或金丝雀通道引入 Windows Insider 的功能。
* The add-on may emulate changes included in Insider Preview builds which
  are subsequently removed, and for these changes, the add-on may remove
  them in future releases.
* 插件的 Dev 通道将包括可能包含或不包含在测试版和稳定版中的实验性内容，而Beta 通道将会包含为未来稳定版计划的更改。
* 插件中的某些功能或将成为NVDA屏幕阅读器的一部分。
* 为了获得内嵌 Web 试图（例如开始菜单及其上下文菜单）的应用程序的最佳体验，请在 NVDA
  的浏览模式设置面板启用“输入焦点移动时的自动焦点模式支持”。

有关每个版本之间所做的具体更改，请参阅[另外发布的更新日志][1]文档。

## 常规增强

* In Windows 11 24H2 Insider Preview builds, Action Center interface
  elements can be navigated using mouse and/or touch interaction.

## 系统键盘

包括表情符号面板、剪贴板历史记录、触摸键盘、听写/语音输入、硬件输入建议、建议的操作（预览）、适用于 Windows10 /
Windows11的某些语言的现代输入法编辑器。查看表情符号时，为了获得最佳体验，请从 NvDA 的语音设置对话框中选中“处理字符和符号时包含
Unicode 数据（表情符号）”复选框，并将符号级别设置为“少数”或更高。在 Windows 10
中从云剪贴板历史记录粘贴时，请按空格键而非回车键来粘贴所选项目。

* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Settings (Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
