# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

This add-on is a collection of app modules for various Windows 10 apps, as
well as enhancements and fixes for certain windows 10 controls.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Reloj y alarmas.
* Calendario
* Calculadora (modern).
* Cortana
* Barra de juegos
* Correo
* Mapas
* Microsoft Edge
* Teclado Moderno (sugerencias de panel emoji /entrada hardware en la
  Versión 1709 y posterior)
* Gente
* Opciones (opciones de sistema, Windows+I)
* Skype (aplicación universal)
* Tienda
* El Tiempo
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

## General

* En menús de contexto para los mosaicos del Menú Inicio, los submenús ahora
  se reconocen apropiadamente.
* Certain dialogs are now recognized as proper dialogs, including Insider
  Preview dialog (settings app).
* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el diálogo Presentación de Objetos.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA:  Controller for, live region
  changed, system alert, element selected, window opened. Con NVDA
  configurado para ejecutarse con el registro de depuración habilitado,
  estos eventos se seguirán.
* Added ability to check for add-on updates (automatic or manual) via
  Windows 10 App Essentials dialog found in NvDA Preferences menu. By
  default, stable and development versions will check for new updates
  automatically on a weekly or daily basis, respectively.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.

## Alarmas y reloj

* Ahora se anuncian los valores del selector de hora. Esto también afecta al
  control utilizado para seleccionar cuándo reiniciar para finalizar la
  instalación de las actualizaciones de Windows.

## Calculadora

* Cuando se pulse INTRO o Escape, NVDA anuncia los resultados del cálculo.
* Para cálculos tales como conversión de unidades y conversión de moneda,
  NVDA anunciará los resultados tan pronto como los cálculos se introduzcan.

## calendario

* NVDA ya no anuncia "editar" o "sólo lectura" en el cuerpo del mensaje y
  otros campos.

## Cortana

* Las respuestas textuales de Cortana se anuncian en la mayoría de las
  situaciones (si no se reabre el menú Inicio y  se trata de buscar de
  nuevo).
* NVDA will be silent when talking to Cortana via voice.
* NVDA ahora anunciará confirmación de recuerdo después de configurarla.

## Barra de juegos

* NVDA anunciará la aparición de la ventana Barra de Juegos. Debido a
  limitaciones técnicas, NVDA no puede interactuar completamente con la
  Barra de Juegos.

## Correo

* Cuando se revisan elementos en la lista de mensajes, ahora puedes utilizar
  órdenes de navegación de tablas para revisar los encabezados de mensaje.
* Cuando se escribe un mensaje, la apariencia de la mención de sugerencias
  se indica con sonidos.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.
* Cuando se utiliza la vista lateral de la calle y si la opción "usar
  teclado" está habilitada, NVDA anunciará las direcciones de las calles
  según utilices las teclas de flechas para navegar por el mapa.

## Microsoft Edge

* Notifications such as file downloads and various webpage alerts are
  announced.

## Teclado Moderno

* Soporte para el panel flotante de entrada de Emoji en la actualización
  1709 (Fall Creators) (para unos mejores resultados, leyendo emojis utiliza
  el sintetizador de voz Windows OneCore).
* Soporte para sugerencias de entrada de teclado hardware en la compilación
  17040 y posterior.

## Gente

* Cuando se busquen contactos, se reproducirá un sonido si hay resultados de
  la búsqueda.

## Opciones

* Certain information such as Windows Update progress is reported
  automatically.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* Los grupos de opciones se reconocen cuando se utilice la navegación de
  objetos para navegar entre controles.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes.
* Los pitidos de la barra de progreso de volumen de audio ya no se oyen en
  la compilación 17035 y posterior.

## Skype

* Al teclear el indicador de texto se anuncia sólo como cliente Skype para
  Escritorio.
* Retorno parcial de las órdenes Control+NVDA+fila de números para leer el
  historial de chats recientes y para mover el navegador de objetos a las
  entradas de chat como en Skype para Escritorio.
* Ahora puedes pulsar Alt+fila de números para localizar y mover a
  conversaciones (1), lista de contactos (2), bots (3) y campo de edición de
  chat (4). Ten en cuenta que estas órdenes funcionarán apropiadamente si
  está instalada la actualización de Skype liberada en Marzo de 2017.
* Se anuncian las etiquetas de los cuadros combinados para la aplicación
  Skype preview liberada en Noviembre de 2016.
* NVDA ya no anuncia "Mensaje Skype" cuando se revisen mensajes para la
  mayoría de los casos.
* Corregidos varios problemas al utilizar Skype con pantallas braille,
  incluyendo la incapacidad para revisar los elementos del historial de
  mensajes en braille.
* Desde la lista del historial de mensajes, pulsando NVDA+D sobre un
  elemento de mensaje ahora permitirá a NVDA anunciar información detallada
  acerca de un mensaje tal como tipo de canal, fecha y hora de envío y
  similar.

## Tienda

* Después de buscar actualizaciones de aplicaciones, los nombres de las
  aplicaciones en la lista de aplicaciones etiquetadas se actualizan
  correctamente.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## El Tiempo

* Pestañas tales como "pronósticos" y "mapas" se reconocen como propias
  pestañas (parche de Derek Riemer).
* cuando se lea un pronóstico, utiliza las flechas izquierda y derecha para
  moverte entre elementos. Utiliza flechas arriba y abajo para leer los
  elementos individuales. Por ejemplo, pulsando la flecha derecha anunciaría
  "Lunes: 79 grados, parcialmente nublado, ..." pulsando flecha abajo dirá
  "lunes" entonces pulsándola de nuevo leerá el siguiente elemento (como la
  temperatura). Actualmente esto funciona para los pronósticos diarios y
  horarios.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
