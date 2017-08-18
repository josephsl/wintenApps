# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como correcciones para ciertos controles de windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Reloj y alarmas.
* Calendario
* Calculadora (modern).
* Cortana
* Barra de juegos
* Groove Music
* Correo
* Mapas
* Microsoft Edge
* Gente
* Opciones (opciones de sistema, Windows+I)
* Skype (aplicación universal)
* Tienda
* El Tiempo
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Nota: este complemento requiere Windows 10 Versión 1607 (build 14393) o
posterior y NVDA 2017.1 o posterior. Para unos mejores resultados, utiliza
el complemento con la compilación estable más reciente (build 15063) y
versión estable más reciente de NVDA. También, después de cambiar las
opciones de actualización para el complemento, asegúrate de guardar la
configuración de NVDA.

Important note about NVDA 2017.3: due to backwards incompatible changes in
NVDA 2017.3, add-on version 17.09 and later will not work on NVDA versions
earlier than 2017.3.

## General

* En menús de contexto para los mosaicos del Menú Inicio, los submenús ahora
  se reconocen apropiadamente.
* Certain dialogs are now recognized as proper dialogs. These include
  Insider Preview dialog (settings app) and new-style UAC dialog in build
  14328 and later for NvDA 2016.2.1 or earlier.
* Appearance/close of suggestions for certain search fields (notably
  Settings and Store apps) is announced via sounds and braille. This also
  includes Start menu search box. This is now part of NVDA as of 2017.3.
* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el diálogo Presentación de Objetos.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA:  Controller for, live region
  changed, system alert, element selected, window opened.
* Añadida la capacidad de buscar actualizaciones del complemento (automática
  o manual) a través del nuevo diálogo Windows 10 App Essentials que se
  encuentra en el menú Preferencias de NVDA. Por defecto, se buscarán las
  actualizaciones para las versiones estable y de desarrollo automáticamente
  semanal o diáriamente, respectivamente.
* Capacidad para seguir eventos que lleguen desde aplicaciones Universal
  Windows Platform (UWP) si NVDA se está ejecutando con el registro de
  depuración habilitado.
* Support for floating Emoji input panel in Fall Creators Update (for best
  experience when reading emojis, use Windows OneCore speech synthesizer).
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases. Most of the scenarios are now part of NVDA
  2017.3.
* Toasts are no longer announced multiple times in Creators Update and
  later. This fix is included in NVDA 2017.3.

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
* NVDA se silenciará cuando hables a Cortana a través de la voz.
* NVDA ahora anunciará confirmación de recuerdo después de configurarla.

## Barra de juegos

* NVDA anunciará la aparición de la ventana Barra de Juegos. Debido a
  limitaciones técnicas, NVDA no puede interactuar completamente con la
  Barra de Juegos.

## Groove Music

* Ahora se detecta la aparición de sugerencias cuando se detecta búsqueda de
  pistas .

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

* Notifications such as file downloads and various webpage alerts are now
  announced. Most of these scenarios are now part of NVDA 2017.3.

## Gente

* Cuando se busquen contactos, se reproducirá un sonido si hay resultados de
  la búsqueda.

## Opciones

* Certain information such as Windows Update progress is now reported
  automatically. NVDA itself will handle majority of cases in 2017.3.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* If it takes a while to search for settings, NVDA will announce "searching"
  and search result status such as if a setting cannot be found. This is now
  done from NVDA in 2017.3.
* Los grupos de opciones se reconocen cuando se utilice la navegación de
  objetos para navegar entre controles.
* For some combo boxes, NVDA will no longer fail to recognize labels and/or
  announce value changes. Value change fix is included in NVDA 2017.3.

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
* Appearance of search suggestions are now announced. This is now part of
  NVDA 2017.3.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress. A basic fix is now part of NVDA
  2017.3.

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
