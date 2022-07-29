# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2021.3 en adelante

Nota: originalmente llamado Windows 10 App Essentials, se renombró a Windows
App Essentials en 2021 para soportar Windows 10 y versiones futuras, como
Windows 11. Algunas partes de este complemento aún harán referencia al
nombre original del mismo.

Este complemento es una colección de módulos de aplicación para varias
aplicaciones de Windows, así como Mejoras y correcciones para ciertos
controles de windows 10 o posterior.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Calculadora
* Cortana
* Mapas
* Teclado Moderno (panel de emojis / dictado / escritura por voz /
  sugerencias de entrada hardware / historial del portapapeles / acciones
  sugeridas (preview) / editores modernos de método de entrada)
* Bloc de notas (Windows 11)
* Gente
* Opciones (opciones de sistema, Windows+I)
* Acceso por voz (Windows 11 22H2)
* El Tiempo
* Módulos varios para controles tales como los mosaicos del Menú Inicio

Notas:

* Este complemento requiere Windows 10 Versión 21H1 (compilación 19043),
  Windows 11 21H2 (compilación 22000) o versiones posteriores.
* Aunque la instalación es posible, este complemento no soporta Windows
  Enterprise LTSC (canal de servicio a largo plazo) ni las versiones de
  Windows Server.
* No se soportarán todas las funciones de las compilaciones Windows Insider
  Preview.
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
* Para las entradas que no se enumeren a continuación, puedes asumir que las
  características son parte de NVDA, no se aplican porque el complemento no
  da soporte a versiones de Windows no soportadas, como versiones antiguas
  de Windows 10, o se han hecho cambios a las aplicaciones que permiten que
  ya no sea necesario aplicarlas.
* Algunas aplicaciones soportan el modo de superposición compacta (siempre
  visible en la calculadora, por ejemplo), y este modo no funcionará
  adecuadamente con la versión portable de NVDA.
* Para tener la mejor experiencia posible con aplicaciones que incrustan
  tecnologías y contenidos web, como el menú Inicio y su menú contextual,
  activa la opción "Modo Foco automático para cambios del foco" desde el
  panel de opciones Modo exploración de NVDA.

Para ver una lista de cambios hechos entre cada actualización del
complemento, consulta el documento [changelogs for add-on releases][3].

## General

* Además de los manejadores de eventos UIA proporcionados por NVDA, se
  reconocen los siguientes eventos y propiedades UIA: drag complete, drag
  drop effect, drop target dropped. Con el nivel de registro de NVDA
  configurado en depuración, estos eventos se rastrearán y se registrarán.
* Al abrir, cerrar, reordenar (Windows 11) o cambiar entre escritorios
  virtuales, NVDA anunciará el nombre del escritorio virtual activo
  (escritorio 2, por ejemplo).
* Al reordenar entradas ancladas (losas en Windows 10) del menú Inicio o
  acciones rápidas del centro de actividades con alt+shift+flechas, NVDA
  anunciará información de los elementos arrastrados o su nueva posición.
* Algunos anuncios, como los de cambio de brillo o volumen en el explorador
  de archivos y las notificaciones de actualización de aplicaciones de la
  tienda Microsoft pueden suprimirse desactivando Anunciar notificaciones
  desde las opciones de presentación de objetos de NVDA.
* En Windows 11 22H2 y posterior, el estado del interruptor para silenciar
  el micrófono (Windows+alt+k) se anuncia desde cualquier sitio.
* NVDA ya no repetirá la salida de texto en la terminal de Windows versión
  1.12.10733 y posteriores. Esto ahora forma parte de NVDA 2022.1.
* NVDA anunciará una vez más los detalles del resultado de búsqueda en el
  menú Inicio. Esto ahora forma parte de NVDA 2022.2.
* En Windows 11, se pueden detectar adecuadamente los elementos de la barra
  de tareas y otros controles de interfaz de usuario cuando se usa el ratón
  o la interacción táctil. Esto ahora forma parte de NVDA 2022.2.

## Calculadora

* En Windows 10, los elementos de historial y lista de memoria se etiquetan
  correctamente. Esto ahora forma parte de NVDA 2022.1.
* NVDA anunciará el contenido de la pantalla de la calculadora al realizar
  comandos en modo científico, tales como operaciones trigonométricas. Esto
  ahora forma parte de NVDA 2022.2.

## Cortana

* Las respuestas textuales de Cortana se verbalizan en la mayoría de
  situaciones.
* NVDA se silenciará cuando hables a Cortana a través de la voz.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.

## Teclado Moderno

Esto incluye el panel de emojis, historial del portapapeles, dictado /
escritura por voz, sugerencias de entrada por hardware, acciones sugeridas
(preview) y los editores modernos de métodos de entrada para ciertos idiomas
en Windows 10 y 11. Al visualizar emojis, para una mejor experiencia, activa
la opción del consorcio Unicode desde las opciones de voz de NVDA y
configura el nivel de símbolos en "alguno" o más alto. Al pegar desde el
portapapeles en Windows 10, pulsa la barra espaciadora en vez de intro para
pegar el elemento seleccionado.

* En Windows 10, cuando se seleccione un grupo de emojis (incluyendo kaomoji
  y el grupo de símbolos), NVDA ya no moverá el navegador de objetos a
  ciertos emojis.
* En Windows 11, vuelve a ser posible usar las flechas para revisar los
  emojis cuando se abre el panel de emojis. Esto ahora forma parte de NVDA
  2022.1.
* En el historial del portapapeles de Windows 11, se desactivará el modo
  exploración por defecto, diseñado para permitir que NVDA anuncie los
  elementos de menú con las entradas del historial del portapapeles.
* En la compilación Insider Preview 25115 y posterior (traído a Windows 11
  beta 22622), NVDA anunciará las acciones sugeridas cuando se copien al
  portapapeles datos compatibles, como números de teléfono.

## Bloc de notas

Esto hace referencia al Bloc de notas de Windows 11, versión 11 o posterior.

* NVDA anunciará elementos de estado, como la información de línea y
  columna, cuando se ejecute la orden para anunciar la barra de estado
  (NVDA+fin en disposición de escritorio, NVDA+shift+fin en disposición
  portátil). Esto ahora forma parte de NVDA 2022.2.

## Gente

* Cuando se busquen contactos, se verbalizará la primera sugerencia,
  particularmente si se usan versiones recientes de las aplicaciones.

## Opciones

* Corregidas etiquetas de controles defectuosas advertidas en ciertas
  instalaciones de Windows.
* NVDA anunciará el nombre del enlace de la actualización de calidad
  opcional si está presente (enlace Descargar e instalar ahora en Windows
  10, botón Descargar en Windows 11).
* En Windows 11, los elementos de la barra de migas de pan se reconocen
  correctamente.
* En Windows 10 y 11 22H2 y posterior, NVDA interrumpirá la voz y anunciará
  las actualizaciones del estado de Windows Update según avancen la descarga
  e instalación. Esto puede resultar en interrupciones de voz al navegar por
  la aplicación de configuración mientras las actualizaciones se descargan y
  se instalan. Si usas Windows 11 22H2 y posterior y el registro selectivo
  de eventos UIA está activado, debes mover el foco a la lista de
  actualizaciones tan pronto como aparezcan para que NVDA pueda anunciar el
  progreso de la actualización.

## Acceso por voz

Esto hace referencia a la función de acceso por voz introducida en Windows
11 22H2.

* NVDA anunciará el estado del micrófono al conmutarlo desde la interfaz del
  acceso por voz.

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
