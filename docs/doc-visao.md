# Documento de visão

# Equipe e Definições dos papeis

Membro | Papel | Email
------ | ----- | -----
Breno | Programador | brenoalves43@hotmail.com
Eduardo | Gerente | eduardo.h3nriqu3@gmail.com
Renildo | Programador | renildorabi22@gmail.com
Jeison | Programador | jeisonjs42@gmail.com
Leonardo | Testador | leonardodds@hotmail.com
Pedro | Testador | pedro.augustohp02@gmail.com

## Matriz de Competências 

Membro | Competência 
------ | -----------
Breno | Desenvolvedor Python(Django), JavaScript, PHP.
Eduardo | Desenvolvedor Python(Django), JavaScript.
Renildo | Desenvolvedor Python(Django), JavaScript.
Jeison | Desenvolvedor Python, JavaScript, C.
Leonardo | Desenvolvedor Python, JavaScript, C.
Pedro | Desenvolvedor Python, JavaScript, Java, C.

# Descrição do projeto

O projeto tem como objetivo facilitar o gerenciamento dos laboratórios, tendo funcionalidades de gestão de equipes, tarefas, projetos, artigos e as apresentações no laboratório LabCoffe MeetUP.

# Perfis dos usuários

O sistema poderá ser usado por Alunos e Professores.

* Perfil do Professor: Os professores poderão fazer solicitações de projetos e pesquisas, gerenciar as atividades dos estágios, visualizar e publicar artigos, atualizar lista de eventos.

* Perfil do Aluno: Os alunos usarão o sistema para entregar os projetos e pesquisas solicitados pelo professor, entregar as atividades dos estágios, visualizar e publicar artigos, vizualizar lista de evetos.

# Requisitos funcionais

