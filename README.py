#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `TeamViewer` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `TeamViewer` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install the `TeamViewer` in `Linux Ubuntu`._

# ## Revisão(ões)/Versão(ões)

# |Revisão número|Data da revisão|Descrição da revisão|Autor da revisão|
# |:-:|:-:|:-|:-|
# |0|24/10/2023|<ul><li>Revisão inicial/criação do documento.</li></ul>|Eden Denis F. da S. L. Santos|
# |0|13/12/2023|<ul><li>Revisado todo o documento.</li></ul>|Eden Denis F. da S. L. Santos|
# 

# ## Controle de configuração/instalação nos Sistemas Operacionais (SO) vs. Computador
# 
# |Numero|Computador          |Sistema Operacional (SO) |Tipo de sistema |Status da configuração/instalação|
# |:----:|:------------------:|:-----------------------:|:--------------:|:-------------------------------:|
# |1     |Dell Precision 7520 |Kali   Linux             |Debian          |OK                               |
# |2     |Dell Precision 7520 |Linux Ubuntu             |Ubuntu          |N/A                              |
# |3     |Dell Precision 7520 |Linux Xubuntu            |Ubuntu          |Pendente                         |
# |4     |Dell Precision 7520 |Windows 10               |Windows         |Pendente                         |
# |5     |Asus                |Kali   Linux             |Debian          |N/A                              |
# |6     |Asus                |Linux Ubuntu             |Ubuntu          |Pendente                         |
# |7     |Asus                |Linux Xubuntu            |Ubuntu          |Pendente                         |
# |8     |Asus                |Windows 10               |Windows         |Pendente                         |
# 
# ### Legenda
# 
# - **N/A:** NOT applicable/NÃO aplicável
# - **OK:** Zero killed
# 

# ## Descrição [2]
# 
# `TeamViewer`
# 
# O TeamViewer é uma popular solução de software de acesso remoto e reuniões online que permite que os usuários acessem computadores e dispositivos remotamente a partir de qualquer lugar do mundo. Ele é amplamente utilizado por indivíduos, empresas e equipes de suporte técnico para fornecer assistência remota, solucionar problemas de computador, realizar apresentações e reuniões virtuais, e colaborar em tempo real. O TeamViewer oferece recursos de controle remoto, transferência de arquivos, compartilhamento de tela, bate-papo e videoconferência, tornando-o uma ferramenta versátil para comunicação e colaboração à distância. É compatível com uma variedade de plataformas, incluindo Windows, macOS, Linux, Android e iOS, e é conhecido por sua segurança e criptografia robusta para proteger as sessões de acesso remoto. O TeamViewer é uma escolha popular para aqueles que precisam de uma solução confiável e eficiente para trabalhar e colaborar remotamente.

# ## 1. Configurar/Instalar para `Team Viewer` no 'Linux Ubuntu' [1]
# 
# Para fazer com que o terminal do Ubuntu mostre apenas o nome da última pasta (ao invés do caminho completo), você precisa modificar o arquivo de configuração do shell que você está usando. Para o bash, este arquivo é geralmente ~/.bashrc. Para o zsh, é ~/.zshrc.
# 
# Vou mostrar como fazer isso para o bash, mas o processo é similar para outros shells.
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Certifique-se de que seu sistema esteja atualizado.
# 
#     2.1 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.2 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`

# Para instalar o TeamViewer no Kali Linux pelo terminal, siga estas etapas:
# 
# 1. **Baixe o pacote DEB do TeamViewer:** Primeiro, você precisa baixar o pacote de instalação do TeamViewer. O TeamViewer oferece um pacote DEB que é compatível com sistemas baseados em Debian, como o Ubuntu. Você pode baixar o pacote usando o comando `wget`. Abra o terminal e digite: `wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb`
# 
# 2. **Instale o pacote DEB:** Após o download do pacote DEB, você pode instalá-lo usando o comando `dpkg`. Se ocorrerem problemas de dependência, você pode resolvê-los com o apt. Execute: 
# 
#     ```
#     sudo dpkg -i teamviewer_amd64.deb
#     sudo apt install -f
#     ```
#     
#     O comando `dpkg -i` instala o pacote, e o `apt install -f` corrige quaisquer problemas de dependência.
# 
# 3. **Abra o TeamViewer:** Depois que a instalação for concluída, você pode iniciar o TeamViewer através do terminal ou encontrar o aplicativo no menu de programas.
# 
#     Para iniciar pelo terminal, digite: `teamviewer`
# 
# Assegure-se de que está baixando o pacote TeamViewer do site oficial para evitar questões de segurança. O processo de instalação no Ubuntu é bastante direto, mas é sempre importante garantir que o sistema esteja atualizado antes de instalar novos softwares.

# ### 1.2 Código completo para configurar/instalar
# 
# Para configurar/instalar o `TeamViewer` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt update -y
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
#     sudo dpkg -i teamviewer_amd64.deb
#     sudo apt install -f
#     teamviewer
#     ```

# ## Referências
# 
# [1] OPENAI. ***Instalar teamviewer no kali linux:*** https://chat.openai.com/c/9a96cf1c-939c-494a-a9ed-918fe64f2380 (texto adaptado). ChatGPT. Acessado em: 13/12/2023 07:56.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 13/12/2023 07:56.
