# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Alarmas e reloxo.
* Calendario
* Calculadora (modern).
* Cortana
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

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

## Xeral

* En menús de contexto para os mosaicos do Menú Inicio, os submenús
  recoñécense apropriadamente.
* Certain dialogs are now recognized as proper dialogs, including Insider
  Preview dialog (settings app).
* NVDA pode anunciar conta de suxerencias cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no diálogo Presentación de Obxectos.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: Controller for, live region changed,
  system alert, element selected, window opened. Co NVDA configurado para
  executarse co rexistro de depuración habilitado, estos eventos seguiranse.
* Added ability to check for add-on updates (automatic or manual) via
  Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.

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
* NVDA will be silent when talking to Cortana via voice.
* NVDA agora anunciará a confirmación de lembrarse despois de que axustes
  unha.

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

* Notifications such as file downloads and various webpage alerts are
  announced.

## Teclado Moderno

* Soporte para o panel flotante de entrada de Emoji na actualización 1709
  Fall Creators  (para uns mellores resultados lendo emojis, usa o
  sintetizador de voz Windows OneCore).
* Soporte para suxerencias de entrada de teclado hardware na compilación
  17040 e posterior.

## Xente

* Cando se procuren contactos, reproducirase un son se hai resultados da
  busca.

## Opcións

* Certain information such as Windows Update progress is reported
  automatically.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* Os grupos de opcións recoñécense ao se usar a navegación de obxectos para
  navegar entre controis.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Os pitidos da barra de progreso do volume de audio xa non se escoitan na
  compilación 17035 e posterior.

## Skype

* Ao teclear o indicador de texto anúnciase só coma cliente Skype para
  Escritorio.
* Volta parcial das ordes Control+NVDA+fila de números para ler o histórico
  de chats recentes e para mover o navegador de obxectos a entradas de chat
  como Skype para Escritorio.
* Agora podes premer Alt+fila de números para localizar e mover a
  conversacións (1), listaxe de contactos (2), bots (3) e campo de edición
  do chat (4). Ten en conta que estas ordes funcionarán apropriadamente se
  está instalada a actualización do Skype liberada en Marzo do 2017.
* Anúncianse as etiquetas das caixas combinadas para a aplicación Skype
  preview liberada en novembro do 2016.
* NVDA xa non anuncia "Mensaxe Skype" cando se revisen mensaxes para a
  maioría dos casos.
* Arranxados varios problemas ao se usar Skype con pantallas braille,
  incluindo a incapacidade para revisar os elementos do historial de
  mensaxes en braille.
* Dende a listaxe do historial de mensaxes, premendo NVDA+D sobre un
  elemento de mensaxe agora permitirá ao NVDA anunciar información detallada
  acerca dunha mensaxe como tipo de canle, data e hora de envío e
  semellante.

## Tenda

* Despois de buscar actualizacións das aplicacións, os nomes das aplicacións
  na lista de aplicacions actualizarán as etiquetas correctamente.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

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
