# Windows 10 aplicativos essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* NVDA compatibility: 2018.3 to 2019.1

Este complemento é uma coleção de módulos de aplicativos — app modules —
para vários aplicativos do Windows 10, bem como aprimoramentos e correções
para determinados controles.

Os seguintes módulos de aplicativos ou módulos de suporte para alguns
aplicativos estão incluídos (consulte a seção de cada aplicativo para obter
detalhes sobre o que está incluído):

* Central de Ações
* Alarmes e Relógio.
* Calendário
* Calculadora (moderna).
* Cortana
* Central de comentários
* Barra de jogos
* Email
* Mapas
* Microsoft Edge
* Teclado moderno (painel de emoji/sugestões de entrada de hardware/itens da
  área de transferência na nuvem na versão 1709 e posteriores)
* Pessoas
* Configurações (configurações do sistema, Windows+I)
* Skype (aplicativo universal)
* Loja — Store
* Clima.
* Módulos diversos para controles, como telas do menu Iniciar.

Notas:

* Este complemento requer o Windows 10 Versão 1709 (compilação 16299) ou
  posterior e o NVDA 2018.3 ou posterior. Para obter melhores resultados,
  use o complemento com a versão estável mais recente do Windows 10
  (compilação 17763) e a versão estável mais recente do NVDA.
* Alguns recursos do complemento são ou farão parte do leitor de tela NVDA.
* Para entradas não listadas abaixo, pode assumir que os recursos já fazem
  parte do NVDA, não mais aplicáveis, pois o complemento não suporta versões
  antigas do Windows 10 ou foram feitas alterações em aplicativos que tornam
  as entradas inválidas.
* Standalone update check from this add-on will be removed in version
  19.02. For future add-on updates, please use Add-on Updater add-on.

Para obter uma lista de alterações feitas entre cada lançamento do
complemento, consulte o documento [changelogs for add-on releases][3].

## Geral

* Mudanças internas para tornar o complemento compatível com futuras versões
  do NVDA.
* Se o complemento Add-on Updater estiver instalado, esse complemento
  verificará as atualizações do Windows 10 aplicativos essenciais.
* O intervalo de verificação de atualização padrão foi alterado para
  verificações semanais para versões estáveis e em desenvolvimento. Isso se
  aplica se o próprio complemento verificar atualizações.
* Se o complemento estiver configurado para verificar se há atualizações, ao
  atualizar o complemento, se a nova versão do complemento exigir uma versão
  mais nova do NVDA, uma mensagem de erro será apresentada.
* Pequenas mudanças em como algumas mensagens são apresentadas em idiomas
  diferentes do inglês.
* Os itens do submenu são reconhecidos corretamente em vários aplicativos,
  incluindo o menu de contexto para os menus do menu Iniciar e o menu de
  aplicativos do Microsoft Edge (Redstone 5).
* Certos diálogos agora são reconhecidos como diálogos apropriados e
  relatados como tal, incluindo a caixa de diálogo Insider Preview (app de
  configurações). Isso agora faz parte do NVDA 2018.3.
* O NVDA pode anunciar a contagem de sugestões ao realizar uma pesquisa na
  maioria dos casos. Essa opção é controlada por "Anunciar informações de
  posição do objeto" no diálogo/painel de apresentação do objeto.
* Em determinados menus de contexto (como no Edge), as informações de
  posição (por exemplo, 1 de 2) deixaram de ser anunciadas.
* Os seguintes eventos UIA são reconhecidos: alteração da posição do texto
  ativo, controlador para, arrastar início, arrastar cancelamento, arrastar
  completo, elemento selecionado, status do item, alteração da região ativa,
  notificação, alerta do sistema, dica de ferramenta aberta, janela
  aberta. Com o NVDA configurado para ser executado com o log de depuração
  ativado, esses eventos serão rastreados e, para o evento de notificação
  UIA, um bipe de depuração será ouvido se as notificações vierem de algum
  lugar diferente do aplicativo atualmente ativo.
* Notificações de versões mais recentes de aplicativos no Windows 10 Versão
  1709 (build 16299) e posteriores são anunciadas. O NVDA 2018.2 e posterior
  suportam isso, com 2018.3 adicionando suporte para mais notificações.
* As dicas de ferramentas do Edge e aplicativos universais são reconhecidas
  e serão anunciadas.
* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará a ID atual da área de trabalho (área de trabalho 2, por
  exemplo).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação da tela.

## Central de Ações

* A ação rápida do brilho agora é um botão em vez de um botão de
  alternância.
* Várias alterações de status, como Assistente de Foco e Brilho, serão
  relatadas.

## Alarmes e relógio

* Os valores do selecionador de tempo são agora anunciados, perceptíveis ao
  mover o foco para os controles do selecionador. Isso também afeta o
  controle usado para selecionar quando reiniciar para concluir a instalação
  das atualizações do Windows.

## Calculadora

* Quando as teclas ENTER ou Escape são pressionadas, o NVDA anuncia os
  resultados do cálculo.
* Para cálculos como conversor de unidades e conversor de moeda, o NVDA
  anunciará os resultados assim que os cálculos forem inseridos.
* O NVDA não anunciará mais "nível de cabeçalho" para os resultados da
  calculadora.

## Calendário

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações
  (se não forem, reabra o menu Iniciar e tente procurar novamente).
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* O NVDA agora anunciará confirmação de lembrete depois de o ter definido.

