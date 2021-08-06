# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros usuários do Windows 10
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* Compatibilidade com NVDA: 2020.4 e além

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

* Calculadora (moderna)
* Calendário
* Cortana (Conversations)
* Email
* Mapas
* Microsoft Solitaire Collection (Coleção de Paciência)
* Microsoft Store (Loja da Microsoft)
* Teclado moderno (painel de emoji/ditado/sugestões de entrada de
  hardware/histórico da área de transferência/editores de métodos de entrada
  modernos)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Clima
* Módulos diversos para controles, como blocos do Menu Iniciar

Notas:

* Este complemento requer Windows 10 20H2 (compilação 19042) ou
  posterior. Para obter melhores resultados, use o complemento com a versão
  mais recente do Windows (Windows 10 21H1/compilação 19043).
* Embora a instalação seja possível, este complemento não oferece suporte
  para Windows Enterprise LTSC (Long-Term Servicing Channel — Canal de
  Manutenção de Longo Prazo) e versões do Windows Server.
* Support for Windows 11 is experimental, and some features will not work
  (see relevant entries for details). A warning dialog will be shown if
  trying to install stable versions of this add-on on Windows 11 prior to
  general availability.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* * Para entradas não listadas abaixo, você pode presumir que os recursos
  fazem parte do NVDA, não são mais aplicáveis, pois o complemento não
  oferece suporte a versões não suportadas do Windows, como versões antigas
  do Windows 10, ou alterações foram feitas no Windows e aplicativos que
  tornam as entradas não mais aplicáveis.
* Alguns aplicativos suportam o modo de sobreposição compacta (sempre no
  topo da Calculadora, por exemplo), e este modo não funcionará corretamente
  com a versão portátil do NVDA.

Para obter uma lista de alterações feitas entre cada lançamento do
complemento, consulte o documento [changelogs for add-on releases][3].

## Geral

* NVDA can announce suggestion count when performing a search in majority of
  cases, including when suggestion count changes as search progresses. This
  option is controlled by "Report object position information" in Object
  presentation panel found in NVDA settings.
* Ao pesquisar no menu Iniciar ou no Explorador de arquivos do Windows 10
  1909 (Atualização de Novembro de 2019) e posteriores, casos de NVDA
  anunciando resultados de pesquisa duas vezes ao explorar resultados são
  menos perceptíveis, o que também torna a saída em braille mais consistente
  ao explorar os itens.
* In addition to UIA event handlers provided by NVDA, the following UIA
  events are recognized: drag start, drag cancel, drag complete, drop target
  drag enter, drop target drag leave, drop target dropped, layout
  invalidated. With NVDA's log level set to debug, these events will be
  tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active
  app. Events built into NVDA such as name change and controller for events
  will be tracked from an add-on called Event Tracker.
* É possível rastrear apenas eventos específicos e/ou eventos provenientes
  de aplicativos específicos.
* Ao abrir, fechar, reordenar (Windows 11) ou alternar entre áreas de
  trabalho virtuais, o NVDA anunciará o nome do desktop virtual ativo (área
  de trabalho 2, por exemplo).
* O NVDA não anunciará mais o texto do tamanho do menu Iniciar ao alterar as
  resoluções ou orientação da tela.
* Ao organizar os blocos do menu Iniciar ou as ações rápidas da Central de
  Ações com as teclas Alt+Shift+setas, o NVDA anuncia informações sobre
  itens arrastados ou nova posição do item arrastado.
* Anúncios como alterações de volume/brilho no Explorador de Arquivo e
  notificações de atualização de aplicativos da Microsoft Store podem ser
  suprimidos desativando Anunciar Notificações nas configurações de
  apresentação de objetos do NVDA.

## Calculadora

* O NVDA não anunciará mais a mensagem de tela calculadora gráfica duas
  vezes.

## Calendário

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

A maioria dos itens são aplicáveis ao usar Cortana Conversations (Windows 10
2004 e posterior).

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* No Windows 10 1909 (Atualização de Novembro de 2019) e posteriores, a
  experiência de pesquisa moderna no Explorador de Arquivos alimentado pela
  interface de usuário de Pesquisa do Windows é suportada.

## Email

* Ao explorar itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para explorar os respectivos cabeçalhos. Note que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, o aparecimento de sugestões de menção é indicado
  por sons.

## Mapas

* NVDA reproduz sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  ativada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Solitaire Collection (Coleção de Paciência)

* O NVDA anunciará os nomes das cartas e dos baralhos.

## Microsoft Store (Loja da Microsoft)

* Depois de verificar as atualizações de aplicativos, os nomes dos
  aplicativos na lista de aplicativos a serem atualizados são rotulados
  corretamente.
* Ao baixar conteúdo como aplicativos e filmes, o NVDA anunciará o nome do
  produto e o andamento do download (não funciona corretamente na Microsoft
  Store atualizada no Windows 11).

## Teclado moderno

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* Ao abrir o histórico da área de transferência, o NVDA não anunciará mais a
  "área de transferência" quando houver itens na área de transferência em
  algumas circunstâncias.
* Nalguns sistemas que executam o Windows 10 1903 (Atualização de Maio de
  2019) e posteriores, o NVDA não parecerá mais fazer nada quando o painel
  de emoji for aberto.
* Quando um grupo de emojis (incluindo o grupo kaomoji e símbolos no Windows
  10 1903 ou posterior) for selecionado, o NVDA não moverá mais o navegador
  de objeto para certos emojis.
* Adicionado suporte para painel de experiência de entrada atualizado
  (painel de emoji combinado e histórico da área de transferência) no
  Windows 11.

## Pessoas

* Ao pesquisar contatos, a primeira sugestão será anunciada, principalmente
  se estiver usando versões recentes do aplicativo.

## Configurações

* Certas informações, como o progresso do Windows Update, são relatadas
  automaticamente, incluindo o widget Sensor de armazenamento/limpeza de
  disco e os erros do Windows Update.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* O diálogo de lembrete do Windows Update é reconhecido como uma caixa de
  diálogo apropriada.
* Foram corrigidos Rótulos de controle estranhos vistos em certas
  instalações do Windows.
* O NVDA anunciará o nome do link de atualização de qualidade opcional se
  presente, normalmente denominado "baixe e instale agora".

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
