# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2022.4 en adelante

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

* Cortana
* Mapas
* Teclado Moderno (panel de emojis / teclado táctil / dictado / escritura
  por voz / sugerencias de entrada hardware / historial del portapapeles /
  acciones sugeridas / editores modernos de método de entrada)
* Opciones (opciones de sistema, Windows+I)
* Acceso por voz (Windows 11 22H2)
* El Tiempo
* Módulos varios para controles y funciones tales como los anuncios de
  escritorios virtuales

Notas:

* Este complemento requiere Windows 10 Versión 21H2 (compilación 19044), 11
  21H2 (compilación 22000) o versiones posteriores.
* La duración del soporte de las actualizaciones de características está
  vinculada a la duración del soporte al cliente (ediciones Home, Pro, Pro
  Education, Pro for Workstations), y el complemento podría finalizar el
  soporte para una actualización de características antes del fin del
  soporte al cliente. Consulta aka.ms/WindowsTargetVersioninfo para más
  información y fechas de soporte.
* Aunque la instalación es posible, este complemento no soporta Windows
  Enterprise LTSC (canal de servicio a largo plazo) ni las versiones de
  Windows Server.
* Si está instalado Add-on Updater y están activadas las actualizaciones en
  segundo plano, Windows App Essentials no se instalará en absoluto en
  versiones no soportadas de Windows.
* No se soportarán todas las funciones de las compilaciones Windows Insider
  Preview, más si se introducen en un subconjunto de insiders de Windows en
  el canal de desarrollo. En el canal beta, sólo se soporta la última
  compilación (22623).
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
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

* Al abrir, cerrar o cambiar entre escritorios virtuales, NVDA anunciará el
  nombre del escritorio virtual activo (escritorio 2, por ejemplo).
* En Windows 11, NVDA anunciará las búsquedas destacadas en el menú Inicio
  cuando se abra. Esto ahora forma parte de NVDA 2023.1.
* En Windows 11 22H2 y posterior, se puede interactuar con la ventana
  flotante rediseñada de la bandeja del sistema (Moment 2) y con el diálogo
  Abrir con al usar interacción táctil o del ratón. Esto ahora forma parte
  de NVDA 2023.1.
* NVDA registrará la arquitectura del procesador de la instalación actual de
  Windows (x86/32 bits, AMD64, ARM64) cuando se inicie. Esto ahora forma
  parte de NVDA 2023.1.
* Experiencia mejorada con la barra de tareas de Windows 11, incluyendo el
  anuncio de los resultados al reordenar iconos pulsando las teclas
  alt+shift+flechas izquierda y derecha (antes de la compilación 25267) e
  indicando la posición del elemento al moverse por iconos de la barra de
  tareas (Windows 10 y 11 antes de la compilación 25281).
* NVDA anunciará el texto de carpeta vacía dentro de las carpetas vacías en
  el explorador de archivos.
* En aplicaciones como el explorador de archivos y el bloc de notas, donde
  se soportan ventanas con pestañas, NVDA anunciará el nombre y la posición
  de las pestañas al pasar entre ellas.

## Cortana

* Las respuestas textuales de Cortana se verbalizan en la mayoría de
  situaciones.
* NVDA se silenciará cuando hables a Cortana a través de la voz.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.
* NVDA ya no interrumpirá la voz al tener el foco en elementos distintos al
  control del mapa en algunos casos.

## Teclado Moderno

Esto incluye el panel de emojis, historial del portapapeles, teclado táctil,
dictado / escritura por voz, sugerencias de entrada por hardware, acciones
sugeridas y los editores modernos de métodos de entrada para ciertos idiomas
en Windows 10 y 11. Al visualizar emojis, para una mejor experiencia, activa
la opción del consorcio Unicode desde las opciones de voz de NVDA y
configura el nivel de símbolos en "alguno" o más alto. Al pegar desde el
historial del portapapeles en Windows 10, pulsa la barra espaciadora en vez
de intro para pegar el elemento seleccionado.

* En el panel de emojis de Windows 10, cuando se seleccione un grupo de
  emojis (incluyendo kaomoji y el grupo de símbolos), NVDA ya no moverá el
  navegador de objetos a ciertos emojis.
* En el historial del portapapeles de Windows 11, se desactivará el modo
  exploración por defecto, diseñado para permitir que NVDA anuncie los
  elementos de menú con las entradas del historial del portapapeles. Esto
  ahora forma parte de NVDA 2023.1.
* En Windows 11 22H2 y posterior, NVDA anunciará las acciones sugeridas
  cuando se copien al portapapeles datos compatibles, como números de
  teléfono.

## Opciones

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
