# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros

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
* Opcións (Windows+I)

Notas:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* O soporte das actualizacións de características está vencellado á duración
  do soporte ó consumidor (edicións Home, Pro, Pro Education, Pro for
  Workstations) e o complemento podería rematar o soporte para unha
  actualización de características antes do final do soporte ó
  consumidor. Consulta <https://aka.ms/WindowsTargetVersioninfo> para máis
  información e datas de soporte.
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
documento [rexistros de trocos para publicacións de complementos][1].

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

## Opcións (Windows+I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
