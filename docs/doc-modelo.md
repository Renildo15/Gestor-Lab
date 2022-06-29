# Documento de Modelos

## Modelo de Dados

### Modelo ER feito no BrModelo

![Modelo ER](/docs//images/Modelo_ER.png)


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
| Observação | |

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
| Observação | |

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
| Observação | |

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
| Observação | |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id            | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| titulo        | titulo do evento                 | VARCHAR | 50 | Not Null |
| area          | área do evento                   | VARCHAR | 50 | Not Null |
| laboratório   | Laboratório o qual o evento está vinculado|  INT | --- | FK/Not Null |
| site          | link do site onde vai está mais informações do evento |  VARCHAR | 200 | Not Null |
| data_sbm      | data do evento                   | DATE | --- | Not Null |
| descricao     | detalhes sobre o evento           | VARCHAR| 250    | --- |

