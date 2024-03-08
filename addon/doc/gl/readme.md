# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Download [beta version][2]
* Descargar [versión de desenvolvemento][3]
* Compatibilidade con NVDA: 2023.3.4 e posterior

Nota: Orixinalmente chamado Windows 10 App Essentials, renomeouse a windows
App Essentials en 2021 para soportar windows 10 e versións futuras como
Windows 11. Parte deste complemento aínda se referirá ó seu nome antigo.

Este complemento é unha coleción de app modules para varias aplicacións de
Windows, así como melloras e correccións para certos controis de windows 10
e posteriores.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Teclado Moderno
* Opcións (opcións do sistema, Windows+I)

Notas:

* Este complemento require do Windows 10 22H2 (compilación 19045), 11 22H2
  (compilación 22621), ou versións posteriores.
* Feature update support duration is tied to consumer support duration
  (Home, Pro, Pro Education, Pro for Workstations editions) and the add-on
  may end support for a feature update prior to end of consumer support. See
  <https://aka.ms/WindowsTargetVersioninfo> for more information and support
  dates.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
* Non se soportarán todas as características de versións Windows Insider
  Preview, máis aínda para as características introducidas nun subconxunto
  de Insiders Windows na canle de desenvolvemento (dev).
* The add-on may emulate changes included in Insider Preview builds which
  are subsequently removed, and for these changes, the add-on may remove
  them in future releases.
* Add-on dev channel will include changes including experimental content
  that may or may not be included in beta and stable releases, and beta
  channel will come with changes planned for future stable releases.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para a mellor experiencia con aplicacións que incrustan tecnoloxías web e
  con contido como o menú inicio e o seu menú de contexto, habilita a opción
  "Modo foco automático para cambios do foco" dende o panel de modo
  navegación das opcións de NVDA.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][4].

## Teclado Moderno

Isto inclúe o panel de Emoji, o historial do portapapeis, o teclado táctil,
o dictado/escritura por voz, as suxestións de entrada por hardware, as
accións suxeridas, e os editores co método de entrada moderna para certas
linguas tanto en windows 10 como 11. Ó ver emojis, para unha mellor
experiencia, habilita a opción Unicode Consortium nos axustes de voz do NvDA
e establece o nivel de símbolos en "algunha" ou superior. Ó pegar dende o
historial do portapapeis en Windows 10, preme a tecla Espazo no canto de
Intro para pegar o elemento seleccionado.

* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Opcións

* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
