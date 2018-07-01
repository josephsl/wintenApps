# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento é unha coleción de app modules para varias aplicacións de
Windows 10, así coma melloras e correccións para certos controis de windows
10.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Alarmas e reloxo.
* Calendario
* Calculadora (modern).
* Cortana
* Centro de Opinións
* Barra de Xogos
* Correo
* Mapas
* Microsoft Edge
* Teclado Moderno (suxerencias de panel emoji /entrada hardware na Versión
  1709 e posterior)
* Xente
* Opcións (opcións do sistema, Windows+I)
* Skype (aplicación universal)
* Tenda
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Notas:

* This add-on requires Windows 10 Version 1709 (build 16299) or later and
  NVDA 2018.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 17134) and latest stable version of NVDA.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support old Windows 10
  releases, or changes were made to apps that makes entries no longer
  applicable.

For a list of changes made between each add-on releases, refer to
[changelogs for add-on releases][3] document.

## Xeral

* En menús de contexto para os mosaicos do Menú Inicio, os submenús
  recoñécense apropriadamente.
* Certain dialogs are now recognized as proper dialogs and reported as such,
  including Insider Preview dialog (settings app).
* NVDA pode anunciar conta de suxerencias cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no diálogo/panel Presentación de Obxectos.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* The following UIA events are recognized: active text position change
  (Redstone 5), controller for, drag start, drag cancel, drag complete,
  element selected, live region change, notification, system alert, tooltip
  opened, window opened. With NVDA set to run with debug logging enabled,
  these events will be tracked, and for UIA notification event, a debug tone
  will be heard.
* Engadida a capacidade de procurar as actualizacións do complemento
  (automática ou manual) a través do diálogo Windows 10 App Essentials que
  se atopa no menú Preferencias do NVDA. Por defecto, procuraranse as
  actualizacións para as versións estable e de desenvolvementeo
  automáticamente semanal ou diáriamente, respectivamente.
* Nalgunhas aplicacións, anúnciase o texto en rexións vivas. Esto inclúe
  alertas en Edge, na calculadora e noutros. Ten en conta que esto poderá
  causar unha fala por duplicado nalgúns casos.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced.
* recoñeceranse e anunciaranse os consellos para o Edge e para as
  aplicacións universais.
* Na compilación 17627 e posterior, cando se abra unha nova lapela de
  conxuntos (ctrl+windows+T), NVDA anunciará os resultados da busca cando se
  procuren elementos na ventá incrustada de Cortana.
* Cando se cambie de lapela de Conxuntos, NVDA anunciará o nome e a posición
  da lapela cara á cal se conmutou.
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o ID do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.

## Alarmas e reloxo

* Agora anúncianse os valores do selector de hora. Esto tamén afecta ó
  control usado para selecionar cando reiniciar para rematar a instalación
  das actualizacións de Windows.

## Calculadora

* Cando se prema INTRO ou Escape, NVDA anuncia os resultados do cálculo.
* Para cálculos coma conversión de unidades e conversión de moneda, o NVDA
  anunciará os resultados tan pronto coma os cálculos se introduzan.

## calendario

* NVDA xa non anuncia "editar" ou "só lectura" para asuntos da cita no
  Calendario e no contido do mensaxe no Correo.

## Cortana

* As respostas testuais de Cortana anúncianse na mayoría das situacións(se
  non se reabre o menú inicio e téntase a procura de novo).
* NVDA silenciarase cando lle fales ao Cortana a través da voz.
* NVDA agora anunciará a confirmación de lembrarse despois de que axustes
  unha.

## Centro de Opinións

* En novas versións da app, NVDA non lerá as categorías de comentarios dúas
  veces.

## Barra de Xogos

* NVDA anunciará a aparición da ventá Barra de Xogos. Debido a limitacións
  técnicas, o NVDA non pode interactuar compretamente coa Barra de Xogos.

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe.
* Cando se escrebe unha mensaxe, a apariencia da mención de suxerencias
  indícase con sons.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.
* Cando se usa a vista lateral da rúa e se a opción "usar teclado" está
  habilitada, NVDA anunciará os enderezos das rúas según utilices as teclas
  das frechas para navegar polo mapa.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts, as well
  as availability of Reading View (if using Version 1709 and later) are
  announced.

## Teclado Moderno

* Soporte para o panel flotante de entrada de Emoji na actualización 1709
  Fall Creators en adiante, incluindo o panel redeseñado na compilación
  17661. Para uns mellores resultados lendo emojis, usa o sintetizador de
  voz Windows OneCore.
* Soporte para suxerencias de entrada de teclado hardware na versión 1803
  (actualización de abril de 2018) e posterior.
* Nas versións posteriores á 1709, o NVDA anunciará o primeiro emoji
  selecionado cando se abra o panel de emoji.
* Soporte para o anunciado de elementos do cloud clipboard na compilación
  17666 (Redstone 5) e posterior.
* Reduced unnecessary verbosity when working with modern keyboard and its
  features. These include no longer announcing "Microsoft Candidate UI" when
  opening hardware keyboard input suggestions and staying silent when
  certain touch keyboard keys raise name change event on some systems.

## Xente

* Cando se procuren contactos, reproducirase un son se hai resultados da
  busca.

## Opcións

* Certa información como o progreso da Actualización de Windows agora é
  anunciada automáticamente.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* Os grupos de opcións recoñécense ao se usar a navegación de obxectos para
  navegar entre controis.
* Para algunhas caixas combinadas, NVDA xa non fallará ao recoñecer
  etiquetas e/ou ao anunciar cambios de valores. 
* Os pitidos da barra de progreso do volume de audio xa non se escoitan na
  versión 1803 e posterior.
* More messages about Windows Update status are announced, especially if
  Windows Update encounters errors.

## Skype

* Ao teclear o indicador de texto anúnciase só coma cliente Skype para
  Escritorio.
* Control+NvDA+number row commands, used to read recent chat history and to
  move navigator object to chat entries in Skype for Desktop, is also
  available in Skype UWP.
* You can press Alt+number row to locate and move to conversations (1),
  contacts list (2), bots (3) and chat edit field if visible (4). Note that
  these commands will work properly if Skype update released in March 2017
  is installed.
* NVDA xa non anuncia "Mensaxe Skype" cando se revisen mensaxes para a
  maioría dos casos.
* From message history list, pressing NVDA+D on a message item will allow
  NVDA to announce detailed information about a message such as channel
  type, sent date and time and so on.

## Tenda

* Despois de buscar actualizacións das aplicacións, os nomes das aplicacións
  na lista de aplicacions actualizarán as etiquetas correctamente.
* Cando se cargue contido como aplicacións e películas, NVDA anunciará o
  nome do producto e o progreso da descarga.

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
