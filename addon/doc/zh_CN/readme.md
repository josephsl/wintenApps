# Windows 应用增强 #

* 作者：Joseph Lee、Derek Riemer 等

注意：此插件最初称为 Windows 10 应用增强，在 2021 年更名为 Windows 应用增强，以支持 Windows 10 和 Windows
11 等后续版本。此插件的部分内容仍将引用原始插件名称。

此插件是用于各种现代 Windows 应用的应用模块集合，以及对 Windows 10 及更高版本中某些控件的增强和修复。

包括以下应用程序的支持模块（有关所包含内容的详细信息，请参阅每个应用程序部分）：

* Settings (Windows+I)

注意:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* 功能更新支持期限与消费者支持期限（家庭版、专业版、专业教育版、工作站专业版）相关联，并且插件可能会在消费者支持结束之前终止对功能更新的支持。有关更多信息和支持日期，请参阅
  <https://aka.ms/WindowsTargetVersioninfo>。
* 尽管可以安装，但此插件不支持 Windows Enterprise LTSC（长期服务版）和 Windows Server 版本。
* 并非支持所有的 Windows Insider Preview 版本，更偏向于支持由开发或金丝雀通道引入 Windows Insider 的功能。

有关每个版本之间所做的具体更改，请参阅[另外发布的更新日志][1]文档。

## 常规增强

* In Windows 11 24H2, quick settings (shellhost.exe) interface elements can
  be navigated using mouse and/or touch interaction. This is now part of
  NVDA 2024.2.
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
