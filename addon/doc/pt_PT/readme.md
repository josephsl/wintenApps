# Windows App Essentials #

* Authors: Joseph Lee, Derek Riemer and others
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* NVDA compatibility: 2021.2 and beyond

Nota: Originalmente chamado Windows 10 App Essentials, foi renomeado para
Windows App Essentials em 2021 para suportar o Windows 10 e futuros
lançamentos como o Windows 11. Partes deste extra continuarão a referir-se
ao nome original do extra.

Este extra é uma colecção de módulos de aplicação para várias aplicações
modernas do Windows, bem como melhorias e correcções para certos controlos
encontrados no Windows 10 e posteriores.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Calculadora
* Cortana
* Correio.
* Mapas.
* Colecção Microsoft Solitaire
* Loja Microsoft
* Modern keyboard (emoji panel/dictation/voice typing/hardware input
  suggestions/clipboard history/modern input method editors)
* Pessoas.
* Configurações (configurações do sistema, Windows + I)
* Meteorologia
* Módulos diversos para controlos, tais como painéis do menu iniciar.

Notas:

* This add-on requires Windows 10 20H2 (build 19042) or later and is
  compatible with Windows 11.
* Embora a instalação seja possível, este suplemento não suporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) e versões Windows Server.
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Para entradas não listadas abaixo, pode assumir que as funcionalidades
  fazem parte do NVDA, já não aplicável, uma vez que o extra não suporta
  versões não suportadas do Windows, tais como versões antigas do Windows
  10, ou foram feitas alterações ao Windows e aplicações que tornam as
  entradas já não aplicáveis.
* Algumas aplicações suportam modo de sobreposição compacto (sempre em cima
  na Calculadora, por exemplo), e este modo não funcionará correctamente com
  a versão portátil do NVDA.

Para obter uma lista de alterações feitas entre cada release do extra,
consulte o documento [changelogs for releases, release][3].

## Geral

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  is now part of NVDA 2021.3.
* Para além dos manipuladores de eventos UIA fornecidos pelo NVDA, são
  reconhecidos os seguintes eventos UIA: arrastar iniciar, arrastar
  cancelar, arrastar completo, largar alvo arrastar entrar, largar alvo
  arrastar sair, largar alvo largar, layout invalidado. Com o nível de
  registo do NVDA definido para depuração, estes eventos serão rastreados, e
  para o evento de notificação UIA, um tom de depuração será ouvido se as
  notificações vierem de outro local que não a aplicação actualmente
  activa. Os eventos integrados no NVDA, tais como mudança de nome e
  controlador de eventos, serão rastreados a partir de um add-on chamado
  Event Tracker.
* Ao abrir, fechar, reordenar (Windows 11), ou alternar entre desktops
  virtuais, o NVDA anunciará o nome do desktop virtual activo (desktop 2,
  por exemplo).
* o NVDA não anunciará mais o tamanho do menu iniciar, quando alterar as
  resoluções ou a orientação do ecrã.
* Ao organizar painéis do menu Iniciar ou acções rápidas do Action Center
  com as teclas Alt+Shift+seta, o NVDA anunciará informação sobre itens
  arrastados ou nova posição do item arrastado.
* Anúncios tais como alterações de volume/brilho no File Explorer e
  notificações de actualização de aplicações do Microsoft Store podem ser
  suprimidos desligando as Notificações de Relatório nas definições de
  apresentação de objectos do NVDA.

## Calculadora

* O NVDA já não lerá duas vezes a mensagem do ecrã da calculadora gráfica.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.

## Correio.

* Ao rever itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para rever os respectivos cabeçalhos. Observe que a
  navegação entre linhas (mensagens) não é suportada.

## Mapas.

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  activada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Colecção Microsoft Solitaire

* o NVDA anunciará os nomes das cartas e dos baralhos de cartas.

## Loja Microsoft

* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Teclado moderno

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* In Windows 10, when an emoji group (including kaomoji and symbols group)
  is selected, NVDA will no longer move navigator object to certain emojis.
* Adicionado suporte para painel de experiência de entrada actualizada
  (painel combinado de emoji e histórico da área de transferência) no
  Windows 11.

## Pessoas.

* Ao procurar contactos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  relatadas automaticamente, incluindo sentido / disco de armazenamento e os
  erros da actualização do Windows.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* As etiquetas de controlo estranhas observadas em certas instalações do
  Windows foram corrigidas.
* NVDA will announce the name of the optional quality update control if
  present (download and install now link in Windows 10, download button in
  Windows 11).

## Meteorologia

* Separadores como "previsão" e "mapas" são reconhecidos como separadores
  adequados (patch de Derek Riemer).
* Ao ler uma previsão, use as setas esquerda e direita para se mover entre
  os itens. Use as setas para cima e para baixo para ler os itens
  individuais. Por exemplo, se pressionar a seta para a direita, poderá ler
  "Segunda-feira: 20 graus, parcialmente nublado, ...", se pressionar a seta
  para baixo, dirá "Segunda-feira" e, em seguida, se pressionar novamente,
  lerá o próximo item (Como a temperatura). Isto funciona actualmente para
  previsões diárias e horárias.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
