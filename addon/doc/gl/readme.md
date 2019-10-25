# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* NVDA compatibility: 2019.2

Este complemento é unha coleción de app modules para varias aplicacións de
Windows 10, así coma melloras e correccións para certos controis de windows
10.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Calculadora (modern).
* Calendario
* Cortana (Classic e Conversations)
* Centro de Opinións
* Correo
* Mapas
* Microsoft Edge
* Tenda Microsoft
* Teclado Moderno (panel de emoji/ditado/suxestións de entrada por
  hardware/elementos do portapapeis na nube na Versión 1709 e posterior)
* Xente
* Opcións (opcións do sistema, Windows+I)
* O Tempo.
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Notas:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
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
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, NVDA will no longer announce search results twice
  when reviewing results, which also makes braille output more consistent
  when reviewing items.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window opened. Co
  NVDA configurado para executarse co rexistro de depuración habilitado,
  estos eventos seguiranse e, no caso do evento UIA notification oirase un
  ton se as notificacións veñen de calquera lugar que non sexa a app
  actualmente activa.
* É posible o seguimento só de eventos específicos e/ou de eventos provintes
  de aplicacións específicas.
* Recoñeceranse e anunciaranse os consellos para o Edge e para as
  aplicacións universais. Isto será parte de NVDA 2019.3.
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o nome do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.
* O nome e a versión da app para varias apps da Tenda Microsoft (Microsoft
  Store) amósanse aagora correctamente.

## Calculadora

* Cando se prema INTRO ou Escape, NVDA anunciará os resultados do cálculo.
* Para cálculos coma conversión de unidades e conversión de moneda, o NVDA
  anunciará os resultados tan pronto coma os cálculos se introduzan.
* NVDA xa non anunciará "Nivel de nivel de cabeceira" para os resltados da
  calculadora.
* NVDA notificará cando se chegue ao límite de díxitos introducindo
  expresións.
* Added support for always on mode in Calculator version 10.1908 and later.

## calendario

* NVDA xa non anuncia "editar" ou "só lectura" para asuntos da cita no
  Calendario e no contido do mensaxe no Correo.

## Cortana

A maioría dos elementos xa non aplican na versión 1903 e
posteriores. Cortana Classic refírese á vella interface de Cortana, que
estaba integrada no menú inicio.

* As respostas testuais de Cortana, tanto (tanto na interface Classic como
  Conversations) anúncianse na mayoría das situacións(se se está a usar
  Cortana Classic, reabre o menú inicio e tenta procurar de novo se as
  respostas non se anuncian).
* NVDA silenciarase cando lle fales ao Cortana a través da voz.
* En Cortana Classic, NVDA agora anunciará a confirmación do recordatorio
  despois de que poñas un.
* Na compilación 18945 e posteriores, sopórtase a experiencia moderna de
  busca no explorador de arquivos proporcionada pola interface de usuario de
  Cortana.

## Centro de Opinións

* En novas versións da app, NVDA non lerá as categorías de comentarios dúas
  veces.

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

Isto refírese ao Edge clásico basado en EdgeHTML.

* Farase un seguimento do autocompletado de texto e anunciarase na omnibarra
  de direccións. Isto formará parte de NVDA 2019.3.
* NVDA xa non reproducirá o son de suxestión ao premer F11 para alternar a
  pantalla completa. Isto formará parte de NVDA 2019.3.
* Eliminada a reprodución do son de suxestión para a barra de busca
  (omnibar). Isto formará parte de NVDA 2019.3.

## Tenda Microsoft

* Despois de buscar actualizacións das aplicacións, os nomes das aplicacións
  na lista de aplicacions actualizarán as etiquetas correctamente.
* Cando se cargue contido como aplicacións e películas, NVDA anunciará o
  nome do producto e o progreso da descarga.

## Teclado Moderno

A maioría das características a continuación son parte de NVDA 2018.3 ou
posterior.

* Soporte para o panel flotante de entrada de Emoji na actualización 1709
  Fall Creators en adiante, incluindo o panel redeseñado na compilación
  17661 e os trocos realizados en 19H1 (compilación 18262 e posterior,
  incluíndo kaomoji e categorías de símbolos na compilación 18305). Isto
  tamén aplica para a compilación 18963 e posteriores onde a app se
  renomeou. Se usas versións de NVDA anteriores á 2018.4, utiliza o
  sintetizador de voz Windows OneCore para a mellor experiencia lendo
  emojis. Se a versión en uso é a 2018.4 ou posterior, habilita a opción do
  Unicode Consortium dende as opcións de voz do NVDA e establece o nivel de
  símbolos en "Algunha" ou máis alto.
* NVDA xa non anunciará "portapapeis" cando haxa elementos no portapapeis
  baixo algunhas circunstancias.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Engadido soporte para a interface de candidatos IME en chino, xaponés e
  coreano (CJK) introducida na 20H1 compilación 18965 e posteriores.

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
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This will be part of NVDA 2019.3.
* NVDA xa non parecerá non facer nada ou non reproducirá tons de erro cando
  se usen ordes de navegación de obxectos baixo certas circunstancias.
* O diálogo de recordatorio de actualización de Windows é recoñecido
  axeitadamente como un diálogo.
* Corrixiuse a disparidade en etiquetas de controis advertida en certas
  instalacións de Windows.
* En revisións máis recentes da versión 1803 e posteriores, por mor de
  cambios no procedemento de Windows Update para actualizacións de
  características, engadiuse unha ligazón "descargar e instalar agora". NVDA
  anunciará agora o título da nova actualización se está presente.

## O Tempo

* As pestanas como "pronósticos" e "mapas" recoñécense coma pestanas en si
  (parche de Derek Riemer).
* cando se lea un pronóstico, usa as frechas esquerda e dereita para moverte
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
