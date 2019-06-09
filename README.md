# Teste desenvolvedor Python

A ong doghouse precisa de um backend para o seu ecommerce. A ong quer encontrar pessoas que desejam adotar cachorros e gatos e as pessoas precisam visualizar os gatos e os cachorros que estão esperando adoção.

O desenvolvedor deve construir o backend que suporte a operação da ONG.


## Instalação

Após clonar esse repsitório, crie e habilite seu ambiente virtual com os seguintes comandos:
`python -m venv env` e após `. env/bin/activate/`
Instale os requerimentos:
`pip install -r requirements.txt`
Após a instalação ser concluída, execute `python manage.py runserver`

A seguir algumas requesições.
Indicamos o uso do Postman para melhor visualização, mas segue os comando via terminal: 


## Adicionar

`curl -X POST http://localhost:8000/animal/ -F adotado=False -F nome=Joselinda -F 'descricao=Joselinda é uma gatinha muito amavel' -F raca=SRD -F cor_pelos=Preto -F cor_olhos=Azul -F tipo_pelagem=Curto -F data_nascimento=2018-04-01 -F data_resgate=2018-12-27 -F adotado=false -F foto=@/..caminho/gata-josefa.jpg`


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