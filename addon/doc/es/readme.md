# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* NVDA compatibility: 2019.2

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como Mejoras y correcciones para ciertos controles de
windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Calculadora (modern).
* Calendario
* Cortana (clásico y conversaciones)
* Centro de opiniones
* Correo
* Mapas
* Microsoft Edge
* Microsoft Store
* Teclado Moderno (panel emoji / dictado / sugerencias de entrada hardware /
  elementos del portapapeles en la nube en la Versión 1709 y posterior)
* Gente
* Opciones (opciones de sistema, Windows+I)
* El Tiempo.
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Notas:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.2 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
* Para las entradas que no se listen a continuación, puedes asumir que las
  características son parte de NVDA, no se aplican porque el complemento no
  da soporte a versiones antiguas de Windows 10, o se han hecho cambios a
  las aplicaciones que permiten que ya no sea necesario aplicarlas.

Para ver una lista de cambios hechos entre cada actualización del
complemento, consulta el documento [changelogs for add-on releases][3].

## General

* NVDA ya no reproducirá tonos de error o se quedará sin hacer nada si este
  complemento se activa en Windows 7, Windows 8.1 y versiones sin soporte de
  Windows 10.
* Se reconocen los elementos de los submenús en diversas aplicaciones,
  incluyendo el menú de contexto para los elementos del menú Inicio y el
  menú de aplicación de Microsoft Edge (Redstone 5).
* Además de los diálogos reconocidos como tales por NVDA, ahora se reconocen
  más diálogos y se anuncian adecuadamente, como el diálogo Insider Preview
  (aplicación de configuración).
* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el panel Presentación de Objetos.
* NVDA will no longer announce "blank" when pressing up or down arrow to
  open all apps views in Start menu.
* When searching in Start menu or File Explorer in Version 1909 (November
  2019 Update) and later, NVDA will no longer announce search results twice
  when reviewing results, which also makes braille output more consistent
  when reviewing items.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. Con NVDA configurado para ejecutarse con el registro de depuración
  habilitado, estos eventos se seguirán, y se oirá un tono de depuración
  para el evento UIA notification si las notificaciones vienen de un lugar
  distinto a la aplicación actual.
* Es posible seguir sólo eventos específicos y/o eventos que vienen de
  aplicaciones específicas.
* Se reconocen y anuncian los consejos para Edge y para aplicaciones
  universales. Esto formará parte de NVDA 2019.3.
* Al abrir, cerrar o cambiar entre escritorios virtuales, NVDA anunciará el
  nombre del escritorio actual (escritorio 2, por ejemplo).
* NVDA ya no anuncia Menú Inicio tamaño de texto al cambiar la resolución de
  pantalla o la orientación.
* Ahora se muestran correctamente el nombre y la versión de diversas
  aplicaciones de la Microsoft Store. Esto formará parte de NVDA 2019.3.

## Calculadora

* Cuando se pulse INTRO o Escape, NVDA anunciará los resultados del cálculo.
* Para cálculos tales como conversión de unidades y conversión de moneda,
  NVDA anunciará los resultados tan pronto como los cálculos se introduzcan.
* NVDA ya no anunciará "Encabezado nivel" en los resultados de la
  calculadora.
* NVDA avisará si se alcanza la cantidad máxima de dígitos al introducir
  expresiones.
* Added support for always on mode in Calculator version 10.1908 and later.

## calendario

* NVDA ya no anuncia "editar" o "sólo lectura" en el cuerpo del mensaje y
  otros campos.

## Cortana

La mayoría de elementos ya no se aplican en la versión 1903 y
posteriores. Cortana clásico hace referencia a la antigua interfaz de
Cortana que formaba parte del menú Inicio.

* Las respuestas textuales de Cortana (interfaz clásica y de conversaciones)
  se anuncian en la mayoría de las situaciones (si utilizas Cortana clásico,
  vuelve a abrir el menú Inicio e intenta buscar de nuevo cuando las
  respuestas no se anuncien).
* NVDA se silenciará cuando hables a Cortana a través de la voz.
* En Cortana clásico, NVDA anunciará confirmación de recuerdo después de que
  configures una.
* En la compilación 18945 y posteriores, se soporta la interfaz de usuario
  de la experiencia de búsqueda moderna proporcionada por Cortana en el
  explorador de Windows.

