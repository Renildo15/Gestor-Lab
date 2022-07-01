# Documento de Modelos

## Modelo de Dados

### Modelo ER feito no BrModelo

![Modelo ER](./images/modelo_ER.png)


## Dicionário de Dados

|   Tabela   | Laboratório |
| ---------- | ----------- |
| Descrição  | Armazena as informações de um laboratório acadêmico. |
| Observação | Laboratórios acadêmicos podem ser de Ensino, Pesquisa, Extensão, P&D, etc. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id        | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome          | nome do laboratório              | VARCHAR      | 60     | Not Null |
| descricao     | detalhes sobre o laboratório     | VARCHAR      | 250     | --- |
| coordenador     | membro coordenador vinculado ao lab     | INT      | ---    | FK/ Not Null |
| vice-coordenador     | membro vice-coordenador vinculado ao lab     | INT      | ---    | FK |


|   Tabela   | Linha de Pesquisa |
| ---------- | ----------- |
| Descrição  | Armazena as informações de uma pesquisa. |
| Observação |---- |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id        | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome          | nome da pesquisa              | VARCHAR      | 60     | Not Null |
| descricao     | detalhes sobre a pesquisa     | VARCHAR      | 250     | --- |
| areaCNPQ     | Área CNPQ     | VARCHAR      | 250    | --- |
| subAreaCNPQ     | Subarea CNPQ     |  VARCHAR      | 250    | --- |
| laboratório     | Laboratório o qual a pesquisa pertence     |  INT      | ---    | FK/Not Null |


|   Tabela   | TCC |
| ---------- | ----------- |
| Descrição  | Armazena as informações de um TCC. |
| Observação |---- |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome          | nome do tcc             | VARCHAR | 50  | Not Null |
| autor         | nome do autor do tcc    | INT     | --- | FK/Not Null |
| orientador    | nome do orientador do tcc| INT    | --- | FK/Not Null |
| dtpublicacao  | data da publicação do tcc| DATE    | --- | Not Null |
| instituicao   | instituição a qual o tcc foi pertence| VARCHAR    | 50 | --- |
| descricao     | detalhes sobre o tcc| VARCHAR| 250    | --- |
| pesquisa      | pesquisa a qual o tcc está vinculada  |  INT      | ---    | FK/Not Null |


|   Tabela   | Artigo |
| ---------- | ----------- |
| Descrição  | Armazena as informações de um artigo. |
| Observação | ----|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| titulo        | titulo do artigo                 | VARCHAR | 50  | Not Null |
| autor         | nome do autor do artigo          | INT     | --- | FK/Not Null |
| local_Publi   | local onde  será publicado o artigo| VARCHAR   | 250 | Not Null |
| descricao     | detalhes sobre o tcc             | VARCHAR| 250    | --- |
| laboratório   | Laboratório o qual o artigo está vinculado|  INT      | --- | FK/Not Null |


|   Tabela   | Evento |
| ---------- | ----------- |
| Descrição  | Armazena as informações de um evento. |
| Observação | ----|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| titulo        | titulo do evento                 | VARCHAR | 50 | Not Null |
| area          | área do evento                   | VARCHAR | 50 | Not Null |
| laboratório   | Laboratório o qual o evento está vinculado|  INT | --- | FK/Not Null |
| site          | link do site onde vai está mais informações do evento |  VARCHAR | 200 | Not Null |
| data_sbm      | data do evento                   | DATE | --- | Not Null |
| descricao     | detalhes sobre o evento           | VARCHAR| 250    | --- |


|   Tabela   | Projeto |
| ---------- | ----------- |
| Descrição  | Armazena as informações de um projeto. |
| Observação |---- |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome          | nome do projeto                  | VARCHAR | 50 | Not Null |
| coordenador_projeto| coordenador responsavel pelo projeto| INT | --- | FK/Not Null |
| participante  | participantes do projeto         |  INT | --- | FK/Not Null |
| laboratorio_projeto| laboratório o qual o projeto está vinculado | INT | --- | FK/Not Null |
| descricao     | detalhes sobre o projeto           | VARCHAR| 250    | --- |

