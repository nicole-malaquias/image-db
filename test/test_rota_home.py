# Fazendo a importação da variável app declarada no __init__.py
from app import app 

# Retornando o test client do nosso app
def app_client():
    return app.test_client()


def test_status_code_rota_home():
    # Pegando o retorno da nossa função app_client()
    client = app_client()

    # Pegando a resposta da requisição na rota "/"
    response = client.get("/")

    # Testando se o status HTTP do retorno é igual ao esperado
    assert response.status_code == 200, "Status incorreto"


def test_json_response_rota_home():
    client = app_client()
    response = client.get("/")

    # Resposta esperada
    expected_dict = {"message": "Meu primeiro teste com flask!"}

    # Testando se o retorno é um dicionário
    assert type(response.get_json()) == dict, "Não retornou dicionário"

    # Testando se o dicionário retornado é igual ao esperado
    assert response.get_json() == expected_dict, "Retorno incorreto"
    


# Rota de listagem '/files';
# Rota de listagem por tipo '/files/<type>';
# Rota de dowload por nome de arquivo '/download/<file_name>';
# Rota de dowload ZIP '/download-zip';
# Rota de upload '/upload';
