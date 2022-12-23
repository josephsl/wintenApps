# Windows App Essentials #

* 저자: Joseph Lee(이성원), Derek Riemer 외 다수
* [출시 버전][1]
* [개발 버전][2]
* NVDA compatibility: 2022.3 and later

참고: 윈도우 10 이상(특히 윈도우 11)을 지원하기 위해 2021년에 Windows 10 App Essentials에서 Windows
App Essentials로 변경되었습니다. 단 특정 부분에서는 옛 이름이 뜰 수 있습니다.

본 추가 기능은 여러 UWP 윈도우 앱 지원 모듈 및 윈도우 10 이상에서 제공하는 컨트롤 지원 기능 향상 및 버그 수정을 포함합니다.

다음 앱 모듈 및 지원 모듈을 포함합니다(각 앱 관련 엔트리를 참고 바람):

* Cortana
* 지도
* 현대식 키보드(에모지 페널/받아쓰기/하드웨어 입력 구성/클립보드 히스토리/추천 엑션/현대식 IME 입력기)
* 설정(시스템 설정 앱, Windows+I)
* Voice access(윈도우 11 22H2)
* 날씨
* 그 외 지원 모듈(가상 데스크탑 알림 등)

사용시 주의 사항:

* 본 추가 기능은 윈도우 10 21H2(빌드 19044), 11 21H2(빌드 22000) 이상을 지원합니다.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* 윈도우 Enterprise LTSC(Long-Term Servicing Channel)와 윈도우 서버 버전에 설치할 수 있으나 지원은
  하지 않습니다.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* 윈도우 참가자 빌드에 탑제된 기능을 모두 지원하지 않습니다(특히 개발자 빌드에서 일부에게만 공개된 경우). 베타 체널 사용시 최신
  빌드(22623)만 지원합니다.
* 일부 추가 기능은 NVDA에 포함되었거나 추후 스크린 리더 버전에 반영될 수 있습니다.
* 여러 앱은 미니(compact overlay) 모드(예: 계산기)를 지원하지만 이 모드는 휴대용 NVDA를 사용시 제대로 사용할 수
  없습니다.
* 시작 메뉴 팝업 메뉴와 같이 웹 기술이 적용된 앱 사용시 NVDA 브라우즈 모드에 있는 "포커스 이동 시 자동 포커스 모드 전환"
  기능을 활성화하시기 바랍니다.

추가 기능 변경 내역은 [변경 내용 문서][3]에서 확인할 수 있습니다.

## 일반

* NVDA가 지원하는 UIA  이벤트 및 속성 외의 다음 이벤트 추적 가능: drag start/cancel/complete(state
  change로 인식), drag drop effect, is grabbed, drop target effect. 이 이벤트들은
  NVDA 2022.4에 추가됨.
* 가상 데스크탑을 열때/닫을때/변경시 NVDA가 데스크탑 이름(예: Desktop 2)를 출력하도록 함.
* 시작 메뉴에 고정된 타일(윈도우 10) 또는 액션 센터네 빠른 액션을 Alt+Shift+반향키로 조절시 "드래그중" 또는 드래그
  변화를 NVDA가 출력하도록 함(NVDA 2022.4에 본 기능이 추가됨).
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.
* In Windows 11 22H2 Moment 2, redesigned system tray overflow area can be
  detected properly when using mouse and/or touch interaction.

## Cortana

* Textual responses from Cortana are announced in most situations.
* NVDA will be silent when talking to Cortana via voice.

## 지도

* NVDA plays location beep for map locations.
* NVDA will no longer interupt speech when focused on items other than the
  map control in some cases.

## 현대식 키보드

현대식 키보드란 에모지 페널, 클립보드 히스토리, 받아쓰기, 하드웨어 입력 구성, 추천 엑션 및 현대식 IME 입력기를 말합니다. 에모지
탐색시 Unicode CLDR 설정을 활성하고 기호 읽기를 "일부" 이상으로 설정하시기 바랍니다. 윈도우 10에서 클립보드 히스토리
사용시 스페이스를 눌러 선택된 내용을 붙여넣으시기 바랍니다.

* 윈도우 10 에모지 페널에서 에모지 그룹(카오모지 및 기호 그룹 포함) 선택시 탐색 객체가 특정 에모지에 고정되는 문제 수정.
* 윈도우 11 클립보드 히스토리에서 항목 팝업 메뉴를 제대로 출력할 수 있도록 브라우즈 모드가 반영되지 않도록 함.
* 윈도우 11 22H2 Moment 1(10월) 이상에서 전화번호와 같은 내용이 클립보드에 복사되었을때 나타나는 추천 엑션을 출력하도록
  함.

## 설정 앱

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
