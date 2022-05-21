# Documento lista de User Stories

## Histórico de Revisão

Data | Versão |  Descrição |  Autor
---- | ------ | ---------- | -----
02/05/2022 | 0.0.1 | Detalhamento do User Story RF001 | Eduardo
17/05/2022 |0.0.2|Atualização dos User Stories|Renildo


### User Story 001 - Manter laboratório de pesquisa:

Descrição | O Sistema deve manter um cadastro do loboratório de pesquisa. O laboratório tem os atributos id, nome, descrição, um coordenador, um vice-coordenador. O administrador será quem poderá cadastrar um laboratório, alterar ou remover, e usuário poderá consultar os laborátorios.
--------- | -----------------------------------------------

Requisitos Envolvidos |       |
--------------------- | -------
RF001 | Cadastrar Laboratório|
RF002 | Alterar Laboratório|
RF003 | Listar Laboratório  |
RF004 | Excluir Laboratório  |

Prioridade | Essencial
---------- | --------
Estimativa | 10h
Tempo Gasto (real): | 5h
Tamanho Funcional | 34 PF
Analista | Breno
Desenvolvedor | Renildo
Revisor | Eduardo
Testador | Jeison

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA01.01 | O usuário precisa cadastrar um laborátorio no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro Laboratório". Então será exibido uma tela onde terá uma tabela com os laboratórios já cadastrados e os botões de Adiconar, atualizar, visualizar e deletar.
TA01.02|Ao clicar em "Adicionar Laboratório " uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos laboratórios cadastrados.
TA01.03|O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA01.04|O usuário deseja ver os dados do laboratório cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do laboratório escolhido.
TA01.05|O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. O usuário faz a edição desejada e depois clica em "Salvar" onde sua alteração será salva e o usuário será levado de volta à tela principal(da tabela).
TA01.06|No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA01.07|O usuário(usuário administrador) deseja deletar um laboratório, então ele clica em "Deletar". o cadastro do laboratório é apagado instantaneamente da tabela e do sistema.
TA01.08|Todas as telas que são exibidas decorrentes ao clique de uma opção, temum botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.

### User Story 002 - Manter linhas de pesquisa:

Descrição | O Sistema deve manter um cadastro de linhas de pesquisa. As linhas de pesquisa tem os atributos nome, descrição, área e CNPQ. O professor será quem poderá cadastrar uma linha de pesquisa, alterar ou remover. O usuário poderá consultar as linhas de pesquisa.
--------- | -----------------------------------------------

Requisitos Envolvidos |     |
--------------------- | -------
RF005 | Cadastrar Linhas de Pesquisa |
RF006 | Alterar Linhas de Pesquisa |
RF007 | Listar Linha de Pesquisa |
RF008 | Excluir Linha de Pesquisa |

Prioridade | Essencial
---------- | --------
Estimativa | 10h
Tempo Gasto (real): | 5h
Tamanho Funcional | 34 PF
Analista | Jeison
Desenvolvedor | Pedro
Revisor | Breno
Testador | Leonardo

### User Story 003 - Manter Membros do laboratório:

Descrição | O Sistema deve manter um cadastro de Membros do laboratório. Os Membros do Laboratório tem os atributos nome, email, telefone e perfil, eles podem ser Docente, Discente, Colaborador. O professor será quem poderá cadastrar um Membro do laboratório, alterar ou remover o mesmo. O usuário poderá consultar os membros.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF009 | Cadastrar Membro do laboratório           |
RF010 | Alterar Membro do laboratório           |
RF011 | Listar Membro do laboratório             |
RF012 | Excluir Membro do laboratório             |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | 5h
Tamanho Funcional | 34 PF
Analista | Pedro
Desenvolvedor | Breno
Revisor | Eduardo
Testador | Renildo

### User Story 004 - Manter projetos de Ensino, Pesquisa e Extensão:


Descrição | O Sistema deve manter um cadastro de projetos de Ensino, Pesquisa e Extensão. Os Projetos terão os atributos nome, descrição, coordenador e participantes. O professor é quem poderá cadastrar e atualizar os projetos. O usuário poderá consultar. Quem poderá deletar um projeto é o administrador.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF013 | Cadastrar Projeto         |
RF014 | Alterar Projeto         |
RF015 | Listar Projeto           |
RF016 | Excluir Projeto           |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | 5h |
Tamanho Funcional | 34 PF
Analista | Renildo
Desenvolvedor | Leonardo
Revisor | Eduardo
Testador | Jeison


### User Story 005 - Manter Eventos:

Descrição | O Sistema deve manter um cadastro de eventos. Os eventos terão os atributos título, descrição, área, data de submissão, site. O usuário profesor será quem poderá cadastrar, alterar, consultar, e o usuário administrador será quem poderá remover um evento.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF017 | Cadastrar Evento         |
RF018 | Alterar Evento        |
RF019 | Listar Evento          |
RF020 | Excluir Evento           |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | 5h |
Tamanho Funcional | 34 PF
Analista | Jeison
Desenvolvedor | Eduardo
Revisor | Breno
Testador | Renildo


### User Story 006 - Manter Artigos publicados:

Descrição | O Sistema deve manter um cadastro de artigos. Os artigos terão os atributos título, autores, local de publicação e descrição. O usuário professor será quem poderá cadastrar,e o usuário administrador poderá alterar e remover e o usuário poderá consultar o artigo.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF021 | Cadastrar Artigos publicados         |
RF022 | Alterar Artigos publicados        |
RF023 | Listar Artigos publicados         |
RF024 | Excluir Artigos publicados           |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | 6h |
Tamanho Funcional | 34 PF
Analista | Breno
Desenvolvedor | Jeison
Revisor | Leonardo
Testador | Pedro

Teste de aceitação (TA) |    |
----------------------- | -----
Código | Descrição
TA01 | 



