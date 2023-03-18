# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* Compatibilidade com o NVDA: 2022.4 e superiores

Nota: Originalmente chamado Windows 10 App Essentials, foi renomeado para
Windows App Essentials em 2021 para suportar o Windows 10 e futuros
lançamentos como o Windows 11. Partes deste extra continuarão a referir-se
ao nome original do extra.

Este extra é uma colecção de módulos de aplicação para várias aplicações
modernas do Windows, bem como melhorias e correcções para certos controlos
encontrados no Windows 10 e posteriores.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Cortana
* Mapas.
* Modern keyboard (emoji panel/touch keyboard/dictation/voice
  typing/hardware input suggestions/clipboard history/Suggested
  Actions/modern input method editors)
* Configurações (configurações do sistema, Windows + I)
* Voice access (Windows 11 22H2)
* Meteorologia
* Miscellaneous modules for controls and features such as virtual desktops
  announcements

Notas:

* Este extra requer o Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  ou posterior.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Embora a instalação seja possível, este suplemento não suporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) e versões Windows Server.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in canary
  and dev channels.
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with the portable version
  of NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Para obter uma lista de alterações feitas entre cada release do extra,
consulte o documento [changelogs for releases, release][3].

## Geral

* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* In Windows 11, NVDA will announce search highlights in Start menu when it
  opens. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, mouse and/or touch interaction can be used
  to interact with redesigned system tray overflow window and Open With
  dialog. This is now part of NVDA 2023.1.
* NVDA will record processor architecture for the current Windows
  installation (x86/32-bit, AMD64, ARM64) when it starts. This is now part
  of NVDA 2023.1.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11 prior to build 25267) and reporting item position when moving
  through taskbar icons (Windows 10 and 11 prior to build 25281).
* NVDA will announce empty folder text inside an empty folder in File
  Explorer.
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.

## Mapas.

* NVDA will no longer interrupt speech when focused on items other than the
  map control in some cases.

## Teclado moderno

This includes emoji panel, clipboard history, touch keyboard,
dictation/voice typing, hardware input suggestions, suggested actions, and
modern input method editors for certain languages across Windows 10 and
11. When viewing emojis, for best experience, enable Unicode Consortium
setting from NVDA's speech settings and set symbol level to "some" or
higher. When pasting from clipboard history in Windows 10, press Space key
instead of Enter key to paste the selected item.

* In Windows 10 emoji panel, when an emoji group (including kaomoji and
  symbols group) is selected, NVDA will no longer move navigator object to
  certain emojis.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu
  items. This is now part of NVDA 2023.1.
* In Windows 11 22H2 and later, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Configurações

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

## Meteorologia

* Separadores como "previsão" e "mapas" são reconhecidos como separadores
  adequados (patch de Derek Riemer).
* Ao ler uma previsão, use as setas esquerda e direita para se mover entre
  os itens. Use as setas para cima e para baixo para ler os itens
  individuais. Por exemplo, se pressionar a seta para a direita, poderá ler
  "Segunda-feira: 20 graus, parcialmente nublado, ...", se pressionar a seta
  para baixo, dirá "Segunda-feira" e, em seguida, se pressionar novamente,
  lerá o próximo item (Como a temperatura). Isto funciona actualmente para
  previsões diárias e horárias.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=wintenApps

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
