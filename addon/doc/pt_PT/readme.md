# Windows 10 aplicações essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* Compatibilidade com NVDA: 2018.3 a 2019.1

Este extra é uma colecção de módulos de aplicações para várias aplicações do
Windows 10, bem como aprimoramentos e correcções para determinados
controlos.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Centro de acção
* Alertas e Relógio.
* Calendário.
* Calculadora (moderna).
* Cortana
* Central de comentários
* Correio.
* Mapas.
* Microsoft Edge
* Teclado moderno (sugestões de entrada do painel de emoji / hardware na
  Versão 1709 e posterior) 
* Pessoas.
* Configurações (configurações do sistema, Windows + I)
* Skype (aplicação universal).
* Loja.
* Meteorologia.
* Módulos diversos para controlos, como ecrãs do menu Iniciar.

Notas:

* Este extra requer o Windows 10 Versão 1803 (compilação 17134) ou posterior
  e o NVDA 2018.3 ou posterior. Para obter melhores resultados, use o extra
  com a versão estável mais recente do Windows 10 (compilação 17763) e a
  versão estável mais recente do NVDA. 
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Para entradas não listadas abaixo, pode assumir que os recursos fazem já
  parte do NVDA, não sendo mais aplicáveis, pois o complemento não suporta
  versões antigas do Windows 10, ou foram feitas alterações no Windows 10 e
  nos aplicativos que tornam as entradas desnecessárias.

Para obter uma lista de alterações feitas entre cada release do extra,
consulte o documento [changelogs for releases, release][3].

## Geral

* O NVDA não reproduzirá mais os tons de erro ou não fará nada se este extra
  ficar activo no Windows 7 e 8.1.
* Os itens do submenu são reconhecidos correctamente em vários aplicativos,
  incluindo o menu de contexto para os menus do menu Iniciar e o menu de
  aplicativos do Microsoft Edge (Redstone 5).
* Para além dos diálogos já reconhecidos pelo NVDA, mais diálogos são agora
  reconhecidos como diálogos apropriados e relatados como tal, incluindo o
  diálogo Insider Preview (app de configurações).
* Na maioria dos casos, o NVDA pode anunciar a contagem de sugestões ao
  realizar uma pesquisa. Esta opção é controlada pelo ítem "fornecer
  informações de posição do objecto" no painel de apresentação de objectos
  que pode ser encontrado nas configurações do NVDA.
* Em determinados menus de contexto (como no Edge), as informações de
  posição (por exemplo, 1 de 2) deixaram de ser anunciadas.
* Os seguintes eventos UIA são, agora, reconhecidos: alteração da posição do
  texto activo, controlador para, arrastar início, arrastar cancelamento,
  arrastar completo, elemento selecionado, alterar região ao vivo,
  notificação, alerta do sistema, tooltip aberta, janela aberta. Com o NVDA
  configurado para ser executado com o log de depuração activado, esses
  eventos serão rastreados e, para o evento de notificação UIA, um beep de
  depuração será ouvido se as notificações vierem de algum lugar diferente
  do aplicativo actualmente activo.
* As dicas de ferramentas do Edge e aplicativos universais são reconhecidas
  e serão anunciadas.
* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará a ID atual da área de trabalho (área de trabalho 2, por
  exemplo).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação do ecrã.
* Na versão 18323 e posteriores, o NVDA anunciará alterações de volume de
  áudio e brilho.

## Centro de acção

* A ação rápida do brilho agora é um botão em vez de um botão de
  alternância. Isto fará parte do NVDA 19.1.
* Várias alterações de status, como Foco Assistido e Brilho, passam a ser
  indicadas.  Isto fará parte do NVDA 19.1.

## Alertas e relógio

* Os valores do Time Picker agora são anunciados, visíveis ao mover o foco
  para os controlos do selector. Isso também afecta o controlo usado para
  seleccionar quando reiniciar para concluir a instalação das actualizações
  do Windows.  Isto fará parte do NVDA 19.1.

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

## Correio.

* Ao rever itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para rever os respectivos cabeçalhos. Observe que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.
* O NVDA não fará mais nada ou reproduzirá tons de erro após fechar este
  aplicativo.

## Mapas.

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  activada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Edge

* O preenchimento automático de texto será rastreado e anunciado na barra de
  endereço.
* O NVDA não reproduzirá mais o som de sugestão ao pressionar F11 para
  alternar para ecrã inteiro.

