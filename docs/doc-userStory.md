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
TA01.01 | O usuário precisa cadastrar um laborátorio no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro Laboratórios". Então será exibido uma tela onde terá uma tabela com os laboratórios já cadastrados e os botões de Adiconar, atualizar, visualizar e deletar. Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nada cadastrado.
TA01.02|Ao clicar em "Adicionar Laboratório " uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos laboratórios cadastrados.
TA01.03|O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA01.04|Os campos "coordenador" e "vice coordenador" não são obrigatórios, sendo possível  cadastrar um laboratório sem informar esses dados. Onde posteriormente no ato da edição, poderá adicioná-los.
TA01.05|O usuário deseja ver os dados do laboratório cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do laboratório escolhido.
TA01.06|O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. O usuário faz a edição desejada e depois clica em "Salvar" onde sua alteração será salva e o usuário será levado de volta à tela principal(da tabela).
TA01.07|No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA01.08|O usuário(usuário administrador) deseja deletar um laboratório, então ele clica em "Deletar". o cadastro do laboratório é apagado instantaneamente da tabela e do sistema.
TA01.09|Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.

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

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA02.01 | O usuário precisa cadastrar um linha de pesquisa no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro Pesquisas". Então será exibido uma tela onde terá uma tabela com as linhas de pesquisa já cadastradas e os botões de Adicionar, atualizar, visualizar e deletar.Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nada cadastrado.
TA02.02 | Ao clicar em "Adicionar Linhas de Pesquisa " uma tela de cadastro será exibida com todos os campos para serem preenchidos.Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela das linhas de pesquisas cadastradas, onde deve ser exibido automaticamente a linha de pesquisa cadastrada.
TA02.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA02.04 | Para cadastrar uma linha de pesquisa é necessário que um laboratório já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA02.05 | O usuário deseja ver os dados da linha de pesquisa cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados da linha de pesquisa escolhida.
TA02.06 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. O usuário faz a edição desejada e depois clica em "Salvar" onde sua alteração será salva e o usuário será levado de volta à tela principal(da tabela).
TA02.07 | Nesse caso, no ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA02.08 | O usuário(usuário administrador) deseja deletar uma linha de pesquisa, então ele clica em "Deletar". O cadastro da linha de pesquisa  é apagada instantaneamente da tabela e do sistema.
TA02.09 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.


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

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA03.01 | O usuário precisa cadastrar um Membro no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro Membros". Então será exibido uma tela onde terá uma tabela com todos os membros já cadastradas e os botões de Adicionar, atualizar, visualizar e deletar.Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nada cadastrado.
TA03.02 |Ao clicar em "Adicionar Membro " uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos membros cadastrados. Onde deve ser exibido automaticamente o membro cadastrado.
TA03.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA03.04 | Para cadastrar um membro não é necessário que um laboratório já tenha sido cadastrado.
TA03.05 | O usuário deseja ver os dados de um membro cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do membro escolhido.
TA03.06 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA03.07 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA03.08 | O usuário(usuário administrador) deseja deletar membro, então ele clica em "Deletar". O cadastro do membro é apagado instantaneamente da tabela e do sistema.
TA03.09 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.

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

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA04.01 | O usuário precisa cadastrar um projeto no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro projetos". Então será exibido uma tela onde terá uma tabela com todos os projetos já cadastradas e os botões de Adicionar, atualizar, visualizar e deletar. Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nada cadastrado.
TA04.02 |Ao clicar em "Adicionar Projeto" uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos projetos cadastrados. Onde deve ser exibido automaticamente o projeto cadastrado.
TA04.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA04.04 | Para cadastrar um projeto é necessário que um laboratório já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA04.05 | Para cadastrar um projeto é necessário que um membro já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA04.06 | O usuário deseja ver os dados de um membro cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do projeto escolhido.
TA04.07 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA04.08 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA04.09 | O usuário(usuário administrador) deseja deletar um projeto, então ele clica em "Deletar". O cadastro do projeto é apagado instantaneamente da tabela e do sistema.
TA04.10 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.



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

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA05.01 | O usuário precisa cadastrar um evento no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro eventos". Então será exibido uma tela onde terá uma tabela com todos os eventos já cadastradas e os botões de Adicionar, atualizar, visualizar e deletar.Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nada cadastrado.
TA05.02 |Ao clicar em "Adicionar Evento" uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos eventos cadastrados. Onde deve ser exibido automaticamente o evento cadastrado.
TA05.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA05.04 | Para cadastrar um evento é necessário que um laboratório já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA05.05 | O usuário deseja ver os dados de um evento cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do evento escolhido.
TA05.06 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA05.07 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA05.08| O usuário(usuário administrador) deseja deletar um evento, então ele clica em "Deletar". O cadastro do evento é apagado instantaneamente da tabela e do sistema.
TA05.09 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.


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

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA06.01 | O usuário precisa cadastrar um artigono sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro artigos". Então será exibido uma tela onde terá uma tabela com todos os artigos já cadastradas e os botões de Adicionar, atualizar, visualizar e deletar.Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nada cadastrado.
TA06.02 |Ao clicar em "Adicionar Artigo" uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos artigos cadastrados.Onde deve ser exibido automaticamente o artigo cadastrado. 
TA06.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA06.04 | Para cadastrar um artigo é necessário que um laboratório já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA06.05 | Para cadastrar um artigo é necessário que um membro já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA06.06 | O usuário deseja ver os dados de um artigo cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do artigo escolhido.
TA06.07 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA06.08 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA06.09 | O usuário(usuário administrador) deseja deletar um artigo, então ele clica em "Deletar". O cadastro do artigo é apagado instantaneamente da tabela e do sistema.
TA06.10 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.






