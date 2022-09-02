# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* NVDA compatibility: 2022.2 and later

Nota: Originalmente chamado de Windows 10 App Essentials, foi renomeado para
Windows App Essentials em 2021 para oferecer suporte ao Windows 10 e versões
futuras, como Windows 11. Partes deste complemento ainda farão referência ao
nome do complemento original.

Este complemento é uma coleção de módulos de aplicativos (app modules) para
vários aplicativos modernos do Windows, bem como aprimoramentos e correções
para determinados controles encontrados no Windows 10 e posteriores.

Os seguintes módulos de aplicativos ou módulos de suporte para alguns
aplicativos estão incluídos (consulte a seção de cada aplicativo para obter
detalhes sobre o que está incluso):

* Cortana
* Mapas
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/Suggested Actions (preview)/modern input
  method editors)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Voice access (Windows 11 22H2)
* Clima
* Módulos diversos para controles, como blocos do Menu Iniciar

Notas:

* This add-on requires Windows 10 21H2 (build 19044), 11 21H2 (build 22000),
  or later releases.
* Embora a instalação seja possível, este complemento não oferece suporte
  para Windows Enterprise LTSC (Long-Term Servicing Channel — Canal de
  Manutenção de Longo Prazo) e versões do Windows Server.
* If Add-on Updater 22.08 or later is installed and background add-on
  updates is enabled, Windows App Essentials will not install at all on
  unsupported Windows releases.
* Not all features from Windows Insider Preview builds will be supported.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* * Para entradas não listadas abaixo, você pode presumir que os recursos
  fazem parte do NVDA, não são mais aplicáveis, pois o complemento não
  oferece suporte a versões não suportadas do Windows, como versões antigas
  do Windows 10, ou alterações foram feitas no Windows e aplicativos que
  tornam as entradas não mais aplicáveis.
* Alguns aplicativos suportam o modo de sobreposição compacta (sempre no
  topo da Calculadora, por exemplo), e este modo não funcionará corretamente
  com a versão portátil do NVDA.
* For best experience with apps that embed web technologies and content such
  as Start menu and its context menu, enable "Automatic focus mode for focus
  changes" setting from NVDA's browse mode settings panel.

Para obter uma lista de alterações feitas entre cada lançamento do
complemento, consulte o documento [changelogs for add-on releases][3].

## Geral

* In addition to UIA event handlers provided by NVDA, the following UIA
  events and properties are recognized: drag complete, drag drop effect,
  drop target dropped. With NVDA's log level set to debug, these events will
  be tracked and logged.
* Ao abrir, fechar, reordenar (Windows 11) ou alternar entre áreas de
  trabalho virtuais, o NVDA anunciará o nome do desktop virtual ativo (área
  de trabalho 2, por exemplo).
* When dragging and dropping items such as arranging pinned entries (tiles
  in Windows 10) in Start menu or Action Center quick actions with
  Alt+Shift+arrow keys, NVDA will announce "dragging" and/or drag and drop
  effects before and while dragging items, respectively. NVDA announcing
  "dragging" is now part of NVDA 2022.4.
* Anúncios como alterações de volume/brilho no Explorador de Arquivo e
  notificações de atualização de aplicativos da Microsoft Store podem ser
  suprimidos desativando Anunciar Notificações nas configurações de
  apresentação de objetos do NVDA.
* In Windows 11 22H2 and later, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* Item status changes are announced in more apps including Visual Studio
  Community 2022. This is now part of NVDA 2022.4.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.

## Mapas

* NVDA reproduz sinal sonoro de localização para locais no mapa.

## Teclado moderno

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, suggested actions (preview), and modern input
method editors for certain languages across Windows 10 and 11. When viewing
emojis, for best experience, enable Unicode Consortium setting from NVDA's
speech settings and set symbol level to "some" or higher. When pasting from
clipboard history in Windows 10, press Space key instead of Enter key to
paste the selected item.

* No Windows 10, quando um grupo de emoji (incluindo kaomoji e grupo de
  símbolos) é selecionado, o NVDA não moverá mais a navegação de objeto para
  certos emojis.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.
* In Insider Preview build 25115 and later (backported to Windows 11 beta
  build 22622), NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard.

## Pessoas

* Ao pesquisar contatos, a primeira sugestão será anunciada, principalmente
  se estiver usando versões recentes do aplicativo.

## Configurações

* Foram corrigidos Rótulos de controle estranhos vistos em certas
  instalações do Windows.
* O NVDA anunciará o nome do controle de atualização de qualidade opcional,
  se houver (link para baixar e instalar agora no Windows 10, botão de
  download no Windows 11).
* No Windows 11, os itens da barra de localização atual são reconhecidos
  corretamente.
* In Windows 10 and 11 22H2 and later, NVDA will interupt speech and report
  updates to Windows Update status as download and install progresses. This
  may result in speech interruption when navigating Settings app while
  updates are being downloaded and installed. If using Windows 11 22H2 and
  later, if selective UIA event registration is on, you must move focus to
  updates list as soon as they appear so NVDA can announce update progress.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2.

* NVDA will announce microphone status when toggling microphone from Voice
  access interface.

## Clima

* Abas como "previsão" e "mapas" são reconhecidas como guias adequadas
  (patch de Derek Riemer).
* Ao ler uma previsão, use as setas esquerda e direita para se mover entre
  os itens. Use as setas para cima e para baixo para ler os itens
  individuais. Por exemplo, pressionar a seta para a direita pode indicar
  "Segunda-feira: 79 graus, parcialmente nublado, ..." pressionar a seta
  para baixo dirá "Segunda-feira". Em seguida, pressionar novamente lerá o
  próximo item (como a temperatura). Atualmente, isso funciona para
  previsões diárias e horárias.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
