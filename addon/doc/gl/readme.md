# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuarios do Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento é unha coleción de app modules para varias aplicacións de
Windows 10, así coma correccións para certos controis de windows 10.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Alarmas e reloxo.
* Bank of America
* Calendario
* Calculadora (modern).
* Cortana
* Insider Hub/Feedback Hub (Só Windows Insiders).
* Correo
* Mapas
* Microsoft Edge
* Opcións (opcións do sistema, Windows+I).
* Previsualización de Skype
* Twitter.
* TeamViewer Touch.
* O Tempo
* Módulos misceláneos para controis como mosaicos do Menú Inicio.

Nota: este complemento require do Windows 10 Versión 1507 (build 10240) ou
posterior e NVDA 2015.4 ou posterior.

## Xeral

* En menús de contexto para os mosaicos do Menú Inicio, os submenús
  recoñécense apropriadamente.
* Ao minimizar windows (Windows+M), xa non se anuncia "panel" (perceptible
  se se usan compilacións Insider Preview).
* Agora recoñécense certos diálogos como proprios diálogos. Esto inclúe o
  diálogo Insider Preview (settings app) e o diálogo de novo estilo do UAC
  na compilación 14328 e anteriores para o NVDA 2016.2.1 e anteriores.
* O anunciado do selector de tempo funciona Nas localizacións distintas do
  inglés.
* A apariencia/peche de suxerencias para certos campos de procura (en
  particular o aplikcativo Configuración) anúnciase a través de sons e/ou de
  braille.

## Alarmas e reloxo

* Agora anúncianse os valores do selector de hora. Esto tamén afecta ó
  control usado para selecionar cando reiniciar para rematar a instalación
  das actualizacións de Windows.

## Calendario e Correo

* NVDA xa non anuncia "só lectura" para asuntos da cita no Calendario e no
  contido do mensaxe no Correo.

## Calculadora

* Cando se prema INTRO, NVDA anuncia os resultados do cálculo.

## Cortana

* As respostas testuais de Cortana anúncianse na mayoría das situacións(se
  non se reabre o menú inicio e téntase a procura de novo).
* Para una mellor experiencia cando fales co Cortana, preme a combinación de
  teclas do modo escoita do Cortana (Windows+C nas Versións 1507 e 1511,
  Windows+Shift+C na versión 1607).

## Insider/Feedback Hub y TeamViewer Touch

* Insider Hub (Feedback Hub en Anniversary Update) só: siñifica que se usa
  olos Windows Insiders executando una compilación Insider.
* Anúncianse as etiquetas para botóns de opción.
* TeamViewer Touch: agora anúncianse as etiquetas para botóns.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.

## Microsoft Edge

* Agora anúncianse notificacións como a descarga de ficheiros.
* Ten en conta que o soporte global é experimental polo de agora (Non
  deberías usar Edge como o teu navegador principal de momento).

## Opcións

* Certa información como o progreso da Actualización de Windows agora é
  anunciada automáticamente.
* Os valores da barra de progreso e outra información xa non se anuncian
  dúas veces.

## Previsualización de Skype

* Ao teclear o indicador de texto anúnciase só coma cliente Skype para
  Escritorio.
* Volta parcial das ordes Control+NVDA+fila de números para ler o histórico
  de chats recentes e para mover o navegador de obxectos a entradas de chat
  como Skype para Escritorio.

## Bank of America/Twitter

* Agora anúncianse as etiquetas dos botóns.

## O Tempo

* As pestanas como "pronósticos" e "mapas" recoñécense coma pestanas en si
  (parche de Derek Riemer).
* Cando se lea un pronóstico, usa as frechas esquerda e dereita para moverte
  entre elementos. Usa as frechas arriba e abaixo para ler os elementos
  individuais. Por exemplo, premendo a frecha dereita anunciaría "luns: 79
  graos, parcialmente nublado, ..." premendo a frecha abaixo dirá "luns"
  logo preméndoo de novo lerá o seguinte elemento (como a
  temperatura). Actualmente esto traballa para pronósticos diarios e
  horarios.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=w10

[2]: http://addons.nvda-project.org/files/get.php?file=w10-dev
