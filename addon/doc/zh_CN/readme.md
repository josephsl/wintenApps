# Windows 应用增强 #

* 作者：Joseph Lee、Derek Riemer 等
* 下载[稳定版][1]
* 下载[开发板][2]
* NVDA 兼容性：2021.3 及更高版本

注意：此插件最初称为 Windows 10 应用增强，在 2021 年更名为 Windows 应用增强，以支持 Windows 10 和 Windows
11 等后续版本。此插件的部分内容仍将引用原始插件名称。

此插件是用于各种现代 Windows 应用的应用模块集合，以及对 Windows 10 及更高版本中某些控件的增强和修复。

包括以下应用程序的支持模块（有关所包含内容的详细信息，请参阅每个应用程序部分）：

* 计算器
* Cortana
* 地图
* 现代键盘（包括表情符号面板、听写、语音输入、硬件输入建议、云剪贴板历史记录、建议操作（预览）、现代输入法编辑器）
* 记事本（Windows 11）
* 人脉
* 设置（Windows + I系统设置）
* Voice access (Windows 11 22H2)
* 天气
* 开始菜单中的瓷贴控件和其他模块

注意:

* This add-on requires Windows 10 21H1 (build 19043), Windows 11 21H2 (build
  22000), or later releases.
* 尽管可以安装，但此插件不支持 Windows Enterprise LTSC（长期服务版）和 Windows Server 版本。
* 并非支持 Windows Insider Preview 版本中的所有功能。
* 插件中的某些功能或将成为NVDA屏幕阅读器的一部分。
* 对于未在下方列出的条目，您可以假定功能已包含在 NVDA 核心中，或者不再适用，因为插件不支持旧版本的
  Windows，或者对相关应用程序进行了更改，使相关条目不再适用。
* 某些应用程序支持紧凑叠加模式（例如，计算器中的始终置顶模式），该模式无法在 NVDA 的便携版中使用。
* 为了获得内嵌 Web 试图（例如开始菜单及其上下文菜单）的应用程序的最佳体验，请在 NVDA
  的浏览模式设置面板启用“输入焦点移动时的自动焦点模式支持”。

有关每个发行版之间所做的更改的详细信息，请参阅[更新日志的附加发布] [3]文档。

## 常规增强

* 除了 NVDA 提供的 UIA 事件处理程序以外，还可以识别以下 UIA 事件和属性：拖动完成、拖放效果、放置目标。将 NVDA
  的日志级别设置为调试，这些事件也会被跟踪和记录。
* 打开、关闭、重新排序（Windows 11）或切换虚拟桌面时，NVDA将朗读当前桌面名称（例如，桌面2）。
* 当使用 Alt+Shift+箭头键在“开始”菜单（Windows 10 中的磁贴）或操作中心快速操作中排列固定条目时，NVDA
  会读出已拖动项目的信息或已拖动项目的新位置。
* 通过在 NVDA 的“对象提示”设置中关闭“读出通知提示”，可以禁止诸如文件资源管理器中的音量、亮度更改和来自 Microsoft Store
  的应用程序更新之类的通知。
* 在 Windows 11 22H2 及更高版本中，可读出 Windows+Alt+K 的麦克风静音切换状态。
* 修复了 NVDA 在 Windows Terminal 1.12.10733 及更高版本中会重复朗读输出文本的错误，该修复已经包含在
  NVDA2022.1 中。
* 修复了 NVDA 不朗读开始菜单搜索结果详情的错误，该修复已经包含在 NVDA2022.2 中。
* 在 Windows 11 中，使用鼠标和/或触摸交互时可以正确读出任务栏项目和其他的用户界面控件元素，该修复已经包含在 NVDA2022.2 中。

## 计算器

* 在 Windows 10 中，可以正确读出历史记录和内存列表项标签。该功能已是 NVDA 2022.1 的一部分。
* NVDA 现可以在执行三角运算等科学计算模式命令时读出计算器显示内容。该修复已经包含在 NVDA2022.2 中。

## Cortana

* 现在，在大多数情况下，都会发布来自Cortana的文字回复。
* 通过语音与Cortana互动时，NVDA会暂停朗读。

## 地图

* NVDA为地图上的位置播放位置嘟嘟声。

## 系统键盘

这包括表情符号面板、剪贴板历史记录、听写/语音输入、硬件输入建议、硬件输入建议、建议的操作（预览）、适用于 Windows10 /
Windows11的某些语言的现代输入法编辑器。查看表情符号时，为了获得最佳体验，请从 NvDA 的语音设置对话框中选中“处理字符和符号时包含
Unicode 数据（表情符号）”复选框，并将符号级别设置为“少数”或更高。在 Windows 10
中从剪贴板历史记录粘贴时，请按空格键而非回车键来粘贴所选项目。

* 在Windows 10中，选择Emoji组（包括Kaomoji和符号组）时，NVDA不会将导航对象移动到某些EMOJI上。
* 在 Windows 11 中，当表情符号面板打开时，可以使用箭头键查看表情符号。该功能已是 NVDA2022.1 的一部分。
* 在 Windows 11 剪贴板历史记录中，为了让 NVDA 宣布剪贴板历史记录条目菜单项，浏览模式将默认关闭。
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## 记事本

这是指 Windows 11 或更高版本系统上的记事本。

* NVDA在执行读出状态栏命令（台式机键盘方案为 NVDA+End，笔记本键盘方案为
  NvDA+Shift+End）时会同时读出行列信息等状态条目。该修复已经包含在 NVDA2022.1 中。

## 人脉

* 搜索联系人时，将首先朗读搜索的建议，特别是在使用最新的应用程序版本时。

## 设置

* 在某些 Windows 安装中看到的奇怪的控件标签已得到更正。
* NVDA 将公布可选质量更新控件的名称（如果存在）（Windows 10 中的立即下载和安装链接，Windows 11 中的下载按钮）。
* 在 Windows 11 中，可以正确识别 breadcrumb 栏项目。
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

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
