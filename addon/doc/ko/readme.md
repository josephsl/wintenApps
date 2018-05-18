# Windows 10 App Essentials #

* 저자: Joseph Lee(이성원), Derek Riemer 외 윈도우 10 사용자들
* [출시 버전][1]
* [개발 버전][2]

본 추가 기능은 여러 윈도우 10 앱 지원 모듈 및 윈도우 10 컨트롤 지원 기능 향상 및 비그 수정을 포함합니다.

다음 앱 모듈 및 지원 모듈을 포함합니다(각 앱 관련 엔트리를 참고 바람):

* 알람 및 시계
* 달력
* 계산기(UWP)
* Cortana
* Feedback Hub
* Game Bar
* 메일
* 지도
* Microsoft Edge
* 현대식 터치 키보드(에모지 페널/하드웨어 입력 구성, 버전 1709 이상)
* People
* 설정(시스템 설정 앱, Windows+I)
* 스카이프(UWP)
* Store
* 날씨
* 그 외 지원 모듈(시작 메뉴 타일 지원 등)

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2018.1 or later. For best results, use the add-on with latest
Windows 10 stable releases (build 16299 or 17134) and latest stable version
of NVDA. Also, after changing update settings for the add-on, be sure to
save NVDA settings.

## 일반

* 시작 메뉴 타일의 팝업 메뉴내 하위 메뉴가 제대로 인식되도록 함.
* 여러 대화상자 컨트롤(예: 설정 앱 내 윈도우 참가자 프로그램 대화상자)이 대화상자로 인식되지 않던 문제 수정.
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog/panel.
* 특정 팝업 메뉴(예: Edge 설정 메뉴) 탐색시 항목 위치(예: 1/2)가 출력되지 않도록 함.
* 다음 UIA 이벤트 추적 가능: Controller for, drag start, drag cancel, drag complete,
  element selected, live region change, notification, system alert, tooltip
  opened, window opened. NVDA가 디버그 로깅 상태로 재시작된 경우 위 이벤트가 추적되며 notification
  이벤트는 추가 디버그 정보가 출력되도록 함.
* 추가 기능 업데이트 확인 기능 추가(Windows 10 App Essentials 설정에서 조절할 수 있음). 기본적으로 출시 버전은
  일주일에 한번씩, 개발 버전은 매일 업데이트를 확인하도록 함.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. Due to technical limitations, this feature
  works properly with NVDA 2018.1 and later, and will be part of NVDA with
  2018.2 release.
* Tooltips from Edge and universal apps are recognized and will be
  announced.
* NVDA will no longer announce "unknown" when opening quick link menu
  (Windows+X). This fix will be part of NVDA 2018.2.
* In build 17627 and later, when opening a new Sets tab (Control+Windows+T),
  NVDA will announce search results when searching for items in the embedded
  Cortana window.
* When switching between Sets tabs, NvDA will announce name and position of
  the tab you are switching to.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop ID (desktop 2, for example).

## Alarms and clock

* Time picker values are now announced, noticeable when moving focus to
  picker controls. This also affects the control used to select when to
  restart to finish installing Windows updates.

## Calculator

* When ENTER or Escape is pressed, NVDA announces calculation results.
* For calculations such as unit converter and currency converter, NVDA will
  announce results as soon as calculations are entered.

## calendar

* NVDA no longer announces "edit" or "read-only" in message body and other
  fields.

## Cortana

* Textual responses from Cortana are announced in most situations (if it
  doesn't, reopen Start menu and try searching again).
* NVDA will be silent when talking to Cortana via voice.
* NVDA will now announce reminder confirmation after you set one.

## Feedback Hub

* For newer app releases, NVDA will no longer announce feedback categories
  twice.

## Game Bar

* NVDA will announce appearance of Game Bar window. Due to technical
  limitations, NVDA cannot interact fully with Game Bar.

## 메일

* When reviewing items in messages list, you can now use table navigation
  commands to review message headers.
* When writing a message, appearance of at mention suggestions are indicated
  by sounds.

## 지도

* NVDA plays location beep for map locations.
* When using street side view and if "use keyboard" option is enabled, NVDA
  will announce street addresses as you use arrow keys to navigate the map.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are
  announced.

## Modern keyboard

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in build 17661 and later. For best
  experience when reading emojis, use Windows OneCore speech synthesizer.
* Support for hardware keyboard input suggestions in Version 1803 (April
  2018 Update) and later.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens.

## People

* When searching for contacts, a sound will play if there are search
  results.

## Settings

* Certain information such as Windows Update progress is reported
  automatically.
* Progress bar values and other information are no longer announced twice.
* Settings groups are recognized when using object navigation to navigate
  between controls.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.

## Skype

* Typing indicator text is announced just like Skype for Desktop client.
* Partial return of Control+NvDA+number row commands to read recent chat
  history and to move navigator object to chat entries just like Skype for
  Desktop.
* You can now press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* Combo box labels for Skype preview app released in November 2016 are
  announced.
* NVDA will no longer announce "Skype Message" when reviewing messages for
  majority of cases.
* Various issues when using Skype with braille displays fixed, including
  inability to review message history items in braille.
* From message history list, pressing NVDA+D on a message item will now
  allow NVDA to announce detailed information about a message such as
  channel type, sent date and time and so on.

## Store

* After checking for app updates, app names in list of apps to be updated
  are correctly labeled.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Weather

* Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by
  Derek Riemer).
* when reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
