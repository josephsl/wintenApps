# Windows 10 Aplicativos Essenciais (Windows 10 App Essentials) #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* NVDA compatibility: 2020.4 and beyond

Este complemento é uma coleção de módulos de aplicativos (app modules) para
vários aplicativos do Windows 10, bem como aprimoramentos e correções para
determinados controles.

Os seguintes módulos de aplicativos ou módulos de suporte para alguns
aplicativos estão incluídos (consulte a seção de cada aplicativo para obter
detalhes sobre o que está incluído):

* Calculator (modern)
* Calendário
* Cortana (Conversations)
* Email
* Mapas
* Microsoft Solitaire Collection (Coleção de Paciência)
* Microsoft Store (Loja da Microsoft)
* Modern keyboard (emoji panel/dictation/hardware input
  suggestions/clipboard history/modern input method editors)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Clima
* Miscellaneous modules for controls such as Start Menu tiles

Notas:

* This add-on requires Windows 10 Version 2004 (build 19041) or later. For
  best results, use the add-on with latest Windows 10 stable release
  (21H1/build 19043).
* Although installation is possible, this add-on does not support Windows 10
  Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* Para entradas não listadas abaixo, você pode assumir que os recursos fazem
  parte do NVDA, não são mais aplicáveis, pois o complemento não oferece
  suporte a versões antigas do Windows 10, ou foram feitas alterações no
  Windows 10 e aplicativos que tornam as entradas não mais aplicáveis.
* Some apps support compact overlay mode (always on top in Calculator, for
  example), and this mode will not work properly with portable version of
  NVDA.

Para obter uma lista de alterações feitas entre cada lançamento do
complemento, consulte o documento [changelogs for add-on releases][3].

## Geral

* NVDA pode anunciar a contagem de sugestões ao realizar uma pesquisa na
  maioria dos casos. Essa opção é controlada por "Anunciar informações de
  posição do objeto" no painel de Apresentação de objetos, encontrado nas
  configurações do NVDA.
* Ao pesquisar no menu Iniciar ou no Explorador de Arquivo na versão 1909
  (Atualização de Novembro de 2019) e posteriores, as instâncias do NVDA
  anunciando os resultados da pesquisa duas vezes ao revisar os resultados
  são menos perceptíveis, o que também torna a saída de braille mais
  consistente ao revisar itens.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped. With NVDA's log
  level set to debug, these events will be tracked, and for UIA notification
  event, a debug tone will be heard if notifications come from somewhere
  other than the currently active app. Some events will provide additional
  information such as element count in controller for event, state of the
  element for state change event, and item text for item status event.
* É possível rastrear apenas eventos específicos e/ou eventos provenientes
  de aplicativos específicos.
* When opening, closing, reordering (build 21337 or later), or switching
  between virtual desktops, NVDA will announce active virtual desktop name
  (desktop 2, for example).
* NVDA will no longer announce Start menu size text when changing screen
  resolutions or orientation.
* Ao organizar os blocos do menu Iniciar ou as ações rápidas da Central de
  Ações com as teclas Alt+Shift+setas, o NVDA anuncia informações sobre
  itens arrastados ou nova posição do item arrastado.
* Anúncios como alterações de volume/brilho no Explorador de Arquivo e
  notificações de atualização de aplicativos da Microsoft Store podem ser
  suprimidos desativando Anunciar Notificações nas configurações de
  apresentação de objetos do NVDA.

## Calculadora

* NVDA will no longer announce graphing calculator screen message twice.

## Calendário

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

Most items are applicable when using Cortana Conversations (Version 2004 and
later).

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* Na Versão 1909 (Atualização de Novembro de 2019) e mais recente, é
  suportada a experiência de pesquisa moderna no Explorador de Arquivo
  desenvolvido pela interface de usuário da Pesquisa do Windows.

## Email

* Ao explorar itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para explorar os respectivos cabeçalhos. Note que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.

## Mapas

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  ativada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Solitaire Collection (Coleção de Paciência)

* O NVDA anunciará os nomes das cartas e dos baralhos.

## Microsoft Store (Loja da Microsoft)

* Depois de verificar as atualizações de aplicativos, os nomes dos
  aplicativos na lista de aplicativos a serem atualizados, são indicados
  corretamente.
* Ao baixar conteúdos, como aplicativos e filmes, o NVDA anunciará o nome do
  produto e o progresso da transferência.

## Teclado moderno

This includes emoji panel, clipboard history, dictation, hardware input
suggestions, and modern input method editors for certain languages. When
viewing emojis, for best experience, enable Unicode Consortium setting from
NVDA's speech settings and set symbol level to "some" or higher. Also, NVDA
supports updated input experience panel in build 21296 and later.

* Ao abrir o histórico da área de transferência, o NVDA não anunciará mais a
  "área de transferência" quando houver itens na área de transferência em
  algumas circunstâncias.
* Em alguns sistemas que executam a Versão 1903 (Atualização de Maio de
  2019) e posteriores, o NVDA não parece mais não fazer nada quando o painel
  de emoji é aberto.
* Quando um grupo de emoji (incluindo o kaomoji e o grupo de símbolos na
  versão 1903 ou posterior) é selecionado, o NVDA não move mais o objeto de
  navegação para determinados emojis.
* Added support for updated input experience panel (combined emoji panel and
  clipboard history) in build 21296 and later.

## Pessoas

* Ao procurar contatos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso do Windows Update, são relatadas
  automaticamente, incluindo o widget de detecção de disco/limpeza de disco
  e os erros do Windows Update.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* A caixa de diálogo do lembrete do Windows Update é reconhecida como um
  diálogo apropriado.
* Etiquetas de controle estranhas vistas em determinadas instalações do
  Windows 10 foram corrigidas.
* Nas revisões mais recentes da Versão 1803 e posteriores, devido a
  alterações no procedimento do Windows Update para atualizações de
  recursos, foi adicionado um link "baixar e instalar agora". Agora, o NVDA
  anunciará o título da nova atualização, se presente.

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
