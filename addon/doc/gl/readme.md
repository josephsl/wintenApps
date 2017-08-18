# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento é unha coleción de app modules para varias aplicacións de
Windows 10, así coma correccións para certos controis de windows 10.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Alarmas e reloxo.
* Calendario
* Calculadora (modern).
* Cortana
* Barra de Xogos
* Groove Music
* Correo
* Mapas
* Microsoft Edge
* Xente
* Opcións (opcións do sistema, Windows+I)
* Skype (aplicación universal)
* Tenda
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Nota: este complemento require do Windows 10 Versión 1607 (build 14393) ou
posterior e do NVDA 2017.1 ou posterior. Para uns mellores resultados, usa o
complemento coa compilación estable máis recente (build 15063) e versión
estable máis recente do NVDA. Tamén, despois de cambiar as opcións de
actualización para o complemento, asegúrate de gardar a configuración do
NVDA.

Important note about NVDA 2017.3: due to backwards incompatible changes in
NVDA 2017.3, add-on version 17.09 and later will not work on NVDA versions
earlier than 2017.3.

## Xeral

* En menús de contexto para os mosaicos do Menú Inicio, os submenús
  recoñécense apropriadamente.
* Certain dialogs are now recognized as proper dialogs. These include
  Insider Preview dialog (settings app) and new-style UAC dialog in build
  14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and braille. This also
  includes Start menu search box. This is now part of NVDA as of 2017.3.
* NVDA pode anunciar conta de suxerencias cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no diálogo Presentación de Obxectos.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: Controller for, live region changed,
  system alert, element selected, window opened.
* Engadida a capacidade de procurar as actualizacións do complemento
  (automática ou manual) a través do novo diálogo Windows 10 App Essentials
  que se atopa no menú Preferencias do NVDA. Por defecto, procuraranse as
  actualizacións para as versións estable e de desenvolvementeo
  automáticamente semanal ou diáriamente, respectivamente.
* Capacidade para seguir eventos que cheguen dende aplicacións Universal
  Windows Platform (UWP) se o NVDA se está a executar co rexistro de
  depuración habilitado.
* Support for floating Emoji input panel in Fall Creators Update (for best
  experience when reading emojis, use Windows OneCore speech synthesizer).
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases. Most of the scenarios are now part of NVDA
  2017.3.
* Toasts are no longer announced multiple times in Creators Update and
  later. This fix is included in NVDA 2017.3.

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

## Barra de Xogos

* NVDA anunciará a aparición da ventá Barra de Xogos. Debido a limitacións
  técnicas, o NVDA non pode interactuar compretamente coa Barra de Xogos.

## Groove Music

* Agora detéctase a aparición de suxerencias cando se procuran pistas.

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

* Notifications such as file downloads and various webpage alerts are now
  announced. Most of these scenarios are now part of NVDA 2017.3.

## Xente

* Cando se procuren contactos, reproducirase un son se hai resultados da
  busca.

## Opcións

* Certain information such as Windows Update progress is now reported
  automatically. NVDA itself will handle majority of cases in 2017.3.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found. This is now
  done from NVDA in 2017.3.
* Os grupos de opcións recoñécense ao se usar a navegación de obxectos para
  navegar entre controis.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes. Value change fix is included in NVDA 2017.3.

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
* Appearance of search suggestions are now announced. This is now part of
  NVDA 2017.3.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress. A basic fix is now part of NVDA
  2017.3.

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
