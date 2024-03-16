# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros

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

* Teclado Moderno
* Configuración (Windows+I)

Notas:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* La duración del soporte de las actualizaciones de características está
  vinculada a la duración del soporte al cliente (ediciones Home, Pro, Pro
  Education, Pro for Workstations), y el complemento podría finalizar el
  soporte para una actualización de características antes del fin del
  soporte al cliente. Consulta <https://aka.ms/WindowsTargetVersioninfo>
  para más información y fechas de soporte.
* Aunque la instalación es posible, este complemento no soporta Windows
  Enterprise LTSC (canal de servicio a largo plazo) ni las versiones de
  Windows Server.
* No se soportarán todas las funciones de las compilaciones Windows Insider
  Preview, más si se introducen en un subconjunto de insiders de Windows en
  los canales dev y canary.
* El complemento puede emular correcciones incluidas en compilaciones
  preliminares de Insider que posteriormente se eliminan, y en estos casos,
  el complemento podría eliminarlas en versiones futuras.
* El canal de desarrollo del complemento incluirá entre sus cambios
  contenido experimental que podrá ir o no en las versiones beta y estables,
  y el canal beta vendrá con cambios planeados para versiones estables
  futuras.
* Algunas de las características del complemento son o serán parte del
  lector de pantalla NVDA.
* Para tener la mejor experiencia posible con aplicaciones que incrustan
  tecnologías y contenidos web, como el menú Inicio y su menú contextual,
  activa la opción "Modo Foco automático para cambios del foco" desde el
  panel de opciones Modo exploración de NVDA.

Para ver una lista de cambios hechos entre cada actualización del
complemento, consulta el documento [Registros de cambios de versiones del
complemento (en inglés)][1].

## Teclado Moderno

Esto incluye el panel de emojis, historial del portapapeles, teclado táctil,
dictado / escritura por voz, sugerencias de entrada por hardware, acciones
sugeridas y los editores modernos de métodos de entrada para ciertos idiomas
en Windows 10 y 11. Al visualizar emojis, para una mejor experiencia, activa
la opción del consorcio Unicode desde las opciones de voz de NVDA y
configura el nivel de símbolos en "alguno" o más alto. Al pegar desde el
historial del portapapeles en Windows 10, pulsa la barra espaciadora en vez
de intro para pegar el elemento seleccionado.

* En Windows 11, NVDA anunciará las acciones sugeridas cuando se copien al
  portapapeles datos compatibles, como números de teléfono. Esto ahora forma
  parte de NVDA 2024.2.

## Configuración (Windows+I)

* NVDA anunciará las actualizaciones del estado de Windows Update según
  avancen la descarga e instalación. En Windows 10, esto puede resultar en
  interrupciones de voz al navegar por la aplicación de configuración
  mientras las actualizaciones se descargan y se instalan. En Windows 11, se
  puede usar el navegador de objetos en la lista de actualizaciones para
  revisar el estado de actualización de entradas individuales.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