### User Story 007 - Manter TCC:

Descrição | O Sistema deve manter um cadastro de TCC´s. Os trabalhos cadastrados terão os seguntes atributos título, autores, orientadores, instituição de ensino, Data da publicação, e descrição. O usuário professor será quem poderá cadastrar, e o usuário administrador poderá alterar e remover e o usuário poderá consultar o artigo.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF022 | Cadastrar TCC         |
RF023 | Alterar TCC        |
RF024 | Listar TCC         |
RF025 | Excluir TCC           |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | XX Hr |
Tamanho Funcional | 34 PF
Analista | Jeison
Desenvolvedor | Pedro
Revisor | Leonardo
Testador | Renildo

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA07.01 | O usuário precisa cadastrar um Tcc no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro de TCC". Então será exibido uma tela onde terá uma tabela com todos os TCC já previamente cadastrados, e os botões de Adicionar, atualizar, visualizar e deletar. Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nenhum TCC cadastrado.
TA07.02 |Ao clicar em "Adicionar TCC" uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela dos TCC´s cadastrados. Onde deve ser exibido automaticamente o artigo cadastrado. 
TA07.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA07.04 | Para cadastrar um TCC, é necessário que um laboratório já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA07.05 | Para cadastrar um TCC é necessário que um membro já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA07.06 | O usuário que deseja ver os dados de um artigo cadastrado com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados do artigo escolhido.
TA07.07 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA07.08 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA07.09 | O usuário(usuário administrador) deseja deletar um artigo, então ele clica em "Deletar". O cadastro é apagado instantaneamente da tabela e do sistema.
TA07.10 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.




### User Story 008 - Manter Horário:

