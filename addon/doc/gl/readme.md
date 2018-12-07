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

* Centro de accións
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

* Este complemento require do Windows 10 Versión 1709 (build 16299) ou
  posterior e do NVDA 2018.3 ou posterior. Para uns mellores resultados, usa
  o complemento coa compilación estable máis recente (build 17763) e versión
  estable máis recente do NVDA.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para entradas non listadas a continuación, podes asumir que as
  características forman parte do NVDA, que xa non aplican debido a que o
  complemento non soporta versións vellas de Windows ou que se fixeron
  cambios nas apps que fan que as entradas xa non sexan aplicables.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][3].

## Xeral

* Trocos internos para facer ó complemento compatible con versións futuras
  do NVDA.
* Se o complemento Actualizador de Complementos está instalado, ese
  complemento verificará as actualizacións do Windows 10 App Essentials.
* O intervalo por defecto para verificar actualizacións cambiou a
  verificacións semanais tanto para versións estables e de
  desenvolvemento. Isto aplícase só se o propio complemento verifica as
  actualizacións.
* Cando o complemento estea configurado para verificar actualizacións, ao
  actualizar o complemento se a nova liberación require unha versión nova do
  NVDA presentarase unha mensaxe de erro.
* Pequenos cambios en como se presentan algunhas mensaxes en linguas
  diferentes do inglés.
* Os elementos de submenú recoñécense adecuadamente en varias apps,
  incluíndo elementos do menú de contexto nas tarxetas do menú inicio e o
  menú da aplicación Microsoft Edge (Restone 5).
* Agora recoñécense certos diálogos como proprios diálogos. Esto inclúe o
  diálogo Insider Preview (settings app). Isto incluirase co NVDA 2018.3.
* NVDA pode anunciar conta de suxerencias cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no diálogo/panel Presentación de Obxectos.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, element selected, live region change, notification,
  system alert, tooltip opened, window opened. Co NVDA configurado para
  executarse co rexistro de depuración habilitado, estos eventos seguiranse
  e, no caso do evento UIA notification oirase un ton se as notificacións
  veñen de calquera lugar que non sexa a app actualmente activa.
* As notificacións de novas versións de apps en Windows 10 versión 1709
  (compilación 16299) en adiante lense correctamente. NVDA 2018.2 e
  posterior soporta isto, engadíndose máis notificacións para a 2018.3.
* recoñeceranse e anunciaranse os consellos para o Edge e para as
  aplicacións universais.
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o ID do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.

## Centro de accións

* A acción rápida Brillo é agora un botón no canto dun botón conmutable.
* Reportaranse varios cambios de estado como Asistencia ao Foco e Brillo.

## Alarmas e reloxo

* Agora anúncianse os valores do selector de hora. Esto tamén afecta ó
  control usado para selecionar cando reiniciar para rematar a instalación
  das actualizacións de Windows.

## Calculadora

* Cando se prema INTRO ou Escape, NVDA anuncia os resultados do cálculo.
* Para cálculos coma conversión de unidades e conversión de moneda, o NVDA
  anunciará os resultados tan pronto coma os cálculos se introduzan.
* NVDA xa non anunciará "Nivel de nivel de cabeceira" para os resltados da
  calculadora.

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
  técnicas, o NVDA non pode interactuar compretamente coa Barra de Xogos
  antes da compilación 17723.

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe. Téñase en
  conta que a navegación entre fileiras(mensaxes) non se soporta.
* Cando se escrebe unha mensaxe, a apariencia da mención de suxerencias
  indícase con sons.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.
* Cando se usa a vista lateral da rúa e se a opción "usar teclado" está
  habilitada, NVDA anunciará os enderezos das rúas según utilices as teclas
  das frechas para navegar polo mapa.

## Microsoft Edge

* Agora anúncianse notificacións como descargas de ficheiros e varias
  alertas de páxina web así como a dispoñibilidade da vista de lectura (se
  se utiliza a versión 1709 e posterior).
* Farase un seguimento do autocompletado de texto e anunciarase na omnibarra
  de direccións.

## Teclado Moderno

Nota: A maioría das características a continuación son parte de NVDA 2018.3.

* Soporte para o panel flotante de entrada de Emoji na actualización 1709
  Fall Creators en adiante, incluindo o panel redeseñado na compilación
  17661. Para uns mellores resultados lendo emojis, usa o sintetizador de
  voz Windows OneCore.
* Soporte para suxerencias de entrada de teclado hardware na versión 1803
  (actualización de abril de 2018) e posterior.
* En compilacións post 1709, NVDA anunciará o primeiro emoji seleccionado
  cando se abra o Panel de Emojis. Isto faise notar máis na compilación
  18262 e posteriores nas que se pode abrir o Panel de Emojis na última
  categoría, como amosar o modificador de tono do deseño ao abrilo na
  categoría Xente.
* Soporte para o anunciado de elementos do portapapeis na nube na
  compilación 17666 (Redstone 5) e posterior.
* Reducida verbosidade innecesaria ao traballar con teclados modernos e as
  súas características. Isto inclúe que xa non se anuncie "Microsoft
  Candidate UI" ao abrir as suxestións de entrada hardware e que NVDA xa non
  quede calado cando certas teclas do teclado táctil lancen o evento cambio
  de nome nalguns sistemas.
* NVDA xa non reproducirá tons de erro ou aparentará non facer nada ao
  pechar o panel de Emojis nas compilacións Insider Preview máis recentes.
* NVDA anunciará os resultados de busca de emojis de ser posible.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* Certa información como o progreso da Actualización de Windows agora é
  anunciada automáticamente, incluíndo o widget de liberación de espazo en
  disco.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* Os grupos de opcións recoñécense ao se usar a navegación de obxectos para
  navegar entre controis.
* Para algunhas caixas combinadas e botóns de opción, NVDA xa non fallará ao
  recoñecer etiquetas e/ou ao anunciar cambios de valores. 
* Os pitidos da barra de progreso do volume de audio xa non se escoitan na
  versión 1803 e posterior.
* Anúncianse máis mensaxes relativas ó estado de Windows Update,
  especialmente se Windows Update atopa erros.
* NVDA xa non parecerá non facer nada ou non reproducirá tons de erro cando
  se usen ordes de navegación de obxectos baixo certas circunstancias.
* Varias ligazóns engadidas na compilación 18282 sen etiqueta agora están
  etiquetadas.
* O diálogo de recordatorio de actualización de Windows é recoñecido
  axeitadamente como un diálogo.

## Skype

Nota: As entradas seguintes non funcionarán axeitadamente na app universal
Skype 14.

* Ao teclear o indicador de texto anúnciase só coma cliente Skype para
  Escritorio.
* O comando Control+NVDA+fila de números, para ler o histórico de chats
  recentes e para mover o navegador de obxectos a entradas de chat en Skype
  para Escritorio, está tamén dispoñible no Skype UWP.
* Agora podes premer Alt+fila de números para localizar e mover a
  conversacións (1), listaxe de contactos (2), bots (3) e campo de edición
  do chat se está visible(4). Ten en conta que estas ordes funcionarán
  apropriadamente se está instalada a actualización do Skype liberada en
  Marzo do 2017.
* NVDA xa non anuncia "Mensaxe Skype" cando se revisen mensaxes para a
  maioría dos casos.
* Dende a listaxe do historial de mensaxes, premendo NVDA+D sobre un
  elemento de mensaxe agora permitirá ao NVDA anunciar información detallada
  acerca dunha mensaxe como tipo de canle, data e hora de envío e
  semellante.

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
