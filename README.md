# tikal-challenge


Para executar a aplicação é necessário ter o `Docker`e o `Docker Compose` instalados.

Para configurar o banco de dados é necessário copiar a pasta `example_env`com o nome `env` na raiz do projeto e colocar a URL do Postgres na variável `RECORTES_DATABASE_URL` no arquivo `django.conf`, substituindo `{{ pass }}`,`{{ host}}`,`{{ port }}` e `{{ database}}` pelos seus respectivos valores.


```
$ mv example_env env
```
URL do Postgres:
```
# ...
RECORTES_DATABASE_URL=psql://{{ pass }}:{{ pass }}@{{ host}}:{{ port }}/{{ database}}
# ...
```


Após o enviroment configurado, para executar aplicação basta utilizar o seguinte comando na raíz do projeto
```
# docker-compose up
```
