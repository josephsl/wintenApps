# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* NVDA compatibility: 2021.3 and later

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

* Calculadora
* Cortana
* Email
* Mapas
* Microsoft Solitaire Collection (Coleção de Paciência)
* Teclado moderno (painel de emoji/ditado/digitação por voz/sugestões de
  entrada de hardware/histórico da área de transferência/editores de métodos
  de entrada modernos)
* Bloco de Notas (Windows 11)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Voice access (Windows 11)
* Clima
* Módulos diversos para controles, como blocos do Menu Iniciar

Notas:

* This add-on requires Windows 10 21H1 (build 19043), Windows 11 21H2 (build
  22000) or later.
* Embora a instalação seja possível, este complemento não oferece suporte
  para Windows Enterprise LTSC (Long-Term Servicing Channel — Canal de
  Manutenção de Longo Prazo) e versões do Windows Server.
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
* When arranging pinned entries (tiles in Windows 10) in Start menu or
  Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce
  information on dragged items or new position of the dragged item.
* Anúncios como alterações de volume/brilho no Explorador de Arquivo e
  notificações de atualização de aplicativos da Microsoft Store podem ser
  suprimidos desativando Anunciar Notificações nas configurações de
  apresentação de objetos do NVDA.
* In Windows 11 Insider Preview builds, microphone mute toggle status
  (Windows+Alt+K) is announced from everywhere.
* NVDA will no longer repeat text output in Windows Terminal 1.12.10733 and
  later. This is now part of NVDA 2022.1.
* NVDA will once again announce search result details in Start menu. This is
  now part of NVDA 2022.2.
* In Windows 11, Taskbar items and other user interface controls can be
  detected properly when using mouse and/or touch interaction.

## Calculadora

* In Windows 10, history and memory list items are properly labeled. This is
  now part of NVDA 2022.1.
* NVDA will announce calculator display content when performing scientific
  mode commands such as trigonometry operations. This is now part of NVDA
  2022.2.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.

## Email

* Ao explorar itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para explorar os respectivos cabeçalhos. Note que a
  navegação entre linhas (mensagens) não é suportada.

## Mapas

* NVDA reproduz sinal sonoro de localização para locais no mapa.

## Microsoft Solitaire Collection (Coleção de Paciência)

* O NVDA anunciará os nomes das cartas e dos baralhos.

## Teclado moderno

Isso inclui painel de emoji, histórico da área de transferência,
ditado/digitação por voz, sugestões de entrada de hardware e editores de
métodos de entrada modernos para determinados idiomas. Ao visualizar emojis,
para melhor experiência, habilite a configuração de Consórcio Unicode das
configurações de voz do NVDA e defina o nível do símbolo para "pouco" ou
superior. Ao colar do histórico da área de transferência no Windows 10,
pressione a tecla Espaço em vez da tecla Enter para colar o item
selecionado. O NVDA também suporta painel de experiência de entrada
atualizado no Windows 11.

* No Windows 10, quando um grupo de emoji (incluindo kaomoji e grupo de
  símbolos) é selecionado, o NVDA não moverá mais a navegação de objeto para
  certos emojis.
* In Windows 11, it is again possible to use the arrow keys to review emojis
  when emoji panel opens. This is now part of NVDA 2022.1.
* In Windows 11 clipboard history, browse mode will be turned off by
  default, designed to let NVDA announce clipboard history entry menu items.

## Bloco de Notas

Isso se refere à versão 11 ou posterior do Bloco de Notas do Windows 11.

* O NVDA anunciará itens de status, como informações de linha e coluna
  quando o comando de informar barra de status (NVDA+End no leiaute de
  computador de mesa, NvDA+Shift+End no leiaute de computador portátil) for
  executado.

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
* In Windows 10, NVDA will interupt speech and report updates to Windows
  Update status as download and install progresses. This may result in
  speech interruption when navigating Settings app while updates are being
  downloaded and installed.

## Voice access

This refers to Voice access feature introduced in Windows 11 22H2 preview.

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