Descrição | O Sistema deve manter um cadastro de Horários. Os horários cadastrados deverão seguir o seguinte padrão: Caracteres numericos que corresponem ao dia da semana, caracter informando o turno, e caracteres numericos informando o horario, exemplo "35T34". O usuário professor será quem poderá cadastrar, alterar e remover e o usuário poderá consultar o horário.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF026 | Cadastrar Horário         |
RF027 | Alterar Horário        |
RF028 | Listar Horário        |
RF029 | Excluir Horário           |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | XX Hr |
Tamanho Funcional | 34 PF
Analista | Jeison
Desenvolvedor | Pedro
Revisor | Eduardo
Testador | Breno

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA08.01 | O usuário precisa cadastrar um Horário no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro de Horários". Então será exibido uma tela onde terá uma tabela com todos os Horários já previamente cadastrados, e os botões de Adicionar, atualizar, visualizar e deletar. Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nenhum Horário cadastrado.
TA08.02 |Ao clicar em "Adicionar Horário" uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", caso haja um conflito de horários uma mensagem é exibida informando o usuario, a necessidade da mudança, caso não haja conflito o cadastro é realizado e o sistema retorna de volta à tela da tabela dos Horários cadastrados. Onde deve ser exibido automaticamente o horário cadastrado. 
TA08.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA08.04 | Para cadastrar um Horário, é necessário que um laboratório já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA08.05| O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA08.06 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA08.07 | O usuário(usuário administrador) deseja deletar um artigo, então ele clica em "Deletar". O cadastro do horário é apagado instantaneamente da tabela e do sistema.
TA08.08 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.




### User Story 009 - Manter Apresentação:

Descrição | O Sistema deve manter um cadastro de Apresentações. As apresentações cadastradas terão os seguntes atributos título, autores, Data da Apresentação, e descrição,as apresentações devem estar vinculadas aos seus autores e a projetos/eventos. O usuário professor será quem poderá cadastrar, e o usuário administrador poderá alterar e remover e o usuário poderá consultar.
--------- | -----------------------------------------------

Requisitos Envolvidos |      |
--------------------- | -------
RF022 | Cadastrar Apresentação         |
RF023 | Alterar Apresentação       |
RF024 | Listar Apresentação         |
RF025 | Excluir TCCApresentação           |

Prioridade | Essencial
---------- | --------
Estimativa | 12h
Tempo Gasto (real): | XX Hr |
Tamanho Funcional | 34 PF
Analista | Jeison
Desenvolvedor | Pedro e leonardo
Revisor | Renildo
Testador | Eduardo

### Testes de aceitação (TA) 
Código | Descrição
-------|----------
TA09.01 | O usuário precisa cadastrar uma apresentação no sistema, então ele vai em "Cadastros" e depois escolhe "Cadastro de Apresentação". Então será exibido uma tela onde terá uma tabela com todas as apresentações já previamente cadastradas, e os botões de Adicionar, atualizar, visualizar e deletar. Caso não tenha nenhum cadastro, será exibida uma mensagem informando que não há nenhuma apresentação cadastrado.
TA09.02 |Ao clicar em "Adicionar Apresentação" uma tela de cadastro será exibida com todos os campos para serem preenchidos. Logo após informar as informações, o administrador clica em "Salvar", e em seguida é levado de volta à tela da tabela das apresentações cadastradas. Onde deve ser exibido automaticamente a apresentação cadastrada. 
TA09.03 |O usuário não preenche todos os campos obrigatorios. Então na tela deverá ser exibida uma mensagem informando que o usuário não preencheu todos os campos obrigatorios.
TA09.04 | Para cadastrar uma apresentação é necessário que um membro já tenha sido cadastrado, caso contrário, não será possível realizar a ação.
TA09.05 | O usuário que deseja ver os dados de uma apresentação cadastrada com mais detalhes. então ele clica em "Visualizar", onde será exibida uma tela com os dados da apresentação escolhida.
TA09.06 | O usuário deseja editar dados de um cadastro. Então ele clica em "editar", onde será exibida uma tela com todos os dados aptos à serem editados. 
TA09.07 | No ato da edição, o usuário deixa um campo obrigatório em branco, então o sistema não permite a alteração e informa na tela que o todos os campos precisam ser preenchidos corretamente.
TA09.08 | O usuário(usuário administrador) deseja deletar uma apresentação, então ele clica em "Deletar". O cadastro é apagado instantaneamente da tabela e do sistema.
TA09.09 | Em todas as telas que são exibidas decorrentes ao clique de uma opção, há um botão Voltar", que permiti o usuário voltar para a tela principal do cadastro.