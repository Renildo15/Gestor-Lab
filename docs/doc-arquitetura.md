# Documento da Arquitetura
<hr>
<img src = "https://miro.medium.com/max/1400/1*AO8Ew0nELCH2w0Bf412UTA.png"/>

|   Componentes   | Descrição |
| ---------- | ----------- |
|Template  | É um arquivo de texto que define a estrutura ou o layout de um arquivo (como uma página HTML), com espaços reservados usados para representar o conteúdo real. |
|View| Uma view é uma função manipuladora de solicitações, que recebe solicitações HTTP e retorna respostas HTTP. As views acessam os dados necessários para satisfazer solicitações por meio dos models (modelos) e encarregam a formatação da resposta aos templates. |
|Model| Modelos são objetos em Python que definem a estrutura dos dados de um aplicativo, e fornecem mecanismos para gerenciar (adicionar, modificar e excluir) e consultar registros no banco de dados.|
|URLs| Um mapeador de URLs é usado para redirecionar solicitações HTTP para a view apropriada com base na URL da solicitação. |
|Banco De Dados| Por padrão, o Django vem com o banco de dados integrado(SQLite), sendo possível mudar para outro(Postgres, por exemplo). A criação do banco é feita automaticamente logo após à criação dos models e das migrações.|



* Referência da imagem:https://diandrasilva.medium.com/como-funciona-a-arquitetura-mtv-django-86af916f1f63