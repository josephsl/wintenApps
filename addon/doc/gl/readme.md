# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: 2021.3 en diante

Nota: Orixinalmente chamado Windows 10 App Essentials, renomeouse a windows
App Essentials en 2021 para soportar windows 10 e versións futuras como
Windows 11. Parte deste complemento aínda se referirá ó seu nome antigo.

Este complemento é unha coleción de app modules para varias aplicacións de
Windows, así como melloras e correccións para certos controis de windows 10
e posteriores.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Calculadora
* Cortana
* Correo
* Mapas
* Microsoft Solitaire Collection
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Bloc de notas (Windows 11)
* Xente
* Opcións (opcións do sistema, Windows+I)
* Voice access (Windows 11)
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio

Notas:

* This add-on requires Windows 10 21H1 (build 19043), Windows 11 21H2 (build
  22000) or later.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
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

* Ademais dos manexadores de eventos UIA proporcionados por NVDA,
  recoñécense os eventos e as propiedades UIA seguintes: drag complete, drag
  drop effect, drop target dropped. co nivel de rexistro de NVDA establecido
  en depuración, estes eventos seguiranse e rexistraranse.
* Cando se abran, pechen, reordenen (Windows 11), ou se conmute entre
  escritorios virtuales, NVDA anunciará o nome do escritorio actual
  (escritorio 2, por exemplo).
* Ao ordear as entradas fixadas (tarxetas en Windows 10) do menú inicio ou
  as accións rápidas do centro de accións con Alt+Shift+teclas de frechas,
  NVDA anunciará información sobre os elementos arrastrados ou da nova
  posición dos mesmos.
* Anuncios como o de cambios no volume/brillo no Explorador de Arquivos e o
  de notificacións de actualización de app da Microsoft Store pódense
  suprimir desactivando Anunciar Notificacións nas opcións de Presentación
  de Obxectos do NVDA.
* En versións de Windows 11 Insider Preview, o estado do conmutador de
  silencio do micrófono (Windows+Alt+K) anúnciase desde calquera sitio.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and
  later. This is now part of NVDA 2022.1.
* NVDA will once again announce search result details in Start menu. This is
  now part of NVDA 2022.2.
* In Windows 11, Taskbar items and other shell user interface elements can
  be detected properly when using mouse and/or touch interaction. This is
  now part of NVDA 2022.2.

## Calculadora

* En Windows 10, o historial e os elementos da lista da memoria están
  correctamente etiquetados. Isto agora é parte de NVDA 2022.1.
* NVDA will announce calculator display content when performing scientific
  mode commands such as trigonometry operations. This is now part of NVDA
  2022.2.

## Cortana

* As respostas textuais de Cortana anúncianse na maioría de situacións.
* NVDA silenciarase cando lle fales ao Cortana a través da voz.

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe. Téñase en
  conta que a navegación entre fileiras(mensaxes) non se soporta.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.

## Microsoft Solitaire Collection

* NVDA anunciará os nomes das tarxetas e das pías de tarxetas.

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
* En Windows 11,, volve a ser posible utilizar as frechas para revisar
  emojis cando se abre o panel de emojis. Isto agora é parte de NVDA 2022.1.
* No historial do portapapeis de Windows 11, o modo exploración
  desactivarase por defecto, deseñado para permitir que NVDA anuncie os
  elementos do menú de entradas do historial do portapapeis.
* In Insider Preview build 25115, NVDA will announce suggested actions when
  compatible data such as phone numbers is copied to the clipboard.

## Bloc de Notas

Isto refírese á versión 11 ou posterior do Bloc de Notas de Windows 11.

* NVDA will announce status items such as line and column information when
  report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in
  laptop layout) is performed. This is now part of NVDA 2022.2.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* Corrixiuse as etiquetas de controis extrañas advertidas en certas
  instalacións de Windows.
* NVDA anunciará o nome do control para a actualización de calidade opcional
  se estiver presente (ligazón descargar e instalar agora en Windows 10 e
  botón descargar en Windows 11).
* En Windows 11, os elementos da barra de faragullas de pan recoñécense
  correctamente.
* In Windows 10, NVDA will interupt speech and report updates to Windows
  Update status as download and install progresses. This may result in
  speech interruption when navigating Settings app while updates are being
  downloaded and installed.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2 preview.

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
