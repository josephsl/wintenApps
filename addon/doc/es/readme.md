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
* Bank of America
* Calendario
* Calculadora (modern).
* Cortana
* Correo
* Mapas
* Microsoft Edge
* Opciones (opciones de sistema, Windows+I).
* Previsualización de Skype
* Tienda
* Twitter.
* TeamViewer Touch.
* El Tiempo
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Nota: este complemento requiere de Windows 10 Versión 1507 (compilación
10240) o posterior y NVDA 2016.3 o posterior. Para unos mejores resultados,
utiliza el complemento con la compilación estable más reciente (compilación
14393).

## General

* En menús de contexto para los mosaicos del Menú Inicio, los submenús ahora
  se reconocen apropiadamente.
* Al minimizar windows (Windows+M), ya no se anuncia "panel" ­(­perceptible
  si se utilizan compilaciones Insider Preview).
* Ahora se reconocen ciertos diálogos como diálogos apropiadamente. Esto
  incluye el diálogo Insider Preview (aplicación de configuración) y el
  diálogo de nuevo estilo del UAC en la compilación 14328 y posteriores para
  NvDA 2016.2.1 o anteriores.
* La apariencia/cierre de sugerencias para ciertos campos de búsqueda (en
  particular la app Opciones) se anuncian a través de sonidos y/o de
  braille.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA: Controller para, live region
  cambiada (manejada por  evento de cambio de nombre).

## Alarmas y reloj

* Ahora se anuncian los valores del selector de hora. Esto también afecta al
  control utilizado para seleccionar cuándo reiniciar para finalizar la
  instalación de las actualizaciones de Windows.

## Calendario y Correo

* NVDA ya no anuncia "solo lectura" para el asunto de la cita en Calendario
  y contenidos de mensajes en Correo.

## Calculadora

* Cuando se pulse INTRO, NVDA anuncia los resultados del cálculo.

## Cortana

* Las respuestas textuales de Cortana se anuncian en la mayoría de las
  situaciones (si no se reabre el menú Inicio y  se trata de buscar de
  nuevo).
* NVDA se silenciará cuando hables a Cortana a través de la voz.
* NVDA ahora anunciará confirmación de recuerdo después de configurarla.

## Correo y calendario

* NVDA ya no anuncia "editar" o "sólo lectura" en el cuerpo del mensaje y
  otros campos.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.

## Microsoft Edge

* Ahora se anuncian notificaciones tales como descargas de ficheros.
* Ten en cuenta que el soporte global es experimental en este momento (No
  deberías utilizar Edge como tu navegador principal por ahora).

## Opciones

* Cierta información tal como el progreso de la Actualización de Windows
  ahora se anuncia automáticamente.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* Si se toma un tiempo para buscar la configuración, NVDA anunciará
  "buscando" y el estado de los resultados de búsqueda tal como si una
  ocpión no se encontrara.

## Previsualización de Skype

* Al teclear el indicador de texto se anuncia sólo como cliente Skype para
  Escritorio.
* Retorno parcial de las órdenes Control+NVDA+fila de números para leer el
  historial de chats recientes y para mover el navegador de objetos a las
  entradas de chat como en Skype para Escritorio.
* Ahora puedes pulsar Alt+fila de números para localizar y mover a lista de
  contactos (1), conversaciones (2) y campo de edición de chat (3). Ten en
  cuenta que deben activarse esas pestañas para moverse a la parte decidida.

## Tienda

* Después de buscar actualizaciones de aplicaciones, los nombres de las
  aplicaciones en la lista de aplicaciones etiquetadas se actualizan
  correctamente.

## TeamViewer Touch

* Se anuncian las etiquetas para botones de opción.
* Se anuncian las etiquetas para botones de opción.

## Bank of America/Twitter

* Ahora se anuncian las etiquetas de los botones.

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

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
