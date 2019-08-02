# Windows 10 aplicações essenciais #

* Autores: Joseph Lee, Derek Riemer e outros utilizadores do Windows 10
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]
* NVDA compatibility: 2019.1 to 2019.2

Este extra é uma colecção de módulos de aplicações para várias aplicações do
Windows 10, bem como aprimoramentos e correcções para determinados
controlos.

Os seguintes módulos de aplicações ou módulos de suporte para algumas
aplicações estão incluídos (consulte a secção de cada aplicação para obter
detalhes sobre o que está incluído):

* Calculadora (moderna).
* Calendário.
* Cortana
* Central de comentários
* Correio.
* Mapas.
* Microsoft Edge
* Teclado moderno (painel de emoji / ditado / sugestões de entrada de
  hardware / itens da área de transferência na nuvem na versão 1709 e
  posterior)
* Pessoas.
* Configurações (configurações do sistema, Windows + I)
* Loja.
* Meteorologia.
* Módulos diversos para controlos, como ecrãs do menu Iniciar.

Notas:

* This add-on requires Windows 10 Version 1809 (build 17763) or later and
  NVDA 2019.1 or later. For best results, use the add-on with latest Windows
  10 stable release (build 18362) and latest stable version of NVDA.
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Para entradas não listadas abaixo, pode assumir que os recursos fazem já
  parte do NVDA, não sendo mais aplicáveis, pois o complemento não suporta
  versões antigas do Windows 10, ou foram feitas alterações no Windows 10 e
  nos aplicativos que tornam as entradas desnecessárias.

Para obter uma lista de alterações feitas entre cada release do extra,
consulte o documento [changelogs for releases, release][3].

## Geral

* O NVDA não reproduzirá mais os tons de erro ou não fará nada se este extra
  ficar activo no Windows 7 e 8.1 ou em versões não suportadas do windows
  10.
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
* The following UIA events are recognized: controller for, drag start, drag
  cancel, drag complete, element selected, item status, live region change,
  notification, system alert, text change, tooltip opened, window
  opened. With NVDA set to run with debug logging enabled, these events will
  be tracked, and for UIA notification event, a debug tone will be heard if
  notifications come from somewhere other than the currently active app.
* It is possible to tracke only specific events and/or events coming from
  specific apps.
* Tooltips from Edge and universal apps are recognized and will be
  announced. This will be part of NVDA 2019.3.
* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará o nome da área de trabalho (área de trabalho 2, por exemplo).
* O NVDA deixará de anunciar o tamanho do texto do menu Iniciar quando
  alterar as resoluções ou a orientação do ecrã.
* In Version 1903 (May 2019 Update), NVDA will announce volume and
  brightness changes immediately if focused on File Explorer. This is now
  part of NVDA 2019.2.

## Calculadora

* Quando as teclas ENTER ou Escape são pressionadas, o NVDA anuncia os
  resultados do cálculo.
* Para cálculos como conversor de unidades e conversor de moeda, o NVDA
  anunciará os resultados assim que os cálculos forem inseridos.
* O NVDA não anunciará mais "nível de cabeçalho" para os resultados da
  calculadora.
* ao inserir expressões, o NVDA notificará se a contagem máxima de dígitos
  foi atingida.

## Calendário

* O NVDA já não anuncia "editar" ou "somente leitura" no corpo da mensagem e
  em outros campos.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações
  (se não forem, reabra o menu Iniciar e tente procurar novamente).
* O NVDA ficará em silêncio ao falar com Cortana via voz.
* O NVDA agora anunciará confirmação de lembrete depois de o ter definido.
* In build 18945 and later, modern search experience in File Explorer
  powered by Cortana user interface is supported.

## Central de comentários

* Para os lançamentos mais recentes de aplicativos, o NVDA deixará de os
  anunciar duas vezes.

## Correio.

* Ao rever itens na lista de mensagens, agora pode usar os comandos de
  navegação da tabela para rever os respectivos cabeçalhos. Observe que a
  navegação entre linhas (mensagens) não é suportada.
* Ao escrever uma mensagem, a aparência das sugestões de menção é indicada
  pelos sons.
* NVDA will no longer do anything or play error tones after closing this
  app. This is now part of NVDA 2019.2.

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
* O NVDA não anunciará mais "área de transferência" quando houver itens na
  área de transferência em algumas circunstâncias.
* Em alguns sistemas que executam a Versão 1903 (Actualização de maio de
  2019), o NVDA não deixará de falar, quando o painel emoji for aberto.

## Pessoas.

* Ao procurar contactos, a primeira sugestão será anunciada, principalmente
  se usar os aplicativos mais recentes.

## Configurações

* Certas informações, como o progresso da actualização do Windows, são
  relatadas automaticamente, incluindo sentido / disco de armazenamento e os
  erros da actualização do Windows.
* Os valores da barra de progresso e outras informações já não são
  anunciados duas vezes.
* Para algumas caixas combinadas e botões de rádio, o NVDA não falhará ao
  reconhecer os rótulos e / ou anunciar mudanças de valor.
* Os sinais sonoros da barra de progresso do volume de áudio deixaram de ser
  ouvidos, a partir da versão 1803 e posteriores.
* O NVDA não irá mais parecer não fazer nada ou tocar tons de erro se usar
  comandos de navegação de objectos sob algumas circunstâncias.
* A caixa de diálogo de lembretes do Windows Update é reconhecida como um
  diálogo apropriado.
* Etiquetas de controlo ímpar, vistas em determinadas instalações do Windows
  10, foram corrigidas.
* In more recent revisions of Version 1803 and later, due to changes to
  Windows Update procedure for feature updates, a "download and install now"
  link has been added. NVDA will now announce the title for the new update
  if present.

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
