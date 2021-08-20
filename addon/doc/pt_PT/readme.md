# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* Compatibilidade com o NVDA: 2020.4 e superiores

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

* Calculadora (moderna)
* Calendário.
* Cortana (Conversas)
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

* Este extra requer o Windows 10 20H2 (build 19042) ou posterior. Para
  melhores resultados, utilizar o add-on com a última versão do Windows
  (Windows 10 21H1/build 19043).
* Embora a instalação seja possível, este suplemento não suporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) e versões Windows Server.
* O suporte para Windows 11 é experimental, e algumas funcionalidades não
  funcionarão (ver entradas relevantes para detalhes). Será mostrado um
  diálogo de aviso se tentar instalar versões estáveis deste suplemento no
  Windows 11 antes da disponibilidade geral.
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

* A NVDA pode anunciar a contagem de sugestões ao efectuar uma pesquisa na
  maioria dos casos, incluindo quando a contagem de sugestões muda à medida
  que a pesquisa progride. Esta opção é controlada por "anunciar a
  informação da posição do objecto" no painel de apresentação de objectos
  encontrado nas configurações do NVDA.
* Ao pesquisar no menu Iniciar ou File Explorer no Windows 10 1909
  (actualização de Novembro de 2019) e mais tarde, os casos do NVDA
  anunciando resultados de pesquisa duas vezes ao rever os resultados são
  menos perceptíveis, o que também torna a saída em braille mais consistente
  ao rever itens.
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
* É possível seguir apenas eventos específicos e/ou eventos provenientes de
  aplicações específicas.
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

## Calendário.

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

A maioria dos itens são aplicáveis quando se utiliza o Cortana Conversations
(Windows 10 2004 e posteriores).

* As respostas textuais da Cortana são anunciadas na maioria das situações.
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* No Windows 10 1909 (Actualização de Novembro de 2019) e mais tarde, é
  suportada uma experiência de pesquisa moderna no File Explorer alimentado
  pela interface do utilizador Windows Search.

## Correio.

* Ao rever itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para rever os respectivos cabeçalhos. Observe que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.

## Mapas.

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  activada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Colecção Microsoft Solitaire

* o NVDA anunciará os nomes das cartas e dos baralhos de cartas.

## Loja Microsoft

* Depois de verificar as atualizações da aplicação, os nomes das aplicações,
  na lista de aplicações a serem actualizadas, são indicados correctamente.
* Ao descarregar conteúdo como aplicações e filmes, o NVDA anunciará o nome
  do produto e o progresso do descarregamento (não funciona correctamente na
  loja da Microsoft, actualizado no Windows 11).

## Teclado moderno

This includes emoji panel, clipboard history, dictation/voice typing,
hardware input suggestions, and modern input method editors for certain
languages. When viewing emojis, for best experience, enable Unicode
Consortium setting from NVDA's speech settings and set symbol level to
"some" or higher. When pasting from clipboard history in Windows 10, press
Space key instead of Enter key to paste the selected item. NVDA also
supports updated input experience panel in Windows 11.

* Ao abrir o histórico da área de transferência, o NVDA deixará de anunciar
  a "área de transferência" quando houver itens na área de transferência, em
  algumas circunstâncias.
* Em alguns sistemas que executam Windows 10 1903 (Actualização de Maio de
  2019) e superiores, o NVDA deixará de parecer não fazer nada quando o
  painel de emojis abrir.
* Quando um grupo emoji (incluindo o grupo kaomoji e símbolos no Windows 10
  1903 ou posterior) está seleccionado, o NVDA deixará de mover o objecto de
  navegação para certos emojis.
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
* O NVDA anunciará o nome da ligação opcional de actualização de qualidade,
  se presente, tipicamente denominada "descarregar e instalar agora".

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
