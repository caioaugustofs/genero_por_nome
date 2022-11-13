import pandas as pd 
from unicodedata import normalize


class JsonDeNome:

    def __init__(self, path:str):
        self.path = str(path)
        
    def geraJson(self) -> dict:
        """
        Carrega dataset e os nomes e os mais prováveis sexos dos usuários.
        """
        data = pd.read_csv(self.path)[['first_name', 'classification']]
        return {i[1]: i[2] for i in data.itertuples()}



class GeneroPorNome:

    def __init__(self, nome, lista_json):
        self.nome = nome  # nome do usuário
        self.lista_json = lista_json

    def __call__(self):
        print(
            'Recebe string com o nome de usuário \
            e retorna o  provável sexo do usuário')

    def normaliza_nome(self):
        """
        Recebe string com o nome de usuário e retorna a string tratada e
        movendo acentos e caracteres específicos,
        e converter string para caixa alta.
        """
        return normalize("NFKD",  self.nome).encode("ascii", errors="ignore"
                                                        ).decode("ascii").upper()
        

    def classifica(self) -> str:
        """
        Recebe o nome tratado e retorna o sexo  do usuário.
        caso o nome do usuário não exista na lista é retornado D.
        """

        try:
            return self.lista_json[self.normaliza_nome()]
        except Exception as e:
            return 'D'


if  __name__ == '__main__':
    data = {
    'nome': ['ana', 'Maria', 'joão','antonio','kelly'],
    'idade': [18, 20, 25,36,20]
    }

    df = pd.DataFrame(data=data)

    json = JsonDeNome(path ='nomes.csv.gz').geraJson()

    def sexo(nome):
        return GeneroPorNome(nome, json).classifica()

    df['sexo'] = df['nome'].apply(sexo)

    print(df)
    