## Teclado moderno

Nota: a maioria dos recursos seguintes, agora, fazem parte do NVDA 2018.3 ou
posteriores.

* Suporte para o painel de entrada de Emoji na Versão 1709 (Actualização
  Creators de Outono) e posterior, incluindo o painel reformulado na Versão
  1809 (compilação 17661 e posterior) e alterações feitas em 19H1
  (compilação 18262 e posteriores, incluindo categorias kaomoji e símbolos
  na compilação 18305). Se estiver a usar versões do NVDA anteriores a
  2018.4, para melhor experiência ao ler emojis, use o sintetizador de fala
  do Windows OneCore. Se 2018.4 ou posterior estiver em uso, active a
  configuração do Unicode Consortium nas configurações de voz do NVDA e
  defina o nível de símbolo como "alguns" ou superior.
* Suporte para sugestões de entrada de teclado de hardware na versão 1803
  (actualização de abril de 2018) e posterior.
* Nas compilações posteriores à  1709, o NVDA anunciará o primeiro emoji
  selecionado quando o painel de emojis for aberto. Isso é mais perceptível
  na versão 18262 e posterior, onde o painel emoji pode ser aberto para a
  última categoria navegada, como a exibição do modificador de tom de pele
  quando aberto na categoria Pessoas.
* Suporte para anunciar itens da área de transferência em nuvem na versão
  1809 (compilação 17666 e posterior).
* Redução dos detalhes desnecessários ao trabalhar com o teclado moderno e
  seus recursos. Estes incluem não mais anunciar "Microsoft Candidate UI" ao
  abrir sugestões de entrada de teclado de hardware e ficar em silêncio
  quando certas teclas do teclado de toque geram eventos de alteração de
  nome em alguns sistemas.
* O NVDA não reproduzirá mais os tons de erro ou não fará nada ao fechar o
  painel de emojis em compilações mais recentes do Insider Preview do
  19H1. Isso fará parte do NVDA 2019.1.
* Na versão 1809 (actualização de outubro de 2018) e posteriores, o NVDA
  anunciará resultados de pesquisa para emojis, se possível. Este recurso
  fará parte do NVDA 2019.1.

## Pessoas.

* Ao procurar contactos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  faladas automaticamente, incluindo a armazenagem e a limpeza do disco.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Para algumas caixas combinadas e botões de rádio, o NVDA não falhará ao
  reconhecer os rótulos e / ou anunciar mudanças de valor.
* Os sinais sonoros da barra de progresso do volume de áudio deixaram de ser
  ouvidos, a partir da versão 1803 e posteriores.
* São anunciadas Mais mensagens sobre o status do Windows Update,
  especialmente se o Windows Update encontrar erros.
* O NVDA não irá mais parecer não fazer nada ou tocar tons de erro se usar
  comandos de navegação de objectos sob algumas circunstâncias.
* A caixa de diálogo de lembretes do Windows Update é reconhecida como um
  diálogo apropriado.

## Skype

Nota: as entradas seguintes não funcionarão correctamente na aplicação
universal do Skype 14.

* O texto do indicador de escrita é anunciado exactamente como no cliente
  Skype para o Desktop.
* Os comandos Control + NvDA + número de linha, usados para ler o histórico
  de conversação recente e mover objectos do navegador para entradas de
  conversação no Skype for Desktop, também estão disponíveis no Skype UWP.
* Agora pode pressionar as teclas Alt+número para localizar e mover-se para
  conversas (1), lista de contactos (2), bots (3) campo de edição da
  conversação se estiver visível (4). Observe que esses comandos funcionarão
  correctamente se a actualização do Skype lançada em março de 2017 estiver
  instalada. 
* O NVDA já não anunciará "Mensagem do Skype" ao revisar as mensagens para a
  maioria dos casos.
* Na lista do histórico de mensagens, pressionar NVDA+D num item de mensagem
  agora permitirá que o NVDA anuncie informações detalhadas sobre essa
  mensagem, como tipo de canal, data e hora de envio e assim por diante. 

## Loja.

* Depois de verificar as atualizações da aplicação, os nomes das aplicações,
  na lista de aplicações a serem actualizadas, são indicados correctamente.
* When downloading content such as apps and movies, NVDA will announce
  product name and download progress.

## Meteorologia

* Separadores como "previsão" e "mapas" são reconhecidos como separadores
  adequados (patch de Derek Riemer).
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
