# Teste desenvolvedor Python

A ong doghouse precisa de um backend para o seu ecommerce. A ong quer encontrar pessoas que desejam adotar cachorros e gatos e as pessoas precisam visualizar os gatos e os cachorros que estão esperando adoção.

O desenvolvedor deve construir o backend que suporte a operação da ONG.


## Instalação

Após clonar esse repsitório, crie e habilite seu ambiente virtual com os seguintes comandos:
`python -m venv env` e após `. env/bin/activate/` ou `Scripts\activate`

Instale os requerimentos:
`pip install -r requirements.txt`

Após a instalação das dependencias serem concluídas, execute os seguintes comandos:
`python manage.py makemigrations`
`python manage.py migrate`

## Execução

Para executar, `python manage.py runserver`

## Superuser

`python manage.py createsuperuser`


Apareceram algumas perguntas.
Importante incluir o nome e a senha do usuário.

## Guia de Rotas

- /animal/

### para adicionar, POST

adotado - Adotado (boolean) ex: false
nome - Nome (string) ex: caramelo
descricao - Descrição (string) ex: Cachorro muito adoravél
raca - Raça (string) ex: SRD
cor_pelos - Cor dos Pelos (string) ex: Caramelo
cor_olhos - Cor dos Olhos (string) ex: Castanhos
tipo_pelagem - Tipo de Pelagem (string) ex: Curto
data_nascimento - Data de Nascimento (Date) ex: 2021-09-26
data-resgate - Data de Resgate (Date) ex: 2021-11-26
foto - Foto ex: 


exemplo:

adotado:false
nome:Caramelo
descricao:O Caramelo é um doguinho caramelo muito simpátio!
raca:SRD
cor_pelos:Caramelo
cor_olhos:Castanhos
tipo_pelagem:Curta
data_nascimento:2021-01-08
data_resgate:2021-11-26


## curl

`curl -X POST http://localhost:8000/animal/ -F adotado=False -F nome=Joselinda -F 'descricao=Joselinda é uma gatinha muito amavel' -F raca=SRD -F cor_pelos=Preto -F cor_olhos=Azul -F tipo_pelagem=Curto -F data_nascimento=2018-04-01 -F data_resgate=2018-12-27 -F foto=@/..img/gata-josefa.jpg`


## Atualizar
Comando para atualizar os todos os campos necessários (PUT)

`curl -X PUT \
  http://localhost:8000/animal/1/ adotado=True -F nome=Josefa -F 'descricao=Josefa é uma gatinha muito amavel' -F raca=SRD -F cor_pelos=Preto -F cor_olhos=Verdes -F tipo_pelagem=Curto -F data_nascimento=2018-04-01 -F data_resgate=2018-12-27 -F adotado=false -F foto=@/..caminho/gata-josefa.jpg`


## Atualizar
Comando para atualizar alguns campos (PATCH)

`curl -X PATCH \
  http://localhost:8000/animal/1/ adotado=True`


## Excluir

`curl -X DELETE http://localhost:8000/animal/1/`


## Listar todos os animais

`curl -X GET http://localhost:8000/animal/`