## Central de comentários

* Para os lançamentos mais recentes de aplicativos, o NVDA deixará de os
  anunciar duas vezes.

## Barra de jogos

* O NVDA anunciará a aparência da janela da barra de jogos. Devido a
  limitações técnicas, o NVDA não pode interagir totalmente com a barra de
  jogos antes da compilação 17723.

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

## Microsoft Edge

* Notificações como downloads de ficheiros e vários alertas de páginas da
  Web, bem como a disponibilidade da Visualização de Leitura (se estiver a
  usar a Versão 1709 e posterior) são anunciadas.
* O preenchimento automático de texto será rastreado e anunciado no endereço
  omnibar.

## Teclado moderno

Nota: a maioria dos recursos abaixo agora fazem parte do NVDA 2018.3.

* Support for Emoji input panel in Version 1709 (Fall Creators Update) and
  later, including the redesigned panel in Version 1809 (build 17661 and
  later) and changes made in 19H1 (build 18262 and later, including kaomoji
  and symbols categories in build 18305). If using NVDA releases earlier
  than 2018.4, for best experience when reading emojis, use Windows OneCore
  speech synthesizer. If 2018.4 or later is in use, enable Unicode
  Consortium setting from NvDA's speech settings and set symbol level to
  "some" or higher.
* Suporte para sugestões de entrada de teclado de hardware na versão 1803
  (atualização de abril de 2018) e posterior.
* In post-1709 builds, NVDA will announce the first selected emoji when
  emoji panel opens. This is more noticeable in build 18262 and later where
  emoji panel may open to last browsed category, such as displaying skin
  tone modifiers when opened to People category.
* Suporte para anunciar itens da área de transferência em nuvem na versão
  1809 (compilação 17666 e posterior).
* Redução dos detalhes desnecessários ao trabalhar com o teclado moderno e
  seus recursos. Estes incluem não mais anunciar "Microsoft Candidate UI" ao
  abrir sugestões de entrada de teclado de hardware e ficar em silêncio
  quando certas teclas do teclado virtual geram eventos de alteração de nome
  em alguns sistemas.
* NVDA will no longer play error tones or do nothing when closing emoji
  panel in more recent 19H1 Insider Preview builds.
* In Version 1809 (October 2018 Update) and later, NVDA will announce search
  results for emojis if possible.

## Pessoas

* Ao procurar contatos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso do Windows Update, são anunciadas
  automaticamente, incluindo o widget Detecção de disco/detecção de
  armazenamento.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Os grupos de configurações são reconhecidos ao usar a navegação por
  objetos para navegar entre controles.
* Para algumas caixas combinadas e botões de opção, o NVDA não falhará ao
  reconhecer os rótulos e / ou anunciar mudanças de valor.
* Os sinais sonoros da barra de progresso do volume de áudio deixaram de ser
  ouvidos, a partir da versão 1803 e posteriores.
* São anunciadas Mais mensagens sobre o status do Windows Update,
  especialmente se o Windows Update encontrar erros.
* O NVDA não irá mais parecer não fazer nada ou tocar tons de erro se usar
  comandos de navegação de objetos sob algumas circunstâncias.
* Vários links adicionados na compilação 18282 sem rótulos agora têm
  rótulos.
* A caixa de diálogo do lembrete do Windows Update é reconhecida como um
  diálogo apropriado.

## Skype

Nota: as entradas abaixo não funcionarão corretamente no aplicativo
universal do Skype 14.

* O texto do indicador de digitação é anunciado exatamente como no cliente
  Skype para a Área de Trabalho.
* Os comandos Control+NvDA+número de linha, usados para ler o histórico de
  conversação recente e mover objetos do navegador para entradas de
  conversação no Skype para a Área de Trabalho, também estão disponíveis no
  Skype UWP.
* Agora pode pressionar as teclas Alt+número para localizar e mover-se para
  conversas (1), lista de contatos (2), bots (3) campo de edição da
  conversação se estiver visível (4). Observe que esses comandos funcionarão
  corretamente se a atualização do Skype lançada em março de 2017 estiver
  instalada. 
* O NVDA já não anunciará "Mensagem do Skype" ao explorar as mensagens na
  maioria dos casos.
* Na lista do histórico de mensagens, pressionar NVDA+D num item de mensagem
  agora permitirá que o NVDA anuncie informações detalhadas sobre essa
  mensagem, como tipo de canal, data e hora de envio e assim por diante. 

## Loja — Store

* Depois de verificar as atualizações de aplicativos, os nomes dos
  aplicativos na lista de aplicativos a serem atualizados, são indicados
  corretamente.
* Ao baixar conteúdos, como aplicativos e filmes, o NVDA anunciará o nome do
  produto e o progresso da transferência.

## Clima

* Abas como "previsão" e "mapas" são reconhecidas como guias adequadas
  (patch de Derek Riemer).
* Ao ler uma previsão, use as setas para a esquerda e para a direita para se
  mover entre os itens. Use as setas para cima e para baixo para ler os
  itens individuais. Por exemplo, pressionar a seta para a direita pode
  indicar "Segunda-feira: 79 graus, parcialmente nublado ...", pressionando
  a seta para baixo, "segunda-feira". Depois, pressionando-a novamente, o
  próximo item será lido (como a temperatura). Isto, atualmente, funciona
  para previsões diárias e horárias.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev

[3]: https://github.com/josephsl/wintenapps/wiki/w10changelog
