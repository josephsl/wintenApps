# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][4] compatible with NVDA 2019.2.1 and earlier

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
* Modern keyboard (emoji panel/dictation/hardware input suggestions/cloud
  clipboard history/modern input method editors)
* Xente
* Opcións (opcións do sistema, Windows+I)
* O Tempo.
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Notas:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.3 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18363) and latest stable version of NVDA.
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
  menú da aplicación Microsoft Edge na versin 1809 (October 2018 Update).
* Agora recoñécense certos diálogos como proprios diálogos. Esto inclúe o
  diálogo Insider Preview (settings app).
* NVDA pode anunciar o número de suxestións cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no panel Presentación de Obxectos ubicado nas opcións
  do NVDA.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu. This is now part of NVDA 2019.3.
* Ao buscar no menú inicio ou no explorador de arquivos na versión 1909
  (November 2019 Update) e posteriores, NVDA xa non anunciará os resultados
  de busca dúas veces ao revisalos, o que tamén fai a saída braille máis
  consistente ao revisar elementos.
* En certos menús de contexto (coma no Edge), a información de posición
  (ex.: 1 de 2) xa non se anuncia.
* Recoñécense os seguintes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. Co NVDA
  configurado para executarse co rexistro de depuración habilitado, estos
  eventos seguiranse e, no caso do evento UIA notification oirase un ton se
  as notificacións veñen de calquera lugar que non sexa a app actualmente
  activa.
* É posible o seguimento só de eventos específicos e/ou de eventos provintes
  de aplicacións específicas.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This is now part of NVDA 2019.3.
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o nome do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.
* App name and version for various Microsoft Store apps are now shown
  correctly. This is now part of NVDA 2019.3.
* Ao ordear as tarxetas do menú inicio ou as accións rápidas do centro de
  accións con Alt+Shift+teclas de frechas, NVDA anunciará información sobre
  os elementos arrastrados ou da nova posición dos mesmos.

## Calculadora

* Cando se prema INTRO ou Escape, NVDA anunciará os resultados do cálculo.
* Para cálculos coma conversión de unidades e conversión de moneda, o NVDA
  anunciará os resultados tan pronto coma os cálculos se introduzan.
* NVDA xa non anunciará "Nivel de nivel de cabeceira" para os resltados da
  calculadora.
* NVDA notificará cando se chegue ao límite de díxitos introducindo
  expresións.
* Engadido soporte para o modo sempre acendida en Calculadora versión
  10.1908 e posterior.

## Calendario

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
* In Version 1909 (November 2019 Update) and later, modern search experience
  in File Explorer powered by Windows Search user interface is supported.

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

* Text auto-complete will be tracked and announced in address omnibar. This
  is now part of NVDA 2019.3.
* NVDA will no longer play suggestion sound when pressing F11 to toggle full
  screen. This is now part of NVDA 2019.3.
* Removed suggestions sound playback for address omnibar. This is now part
  of NVDA 2019.3.

## Tenda Microsoft

* Despois de buscar actualizacións das aplicacións, os nomes das aplicacións
  na lista de aplicacions actualizarán as etiquetas correctamente.
* Cando se cargue contido como aplicacións e películas, NVDA anunciará o
  nome do producto e o progreso da descarga.

## Teclado Moderno

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NvDA's speech settings and set symbol level to "some" or higher.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including redesigned panel in Version 1809 (build 17661 and later)
  and changes made in Version 1903 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). This is also applicable in Version
  2004 (build 18963 and later) as the app has been renamed. All of these
  changes are now part of NVDA 2019.3.
* When opening clipboard history, NVDA will no longer announce "clipboard"
  when there are items in the clipboard under some circumstances.
* Nalgúns sistemas coa versión 1903 (May 2019 Update), NVDA xa non
  aparentará non facer nada cando se abra o panel de emoji.
* Added support for modern Chinese, Japanese, and Korean (CJK) IME
  candidates interface introduced in Version 2004 (build 18965 and later).

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
  later. This is now part of NVDA 2019.3.
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

[4]: https://addons.nvda-project.org/files/get.php?file=w10-2019
