# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: da 2020.3 á 2020.4

Este complemento é unha coleción de app modules para varias aplicacións de
Windows 10, así coma melloras e correccións para certos controis de windows
10.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Calculadora (modern)
* Calendario
* Cortana (Conversations)
* Correo
* Mapas
* Microsoft Solitaire Collection
* Tenda Microsoft
* Teclado Moderno (panel de emoji/ditado/suxestións de entrada por
  hardware/historial do portapapeis/editores co método de entrada moderna)
* Xente
* Opcións (opcións do sistema, Windows+I)
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio

Notas:

* Este complemento require do Windows 10 Versión 2004 (compilación 19041) ou
  posterior. Para uns mellores resultados, usa o complemento coa última
  versión estable do windows 10 (20H2/compilación 19042).
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para entradas non listadas a continuación, podes asumir que as
  características forman parte do NVDA, que xa non aplican debido a que o
  complemento non soporta versións vellas de Windows, ou que se fixeron
  cambios nas apps que fan que as entradas xa non sexan aplicables.
* Algunhas apps soportan o modo de capa compacto (sempre enriba na
  Calculadora, por exemplo), e este modo non funcionará correctamente con
  versións portables de NVDA.

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
* Ademais dos manexadores de eventos UIA proporcionados por NVDA,
  recoñécense os seguintes eventos UIA: drag start, drag cancel, drag
  complete, drop target drag enter, drop target drag leave, drop target
  dropped. Co nivel de rexistro de NVDA configurado como depuración, estes
  eventos seguiranse, e no caso de eventos UIA notification oirase un ton de
  depuración se as notificacións veñen de calquera lugar que non sexa a app
  actualmente activa. Algúns eventos proporcionarán información adicional
  como o contador de elementos en eventos controlled for, estado do elemento
  en eventos state change, e o texto do elemento para eventos item status.
* É posible o seguimento só de eventos específicos e/ou de eventos provintes
  de aplicacións específicas.
* Cando se abran, pechen ou se conmute entre escritorios virtuales, NVDA
  anunciará o nome do escritorio actual (escritorio 2, por exemplo).
* NVDA xa non anuncia Menú Inicio tamaño de texto ao cambiar a resolución de
  pantalla ou a orientación.
* Ao ordear as tarxetas do menú inicio ou as accións rápidas do centro de
  accións con Alt+Shift+teclas de frechas, NVDA anunciará información sobre
  os elementos arrastrados ou da nova posición dos mesmos.
* Anuncios como o de cambios no volume/brillo no Explorador de Arquivos e o
  de notificacións de actualización de app da Microsoft Store pódense
  suprimir desactivando Anunciar Notificacións nas opcións de Presentación
  de Obxectos do NVDA.

## Calculadora

* Cando se prema INTRO ou Escape, NVDA anunciará os resultados do cálculo.
* Para cálculos coma conversión de unidades e conversión de moneda, o NVDA
  anunciará os resultados tan pronto coma os cálculos se introduzan.
* NVDA notificará cando se chegue ao límite de díxitos introducindo
  expresións.
* NVDA xa non anunciará dúas veces a mensaxe en pantalla da calculadora
  gráfica.

## Calendario

* NVDA xa non anuncia "editar" ou "só lectura" para asuntos da cita no
  Calendario e no contido do mensaxe no Correo.

## Cortana

A maioría dos elementos aplican se se usa Cortana Conversations (versión
2004 e posteriores).

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
o nivel de símbolos en "algunha" ou superior. Ademais, NVDA soporta o panel
de experiencia de entrada actualizado na compilación 21296 e posterior.

* Ao abrir o historial do portapapeis, NVDA xa non anunciará "portapapeis"
  cando haxa elementos no portapapeis baixo algunhas circunstancias.
* Nalgúns sistemas coa versión 1903 (May 2019 Update), NVDA xa non
  aparentará non facer nada cando se abra o panel de emoji.
* Engadido soporte para a interface de candidatos IME en chino, xaponés e
  coreano (CJK) introducida na versión 2004 (compilación 18965 e
  posteriores).
* Cando se selecciona un grupo de emojis (incluindo kaomoji e grupos de
  símbolos na Versión 1903 ou posterior), NVDA xa non moverá o navegador de
  obxectos a certos emojis.
* Engadido soporte para o panel actualizado de experiencia de entrada (panel
  de emoji e historial de portapapeis combinados) na compilación 21296 e
  posterior.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* Certa información como o progreso de Windows Update agora é anunciada
  automaticamente, incluíndo o widget de Storage Sense/liberación de espazo
  en disco e os erros de windows Update.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
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
