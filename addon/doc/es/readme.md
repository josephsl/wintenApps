# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como Mejoras y correcciones para ciertos controles de
windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Reloj y alarmas.
* Calendario
* Calculadora (modern).
* Cortana
* Centro de opiniones
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
and NVDA 2018.1 or later. For best results, use the add-on with latest
Windows 10 stable releases (build 16299 or 17134) and latest stable version
of NVDA. Also, after changing update settings for the add-on, be sure to
save NVDA settings.

## General

* En menús de contexto para los mosaicos del Menú Inicio, los submenús ahora
  se reconocen apropiadamente.
* Ahora se reconocen ciertos diálogos como diálogos apropiadamente. Esto
  incluye el diálogo Insider Preview (aplicación de configuración).
* NVDA can announce suggestion count when performing a search in majority of
  cases. This option is controlled by "Report object position information"
  in Object presentation dialog/panel.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, element selected, live region change, notification,
  system alert, tooltip opened, window opened. Con NVDA configurado para
  ejecutarse con el registro de depuración habilitado, estos eventos se
  seguirán, y se oirá un tono de depuración para el elemento UIA
  notification
* Añadida la capacidad de buscar actualizaciones del complemento (automática
  o manual) a través del diálogo Windows 10 App Essentials que se encuentra
  en el menú Preferencias de NVDA. Por defecto, se buscarán las
  actualizaciones para las versiones estable y de desarrollo automáticamente
  semanal o diáriamente, respectivamente.
* En algunas aplicaciones, se anuncia el texto en regiones vivas. Esto
  incluye alertas en Edge, resultados en la calculadora y otros. Ten en
  cuenta que esto podrá causar una verbalización por duplicado en algunos
  casos.
* Notifications from newer app releases on Windows 10 Version 1709 (build
  16299) and later are announced. Due to technical limitations, this feature
  works properly with NVDA 2018.1 and later, and will be part of NVDA with
  2018.2 release.
* Se reconocerán y anunciarán los consejos para Edge y para aplicaciones
  universales.
* NVDA will no longer announce "unknown" when opening quick link menu
  (Windows+X). This fix will be part of NVDA 2018.2.
* In build 17627 and later, when opening a new Sets tab (Control+Windows+T),
  NVDA will announce search results when searching for items in the embedded
  Cortana window.
* When switching between Sets tabs, NvDA will announce name and position of
  the tab you are switching to.
* When opening, closing, or switching between virtual desktops, NVDA will
  announce current desktop ID (desktop 2, for example).

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

## Centro de opiniones

* En nuevas versiones de la app, NVDA no anunciará las categorías de los
  comentarios dos veces.

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

* Ahora se anuncian notificaciones tales como descargas de ficheros y varias
  alertas de página web.

## Teclado Moderno

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in build 17661 and later. For best
  experience when reading emojis, use Windows OneCore speech synthesizer.
* Support for hardware keyboard input suggestions in Version 1803 (April
  2018 Update) and later.
* En las versiones posteriores a 1709, NVDA anunciará el primer emoji
  seleccionado cuando se abra el panel de emoji.

## Gente

* Cuando se busquen contactos, se reproducirá un sonido si hay resultados de
  la búsqueda.

## Opciones

* Cierta información tal como el progreso de la Actualización de Windows
  ahora se anuncia automáticamente. 
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* Los grupos de opciones se reconocen cuando se utilice la navegación de
  objetos para navegar entre controles.
* Para algunos cuadros combinados, NVDA ya no fallará al reconocer etiquetas
  y/o al anunciar cambios de valores. 
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later.

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
* Cuando se cargue contenido tal como aplicaciones y películas, NVDA
  anunciará el nombre del producto y el progreso de la descarga.

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
