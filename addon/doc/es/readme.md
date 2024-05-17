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

* Configuración (Windows+I)

Notas:

* Este complemento requiere Windows 10 Versión 22H2 (compilación 19045) de
  64 bits, 11 22H2 (compilación 22621) o versiones posteriores.
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

Para ver una lista de cambios hechos entre cada actualización del
complemento, consulta el documento [Registros de cambios de versiones del
complemento (en inglés)][1].

## General

* En las compilaciones insider de Windows 11 24H2, se puede navegar con el
  ratón o con interacción táctil por los elementos de la interfaz de los
  ajustes rápidos (shellhost.exe). Esto ahora forma parte de NVDA 2024.2.
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
