# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Baixe a [versão estável][1]
* Download [beta version][2]
* Download [development version][3]
* NVDA compatibility: 2023.1 and later

Nota: Originalmente chamado de Windows 10 App Essentials, foi renomeado para
Windows App Essentials em 2021 para oferecer suporte ao Windows 10 e versões
futuras, como Windows 11. Partes deste complemento ainda farão referência ao
nome do complemento original.

Este complemento é uma coleção de módulos de aplicativos (app modules) para
vários aplicativos modernos do Windows, bem como aprimoramentos e correções
para determinados controles encontrados no Windows 10 e posteriores.

Os seguintes módulos de aplicativos ou módulos de suporte para alguns
aplicativos estão incluídos (consulte a seção de cada aplicativo para obter
detalhes sobre o que está incluso):

* Cortana
* Mapas
* Modern keyboard (emoji panel/touch keyboard/dictation/voice
  typing/hardware input suggestions/clipboard history/Suggested
  Actions/modern input method editors)
* Configurações (configurações do sistema, Windows+I)
* Voice access (Windows 11 22H2)
* Clima
* Miscellaneous modules for controls and features such as virtual desktops
  announcements

Notas:

* This add-on requires Windows 10 22H2 (build 19045), 11 21H2 (build 22000),
  or later releases.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  aka.ms/WindowsTargetVersioninfo for more information and support dates.
* Embora a instalação seja possível, este complemento não oferece suporte
  para Windows Enterprise LTSC (Long-Term Servicing Channel — Canal de
  Manutenção de Longo Prazo) e versões do Windows Server.
* If Add-on Updater is installed and background add-on updates is enabled,
  Windows App Essentials will not install at all on unsupported Windows
  releases.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in canary
  and dev channels.
* Add-on dev channel will include changes including experimental content
  that may or may not be included in beta and stable releases, and beta
  channel will come with changes planned for future stable releases.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][4] document.

## Geral

* When opening, closing, or switching between virtual desktops, NVDA will
  announce active virtual desktop name (desktop 2, for example).
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11) and reporting item position when moving through taskbar icons
  (Windows 10 and 11).
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them. This is now part of NVDA 2023.2.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.

## Mapas

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

* In Windows 11 22H2 and later, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Configurações

* O NVDA anunciará o nome do controle de atualização de qualidade opcional,
  se houver (link para baixar e instalar agora no Windows 10, botão de
  download no Windows 11).
* No Windows 11, os itens da barra de localização atual são reconhecidos
  corretamente.
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and selective UIA event registration is on or set to selective,
  you must move focus to updates list as soon as they appear so NVDA can
  announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice
  access interface.

## Clima

* Abas como "previsão" e "mapas" são reconhecidas como guias adequadas
  (patch de Derek Riemer).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
