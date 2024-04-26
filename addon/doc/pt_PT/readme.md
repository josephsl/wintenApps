# Windows App Essentials #

* Autores: Joseph Lee, Derek Riemer e outros

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

* Configurações (Windows + I)

Notas:

* This add-on requires 64-bit Windows 10 22H2 (build 19045), 11 22H2 (build
  22621), or later releases.
* A duração do suporte da actualização de funcionalidades está associada à
  duração do suporte ao consumidor (edições Home, Pro, Pro Education, Pro
  para Estações de Trabalho) e o suplemento pode terminar o suporte para uma
  actualização de funcionalidades antes do fim do suporte ao
  consumidor. Consulte <https://aka.ms/WindowsTargetVersioninfo> para obter
  mais informações e datas de suporte.
* Embora a instalação seja possível, este suplemento não suporta Windows
  Enterprise LTSC (Long-Term Servicing Channel) e versões Windows Server.
* Nem todas as funcionalidades das compilações do Windows Insider Preview
  serão suportadas, sobretudo as funcionalidades apresentadas a um
  subconjunto de Windows Insiders nos canais Canary e Dev.
* O canal de desenvolvimento de complementos incluirá alterações, incluindo
  conteúdos experimentais que podem ou não ser incluídos nas versões beta e
  estável, e o canal beta incluirá alterações planeadas para futuras versões
  estáveis.
* Alguns recursos adicionais são ou farão parte do leitor de tela do NVDA.

Para obter uma lista das alterações efectuadas entre cada versão do extra,
consulte o documento [changelogs for add-on releases][1].

## Geral

* In Windows 11 24H2, quick settings (shellhost.exe) interface elements can
  be navigated using mouse and/or touch interaction. This is now part of
  NVDA 2024.2.
* In Windows 11, NVDA will announce suggested actions when compatible data
  such as phone numbers is copied to the clipboard. This is now part of NVDA
  2024.2.

## Configurações (Windows + I)

* NVDA will report updates to Windows Update status as download and install
  progresses. In Windows 10, this may result in speech interruption when
  navigating Settings app while updates are being downloaded and
  installed. In Windows 11, object navigation can be used in updates list to
  review update status for individual entries.

[[!tag dev stable]]

[1]: https://github.com/josephsl/wintenapps/wiki/w10changelog
