# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: 2021.3 en diante

Nota: Orixinalmente chamado Windows 10 App Essentials, renomeouse a windows
App Essentials en 2021 para soportar windows 10 e versións futuras como
Windows 11. Parte deste complemento aínda se referirá ó seu nome antigo.

Este complemento é unha coleción de app modules para varias aplicacións de
Windows, así como melloras e correccións para certos controis de windows 10
e posteriores.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Calculadora
* Cortana
* Correo
* Mapas
* Microsoft Solitaire Collection
* Teclado Moderno (panel de emoji/ditado/escritura por voz/suxestións de
  entrada por hardware/historial do portapapeis/editores co método de
  entrada moderna)
* Bloc de notas (Windows 11)
* Xente
* Opcións (opcións do sistema, Windows+I)
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio

Notas:

* Este complemento require do Windows 10 21H1 (compilación 19043) ou
  posterior e é compatible con Windows 11.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
* Non se soportarán todas as características de versións Windows Insider
  Preview.
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Para entradas non listadas a continuación, podes asumir que as
  características forman parte do NVDA, que xa non aplican debido a que o
  complemento non soporta versións vellas de Windows 10, ou que se fixeron
  cambios nas apps que fan que as entradas xa non sexan aplicables.
* Algunhas apps soportan o modo de capa compacto (sempre enriba na
  Calculadora, por exemplo), e este modo non funcionará correctamente con
  versións portables de NVDA.
* Para a mellor experiencia con aplicacións que incrustan tecnoloxías web e
  con contido como o menú inicio e o seu menú de contexto, habilita a opción
  "Modo foco automático para cambios do foco" dende o panel de modo
  navegación das opcións de NVDA.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][3].

## Xeral

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* Cando se abran, pechen, reordenen (Windows 11), ou se conmute entre
  escritorios virtuales, NVDA anunciará o nome do escritorio actual
  (escritorio 2, por exemplo).
* Ao ordear as entradas fixadas (tarxetas en Windows 10) do menú inicio ou
  as accións rápidas do centro de accións con Alt+Shift+teclas de frechas,
  NVDA anunciará información sobre os elementos arrastrados ou da nova
  posición dos mesmos.
* Anuncios como o de cambios no volume/brillo no Explorador de Arquivos e o
  de notificacións de actualización de app da Microsoft Store pódense
  suprimir desactivando Anunciar Notificacións nas opcións de Presentación
  de Obxectos do NVDA.
* En versións de Windows 11 Insider Preview, o estado do conmutador de
  silencio do micrófono (Windows+Alt+K) anúnciase desde calquera sitio.

## Calculadora

* NVDA xa non anunciará dúas veces a mensaxe en pantalla da calculadora
  gráfica.
* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will now announce calculator display content when performing
  scientific mode commands such as trigonometry operations.

## Cortana

* As respostas textuais de Cortana anúncianse na maioría de situacións.
* NVDA silenciarase cando lle fales ao Cortana a través da voz.

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe. Téñase en
  conta que a navegación entre fileiras(mensaxes) non se soporta.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.

## Microsoft Solitaire Collection

* NVDA anunciará os nomes das tarxetas e das pías de tarxetas.

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
  símbolos en Windows 10), NVDA xa non moverá o navegador de obxectos a
  certos emojis.
* Engadido soporte para o panel actualizado de experiencia de entrada (panel
  de emoji e historial de portapapeis combinados) en windows 11.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.

## Bloc de Notas

Isto refírese á versión 11 ou posterior do Bloc de Notas de Windows 11.

* NVDA anunciará elementos de estado como a información de liña e columna
  cando se execute a orde de anunciar barra de estado (NVDA+Fin en
  distribución de escritorio, NVDA+Shift+Fin en distribución portátil).
* NVDA xa non anuncia´ra o texto introducido ao premer a tecla Intro dende o
  documento.

## Xente

* Cando se procuren contactos, anunciarase a primeira suxestión,
  particularmente cando se utilicen versións recentes da app.

## Opcións

* Corrixiuse as etiquetas de controis extrañas advertidas en certas
  instalacións de Windows.
* NVDA anunciará o nome do control para a actualización de calidade opcional
  se estiver presente (ligazón descargar e instalar agora en Windows 10 e
  botón descargar en Windows 11).
* En Windows 11, os elementos da barra de faragullas de pan recoñécense
  correctamente.

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
