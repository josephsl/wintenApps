# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: 2021.2 en diante

Nota: Orixinalmente chamado Windows 10 App Essentials, renomeouse a windows
App Essentials en 2021 para soportar windows 10 e versións futuras como
Windows 11. Parte deste complemento aínda se referirá ó seu nome antigo.

Este complemento é unha coleción de app modules para varias aplicacións de
Windows, así como melloras e correccións para certos controis de windows 10
e posteriores.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Calculadora (modern)
* Cortana (Conversations)
* Correo
* Mapas
* Microsoft Solitaire Collection
* Tenda Microsoft
* Teclado Moderno (panel de emoji/ditado/escritura por voz/suxestións de
  entrada por hardware/historial do portapapeis/editores co método de
  entrada moderna)
* Xente
* Opcións (opcións do sistema, Windows+I)
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio

Notas:

* Este complemento require do Windows 10 20H2 (compilación 19042) ou
  posterior e é compatible con Windows 11.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para entradas non listadas a continuación, podes asumir que as
  características forman parte do NVDA, que xa non aplican debido a que o
  complemento non soporta versións vellas de Windows 10, ou que se fixeron
  cambios nas apps que fan que as entradas xa non sexan aplicables.
* Algunhas apps soportan o modo de capa compacto (sempre enriba na
  Calculadora, por exemplo), e este modo non funcionará correctamente con
  versións portables de NVDA.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][3].

## Xeral

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses.
* Ademais dos manexadores de eventos UIA proporcionados por NVDA,
  recoñécense os seguintes eventos UIA: drag start, drag cancel, drag
  complete, drop target drag enter, drop target drag leave, drop target
  dropped, layout invalidated. Co nivel de rexistro de NVDA configurado como
  depuración, estes eventos seguiranse, e no caso de eventos UIA
  notification oirase un ton de depuración se as notificacións veñen de
  calquera lugar que non sexa a app actualmente activa. Eventos incluídos en
  NVDA como os eventos name change e controller for monitorizaranse por
  parte dun complemento denominado Event Tracker.
* Cando se abran, pechen, reordenen (Windows 11), ou se conmute entre
  escritorios virtuales, NVDA anunciará o nome do escritorio actual
  (escritorio 2, por exemplo).
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

* NVDA xa non anunciará dúas veces a mensaxe en pantalla da calculadora
  gráfica.

## Cortana

A maioría dos elementos aplican se se usa Cortana Conversations (Windows 10
2004 e posteriores).

* As respostas textuais de Cortana anúncianse na maioría de situacións.
* NVDA silenciarase cando lle fales ao Cortana a través da voz.

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe. Téñase en
  conta que a navegación entre fileiras(mensaxes) non se soporta.

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
* Cando se descargue contido como aplicacións e películas, NVDA anunciará o
  nome do produto e o progreso da descarga.

## Teclado Moderno

Isto inclúe o panel de Emoji, o historial do portapapeis, o
dictado/escritura por voz, as suxestións de entrada por hardware, e os
editores co método de entrada moderna para certas linguas. Ao ver emojis,
para unha mellor experiencia, habilita a opción Unicode Consortium nos
axustes de voz do NvDA e establece o nivel de símbolos en "algunha" ou
superior. Ao pegar dende o historial do portapapeis en Windows 10, preme a
tecla Espacio no canto de Intro para pegar o elemento seleccionado. NVDA
tamén soporta o panel de experiencia de entrada actualizado en Windows 11.

* Cando se selecciona un grupo de emojis (incluindo kaomoji e grupos de
  símbolos en Windows 10 1903 ou posterior), NVDA xa non moverá o navegador
  de obxectos a certos emojis.
* Engadido soporte para o panel actualizado de experiencia de entrada (panel
  de emoji e historial de portapapeis combinados) en windows 11.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* Certa información como o progreso de Windows Update agora é anunciada
  automaticamente, incluíndo o widget de Storage Sense/liberación de espazo
  en disco e os erros de windows Update.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.
* Corrixiuse as etiquetas de controis extrañas advertidas en certas
  instalacións de Windows.
* NVDA anunciará o nome da ligazón á actualización de calidade opcional se
  estiver presente, normalmente chamado "descargar e instalar agora".

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
