# Windows 10 App Essentials #

* Autor: Joseph Lee
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como correcciones para ciertos controles de windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Reloj y alarmas.
* Bank of America
* Calculadora (modern).
* Cortana
* Insider Hub/Feedback Hub (sólo Windows Insiders).
* Microsoft Edge
* Opciones (opciones de sistema, Windows+I).
* Previsualización de Skype
* Twitter.
* TeamViewer Touch.
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

## General

* En menús de contexto para los mosaicos del Menú Inicio, los submenús ahora
  se reconocen apropiadamente.
* Al minimizar windows (Windows+M), ya no se anuncia "panel" ­(­perceptible
  si se utilizan compilaciones Insider Preview).
* Ahora se reconocen ciertos diálogos como diálogos propios. Esto incluye el
  diálogo Insider Preview (settings app) y el diálogo de nuevo estilo del
  UAC en la compilación 14328 y anterior.
* El anunciado de selector de hora funciona en localizaciones diferentes al
  inglés.

## Alarmas y reloj

* Ahora se anuncian los valores del selector de hora. Esto también afecta al
  control utilizado para seleccionar cuándo reiniciar para finalizar la
  instalación de las actualizaciones de Windows.

## Calculadora

* Cuando se pulse INTRO, NVDA anuncia los resultados del cálculo.

## Cortana

* Las respuestas textuales de Cortana se anuncian en la mayoría de las
  situaciones (si no se reabre el menú Inicio y  se trata de buscar de
  nuevo).

## Insider/Feedback Hub y TeamViewer Touch

* Insider Hub (Retroalimentación de Hub en Anniversary Update) solo:
  Significa que se utiliza por Windows Insiders ejecutando una compilación
  Insider.
* Se anuncian las etiquetas para botones de opción.
* TeamViewer Touch: se anuncian las etiquetas para los botones.

## Microsoft Edge

* Ahora se anuncian notificaciones tales como descargas de ficheros.
* Ten en cuenta que el soporte global es experimental en este momento (No
  deberías utilizar Edge como tu navegador principal por ahora).

## Opciones

* Cierta información tal como el progreso de la Actualización de Windows
  ahora se anuncia automáticamente.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.

## Previsualización de Skype

* Al teclear el indicador de texto se anuncia sólo como cliente Skype para
  Escritorio.
* Retorno parcial de las órdenes Control+NVDA+fila de números para leer el
  histórico de chats recientes.

## Bank of America/Twitter

* Ahora se anuncian las etiquetas de los botones.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
