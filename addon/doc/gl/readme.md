# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* NVDA compatibility: 2022.2 and later

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
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Xente
* Opcións (opcións do sistema, Windows+I)
* Voice access (Windows 11 22H2)
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio

Notas:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Non se soportarán todas as características de versións Windows Insider
  Preview.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para entradas non listadas a continuación, podes asumir que as
  características forman parte do NVDA, que xa non aplican debido a que o
  complemento non soporta versións vellas de Windows 10, ou que se fixeron
  cambios nas apps que fan que as entradas xa non sexan aplicables.
* Algunhas apps soportan o modo de capa compacto (sempre enriba na
  Calculadora, por exemplo), e este modo non funcionará correctamente con
  versións portables de NVDA.
* Para a mellor experiencia con aplicacións que incrustan tecnoloxías web e
  con contido como o menú inicio e o seu menú de contexto, habilita a opción
  "Modo foco automático para cambios do foco" dende o panel de modo
  navegación das opcións de NVDA.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][3].

## Xeral

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag start/cancel/complete
  (recognized as state change event), drag drop effect, drag item is
  grabbed, drop target effect. With NVDA's log level set to debug, these
  events will be tracked and logged.
* Cando se abran, pechen, reordenen (Windows 11), ou se conmute entre
  escritorios virtuales, NVDA anunciará o nome do escritorio actual
  (escritorio 2, por exemplo).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. This is now part of
  NVDA 2022.4.
* Anuncios como o de cambios no volume/brillo no Explorador de Arquivos e o
  de notificacións de actualización de app da Microsoft Store pódense
  suprimir desactivando Anunciar Notificacións nas opcións de Presentación
  de Obxectos do NVDA.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* Item status changes are announced in more apps including Visual Studio
  Community 2022. This is now part of NVDA 2022.4.

## Cortana

* As respostas textuais de Cortana anúncianse na maioría de situacións.
* NVDA silenciarase cando lle fales ao Cortana a través da voz.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.

## Teclado Moderno

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* Cando se selecciona un grupo de emojis (incluindo kaomoji e grupos de
  símbolos en Windows 10), NVDA xa non moverá o navegador de obxectos a
  certos emojis.
* No historial do portapapeis de Windows 11, o modo exploración
  desactivarase por defecto, deseñado para permitir que NVDA anuncie os
  elementos do menú de entradas do historial do portapapeis.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* NVDA anunciará o nome do control para a actualización de calidade opcional
  se estiver presente (ligazón descargar e instalar agora en Windows 10 e
  botón descargar en Windows 11).
* En Windows 11, os elementos da barra de faragullas de pan recoñécense
  correctamente.
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

## O Tempo

* As pestanas como "pronósticos" e "mapas" recoñécense coma pestanas en si
  (parche de Derek Riemer).
* Cando se lea un pronóstico, usa as frechas esquerda e dereita para moverte
  entre elementos. Usa as frechas arriba e abaixo para ler os elementos
  individuais. Por exemplo, premendo a frecha dereita anunciaría "luns: 79
  graos, parcialmente nublado, ..." premendo a frecha abaixo dirá "luns"
  logo preméndoo de novo lerá o seguinte elemento (como a
  temperatura). Actualmente esto traballa para pronósticos diarios e
  horarios.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
