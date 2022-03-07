import requests


def test_api_post():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }


    url = "http://192.168.0.14:5000/api/post/{}".format("facilidades")

    resposta = requests.get(url, headers=headers)

    status = resposta.status_code
    tamanho_lista = len(resposta.json())

    # print(len(resposta.text), resposta.json(), tamanho_lista)

    assert (status == 'success' or status == 200) and tamanho_lista > 0

    # print(resposta.status_code)
    # print("---------------------------------\n")
    # print(resposta.json)
    # print(resposta.text)



def test_api_post_clique_id():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }


    url = "http://192.168.0.14:5000/api/post/clique/{}".format(2)

    resposta = requests.get(url, headers=headers)

    status = resposta.status_code
    tamanho_lista = len(resposta.json())

    # print(len(resposta.text), resposta.json(), tamanho_lista)

    assert (status == 'success' or status == 200) and tamanho_lista > 0
    

test_api_post()
test_api_post_clique_id()