|   Tabela   | Apresentação |
| ---------- | ----------- |
| Descrição  | Armazena as informações de uma apresentação. |
| Observação | -----|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| titulo        | titulo da apresentação           | VARCHAR      | 50      | Not Null |
| autor         | autor da apresentação            | INT          | ---     | FK/Not Null |
| dataApresentacao| data da apresentação           | DATE         | ---     | Not Null |
| descricao     | detalhes sobre o projeto         | VARCHAR      | 250     | --- |
| pesquisa      | pesquisa a qual a apresentação está vinculada   | INT     | ---    | FK/Not Null |


|   Tabela   | Horário |
| ---------- | ----------- |
| Descrição  | Armazena as informações dos horários dos membros. |
| Observação |----- |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| horario_entrada| hora de entrada                 | DATETIME     | ---     | Not Null |
| horario_saida  | hora de saída                   | DATETIME     | ---     | Not Null |
| turno         | turnos(matutino, vespertino, noturno)| VARCHAR  | 50      | Not Null |
| dia_semana    | dias da semana                  | VARCHAR  | 50      | Not Null |
| membro        | nome do membro                  | INT     | ---    | FK/Not Null |


|   Tabela   | Estágio |
| ---------- | ----------- |
| Descrição  | Armazena as informações dos estágios. |
| Observação | ----|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| estagiario    | nome do estagiario               | INT          | ---     | FK/Not Null |
| orientador    | nome do orientador               | INT          | ---     | FK/Not Null |
| supervisor    | nome do supervisor               | INT          | ---     | FK/Not Null |
| atividade     | atividade de estagio             | VARCHAR      | 250     | Not Null |
| laboratório   | Laboratório o qual o estágio está vinculado|  INT      | --- | FK/Not Null |


|   Tabela   | Discente |
| ---------- | ----------- |
| Descrição  | Armazena as informações do discente. |
| Observação | ----|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity         |
| matricula     | matricula do discente            | INT          | ---     | UNIQUE                |
| nome_discente | nome do discente                 | VARCHAR      | 100     | Not Null              |
| sexo          | sexo do discente                 | VARCHAR      | 15      | ---                   |
| ano_ingresso  | ano do ingresso                  | INT          | ---     | Not Null              |
| periodo_ingresso| periodo do ingresso            | INT          | ---     | Not Null              |
| forma_ingresso| Forma de ingresso na universidade| VARCHAR      | 250     | Not Null              |
| tipo_discente | Tipo de discente (regular ou especial)| VARCHAR | 60      | Not Null              |
| status        | Status do discente (Ativo ou Concluído)| VARCHAR | 60     | Not Null              |
| sigla_nivel_ensino| Sigla do nível de ensino do discente| VARCHAR| 60     | Not Null              |
| nivel_ensino  | Nível de ensino do discente      | VARCHAR      | 60      | Not Null              |
| id_curso      | Identificador do curso do discente| VARCHAR     | 60      | Not Null              |
| nome_curso    | Nome do curso do discente        | VARCHAR      | 60      | Not Null              |
| usuario       | Nome do usuario do discente      | INT          | 60      | ---                   |
| laboratório   | Laboratório o qual o discente está vinculado|  INT      | --- | FK/Not Null       |


|   Tabela   | Docente |
| ---------- | ----------- |
| Descrição  | Armazena as informações do docente. |
| Observação | ----|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity         |
| siape         | Matrícula SIAPE do docente       | INT          | ---     | UNIQUE                |
| nome_discente | Nome do docente                  | VARCHAR      | 100     | Not Null              |
| sexo          | Sexo do docente                  | VARCHAR      | 15      | ---                   |
| formacao      | Denominação da formação/titulação do docente    | VARCHAR | 60     | Not Null     |
| tipo_jornada_trabalho| Regime de trabalho do docente | VARCHAR  | 60      | Not Null              |
| vinculo       | Vínculo do docente               | VARCHAR      | 60      | Not Null              |
| categoria     | Cargo do docente                 | VARCHAR      | 60      | Not Null              |
| classe_funcional | Classe funcional do docente   | VARCHAR      | 60      | Not Null              |
| id_unidade_lotacao| Identificador da unidade de lotação do docente| INT | ---     | ---           |
| lotacao       | Unidade de lotação do docente    | VARCHAR      | 60      | ---                   |
| admissao      | Data em que o docente foi admitido na instituição| DATE     | ---      | Not Null |
| usuario       | Nome do usuario do docente      | INT          | 60      | ---                    |
| laboratório   | Laboratório o qual o docente está vinculado|  INT      | --- | FK/Not Null        |

