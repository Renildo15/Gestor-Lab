## GestorLab

Projeto de Gestão de Laboratórios para gerenciar a equipe, as tarefas, os projetos, os artigos
e as apresentações no laboratório.

* A tecnologia escolhida para o projeto foi o **Python** utilizando o frame work **Django**

* Tutoriais da tecnologia escolhida: https://www.youtube.com/watch?v=Dzuiy-JNi-E&ab_channel=FabioRuicci, https://www.w3schools.com/django/index.php

## Documentos

[Documento de visão](https://github.com/Renildo15/Gestor-Lab/blob/main/docs/doc-visao.md)<br/>
[Documento de Modelos](https://github.com/Renildo15/Gestor-Lab/blob/main/docs/doc-modelo.md)<br/>
[Plano de Interação e Releases](https://github.com/Renildo15/Gestor-Lab/blob/main/docs/doc-interacao.md)<br/>
[Documento de User Story base](https://github.com/Renildo15/Gestor-Lab/blob/main/docs/doc-userStory.md)<br/>


## Instalação

1. Clone o repositório do projeto para a sua máquina:
```console
git clone https://github.com/Renildo15/Gestor-Lab.git
```

2. Caso não tenha o docker instalado clique no link e o baixe. Se já possui, pule para o passo 3. [Baixar o Docker Desktop](https://docs.docker.com/desktop/windows/install/)
<br>

3. Se já possui o docker o seguinte passo é Criar a network
```console
docker network create -d bridge imd-network
```

4. Criar o container do PostgreSQL 
```console
docker run --name postgres-server -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 -v $HOME/dev/docker/volumes/postgres/postgresql:/var/lib/postgresql -v $HOME/dev/docker/volumes/postgres/postgresql_data:/var/lib/postgresql/data --network=imd-network -d postgres:latest
```

5. Criar o container do PgAdmin
```console
docker run --name pgadmin-server -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=admin@admin.com" -e "PGADMIN_DEFAULT_PASSWORD=pgadmin" --network=imd-network -d dpage/pgadmin4:latest
```
6. Instale o docker compose [link](https://docs.docker.com/compose/install/)
<br>
8. Rodando o Gestor lab

```console
docker-compose up

```
