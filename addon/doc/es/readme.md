# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2019.3 a 2020.1

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como Mejoras y correcciones para ciertos controles de
windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Calculadora (modern).
* Calendario
* Cortana (conversaciones)
* Correo
* Mapas
* Microsoft Solitaire Collection
* Microsoft Store
* Teclado Moderno (panel emoji / dictado / sugerencias de entrada hardware /
  elementos del portapapeles en la nube / editores modernos de método de
  entrada)
* Gente
* Opciones (opciones de sistema, Windows+I)
* El Tiempo.
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Notas:

* Este complemento requiere Windows 10 Versión 1903 (compilación 18362) o
  posterior. Para unos mejores resultados, utiliza el complemento con la
  compilación estable más reciente de Windows 10 (compilación 18363).
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
* Además de los diálogos reconocidos como tales por NVDA, ahora se reconocen
  más diálogos y se anuncian adecuadamente, como el diálogo Insider Preview
  (aplicación de configuración).
* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el panel Presentación de Objetos.
* Al buscar en el menú Inicio o el explorador de archivos de la versión 1909
  (actualización de noviembre de 2019) y posteriores, NVDA ya no anunciará
  tanto los resultados de búsqueda dos veces al revisarlos, lo que al mismo
  tiempo hace la salida braille más consistente al revisar elementos.
* Se reconocen los siguientes eventos UIA: Controller for, drag start, drag
  cancel, drag complete, drag target enter, drag target leave, drag target
  dropped, element selected, item status, live region change, notification,
  system alert, text change, tooltip opened, window opened. Con NVDA
  configurado para ejecutarse con el registro de depuración habilitado,
  estos eventos se seguirán, y se oirá un tono de depuración para el evento
  UIA notification si las notificaciones vienen de un lugar distinto a la
  aplicación actual.
* Es posible seguir sólo eventos específicos y/o eventos que vienen de
  aplicaciones específicas.
* Al abrir, cerrar o cambiar entre escritorios virtuales, NVDA anunciará el
  nombre del escritorio actual (escritorio 2, por ejemplo).
* NVDA ya no anuncia Menú Inicio tamaño de texto al cambiar la resolución de
  pantalla o la orientación.
* Al reordenar los elementos del menú Inicio o acciones rápidas del centro
  de actividades con alt+shift+flechas, NVDA anunciará información de los
  elementos arrastrados o su nueva posición.
* En las últimas versiones de Word 365, NVDA ya no anunciará "Eliminar
  palabra anterior" al pulsar control+retroceso.

## Calculadora

* Cuando se pulse INTRO o Escape, NVDA anunciará los resultados del cálculo.
* Para cálculos tales como conversión de unidades y conversión de moneda,
  NVDA anunciará los resultados tan pronto como los cálculos se introduzcan.
* NVDA ya no anunciará "Encabezado nivel" en los resultados de la
  calculadora.
* NVDA avisará si se alcanza la cantidad máxima de dígitos al introducir
  expresiones.
* Se ha añadido soporte para el modo Siempre Encendido de las versiones
  10.1908 y posteriores de la calculadora.

## Calendario

* NVDA ya no anuncia "editar" o "sólo lectura" en el cuerpo del mensaje y
  otros campos.

## Cortana

La mayoría de elementos ya no se aplican en la versión 1903 y posteriores a
menos que las conversaciones de Cortana (Versión 2004 y posteriores) estén
en uso.

* Las respuestas textuales de Cortana se verbalizan en la mayoría de
  situaciones.
* NVDA se silenciará cuando hables a Cortana a través de la voz.
* En la versión 1909 (actualización de noviembre de 2019) y posteriores, se
  soporta la interfaz de usuario de la experiencia de búsqueda moderna
  proporcionada por Windows Search en el explorador de Windows.

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

## Microsoft Solitaire Collection

* NVDA anunciará los nombres de las cartas y los montones de cartas.

## Microsoft Store

* Después de buscar actualizaciones de aplicaciones, los nombres de las
  aplicaciones en la lista de aplicaciones etiquetadas se actualizan
  correctamente.
* Cuando se cargue contenido tal como aplicaciones y películas, NVDA
  anunciará el nombre del producto y el progreso de la descarga.

## Teclado Moderno

Esto incluye el panel de emojis, historial del portapapeles, dictado,
sugerencias de entrada por hardware, y los editores modernos de métodos de
entrada para ciertos idiomas. Al visualizar emojis, para una mejor
experiencia, activa la opción del consorcio Unicode desde las opciones de
voz de NVDA y configura el nivel de símbolos en "alguno" o más alto.

* Al abrir el historial del portapapeles, NVDA ya no dirá "portapapeles"
  cuando haya elementos en el portapapeles bajo algunas circunstancias.
* En algunos sistemas que ejecutan la versión 1903 (actualización de mayo de
  2019) y posteriores, NVDA ya no parecerá hacer nada cuando el panel de
  emojis se abra.
* Se ha añadido soporte para la interfaz de candidatos IME en chino moderno,
  japonés y coreano (CJK) introducida en la versión 2004 (compilación 18965
  y posteriores).

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
* Cuando se lea un pronóstico, utiliza las flechas izquierda y derecha para
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
