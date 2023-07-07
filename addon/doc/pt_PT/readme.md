# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros
* Baixar [versão estável][1]
* Descarregar [versão beta][2]
* Baixar a [versão de desenvolvimento][3]
* Compatibilidade com NVDA: 2023.1 e posterior

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

* Cortana (to be replaced by Windows Copilot)
* Teclado moderno (painel de emojis/teclado táctil/ditado/digitação por
  voz/sugestões de entrada de hardware/histórico do clipboard/acções
  sugeridas/editores de métodos de entrada modernos)
* Configurações (configurações do sistema, Windows + I)
* Acesso por voz

Notas:

* This add-on requires Windows 10 22H2 (build 19045), 11 22H2 (build 22621),
  or later releases.
* A duração do suporte da actualização de funcionalidades está associada à
  duração do suporte ao consumidor (edições Home, Pro, Pro Education, Pro
  para Estações de Trabalho) e o suplemento pode terminar o suporte para uma
  actualização de funcionalidades antes do fim do suporte ao
  consumidor. Consulte aka.ms/WindowsTargetVersioninfo para obter mais
  informações e datas de suporte.
* Embora a instalação seja possível, este suplemento não suporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) e versões Windows Server.
* Se o Atualizador de Complementos estiver instalado e as atualizações de
  complementos em segundo plano estiverem ativadas, o Windows App Essentials
  não será instalado em versões não suportadas do Windows.
* Nem todas as funcionalidades das compilações do Windows Insider Preview
  serão suportadas, sobretudo as funcionalidades apresentadas a um
  subconjunto de Windows Insiders nos canais Canary e Dev.
* The add-on may emulate fixes included in Insider Preview builds which are
  subsequently removed, and for these changes, the add-on may remove them in
  future releases.
* O canal de desenvolvimento de complementos incluirá alterações, incluindo
  conteúdos experimentais que podem ou não ser incluídos nas versões beta e
  estável, e o canal beta incluirá alterações planeadas para futuras versões
  estáveis.
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.
* Para melhor experiência com aplicações que incorporam tecnologias web e
  conteúdos como o menu Iniciar e o seu menu de contexto, active a
  configuração "Modo de focagem automática para alterações de focagem" do
  painel de configurações do modo de navegação da NVDA.

Para obter uma lista das alterações efectuadas entre cada versão do extra,
consulte o documento [changelogs for add-on releases][4].

## Geral

* Ao abrir, fechar ou alternar entre áreas de trabalho virtuais, o NVDA
  anunciará o nome da área de trabalho virtual ativa (área de trabalho 2,
  por exemplo). Isso agora faz parte do NVDA 2023.2.
* Improved Windows 10 and 11 taskbar experience, including announcing
  results of rearranging icons when pressing Alt+Shift+left/right arrow keys
  (Windows 11) and reporting item position when moving through taskbar icons
  (Windows 10 and 11). Note that these are emulated workarounds for features
  introduced and then subsequently removed in Insider Preview builds and may
  be removed from the add-on in the future.
* In aps such as Windows 11 22H2 File Explorer and Notepad where tabbed
  windows are supported, NVDA will announce the name and the position of
  tabs when switching between them. This is now part of NVDA 2023.2.

## Cortana

* As respostas textuais da Cortana são anunciadas na maioria das situações.

## Teclado moderno

Isto inclui o painel de emoji, histórico da área de transferência, teclado
táctil, ditado/digitação por voz, sugestões de entrada de hardware, acções
sugeridas e editores de métodos de entrada modernos para determinados
idiomas no Windows 10 e 11. Ao visualizar emojis, para obter a melhor
experiência, active a definição Consórcio Unicode nas definições de voz do
NVDA e defina o nível de símbolo para "alguns" ou superior. Ao colar do
histórico da área de transferência no Windows 10, prima a tecla Espaço em
vez da tecla Enter para colar o item seleccionado.

* No Windows 11 22H2 e posterior, o NVDA anunciará acções sugeridas quando
  dados compatíveis, como números de telefone, forem copiados para a área de
  transferência.

## Configurações

* O NVDA anunciará o nome do controlo de actualização de qualidade opcional,
  se presente (ligação descarregar e instalar agora no Windows 10, botão
  descarregar no Windows 11).
* No Windows 11, os itens da barra de navegação são reconhecidos
  correctamente.
* NVDA will report updates to Windows Update status as download and install
  progresses. This may result in speech interruption when navigating
  Settings app while updates are being downloaded and installed. If using
  Windows 11 and UIA event registration is set to selective from NVDA
  advanced settings panel, you must move focus to updates list as soon as
  they appear so NVDA can announce update progress.

## Acesso por voz

Isto refere-se à funcionalidade de acesso por voz introduzida no Windows 11
22H2.

* O NVDA anunciará o estado do microfone quando alternar entre o microfone e
  a interface de acesso por voz.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps

[2]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=wintenApps-dev

[4]: https://github.com/josephsl/wintenapps/wiki/w10changelog
