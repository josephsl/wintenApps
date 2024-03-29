# Windows App Essentials #

* 저자: Joseph Lee(이성원), Derek Riemer 외 다수

참고: 윈도우 10 이상(특히 윈도우 11)을 지원하기 위해 2021년에 Windows 10 App Essentials에서 Windows
App Essentials로 변경되었습니다. 단 특정 부분에서는 옛 이름이 뜰 수 있습니다.

본 추가 기능은 여러 UWP 윈도우 앱 지원 모듈 및 윈도우 10 이상에서 제공하는 컨트롤 지원 기능 향상 및 버그 수정을 포함합니다.

다음 앱 모듈 및 지원 모듈을 포함합니다(각 앱 관련 엔트리를 참고 바람):

* 현대식 키보드
* 설정(Windows+I)

사용시 주의 사항:

* 본 추가 기능은 64비트 윈도우 10 22H2(빌드 19045), 11 22H2(빌드 22621) 이상을 지원합니다.
* 기능 업데이트 지원일은 일반 사용자 버전(Home, Pro, Pro Education, Pro for Workstations)을
  기준으로 하며 지원 종료전 추가 기능 자체에서 기능 업데이트 지원을 종료할 수 있습니다. 자세한 정보 및 기능 업데이트 지원에
  대해서는 <https://aka.ms/WindowsTargetVersioninfo>를 참고하시기 바랍니다.
* 윈도우 Enterprise LTSC(Long-Term Servicing Channel)와 윈도우 서버 버전에 설치할 수 있으나 지원은
  하지 않습니다.
* 윈도우 참가자 빌드에 탑제된 기능을 모두 지원하지 않습니다(특히 카나리아 및 개발자 빌드에서 일부에게만 공개된 경우).
* The add-on may emulate changes included in Insider Preview builds which
  are subsequently removed, and for these changes, the add-on may remove
  them in future releases.
* 추가 기능 개발자(dev)체널은 베타 및 일반 업데이트 체널에 포함되지 않을 실험적 기능을 포함할 수 있으며 베타 체널 사용시 일반
  사용자 체널에 포함될 기능을 미리 체험할 수 있습니다.
* 일부 추가 기능은 NVDA에 포함되었거나 추후 스크린 리더 버전에 반영될 수 있습니다.
* 시작 메뉴 팝업 메뉴와 같이 웹 기술이 적용된 앱 사용시 NVDA 브라우즈 모드에 있는 "포커스 이동 시 자동 포커스 모드 전환"
  기능을 활성화하시기 바랍니다.

추가 기능 변경 내역은 [변경 내용 문서][1]에서 확인할 수 있습니다.

## 일반

* In Windows 11 24H2 Insider Preview builds, quick settings (shellhost.exe)
  interface elements can be navigated using mouse and/or touch interaction.

## 현대식 키보드

현대식 키보드란 에모지 페널, 클립보드 히스토리, 터치 키보드, 받아쓰기, 하드웨어 입력 구성, 추천 엑션 및 현대식 IME 입력기를
말합니다. 에모지 탐색시 Unicode CLDR 설정을 활성하고 기호 읽기를 "일부" 이상으로 설정하시기 바랍니다. 윈도우 10에서
클립보드 히스토리 사용시 스페이스를 눌러 선택된 내용을 붙여넣으시기 바랍니다.

* 윈도우 11에서 전화번호와 같은 내용이 클립보드에 복사되었을때 나타나는 추천 엑션을 출력하도록 함(NVDA 2024.2에 포함됨).

## 설정(Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
