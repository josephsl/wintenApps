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

Nota: este complemento require do Windows 10 Versión 1607 (build 14393) ou
posterior e do NVDA 2017.3 ou posterior. Para uns mellores resultados, usa o
complemento coa compilación estable máis recente (build 16299) e versión
estable máis recente do NVDA. Tamén, despois de cambiar as opcións de
actualización para o complemento, asegúrate de gardar a configuración do
NVDA.

## Xeral

* En menús de contexto para os mosaicos do Menú Inicio, os submenús
  recoñécense apropriadamente.
* Agora recoñécense certos diálogos como proprios diálogos. Esto inclúe o
  diálogo Insider Preview (settings app) e o diálogo de novo estilo do UAC
  na compilación 14328 e anteriores para o NVDA 2016.2.1 e anteriores.
* NVDA pode anunciar conta de suxerencias cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no diálogo Presentación de Obxectos.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: Controller for, live region changed,
  system alert, element selected, window opened. Co NVDA configurado para
  executarse co rexistro de depuración habilitado, estos eventos seguiranse.
* Engadida a capacidade de procurar as actualizacións do complemento
  (automática ou manual) a través do novo diálogo Windows 10 App Essentials
  que se atopa no menú Preferencias do NVDA. Por defecto, procuraranse as
  actualizacións para as versións estable e de desenvolvementeo
  automáticamente semanal ou diáriamente, respectivamente.
* Nalgunhas aplicacións, anúnciase o texto en rexións vivas. Esto inclúe
  alertas en Edge, na calculadora e noutros. Ten en conta que esto poderá
  causar unha fala por duplicado nalgúns casos. A maioría dos escenarios son
  agora parte do NVDA 2017.3.

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

* Agora anúncianse notificacións como descargas de ficheiros e varias
  alertas de páxina web. A maioría de estos escenarios forman parte do NVDA
  2017.3

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

* Certa información como o progreso da Actualización de Windows agora é
  anunciada automáticamente. O NVDA manexará por si mesmo a maioría dos
  casos na 2017.3.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* Se está a tomar un tempo para procurar unha configuración, NVDA anunciará
  "buscando" e o resultado do estado da procura como se unha opción non se
  poidera atopar. Agora esto faise dende o NVDA na 2017.3.
* Os grupos de opcións recoñécense ao se usar a navegación de obxectos para
  navegar entre controis.
* Para algunhas caixas combinadas, NVDA xa non fallará ao recoñecer
  etiquetas e/ou ao anunciar cambios de valores. O arranxo do cambio de
  valor inclúese no NVDA 2017.3.
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
* Agora anúnciase a aparición de suxerencias de procura. Esto é agora parte
  do NVDA 2017.3.
* Cando se cargue contido como aplicacións e películas, NVDA anunciará o
  nome do producto e o progreso da descarga. Un arranxo básico é agora parte
  do NVDA 2017.3

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
