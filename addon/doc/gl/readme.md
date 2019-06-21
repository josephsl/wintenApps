# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: da 2018.4 á 2019.2

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
* Correo
* Mapas
* Microsoft Edge
* Teclado Moderno (panel de emoji/ditado/suxestións de entrada por
  hardware/elementos do portapapeis na nube na Versión 1709 e posterior)
* Xente
* Opcións (opcións do sistema, Windows+I)
* Tenda
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Notas:

* Este complemento require do Windows 10 Versión 1803 (compilación 17134) ou
  posterior e do NVDA 2018.4 ou posterior. Para uns mellores resultados, usa
  o complemento coa compilación estable máis recente (compilación 18362) e
  versión estable máis recente do NVDA.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para entradas non listadas a continuación, podes asumir que as
  características forman parte do NVDA, que xa non aplican debido a que o
  complemento non soporta versións vellas de Windows, ou que se fixeron
  cambios nas apps que fan que as entradas xa non sexan aplicables.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][3].

## Xeral

* NVDA xa non reproducirá tons de erro ou aparentará non facer nada se este
  complemento se activa en Windows 7, Windows 8.1 e versións sen soporte de
  Windows 10.
* Os elementos de submenú recoñécense adecuadamente en varias apps,
  incluíndo elementos do menú de contexto nas tarxetas do menú inicio e o
  menú da aplicación Microsoft Edge (Restone 5).
* Agora recoñécense certos diálogos como proprios diálogos. Esto inclúe o
  diálogo Insider Preview (settings app).
* NVDA pode anunciar o número de suxestións cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no panel Presentación de Obxectos ubicado nas opcións
  do NVDA.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: active text position change,
  Controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, text change,
  tooltip opened, window opened. Co NVDA configurado para executarse co
  rexistro de depuración habilitado, estos eventos seguiranse e, no caso do
  evento UIA notification oirase un ton se as notificacións veñen de
  calquera lugar que non sexa a app actualmente activa.
* recoñeceranse e anunciaranse os consellos para o Edge e para as
  aplicacións universais.
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o nome do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.
* Na versión 1903 (May 2019 Update), NVDA anunciará cambios no volume e o
  brillo inmediatamente.

## Centro de accións

* A acción rápida Brillo é agora un botón no canto dun botón
  conmutable. Agora xa forma parte de NVDA 2019.1
* Reportaranse varios cambios de estado como Asistencia ao Foco e
  Brillo. Agora xa forma parte do NVDA 2019.1.

## Alarmas e reloxo

* Agora anúncianse os valores do selector de hora. Esto tamén afecta ó
  control usado para selecionar cando reiniciar para rematar a instalación
  das actualizacións de Windows. Agora xa forma parte do NVDA 2019.1.

## Calculadora

* Cando se prema INTRO ou Escape, NVDA anuncia os resultados do cálculo.
* Para cálculos coma conversión de unidades e conversión de moneda, o NVDA
  anunciará os resultados tan pronto coma os cálculos se introduzan.
* NVDA xa non anunciará "Nivel de nivel de cabeceira" para os resltados da
  calculadora.
* NVDA notificará cando se chegue ao límite de díxitos introducindo
  expresións.

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

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe. Téñase en
  conta que a navegación entre fileiras(mensaxes) non se soporta.
* Cando se escrebe unha mensaxe, a apariencia da mención de suxerencias
  indícase con sons.
* NVDA xa non parecerá non facer nada ou non reproducirá tons de erro tras
  pechar esta app. agora xa forma parte de NVDA 2019.1.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.
* Cando se usa a vista lateral da rúa e se a opción "usar teclado" está
  habilitada, NVDA anunciará os enderezos das rúas según utilices as teclas
  das frechas para navegar polo mapa.

## Microsoft Edge

* Farase un seguimento do autocompletado de texto e anunciarase na omnibarra
  de direccións.
* NVDA xa non reproducirá o son de suxestión ao premer F11 para alternar a
  pantalla completa.

## Teclado Moderno

Nota: A maioría das características a continuación son parte de NVDA 2018.3
ou posterior.

* Soporte para o panel flotante de entrada de Emoji na actualización 1709
  Fall Creators en adiante, incluindo o panel redeseñado na compilación
  17661 e os trocos realizados en 19H1 (compilación 18262 e posterior,
  incluíndo kaomoji e categorías de símbolos na compilación 18305). Se usas
  versións de NVDA anteriores á 2018.4, utiliza o sintetizador de voz
  Windows OneCore para a mellor experiencia lendo emojis. Se a versión en
  uso é a 2018.4 ou posterior, habilita a opción do Unicode Consortium dende
  as opcións de voz do NVDA e establece o nivel de símbolos en "Algunha" ou
  máis alto.
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
  pechar o panel de emoji nas compilacións Insider Preview 19H1 máis
  recentes. Agora isto forma parte de NVDA 2019.1.
* Na versión 1809 (October 2018 Update) e posteriores, NVDA anunciará os
  resultados de busca de emojis de ser posible. agora isto forma parte de
  NVDA 2019.1.
* NVDA xa non anunciará "portapapeis" cando haxa elementos no portapapeis
  baixo algunhas circunstancias.
* Nalgúns sistemas coa versión 1903 (May 2019 Update), NVDA xa non
  aparentará non facer nada cando se abra o panel de emoji.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* Certa información como o progreso de Windows Update agora é anunciada
  automaticamente, incluíndo o widget de Storage Sense/liberación de espazo
  en disco e os erros de windows Update.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* Para algunhas caixas combinadas e botóns de opción, NVDA xa non fallará ao
  recoñecer etiquetas e/ou ao anunciar cambios de valores. 
* Os pitidos da barra de progreso do volume de audio xa non se escoitan na
  versión 1803 e posterior.
* NVDA xa non parecerá non facer nada ou non reproducirá tons de erro cando
  se usen ordes de navegación de obxectos baixo certas circunstancias.
* O diálogo de recordatorio de actualización de Windows é recoñecido
  axeitadamente como un diálogo.
* Corrixiuse a disparidade en etiquetas de controis advertida en certas
  instalacións de Windows.

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
