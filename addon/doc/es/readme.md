# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2022.2 en adelante

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
* Teclado Moderno (panel de emojis / dictado / escritura por voz /
  sugerencias de entrada hardware / historial del portapapeles / acciones
  sugeridas / editores modernos de método de entrada)
* Gente
* Opciones (opciones de sistema, Windows+I)
* Acceso por voz (Windows 11 22H2)
* El Tiempo
* Módulos varios para controles tales como los mosaicos del Menú Inicio

Notas:

* Este complemento requiere Windows 10 Versión 21H2 (compilación 19044), 11
  21H2 (compilación 22000) o versiones posteriores.
* Aunque la instalación es posible, este complemento no soporta Windows
  Enterprise LTSC (canal de servicio a largo plazo) ni las versiones de
  Windows Server.
* Si está instalado Add-on Updater 22.08 o posterior y están activadas las
  actualizaciones en segundo plano, Windows App Essentials no se instalará
  en absoluto en versiones no soportadas de Windows.
* No se soportarán todas las funciones de las compilaciones Windows Insider
  Preview.
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
* Para las entradas que no se enumeren a continuación, puedes asumir que las
  características son parte de NVDA, no se aplican porque el complemento ya
  no da soporte a versiones de Windows no soportadas, como versiones
  antiguas de Windows 10, o se han hecho cambios a Windows, las aplicaciones
  y NVDA que permiten que ya no sea necesario aplicarlas.
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
  reconocen los siguientes eventos y propiedades UIA: drag
  start/cancel/complete (reconocido como evento de cambio de estado), drag
  drop effect, drag item is grabbed, drop target effect.
* Al abrir, cerrar o cambiar entre escritorios virtuales, NVDA anunciará el
  nombre del escritorio virtual activo (escritorio 2, por ejemplo).
* Al arrastrar y soltar elementos, como reordenar entradas ancladas (losas
  en Windows 10) del menú Inicio o acciones rápidas del centro de
  actividades con alt+shift+flechas, NVDA anunciará "arrastrando" o los
  efectos de arrastrar y soltar antes y mientras se arrastran,
  respectivamente. Esto ahora forma parte de NVDA 2022.4.
* Anuncios como los de cambio de brillo, volumen o silencio del micrófono
  (Windows 11 22H2 y posterior) en el explorador de archivos y las
  notificaciones de actualización de aplicaciones de la tienda Microsoft
  pueden suprimirse desactivando Anunciar notificaciones desde las opciones
  de presentación de objetos de NVDA.
* En Windows 11, NVDA anunciará las búsquedas destacadas en el menú Inicio
  cuando se abra.

## Cortana

* Las respuestas textuales de Cortana se verbalizan en la mayoría de
  situaciones.
* NVDA se silenciará cuando hables a Cortana a través de la voz.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.

## Teclado Moderno

Esto incluye el panel de emojis, historial del portapapeles, dictado /
escritura por voz, sugerencias de entrada por hardware, acciones sugeridas y
los editores modernos de métodos de entrada para ciertos idiomas en Windows
10 y 11. Al visualizar emojis, para una mejor experiencia, activa la opción
del consorcio Unicode desde las opciones de voz de NVDA y configura el nivel
de símbolos en "alguno" o más alto. Al pegar desde el portapapeles en
Windows 10, pulsa la barra espaciadora en vez de intro para pegar el
elemento seleccionado.

* En el panel de emojis de Windows 10, cuando se seleccione un grupo de
  emojis (incluyendo kaomoji y el grupo de símbolos), NVDA ya no moverá el
  navegador de objetos a ciertos emojis.
* En el historial del portapapeles de Windows 11, se desactivará el modo
  exploración por defecto, diseñado para permitir que NVDA anuncie los
  elementos de menú con las entradas del historial del portapapeles.
* En Windows 11 22H2 Moment 1 y posterior, NVDA anunciará las acciones
  sugeridas cuando se copien al portapapeles datos compatibles, como números
  de teléfono.

## Gente

* Cuando se busquen contactos, se verbalizará la primera sugerencia.

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