## Centro de opiniones

* En nuevas versiones de la app, NVDA no anunciará las categorías de los
  comentarios dos veces.

## Correo

* Cuando se revisan elementos en la lista de mensajes, ahora puedes utilizar
  órdenes de navegación de tablas para revisar los encabezados de
  mensaje. Ten en cuenta que no está soportado navegar por filas (mensajes).
* Cuando se escribe un mensaje, la apariencia de la mención de sugerencias
  se indica con sonidos.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.
* Cuando se utiliza la vista lateral de la calle y si la opción "usar
  teclado" está habilitada, NVDA anunciará las direcciones de las calles
  según utilices las teclas de flechas para navegar por el mapa.

## Microsoft Edge

Esto hace referencia al Microsoft Edge clásico basado en EdgeHTML.

* Se seguirá y se anunciará el texto de autocompletado en la barra de
  direcciones omni. Esto formará parte de NVDA 2019.3.
* NVDA ya no reproducirá el sonido de sugerencias de búsqueda al pulsar f11
  para conmutar la pantalla completa. Esto formará parte de NVDA 2019.3.
* Se ha eliminado la reproducción de sonidos de sugerencia en la barra de
  direcciones. Esto formará parte de NVDA 2019.3.

## Microsoft Store

* Después de buscar actualizaciones de aplicaciones, los nombres de las
  aplicaciones en la lista de aplicaciones etiquetadas se actualizan
  correctamente.
* Cuando se cargue contenido tal como aplicaciones y películas, NVDA
  anunciará el nombre del producto y el progreso de la descarga.

## Teclado Moderno

La mayoría de las siguientes características ya son parte de NVDA 2018.3 o
posterior.

* Soporte para el panel de entrada de Emoji en la versión 1709 (Fall
  Creators Update) y posteriores, incluyendo el panel rediseñado en la
  versión 1809 (versión 17661 y posteriores) y los cambios realizados en la
  19H1 (versión 18262 y posteriores, incluyendo kaomoji y categorías de
  símbolos en la versión 18305). Esto también se aplica en la compilación
  18963 y posteriores, a pesar de que se ha renombrado la aplicación. Si
  utilizas versiones de NVDA anteriores a 2018.4, para obtener la mejor
  experiencia al leer emojis, utiliza el sintetizador de voz Windows
  OneCore. Si se está utilizando 2018.4 o posterior, habilita la
  configuración de Unicode Consortium a partir de la configuración de voz de
  NVDA y establece el nivel de símbolos en "alguna" o superior.
* NVDA ya no dirá "portapapeles" cuando haya elementos en el portapapeles
  bajo algunas circunstancias.
* On some systems running Version 1903 (May 2019 Update) and later, NVDA
  will no longer appear to do nothing when emoji panel opens.
* Se ha añadido soporte para la interfaz de candidatos IME en chino moderno,
  japonés y coreano (CJK) introducida en la versión 20H1 a partir de la
  compilación 18965.

## Gente

* Cuando se busquen contactos, se verbalizará la primera sugerencia,
  particularmente si se usan versiones recientes de las aplicaciones.

## Opciones

* Cierta información como el progreso de Windows Update se anuncia
  automáticamente, incluyendo el widget de sensor de almacenamiento /
  limpieza de disco y los errores del propio Windows Update.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* En algunos cuadros combinados y botones de opción, NVDA ya no fallará al
  reconocer etiquetas y/o al anunciar cambios de valores.
* Audio Volume progress bar beeps are no longer heard in Version 1803 and
  later. This will be part of NVDA 2019.3.
* NVDA ya no parecerá hacer nada o reproducir tonos de error si se usan
  órdenes de navegación por objetos en algunas circunstancias.
* El diálogo de recordatorio de Windows Update se reconoce correctamente
  como un diálogo.
* Corregida disparidad en etiquetas de controles advertida en ciertas
  instalaciones de Windows.
* En revisiones más recientes de la versión 1803 y posterior, debido a los
  cambios en el procedimiento de Windows Update para actualizaciones de
  características, se ha añadido un enlace "Descargar e instalar
  ahora". NVDA anunciará ahora el título de la nueva actualización si está
  presente.

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

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