Requisito| Descrição   | Ator |
---------| ----------- | ---------- |
RF001 - Cadastrar Laboratório de pesquisa | O laboratório possuem nome, descrição, linhas de pesquisa, coordenador, vice-coordenador, membros discentes, docentes e colaboradores externos. | Administrador 
RF002 - Atualizar Laboratório de pesquisa | Permite a mudança de nome, descrição, linhas de pesquisa, coordenador, vice-coordenador, discentes, docentes e colaboradores externos. | Administrador
RF003 - Listar laboratórios de pesquisa | Permite listar todos os laboratórios. | Usuário
RF004 - Deletar laboratório de pesquisa | Permite deletar o Laboratório do sistema. | Administrador
RF005 - Cadastrar linhas de pesquisa | As linhas de pesquisa possuem nome, descrição e área do CNPQ. | Professor
RF006 - Atualizar linha de pesquisa | Permite a mudança no nome, descrição e na área do CNPQ. | Professor
RF007 - Listar linhas de pesquisa | lista as linhas de pesquisa. | Usuário
RF008 - Deletar linhas de pesquisa | Deleta linha de pesquisa. | Professor
RF009 - Cadastrar membos do laboratório | Os membros possuem nome, email, telefone e perfil(coordenador, docente, discente e colaborador). | Professor
RF010 - Atualizar membros do laboratório | Permite a mudança no nome, email, telefone e perfil. | Professor
RF011 - Listar membros do laboratório | Lista todos os membros participantes do laboratório. | Usuário
RF012 - Deletar membro do laboratório | Deleta um membro da lista do laboratório | Professor
RF013 - Cadastrar projeto de ensino, Pesquisa, Extensão | Os projetos possuem nome, descrição, coordenador, participantes e tipo(Ensino, Pesquisa e Extensão). | Professor
RF014 - Atualizar projeto de ensino, Pesquisa ou Extensão | Permite a mudança no nome, descrição, coordenador, participantes e tipo. | Professor
RF015 - Listar projeto de ensino, Pesquisa ou Extensão | Lista todos os projetos por todos tipo, ou por cada tipo. | Usuário
RF016 - Deletar projeto de ensino, Pesquisa ou Extensão | Deleta o projeto de ensino, Pesquisa ou Extensão. | Administrador
RF017 - Cadastrar evento | O evento possui título, descrição, área, data de submissão, site. | Professor
RF018 - Atulizar evento | Permite a mudança no título, descrição, área e site. | professor
RF019 - Listar eventos | Lista todos os eventos que serão realizados, que já ocorreram, ou todos os eventos. | Professor
RF020 - Deleta evento | Deleta um evento do banco de dados. | Administrador
RF021 - Cadastrar artigos publicados | Os artigos possuem título, autores, local de publicação e descrição. | Professor
RF022 - Atualizar artigos publicados | Permite a mudança no título, autor, local de publização e descrição. | Administrador
RF023 - Listar artigos publicados | lista todos os artigos publicados. | Usuário
RF024 - Deletar artigos publicados | Deleta um artigo publicado. | Administrador
RF025 - Cadastrar estágios | Os estágios possuem informações do estagiário, orientador, supervisor e atividades. | Administrador
RF026 - Aualizar estágios | Permite mudança nas informações do estagiário, orientador, supervisor e atividades. | Administrador
RF027 - Listar estágios | lista os estágios ativos, encerrados ou todos. | Usuário
RF028 - Deletar estágios | Deleta um estágio. | Administrador
RF029 - Cadastrar apresentações | As apresentações possuem autores e são vinculados a um evento ou projeto. | Professor
RF030 - Atualizar apresentações | Permite a mudança no autor(es), e a vinculação do evento. | Professor
RF031 - Lista apresentações | Lista as apresentações que iram acontecer, que aconteceram, ou todas. | Professor
RF032 - Cadastrar horários dos membros dos laboratórios | Os horários possuem horário de entrada, horário de saída e os dias na semana em que os membros estaram trabalhando. | Professor
RF033 - Atulizar horários dos membros dos laboratórios | Permite a mudança do horário de entrada, horário de saída e os dias na semana em que os membros estaram trabalhando. | Professor
RF034 - Listar horários dos membros dos laboratórios | Lista todos os horários dos membros ativos dos laboratórios | Usuário
RF035 - Deletar horários dos membros dos laboratórios | Deleta um horário de um membro do laboratório | Professor
RF036 - Cadastrar TCC | O TCC possui título, descrição, linha de pesquisa, informações do discente, do orientador. | Professor
RF037 - Atulizar TCC | Permite a atualização do título, descrição, linha de pesquisa, informações do orientador. | Administrador
RF038 - Listar TCC | Lista todos os TCC por linha de pesquisa. | Usuário 
RF039 - Deletar TCC | Deleta um TCC. | Administrador
 




.................
# Requisitos não funcionais 
Requisitos| Descrição|
----------| ---------|
RNF001 - Deve ser acessível via navegador| O sistema deve abrir perfeitamente nos navegadores web Chrome e Firefox.|
RNF002 - Consultas rápidas| O sistema deve executar consultas rapidas, não ultrapassando o tempo limite de 1 minuto.|
RNF003 - Conexão com Banco de Dados| O sistema deve ter uma conexão com o banco de dados.|
RNF004 - Fácil utlização| O sistema deve layout intuitivo para que o usuário possa usar sem problemas.|
RNF005 - Idioma | O sistema deve apresentar mensagens e telas no idioma português do Brasil.|
RNF006 - Proteção de dados | O sistema deve garantir proteção aos dados coletados.|


# Riscos

Data | Risco | Prioridade | Responsável | status | Providência/Solução
---- | ----- | ---------- | ----------- | ------ | ------------------
02/05/2022 | Má divisão de tarefas | Baixa | Gerente | Vigente | acompanhar o trabalho realizado pelos membros
02/05/2022 | Algum membro precisar se ausêntar por motivo pessoal | Alta | Gerente | Vigente |Passar as funções do membro afastado para os demais membros
02/05/2022 | Problemas com a aprendizagem das ferramentas usadas pelo componentes do grupo | Alta | Todos | Vigente | Contatar os colegas para um possível esclarecimento do erro, e procurar soluções online 


