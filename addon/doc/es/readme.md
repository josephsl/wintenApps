# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: 2020.4 y posterior

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como Mejoras y correcciones para ciertos controles de
windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Calculadora (moderna).
* Calendario
* Cortana (conversaciones)
* Correo
* Mapas
* Microsoft Solitaire Collection
* Microsoft Store
* Teclado Moderno (panel de emojis / dictado / sugerencias de entrada
  hardware / historial del portapapeles / editores modernos de método de
  entrada)
* Gente
* Opciones (opciones de sistema, Windows+I)
* El Tiempo
* Módulos varios para controles tales como los mosaicos del Menú Inicio

Notas:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows release (Windows 10
  Version 21H1/build 19043).
* Although installation is possible, this add-on does not support Windows
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
* For entries not listed below, you can assume that features are part of
  NVDA, no longer applicable as the add-on does not support older Windows
  releases, or changes were made to Windows and apps that makes entries no
  longer applicable.
* Algunas aplicaciones soportan el modo de superposición compacta (siempre
  visible en la calculadora, por ejemplo), y este modo no funcionará
  adecuadamente con la versión portable de NVDA.

Para ver una lista de cambios hechos entre cada actualización del
complemento, consulta el documento [changelogs for add-on releases][3].

## General

* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el panel Presentación de Objetos.
* Al buscar en el menú Inicio o el explorador de archivos de la versión 1909
  (actualización de noviembre de 2019) y posteriores, NVDA ya no anunciará
  tanto los resultados de búsqueda dos veces al revisarlos, lo que al mismo
  tiempo hace la salida braille más consistente al revisar elementos.
* Además de los manejadores de eventos UIA proporcionados por NVDA, se
  reconocen los siguientes eventos UIA: drag start, drag cancel, drag
  complete, drop target drag enter, drop target drag leave, drop target
  dropped. Con NVDA configurado para ejecutarse con el registro de
  depuración habilitado, estos eventos se seguirán, y se oirá un tono de
  depuración para el evento UIA notification si las notificaciones vienen de
  un lugar distinto a la aplicación actual. Algunos eventos proporcionarán
  información adicional, como la cantidad de elementos en el evento
  Controller for, el estado del elemento en el evento State change, y el
  texto del elemento en el evento Item status.
* Es posible seguir sólo eventos específicos y/o eventos que vienen de
  aplicaciones específicas.
* Al abrir, cerrar, reordenar (compilación 21337 o posterior) o cambiar
  entre escritorios virtuales, NVDA anunciará el nombre del escritorio
  virtual activo (escritorio 2, por ejemplo).
* NVDA ya no anunciará el tamaño del texto del Menú Inicio al cambiar la
  resolución de pantalla o la orientación.
* Al reordenar los elementos del menú Inicio o acciones rápidas del centro
  de actividades con alt+shift+flechas, NVDA anunciará información de los
  elementos arrastrados o su nueva posición.
* Algunos anuncios, como los de cambio de brillo o volumen en el explorador
  de archivos y las notificaciones de actualización de aplicaciones de la
  tienda Microsoft pueden suprimirse desactivando Anunciar notificaciones
  desde las opciones de presentación de objetos de NVDA.

## Calculadora

* NVDA ya no anunciará dos veces el mensaje en pantalla de la calculadora
  gráfica.

## Calendario

* NVDA ya no anuncia "editar" o "sólo lectura" en el cuerpo del mensaje y
  otros campos.

## Cortana

La mayoría de elementos se aplican al usar las conversaciones de Cortana
(versión 2004 y posteriores).

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
voz de NVDA y configura el nivel de símbolos en "alguno" o más alto. NVDA
también soporta el panel actualizado de experiencia de entrada, disponible
en la compilación 21296 y posteriores.

* Al abrir el historial del portapapeles, NVDA ya no dirá "portapapeles"
  cuando haya elementos en el portapapeles bajo algunas circunstancias.
* En algunos sistemas que ejecutan la versión 1903 (actualización de mayo de
  2019) y posteriores, NVDA ya no parecerá hacer nada cuando el panel de
  emojis se abra.
* Cuando se seleccione un grupo de emojis (incluyendo kaomoji y el grupo de
  símbolos en la versión 1903 o posteriores), NVDA ya no moverá el navegador
  de objetos a ciertos emojis.
* Se ha añadido soporte para el panel actualizado de experiencia de entrada
  (una combinación del panel de emojis y el historial del portapapeles) en
  la compilación 21296 y posteriores.

## Gente

* Cuando se busquen contactos, se verbalizará la primera sugerencia,
  particularmente si se usan versiones recientes de las aplicaciones.

## Opciones

* Cierta información como el progreso de Windows Update se anuncia
  automáticamente, incluyendo el widget de sensor de almacenamiento /
  limpieza de disco y los errores del propio Windows Update.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* El diálogo de recordatorio de Windows Update se reconoce correctamente
  como un diálogo.
* Odd control labels seen in certain Windows installations has been
  corrected.
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
