# Windows App Essentials #

* 저자: Joseph Lee(이성원), Derek Riemer 외 다수
* [출시 버전][1]
* [개발 버전][2]
* NVDA 호환: 2021.3 이상

참고: 윈도우 10 이상(특히 윈도우 11)을 지원하기 위해 2021년에 Windows 10 App Essentials에서 Windows
App Essentials로 변경되었습니다. 단 특정 부분에서는 옛 이름이 뜰 수 있습니다.

본 추가 기능은 여러 UWP 윈도우 앱 지원 모듈 및 윈도우 10 이상에서 제공하는 컨트롤 지원 기능 향상 및 버그 수정을 포함합니다.

다음 앱 모듈 및 지원 모듈을 포함합니다(각 앱 관련 엔트리를 참고 바람):

* 계산기
* Cortana
* 지도
* Microsoft Solitaire Collection
* 현대식 키보드(에모지 페널/받아쓰기/하드웨어 입력 구성/클립보드 히스토리/추천 엑션(프리뷰)/현대식 IME 입력기)
* 메모장(윈도우 11)
* People
* 설정(시스템 설정 앱, Windows+I)
* Voice access(윈도우 11 22H2)
* 날씨
* 그 외 지원 모듈(시작 메뉴 타일 지원 등)

사용시 주의 사항:

* 본 추가 기능은 윈도우 10 21H1(빌드 19043), 11 21H2(빌드 22000) 이상을 지원합니다.
* 윈도우 Enterprise LTSC(Long-Term Servicing Channel)와 윈도우 서버 버전에 설치할 수 있으나 지원은
  하지 않습니다.
* 윈도우 참가자 빌드에 탑제된 기능을 모두 지원하지 않습니다.
* 일부 추가 기능은 NVDA에 포함되었거나 추후 스크린 리더 버전에 반영될 수 있습니다.
* 다음 중 하나 이상 발생시 본 추가 기능에 탑제된 기능중 몇이 삭제됩니다: NVDA가 그 기능을 탑제할때, 지원이 중단된 윈도우
  버전(예: 지원이 중단된 윈도우 10 기능 업데이트)에서 제공하는 기능일 경우, 윈도우나 앱이 변경되어 기능 지원이 필요가 없을때.
* 여러 앱은 미니(compact overlay) 모드(예: 계산기)를 지원하지만 이 모드는 휴대용 NVDA를 사용시 제대로 사용할 수
  없습니다.
* 시작 메뉴 팝업 메뉴와 같이 웹 기술이 적용된 앱 사용시 NVDA 브라우즈 모드에 있는 "포커스 이동 시 자동 포커스 모드 전환"
  기능을 활성화하시기 바랍니다.

추가 기능 변경 내역은 [변경 내용 문서][3]에서 확인할 수 있습니다.

## 일반

* NVDA가 지원하는 UIA  이벤트 외의 다음 이벤트 추적 가능: drag complete, drag drop effect, drop
  target dropped. NVDA 로깅 옵션을 디버그로 설정한 경우 위 이벤트가 추적되도록 함.
* 가상 데스크탑을 열때/닫을때/위치 변경시(윈도우 11 한정)/변경시 NVDA가 데스크탑 이름(예: Desktop 2)를 출력하도록
  함.
* 시작 메뉴에 고정된 타일(윈도우 10) 또는 액션 센터네 빠른 액션을 Alt+Shift+반향키로 조절시 드래그된 항목 또는 새 위치를
  NVDA가 출력하도록 함.
* Announcements such as volume/brightness changes in File Explorer and app
  update notifications from Microsoft Store can be suppressed by turning off
  Report Notifications in NVDA's object presentation settings.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and
  later. This is now part of NVDA 2022.1.
* NVDA will once again announce search result details in Start menu. This is
  now part of NVDA 2022.2.
* In Windows 11, Taskbar items and other shell user interface elements can
  be detected properly when using mouse and/or touch interaction. This is
  now part of NVDA 2022.2.

## 계산기

* 윈도우 10 사용시 히스토리 및 메모리 목록 이름이 제대로 출력됨(본 기능은 NVDA 2022.1에 추가됨).
* 삼각 함수와 같은 공학 계산기 명령 실행시 결과가 출력되도록 함(본 기능은 NVDA 2022.2에 추가됨).

## Cortana

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.

## 지도

* NVDA plays location beep for map locations.

## Microsoft Solitaire Collection

* NVDA will announce names of cards and card decks.

## 현대식 키보드

현대식 키보드란 에모지 페널, 클립보드 히스토리, 받아쓰기, 하드웨어 입력 구성, 추천 엑션(프리뷰) 및 현대식 IME 입력기를
말합니다. 에모지 탐색시 Unicode CLDR 설정을 활성하고 기호 읽기를 "일부" 이상으로 설정하시기 바랍니다. 윈도우 10에서
클립보드 히스토리 사용시 스페이스를 눌러 선택된 내용을 붙여넣으시기 바랍니다.

* 윈도우 10에서 에모지 그룹(카오모지 및 기호 그룹 포함) 선택시 탐색 객체가 특정 에모지에 고정되는 문제 수정.
* 윈도우 11 사용시 방향키를 사용하여 에모지 탐색 가능(본 기능은 NVDA 2022.1에 추가됨).
* 윈도우 11 클립보드 히스토리에서 항목 팝업 메뉴를 제대로 출력할 수 있도록 브라우즈 모드가 반영되지 않도록 함.
* 참가자 빌드 25115 이상(윈도우 11 베타 빌드 22622로 백포팅됨)에서 전화번호와 같은 내용이 클립보드에 복사되었을때 나타나는
  추천 엑션을 출력하도록 함.

## 메모장

This refers to Windows 11 Notepad version 11 or later.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed. This is now part of NVDA 2022.2.

## People

* When searching for contacts, first suggestion will be announced,
  particularly if using recent app releases.

## 설정 앱

* Odd control labels seen in certain Windows installations has been
  corrected.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).
* In Windows 11, breadcrumb bar items are properly recognized.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice
  access interface.

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
