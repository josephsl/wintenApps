# Windows App Essentials #

* 저자: Joseph Lee(이성원), Derek Riemer 외 윈도우 10 사용자들
* [출시 버전][1]
* [개발 버전][2]
* NVDA 호환: 2020.4 이상

참고: 윈도우 10 이상(특히 윈도우 11)을 지원하기 위해 2021년에 Windows 10 App Essentials에서 Windows
App Essentials로 변경되었습니다. 단 특정 부분에서는 옛 이름이 뜰 수 있습니다.

본 추가 기능은 여러 UWP 윈도우 앱 지원 모듈 및 윈도우 10 이상에서 제공하는 컨트롤 지원 기능 향상 및 버그 수정을 포함합니다.

다음 앱 모듈 및 지원 모듈을 포함합니다(각 앱 관련 엔트리를 참고 바람):

* 계산기(UWP)
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
* 그 외 지원 모듈(시작 메뉴 타일 지원 등)

사용시 주의 사항:

* 본 추가 기능은 윈도우 10 20H2(빌드 19042) 이상을 지원하며 최신 윈도우 버전(윈도우 10 21H1/빌드 19043)에
  최적화되어 있습니다.
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details).
* 일부 추가 기능은 NVDA에 포함되었거나 추후 스크린 리더 버전에 반영될 수 있습니다.
* 다음 중 하나 이상 발생시 본 추가 기능에 탑제된 기능중 몇이 삭제됩니다: NVDA가 그 기능을 탑제할때, 지원이 중단된 윈도우
  버전(예: 지원이 중단된 윈도우 10 기능 업데이트)에서 제공하는 기능일 경우, 윈도우나 앱이 변경되어 기능 지원이 필요가 없을때.
* 여러 앱은 미니(compact overlay) 모드(예: 계산기)를 지원하지만 이 모드는 휴대용 NVDA를 사용시 제대로 사용할 수
  없습니다.

추가 기능 변경 내역은 [변경 내용 문서][3]에서 확인할 수 있습니다.

## 일반

* 특정 검색창에서 검색 결과수가 출력되도록 함(본 기능은 NVDA 설정내 객체 알림 페널에 있는 객체 위치 출력 설정으로 제어할 수
  있음).
* When searching in Start menu or File Explorer in Windows 10 1909 (November
  2019 Update) and later, instances of NVDA announcing search results twice
  when reviewing results are less noticeable, which also makes braille
  output more consistent when reviewing items.
* NVDA가 지원하는 UIA  이벤트 외의 다음 이벤트 추적 가능: drag start, drag cancel, drag
  complete, drop target drag enter, drop target drag leave, drop target
  dropped. NVDA가 디버그 로깅 상태로 재시작된 경우 위 이벤트가 추적되며 notification 이벤트는 추가 디버그 정보가
  출력되도록 함.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* When opening, closing, reordering (Windows 11), or switching between
  virtual desktops, NVDA will announce active virtual desktop name (desktop
  2, for example).
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

Most items are applicable when using Cortana Conversations (Windows 10 2004
and later).

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.
* In Windows 10 1909 (November 2019 Update) and later, modern search
  experience in File Explorer powered by Windows Search user interface is
  supported.

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
  product name and download progress (does not work properly in updated
  Microsoft Store in Windows 11).

## 현대식 키보드

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in Windows 11.

* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* On some systems running Windows 10 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* When an emoji group (including kaomoji and symbols group in Windows 10
  1903 or later) is selected, NVDA will no longer move navigator object to
  certain emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in Windows 11.

## People

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## 설정 앱

* Certain information such as Windows Update progress is reported
  automatically, including Storage sense/disk cleanup widget and errors from
  Windows Update.
* Progress bar values and other information are no longer announced twice.
* Windows Update reminder dialog is recognized as a proper dialog.
* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update link if
  present, typically named "download and install now".

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
