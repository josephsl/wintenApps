# Windows 10 aplicações essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]

Este extra é uma colecção de módulos de aplicações para várias aplicações do
Windows 10, bem como aprimoramentos e correcções para determinados
controlos.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Alertas e Relógio.
* Calendário.
* Calculadora (moderna).
* Cortana
* Central de comentários
* Barra de jogos.
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

* Nota: este extra requer o Windows 10 Versão 1703 (build 15063) ou
  posterior e o NVDA 2018.2 ou posterior. Para obter melhores resultados,
  use o extra com a última versão estável do Windows 10 (build 16299) e a
  última versão estável do NVDA. Além disso, após alterar as configurações
  de actualização do extra, certifique-se de guardar as configurações do
  NVDA. 
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.

## Geral

* Nos menus de contexto para os ecrãs do menu Iniciar, os submenus são
  devidamente reconhecidos.
* Certos diálogos agora são reconhecidos como diálogos adequados, incluindo
  a caixa de diálogo Insider Preview (aplicativo de configurações).
* O NVDA pode anunciar a contagem de sugestões, ao realizar uma pesquisa na
  maioria dos casos. Esta opção é controlada por "fornecer informações de
  posição do objeto" na caixa de diálogo de apresentação do objeto.
* Em determinados menus de contexto (como no Edge), as informações de
  posição (por exemplo, 1 de 2) deixaram de ser anunciadas.
* Os seguintes eventos UIA são reconhecidos: Controlador para, arrastar para
  início, arrastar para cancelamento, arrastar para completo, elemento
  seleccionado, alterar região, notificação, alerta do sistema, barra de
  ferramentas aberta, janela aberta. Com o NVDA configurado para ser
  executado com o log de depuração ativado, esses eventos serão rastreados
  e, para o evento de notificação do UIA, um tom de depuração será ouvido.
* Adicionada a capacidade de verificar actualizações adicionais (automáticas
  ou manuais) através da caixa de diálogo do Windows 10 aplicações
  essenciais encontrada no menu de preferências do NVDA. Por defeito, as
  versões estáveis e de desenvolvimento verificarão novas actualizações
  semanalmente ou diariamente, conforme determinado.
* Em algumas aplicações, o texto da região é anunciado. Isto inclui alertas
  no Edge, resultados na Calculadora e outros. Observe que isso pode
  resultar em fala dupla em alguns casos.
* As notificações de versões mais recentes de aplicativos no Windows 10
  Versão 1709 (build 16299) e posteriores são anunciadas. Devido a
  limitações técnicas, esse recurso funciona corretamente com o NVDA 2018.1
  e posterior e faz parte do NVDA com a versão 2018.2.
* As dicas de ferramentas do Edge e aplicativos universais são reconhecidas
  e serão anunciadas.
* O NVDA não anunciará mais "desconhecido", ao abrir o menu de links rápidos
  (Windows + X). Esta correção fará parte do NVDA 2018.2.
* Na versão 17627 e posteriores, ao abrir uma nova guia Conjuntos (Control +
  Windows + T), o NVDA anunciará os resultados da pesquisa ao pesquisar
  itens na janela Cortana incorporada.
* Ao alternar entre os separadores, o NVDA anunciará o nome e a posição do
  separador para o qual se está a deslocar.
* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará a ID atual da área de trabalho (área de trabalho 2, por
  exemplo).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação do ecrã.

## Alertas e relógio

* Os valores do Time Picker agora são anunciados, visíveis ao mover o foco
  para os controlos do selector. Isso também afecta o controlo usado para
  seleccionar quando reiniciar para concluir a instalação das actualizações
  do Windows.

## Calculadora

* Quando as teclas ENTER ou Escape são pressionadas, o NVDA anuncia os
  resultados do cálculo.
* Para cálculos como conversor de unidades e conversor de moeda, o NVDA
  anunciará os resultados assim que os cálculos forem inseridos.

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

## Barra de jogos.

* O NVDA anunciará a aparência da janela da barra de jogos. Devido a
  limitações técnicas, o NVDA não pode interagir completamente com a barra
  de jogos.

## Correio.

* Ao rever itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para rever os respectivos cabeçalhos.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.

## Mapas.

* NVDA reproduz o sinal sonoro de localização para locais no mapa.
* Ao usar a vista lateral da rua e se a opção "Usar teclado" estiver
  activada, o NVDA anunciará os endereços de rua enquanto usa as teclas de
  seta para navegar no mapa.

## Microsoft Edge

* Notificações como downloads de ficheiros e vários alertas da página são
  anunciados.

## Teclado moderno

* Suporte para o painel de entrada do Emoji na versão 1709 (Actualização
  "Fall Creators ") e posterior, incluindo o painel reprojetado na
  compilação 17661 e posterior. Para obter uma melhor experiência ao ler
  emojis, use o sintetizador de fala do Windows OneCore.
* Suporte para sugestões de entrada de teclado de hardware na versão 1803
  (actualização de abril de 2018) e posterior.
* Ao procurar contactos, será reproduzido um som, se houver resultados da
  procura.
* Suporte para anunciar itens da área de transferência em nuvem no build
  17666 (Redstone 5) e posterior.

## Pessoas.

* Ao procurar contactos, um som será reproduzido se houver resultados de
  pesquisa.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  faladas automaticamente.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Os grupos de configurações são reconhecidos ao usar a navegação por
  objectos para navegar entre controlos.
* Para algumas caixas combinadas, o NVDA não falhará ao reconhecer os
  rótulos e / ou anunciar mudanças de valor.
* Os sinais sonoros da barra de progresso do volume de áudio deixaram de ser
  ouvidos, a partir da versão 1803 e posteriores.

## Skype

* O texto do indicador de escrita é anunciado exactamente como no cliente
  Skype para o Desktop.
* Retorno parcial do Control+NvDA+números para ler o histórico de
  conversação recente e mover o navegador de objecto para entradas de
  conversação, exactamente como no Skype para Desktop.
* Agora pode pressionar as teclas Alt+número para localizar e mover-se para
  conversas (1), lista de contactos (2), bots (3) campo de edição da
  conversação se estiver visível (4). Observe que esses comandos funcionarão
  correctamente se a actualização do Skype lançada em março de 2017 estiver
  instalada.
* Agora são anunciados os rótulos de caixa combinada para o aplicativo de
  pré-visualização do Skype lançado em novembro de 2016.
* O NVDA já não anunciará "Mensagem do Skype" ao revisar as mensagens para a
  maioria dos casos.
* Foram resolvidos Vários problemas ao usar o Skype com linhas braille,
  incluindo a incapacidade de rever itens do histórico de mensagens em
  braille.
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
