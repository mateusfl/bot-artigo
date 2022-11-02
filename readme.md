## Artigo Do Dia

Status: Em construção

Esse é o projeto de um bot de twitter para postar todos os dias um artigo aleatório da Wikipédia. Por enquanto a postagem é feita manualmente, ainda faltam coisas pra serem implementadas.

### Algumas considerações:

- O arquivo **script.py** contém o código responsável por buscar, filtrar e apresentar o título, url e primeiro parágrafo de um artigo aleatório da wikipédia para ser escolhido ou não pelo usuário. Esse script pode ser usado independente do arquivo **twitter_script**, que contém a parte responsável pela api do twitter.
- Devido à estruturação das páginas da wikipédia ser um pouco inconsistente, alguns parágrafos podem ser selecionados de forma estranha e não trazer informações úteis sobre o artigo. Nesse caso deve-se escolher outro artigo.