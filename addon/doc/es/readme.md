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
* El Tiempo.
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Notas:

* Este complemento requiere Windows 10 Versión 1709 (compilación 16299) o
  posterior y NVDA 2018.2 o posterior. Para unos mejores resultados, utiliza
  el complemento con la compilación estable más reciente de Windows 10
  (compilación 17134) y la versión estable más reciente de NVDA.
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
* Para las entradas que no se listen a continuación, puedes asumir que las
  características son parte de NVDA, no se aplican porque el complemento no
  da soporte a versiones antiguas de Windows 10, o se han hecho cambios a
  las aplicaciones que permiten que ya no sea necesario aplicarlas.

Para ver una lista de cambios hechos entre cada actualización del
complemento, consulta el documento [changelogs for add-on releases][3].

## General

* Se reconocen los elementos de los submenús en diversas aplicaciones,
  incluyendo el menú de contexto para los elementos del menú Inicio y el
  menú de aplicación de Microsoft Edge (Redstone 5).
* Ahora se reconocen ciertos diálogos como diálogos apropiadamente y se
  anuncian como tales, como el diálogo Insider Preview (aplicación de
  configuración). Esta función formará parte de NVDA 2018.3.
* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el diálogo/panel Presentación de Objetos.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, element selected, live region change, notification,
  system alert, tooltip opened, window opened. Con NVDA configurado para
  ejecutarse con el registro de depuración habilitado, estos eventos se
  seguirán, y se oirá un tono de depuración para el elemento UIA
  notification si las notificaciones vienen de un lugar distinto a la
  aplicación actual.
* Añadida la capacidad de buscar actualizaciones del complemento (automática
  o manual) a través del diálogo Windows 10 App Essentials que se encuentra
  en el menú Preferencias de NVDA. Por defecto, se buscarán las
  actualizaciones para las versiones estable y de desarrollo automáticamente
  semanal o diáriamente, respectivamente.
* En algunas aplicaciones, se anuncia el texto en regiones vivas. Esto
  incluye alertas en Edge (incluyendo elementos marcados con
  aria-role=alert), resultados en la calculadora y otros. Ten en cuenta que
  esto podrá causar una verbalización por duplicado en algunos casos. Esto
  ya forma parte de NVDA 2018.3 y versiones posteriores.
* Las notificaciones de versiones de apps recientes en Windows 10 versión
  1709 (compilación 16299) en adelante se anuncian correctamente. NVDA
  2018.2 y las versiones posteriores ya las soportan, y la versión 2018.3 da
  soporte a más notificaciones.
* Se reconocerán y anunciarán los consejos para Edge y para aplicaciones
  universales.
* Con los conjuntos activados (compilaciones 17627 a 17692 para algunos
  insiders), al abrir una nueva pestaña de conjuntos (control+windows+t),
  NVDA indicará los resultados de búsqueda al buscar elementos en la ventana
  incrustada de Cortana.
* Con los conjuntos activados, al saltar entre pestañas de Conjuntos, NVDA
  anunciará nombre y posición de la pestaña hacia la cual se está
  conmutando.
* Al abrir, cerrar o cambiar entre escritorios virtuales, NVDA anunciará el
  ID del escritorio actual (escritorio 2, por ejemplo).
* NVDA ya no anuncia Menú Inicio tamaño de texto al cambiar la resolución de
  pantalla o la orientación.

## Alarmas y reloj

* Ahora se anuncian los valores del selector de hora. Esto también afecta al
  control utilizado para seleccionar cuándo reiniciar para finalizar la
  instalación de las actualizaciones de Windows.

## Calculadora

* Cuando se pulse INTRO o Escape, NVDA anuncia los resultados del cálculo.
* Para cálculos tales como conversión de unidades y conversión de moneda,
  NVDA anunciará los resultados tan pronto como los cálculos se introduzcan.
* NVDA ya no anunciará "Encabezado nivel" en los resultados de la
  calculadora.

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
  Barra de Juegos en compilaciones anteriores a la 17723.

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

* Ahora se anuncian notificaciones tales como descargas de ficheros,
  diversas alertas de páginas web, así como la disponibilidad de la vista de
  lectura (si se usa la versión 1709 o posterior).

## Teclado Moderno

* Soporte para el panel flotante de entrada de Emoji en la actualización
  1709 (Fall Creators) o posterior, incluyendo el panel rediseñado en la
  compilación 17661 y posterior. Para unos mejores resultados, leyendo
  emojis utiliza el sintetizador de voz Windows OneCore.
* Soporte para sugerencias de entrada de teclado hardware en la versión 1803
  (actualización de Abril de 2018).
* En las versiones posteriores a 1709, NVDA anunciará el primer emoji
  seleccionado cuando se abra el panel de emoji.
* Soporte para el anunciado de elementos del cloud clipboard en la
  compilación 17666 (Redstone 5) y posterior.
* Se ha reducido la verbalización de información innecesaria al trabajar con
  el teclado moderno y sus funciones. Esto incluye no verbalizar más
  "Microsoft Candidate UI" al abrir las sugerencias de entrada del teclado
  hardware y permanecer en silencio cuando ciertas teclas del teclado táctil
  disparan un evento de cambio de nombre en algunos sistemas.

## Gente

* Cuando se busquen contactos, se verbalizará la primera sugerencia,
  particularmente si se usan versiones recientes de las aplicaciones.

## Opciones

* Cierta información tal como el progreso de la Actualización de Windows
  ahora se anuncia automáticamente.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* Los grupos de opciones se reconocen cuando se utilice la navegación de
  objetos para navegar entre controles.
* Para algunos cuadros combinados, NVDA ya no fallará al reconocer etiquetas
  y/o al anunciar cambios de valores.
* Los pitidos de la barra de progreso de volumen de audio ya no se oyen en
  la versión 1803 y posterior.
* Se anuncian más mensajes de estado de Windows Update, especialmente si
  este encuentra errores.

## Skype

* Al teclear el indicador de texto se anuncia sólo como cliente Skype para
  Escritorio.
* Las órdenes control+NVDA+fila de números, usadas para leer el historial
  reciente del chat y mover el navegador de objetos a las entradas de chat
  en Skype para escritorio, también están disponibles en Skype UWP.
* Ahora puedes pulsar Alt+fila de números para localizar y mover a
  conversaciones (1), lista de contactos (2), bots (3) y campo de edición de
  chat si está visible (4). Ten en cuenta que estas órdenes funcionarán
  apropiadamente si está instalada la actualización de Skype liberada en
  Marzo de 2017.
* NVDA ya no anuncia "Mensaje Skype" cuando se revisen mensajes para la
  mayoría de los casos.
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

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
