# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2018.4 a 2019.2

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como Mejoras y correcciones para ciertos controles de
windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Centro de actividades
* Reloj y alarmas.
* Calendario
* Calculadora (modern).
* Cortana
* Centro de opiniones
* Correo
* Mapas
* Microsoft Edge
* Teclado Moderno (panel emoji / dictado / sugerencias de entrada hardware /
  elementos del portapapeles en la nube en la Versión 1709 y posterior)
* Gente
* Opciones (opciones de sistema, Windows+I)
* Tienda
* El Tiempo.
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Notas:

* Este complemento requiere Windows 10 Versión 1803 (compilación 17134) o
  posterior y NVDA 2018.4 o posterior. Para unos mejores resultados, utiliza
  el complemento con la compilación estable más reciente de Windows 10
  (compilación 18362) y la versión estable más reciente de NVDA.
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
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA: active text position change,
  Controller for, drag start, drag cancel, drag complete, element selected,
  item status, live region change, notification, system alert, text change,
  tooltip opened, window opened. Con NVDA configurado para ejecutarse con el
  registro de depuración habilitado, estos eventos se seguirán, y se oirá un
  tono de depuración para el evento UIA notification si las notificaciones
  vienen de un lugar distinto a la aplicación actual.
* Se reconocerán y anunciarán los consejos para Edge y para aplicaciones
  universales.
* Al abrir, cerrar o cambiar entre escritorios virtuales, NVDA anunciará el
  nombre del escritorio actual (escritorio 2, por ejemplo).
* NVDA ya no anuncia Menú Inicio tamaño de texto al cambiar la resolución de
  pantalla o la orientación.
* En la versión 1903 (actualización de mayo de 2019), NVDA anunciará
  inmediatamente los cambios de brillo y volumen.

## Centro de actividades

* La acción rápida de brillo es ahora un botón en vez de un botón
  conmutador. Ahora ya forma parte de NVDA 2019.1.
* Se anuncian diversos cambios de estado, como la ayuda al enfoque o el
  brillo. Ahora ya forma parte de NVDA 2019.1.

## Alarmas y reloj

* Ahora se anuncian los valores del selector de hora. Esto también afecta al
  control utilizado para seleccionar cuándo reiniciar para finalizar la
  instalación de las actualizaciones de Windows.Ahora ya  forma parte de
  NVDA 2019.1.

## Calculadora

* Cuando se pulse INTRO o Escape, NVDA anuncia los resultados del cálculo.
* Para cálculos tales como conversión de unidades y conversión de moneda,
  NVDA anunciará los resultados tan pronto como los cálculos se introduzcan.
* NVDA ya no anunciará "Encabezado nivel" en los resultados de la
  calculadora.
* NVDA avisará si se alcanza la cantidad máxima de dígitos al introducir
  expresiones.

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

## Correo

* Cuando se revisan elementos en la lista de mensajes, ahora puedes utilizar
  órdenes de navegación de tablas para revisar los encabezados de
  mensaje. Ten en cuenta que no está soportado navegar por filas (mensajes).
* Cuando se escribe un mensaje, la apariencia de la mención de sugerencias
  se indica con sonidos.
* NVDA ya no parecerá hacer nada o reproducir tonos de error después de
  cerrar esta aplicación. Ahora ya es parte de NVDA 2019.1.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.
* Cuando se utiliza la vista lateral de la calle y si la opción "usar
  teclado" está habilitada, NVDA anunciará las direcciones de las calles
  según utilices las teclas de flechas para navegar por el mapa.

## Microsoft Edge

* Se seguirá y se anunciará el texto de autocompletado en la barra de
  direcciones omni.
* NVDA ya no reproducirá el sonido de sugerencias de búsqueda al pulsar f11
  para conmutar la pantalla completa.

## Teclado Moderno

Nota: la mayoría de las siguientes características ya son parte de NVDA
2018.3 o posterior.

* Soporte para el panel de entrada de Emoji en la versión 1709 (Fall
  Creators Update) y posteriores, incluyendo el panel rediseñado en la
  versión 1809 (versión 17661 y posteriores) y los cambios realizados en la
  19H1 (versión 18262 y posteriores, incluyendo kaomoji y categorías de
  símbolos en la versión 18305). Si utilizas versiones de NVDA anteriores a
  2018.4, para obtener la mejor experiencia al leer emojis, utiliza el
  sintetizador de voz Windows OneCore. Si se está utilizando 2018.4 o
  posterior, habilita la configuración de Unicode Consortium a partir de la
  configuración de voz de NVDA y establece el nivel de símbolos en "alguna"
  o superior.
* Soporte para sugerencias de entrada de teclado hardware en la versión 1803
  (actualización de Abril de 2018).
* En las versiones posteriores a 1709, NVDA anunciará el primer emoji
  seleccionado cuando se abra el panel emoji. Esto se nota más en la versión
  18262 y posteriores, donde el panel emoji puede abrirse hasta la última
  categoría por la que se haya navegado, así como mostrar modificadores de
  tono de piel cuando se abra en la categoría Personas.
* Soporte para el anunciado de elementos del portapapeles en la nube en la
  versión 1809 (compilación 17666 y posterior).
* Se ha reducido la verbalización de información innecesaria al trabajar con
  el teclado moderno y sus funciones. Esto incluye no verbalizar más
  "Microsoft Candidate UI" al abrir las sugerencias de entrada del teclado
  hardware y permanecer en silencio cuando ciertas teclas del teclado táctil
  disparan un evento de cambio de nombre en algunos sistemas.
* NVDA ya no reproducirá tonos de error o se quedará sin hacer nada al
  cerrar el panel de emojis en las versiones más recientes de Windows
  Insider Preview 19H1. Esto ya forma parte de NVDA 2019.1.
* En la Versión 1809 (October 2018 Update) y posteriores, NVDA verbalizará
  los resultados de búsqueda para emojis si es posible. Esta función ya
  forma parte de NVDA 2019.1.
* NVDA ya no dirá "portapapeles" cuando haya elementos en el portapapeles
  bajo algunas circunstancias.
* En algunos sistemas que ejecutan la versión 1903 (actualización de mayo de
  2019), NVDA ya no parecerá hacer nada cuando el panel de emojis se abra.

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
* Los pitidos de la barra de progreso de volumen de audio ya no se oyen en
  la versión 1803 y posterior.
* NVDA ya no parecerá hacer nada o reproducir tonos de error si se usan
  órdenes de navegación por objetos en algunas circunstancias.
* El diálogo de recordatorio de Windows Update se reconoce correctamente
  como un diálogo.
* Corregida disparidad en etiquetas de controles advertida en ciertas
  instalaciones de Windows.

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

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
