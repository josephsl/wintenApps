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

Note: this add-on requires Windows 10 Version 1703 (build 15063) or later
and NVDA 2017.3 or later. For best results, use the add-on with latest
Windows 10 stable build (build 16299) and latest stable version of
NVDA. Also, after changing update settings for the add-on, be sure to save
NVDA settings.

## Geral

* Nos menus de contexto para os ecrãs do menu Iniciar, os submenus são
  devidamente reconhecidos.
* Certos diálogos agora são reconhecidos como diálogos adequados, incluindo
  a caixa de diálogo Insider Preview (aplicativo de configurações).
* O NVDA pode anunciar a contagem de sugestões ao realizar uma pesquisa na
  maioria dos casos. Esta opção é controlada por "fornecer informações de
  posição do objeto" na caixa de diálogo de apresentação do objeto.
* Em determinados menus de contexto (como no Edge), as informações de
  posição (por exemplo, 1 de 2) deixaram de ser anunciadas.
* The following UIA events are recognized: Controller for, element selected,
  live region change, notification, system alert, window opened. With NVDA
  set to run with debug logging enabled, these events will be tracked.
* Adicionada a capacidade de verificar actualizações adicionais (automáticas
  ou manuais) através da caixa de diálogo do Windows 10 aplicações
  essenciais encontrada no menu de preferências do NVDA. Por defeito, as
  versões estáveis e de desenvolvimento verificarão novas actualizações
  semanalmente ou diariamente, conforme determinado.
* In some apps, live region text is announced. This includes alerts in Edge,
  results in Calculator and others. Note that this may result in
  double-speaking in some cases.

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

* Suporte para o painel flutuante de entrada Emoji na Versão 1709
  (Actualização do Fall Creators). Para obter a melhor experiência ao ler
  emojis, use o sintetizador próprio do Windows.
* Suporte para sugestões de entrada de teclado de hardware na compilação
  17040 e posterior.
* Ao procurar contactos, será reproduzido um som, se houver resultados da
  procura.

## Pessoas.

* When searching for contacts, a sound will play if there are search
  results.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  faladas automaticamente.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Os grupos de configurações são reconhecidos ao usar a navegação por
  objectos para navegar entre controlos.
* Para algumas caixas combinadas, o NVDA não falhará ao reconhecer os
  rótulos e / ou anunciar mudanças de valor.
* Os toques da barra de progresso do volume de áudio deixaram de ser ouvidos
  na compilação 17035 e posterior.

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
* when reading a forecast, use the left and right arrows to move between
  items. Use the up and down arrows to read the individual items. For
  example, pressing the right arrow might report "Monday: 79 degrees, partly
  cloudy, ..." pressing the down arrow will say "Monday" Then pressing it
  again will read the next item (Like the temperature). This currently works
  for daily and hourly forecasts.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
