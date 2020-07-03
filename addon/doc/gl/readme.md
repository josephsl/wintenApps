# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: da 2019.3 á 2020.2

Este complemento é unha coleción de app modules para varias aplicacións de
Windows 10, así coma melloras e correccións para certos controis de windows
10.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Calculadora (modern).
* Calendario
* Cortana (Conversations)
* Correo
* Mapas
* Microsoft Solitaire Collection
* Tenda Microsoft
* Teclado Moderno (panel de emoji/ditado/suxestións de entrada por
  hardware/historial do portapapeis na nube/editores co método de entrada
  moderna)
* Xente
* Opcións (opcións do sistema, Windows+I)
* O Tempo.
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Notas:

* This add-on requires Windows 10 Version 1909 (build 18363) or later. For
  best results, use the add-on with latest Windows 10 stable release (build
  19041).
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
* Agora recoñécense certos diálogos como proprios diálogos. Esto inclúe o
  diálogo Insider Preview (settings app).
* NVDA pode anunciar o número de suxestións cando se realiza unha procura na
  maioría dos casos. Esta opción contrólase por "Anunciar información de
  posición do obxecto" no panel Presentación de Obxectos ubicado nas opcións
  do NVDA.
* Ao buscar no menú inicio ou no explorador de arquivos na versión 1909
  (November 2019 Update) e posteriores, NVDA xa non anunciará os resultados
  de busca dúas veces ao revisalos, o que tamén fai a saída braille máis
  consistente ao revisar elementos.
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
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o nome do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.
* Ao ordear as tarxetas do menú inicio ou as accións rápidas do centro de
  accións con Alt+Shift+teclas de frechas, NVDA anunciará información sobre
  os elementos arrastrados ou da nova posición dos mesmos.
* En novas versións de Word 365, NVDA non lerá "delete back word" ao premer
  Control+Retroceso.
* Anuncios como o de cambios no volume/brillo no Explorador de Arquivos e o
  de notificacións de actualización de app da Microsoft Store pódense
  suprimir desactivando Anunciar Notificacións nas opcións de Presentación
  de Obxectos do NVDA.

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

A maioría dos elementos xa non aplican na versión 1903 e posteriores a menos
que esteas a usar Cortana Conversations (versión 2004 e posteriores).

* As respostas textuais de Cortana anúncianse na maioría de situacións.
* NVDA silenciarase cando lle fales ao Cortana a través da voz.
* Na versión 1909 (November 2019 update) e posteriores, sopórtase a
  experiencia moderna de busca no explorador de arquivos proporcionada pola
  interface de usuario de Windows Search.

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

## Microsoft Solitaire Collection

* NVDA anunciará os nomes das tarxetas e das pías de tarxetas.

## Tenda Microsoft

* Despois de buscar actualizacións das aplicacións, os nomes das aplicacións
  na lista de aplicacions actualizarán as etiquetas correctamente.
* Cando se cargue contido como aplicacións e películas, NVDA anunciará o
  nome do producto e o progreso da descarga.

## Teclado Moderno

Isto inclúe o panel de Emoji, o historial do portapapeis, o dictado, as
suxestións de entrada por hardware, e os editores co método de entrada
moderna para certas linguas. Ao ver emojis, para unha mellor experiencia,
habilita a opción Unicode Consortium nos axustes de voz do NvDA e establece
o nivel de símbolos en "algunha" ou superior.

* Ao abrir o historial do portapapeis, NVDA xa non anunciará "portapapeis"
  cando haxa elementos no portapapeis baixo algunhas circunstancias.
* Nalgúns sistemas coa versión 1903 (May 2019 Update), NVDA xa non
  aparentará non facer nada cando se abra o panel de emoji.
* Engadido soporte para a interface de candidatos IME en chino, xaponés e
  coreano (CJK) introducida na versión 2004 (compilación 18965 e
  posteriores).

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
