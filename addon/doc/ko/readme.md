# Windows 10 App Essentials #

* 저자: Joseph Lee(이성원), Derek Riemer 외 윈도우 10 사용자들
* [출시 버전][1]
* [개발 버전][2]
* NVDA compatibility: 2020.4 and beyond

본 추가 기능은 여러 윈도우 10 앱 지원 모듈 및 윈도우 10 컨트롤 지원 기능 향상 및 버그 수정을 포함합니다.

다음 앱 모듈 및 지원 모듈을 포함합니다(각 앱 관련 엔트리를 참고 바람):

* Calculator (modern)
* 달력
* Cortana(Conversations)
* 메일
* 지도
* Microsoft Solitaire Collection
* Microsoft Store
* 현대식 키보드(에모지 페널/받아쓰기/하드웨어 입력 구성/클립보드 히스토리/현대식 IME 입력기)
* People
* 설정(시스템 설정 앱, Windows+I)
* 날씨
* Miscellaneous modules for controls such as Start Menu tiles

사용시 주의 사항:

* 본 추가 기능은 윈도우 10 버전 2004(빌드 19041) 이상을 지원하며 최신 윈도우 10 출시 버전(21H1/빌드 19043)에
  최적화되어 있습니다.
* 일부 추가 기능은 NVDA에 포함되었거나 추후 스크린 리더 버전에 반영될 수 있습니다.
* 다음 중 하나 이상 발생시 본 추가 기능에 탑제된 기능중 몇이 삭제됩니다: NVDA가 그 기능을 탑제할때, 지원이 중단된 윈도우 10
  버전에서 제공하는 기능일 경우, 윈도우 10이나 앱이 변경되어 기능 지원이 필요가 없을때.
* 여러 앱은 미니(compact overlay) 모드(예: 계산기)를 지원하지만 이 모드는 휴대용 NVDA를 사용시 제대로 사용할 수
  없습니다.

추가 기능 변경 내역은 [변경 내용 문서][3]에서 확인할 수 있습니다.

## 일반

* In addition to dialogs recognized by NVDA, more dialogs are now recognized
  as proper dialogs and reported as such, including Insider Preview dialog
  (settings app).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation panel found in NVDA settings.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped. With NVDA's log
  level set to debug, these events will be tracked, and for UIA notification
  event, a debug tone will be heard if notifications come from somewhere
  other than the currently active app. Some events will provide additional
  information such as element count in controller for event, state of the
  element for state change event, and item text for item status event.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, reordering (build 21337 or later), or switching
  between virtual desktops, NVDA will announce active virtual desktop name
  (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* When arranging Start menu tiles or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce information on dragged items or
  new position of the dragged item.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.

## 계산기

* NVDA will no longer announce graphing calculator screen message twice.

## 달력

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

Most items are applicable when using Cortana Conversations (Version 2004 and
later).

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

## 메일

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers. Note that navigating between rows
  (messages) is not supported.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## 지도

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## Microsoft Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## 현대식 키보드

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in build 21296 and later.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* When an emoji group (including kaomoji and symbols group in Version 1903
  or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in build 21296 and later.

## People

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## 설정 앱

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Progress bar values and other information are no longer announced twice.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows 10 installations has been
  corrected.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

## 날씨

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
* When reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
