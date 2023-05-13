# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Download [beta version][2]
* Descargar [versión de desenvolvemento][3]
* Compatibilidade con NVDA: 2023.1 e posterior

Nota: Orixinalmente chamado Windows 10 App Essentials, renomeouse a windows
App Essentials en 2021 para soportar windows 10 e versións futuras como
Windows 11. Parte deste complemento aínda se referirá ó seu nome antigo.

Este complemento é unha coleción de app modules para varias aplicacións de
Windows, así como melloras e correccións para certos controis de windows 10
e posteriores.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Cortana
* Mapas
* Teclado Moderno (panel de emoji/teclado táctil/ditado/escritura por
  voz/suxestións de entrada por hardware/historial do portapapeis/Accións
  Suxeridas/editores co método de entrada moderna)
* Opcións (opcións do sistema, Windows+I)
* Acceso por voz (Windows 11 22H2)
* O Tempo
* Módulos misceláneos para controis e características como os anuncios dos
  escritorios virtuais

Notas:

* Este complemento require do Windows 10 22H2 (compilación 19045), 11 21H2
  (compilación 22000), ou versións posteriores.
* O soporte das actualizacións de características está vencellado á duración
  do soporte ó consumidor (edicións Home, Pro, Pro Education, Pro for
  Workstations) e o complemento podería rematar o soporte para unha
  actualización de características antes do final do soporte ó
  consumidor. Consulta aka.ms/WindowsTargetVersioninfo para máis información
  e datas de soporte.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
* Se Add-on Updater está instalado e están activadas as actualizaciónes en
  segundo plano, Windows App Essentials non se instalará en absoluto en
  versións de Windows non soportadas.
* Not all features from Windows Insider Preview builds will be supported,
  more so for features introduced to a subset of Windows Insiders in canary
  and dev channels.
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

## Xeral

* Cando se abran, pechen ou se cambie entre escritorios virtuales, NVDA
  anunciará o nome do escritorio activo (escritorio 2, por exemplo).
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11) and reporting item position when moving through taskbar icons
  (Windows 10 and 11).
* In aps such as File Explorer and Notepad where tabbed windows are
  supported, NVDA will announce the name and the position of tabs when
  switching between them. This is now part of NVDA 2023.2.

## Cortana

* As respostas textuais de Cortana anúncianse na maioría de situacións.

## Mapas

* NVDA xa non interromperá a fala cando estea enfocado en elementos
  distintos do control do mapa nalgúns casos.

## Teclado Moderno

Isto inclúe o panel de Emoji, o historial do portapapeis, o teclado táctil,
o dictado/escritura por voz, as suxestións de entrada por hardware, as
accións suxeridas, e os editores co método de entrada moderna para certas
linguas tanto en windows 10 como 11. Ó ver emojis, para unha mellor
experiencia, habilita a opción Unicode Consortium nos axustes de voz do NvDA
e establece o nivel de símbolos en "algunha" ou superior. Ó pegar dende o
historial do portapapeis en Windows 10, preme a tecla Espazo no canto de
Intro para pegar o elemento seleccionado.

* En Windows 11 22H2 e posterior, NVDA anunciará accións suxeridas cando se
  copien ó portapapeis datos compatibles como números de teléfono.

## Opcións

* NVDA anunciará o nome do control para a actualización de calidade opcional
  se estiver presente (ligazón descargar e instalar agora en Windows 10 e
  botón descargar en Windows 11).
* En Windows 11, os elementos da barra de faragullas de pan recoñécense
  correctamente.
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and selective UIA event registration is on or set to selective,
  you must move focus to updates list as soon as they appear so NVDA can
  announce update progress.

## Acceso por voz

Esto se refiere a la característica Acceso por voz introducida en Windows 11
22H2.

* NVDA anunciará o estado do micrófono cando se active ou desactive o
  micrófono dende a interface de Acceso por voz.

## O Tempo

* As pestanas como "pronósticos" e "mapas" recoñécense coma pestanas en si
  (parche de Derek Riemer).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
