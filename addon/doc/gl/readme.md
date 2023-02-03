# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: 2022.4 e posterior

Nota: Orixinalmente chamado Windows 10 App Essentials, renomeouse a windows
App Essentials en 2021 para soportar windows 10 e versións futuras como
Windows 11. Parte deste complemento aínda se referirá ó seu nome antigo.

Este complemento é unha coleción de app modules para varias aplicacións de
Windows, así como melloras e correccións para certos controis de windows 10
e posteriores.

Inclúense os seguintes app modules ou o apoio para módulos para algunhas
aplicacións (consulta cada sección para a aplicación para detalles sobre que
se inclúe):

* Cortana
* Mapas
* Teclado Moderno (panel de emoji/teclado táctil/ditado/escritura por
  voz/suxestións de entrada por hardware/historial do portapapeis/Accións
  Suxeridas/editores co método de entrada moderna)
* Opcións (opcións do sistema, Windows+I)
* Acceso por voz (Windows 11 22H2)
* O Tempo
* Módulos misceláneos para controis e características como os anuncios dos
  escritorios virtuais

Notas:

* Este complemento require do Windows 10 21H2 (compilación 19044), 11 22H2
  (compilación 22000), ou versións posteriores.
* O soporte das actualizacións de características está vencellado á duración
  do soporte ó consumidor (edicións Home, Pro, Pro Education, Pro for
  Workstations) e o complemento podería rematar o soporte para unha
  actualización de características antes do final do soporte ó
  consumidor. Consulta aka.ms/WindowsTargetVersioninfo para máis información
  e datas de soporte.
* Aínda que a instalación é posible, este complemento non soporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) nin versións de Windows
  Server.
* Se Add-on Updater está instalado e están activadas as actualizaciónes en
  segundo plano, Windows App Essentials non se instalará en absoluto en
  versións de Windows non soportadas.
* Non se soportarán todas as características de versións Windows Insider
  Preview, máis aínda para as características introducidas nun subconxunto
  de Insiders Windows na canle de desenvolvemento (dev). Para a canle beta,
  só se soporta a última compilación (22623).
* Algunhas das características do complemento son ou serán parte do lector
  de pantalla NVDA.
* Algunhas apps soportan o modo de capa compacto (sempre enriba na
  Calculadora, por exemplo), e este modo non funcionará correctamente coa
  versión portable de NVDA.
* Para a mellor experiencia con aplicacións que incrustan tecnoloxías web e
  con contido como o menú inicio e o seu menú de contexto, habilita a opción
  "Modo foco automático para cambios do foco" dende o panel de modo
  navegación das opcións de NVDA.

Para unha lista de trocos feitos entre cada versión do complemento, visita o
documento [rexistros de trocos para publicacións de complementos][3].

## Xeral

* Cando se abran, pechen ou se cambie entre escritorios virtuales, NVDA
  anunciará o nome do escritorio activo (escritorio 2, por exemplo).
* En Windows 11,, NVDA anunciará os destaques da procura no Menú inicio
  cando se abra. Agora isto forma parte de NVDA 2023.1.
* En Windows 11 22H2 e posterior, pódese utilizar rato e/ou interacción
  táctil para interactuar coa área de desbordamento da bandexa do sistema
  redeseñada (Moment 2) e o diálogo Abrir con. Agora isto forma parte de
  NVDA 2023.1.
* NVDA gravará a arquitectura do procesador para a instalación actual de
  Windows (x86/32 bits, AMD64, ARM64) cando se inicie. Agora isto forma
  parte de NVDA 2023.1.
* Mellorada a experiencia coa barra de tarefas en Windows 10 e 11, incluíndo
  o anunciado dos resultados ó reordear iconos premendo as teclas
  Alt+Shift+Frechas esquerda/dereita (Windows 11 antes da compilación 25267)
  e o anunciado da posición do elemento ó moverse por iconos da barra de
  tarefas (Windows 10 e 11 antes da compilación 25281).
* NVDA anunciará o texto carpeta baleira dentro dunha carpeta baleira no
  Explorador de Arquivos.
* En aplicacións como o Explorador de Arquivos ou o Bloc de Notas onde se
  soportan as xanelas en lapelas, NVDA anunciará o nome e a posición das
  lapelas ó cambiar entre elas.

## Cortana

* As respostas textuais de Cortana anúncianse na maioría de situacións.
* NVDA silenciarase cando lle fales ao Cortana a través da voz.

## Mapas

* NVDA reproduce pitidos de localización para lugares no mapa.
* NVDA xa non interromperá a fala cando estea enfocado en elementos
  distintos do control do mapa nalgúns casos.

## Teclado Moderno

Isto inclúe o panel de Emoji, o historial do portapapeis, o teclado táctil,
o dictado/escritura por voz, as suxestións de entrada por hardware, as
accións suxeridas, e os editores co método de entrada moderna para certas
linguas tanto en windows 10 como 11. Ó ver emojis, para unha mellor
experiencia, habilita a opción Unicode Consortium nos axustes de voz do NvDA
e establece o nivel de símbolos en "algunha" ou superior. Ó pegar dende o
historial do portapapeis en Windows 10, preme a tecla Espazo no canto de
Intro para pegar o elemento seleccionado.

* No panel de emoji de windows 10, cando se selecciona un grupo de emojis
  (incluindo kaomoji e grupos de símbolos), NVDA xa non moverá o navegador
  de obxectos a certos emojis.
* No historial do portapapeis de Windows 11, o modo exploración
  desactivarase por defecto, deseñado para permitir que NVDA anuncie os
  elementos do menú de entradas do historial do portapapeis. Isto agora
  forma parte de NVDA 2023.1.
* En Windows 11 22H2 e posterior, NVDA anunciará accións suxeridas cando se
  copien ó portapapeis datos compatibles como números de teléfono.

## Opcións

* NVDA anunciará o nome do control para a actualización de calidade opcional
  se estiver presente (ligazón descargar e instalar agora en Windows 10 e
  botón descargar en Windows 11).
* En Windows 11, os elementos da barra de faragullas de pan recoñécense
  correctamente.
* En Windows 10 e 11 22H2 e posterior, NVDA interrumpirá a voz e anunciará
  actualizacións ós estados de windows Update como progresos de descarga e
  instalación. Isto podería conlevar interrupcións da voz ó navegar pola
  aplicación Configuración cando se estean a descargar e instalar
  actualizacións. Se usas Windows 11 22H2 e posterior, se está activado o
  rexistro selectivo de eventos UIA, tes que mover o foco á lista de
  actualizacións tan pronto apareza para que NVDA poida anunciar o progreso
  de actualización.

## Acceso por voz

Esto se refiere a la característica Acceso por voz introducida en Windows 11
22H2.

* NVDA anunciará o estado do micrófono cando se active ou desactive o
  micrófono dende a interface de Acceso por voz.

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

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
