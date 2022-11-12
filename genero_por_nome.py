import pandas as pd 
from unicodedata import normalize


class GeneroPorNome:
    
    """ 
    Retorno  provável sexo do usuário através do nome. 
    M - Masculino
    F - Feminino
    N - Erro
    """

    def __init__(self, nome: str = None):
        self.nome = nome  # nome do usuário


    def __call__(self):
        print(
            'Recebe string com o nome de usuário \
            e retorna o  provável sexo do usuário')


    def normaliza_nome(self) -> str:
        """
        Recebe string com o nome de usuário e retorna a string tratada e
        movendo acentos e caracteres específicos,
        e converter string para caixa alta.
        """
        if self.nome is not None:
            return normalize("NFKD",  self.nome).encode("ascii",
                                                        errors="ignore"
                                                        ).decode("ascii").upper()


    def genJson(self) -> dict: 
        """
        Carrega dataset e os nomes e os mais prováveis sexos dos usuários.
        """
        data = pd.read_csv('nomes.csv.gz')[['first_name', 'classification']]
        return {i[1]: i[2] for i in data.itertuples()}


    def classifica(self) -> str:
        """
        Recebe o nome tratado e retorna o sexo  do usuário.
        caso o nome do usuário não exista na lista é retornado N.
        """
        try:
            return self.genJson()[self.normaliza_nome()]
        except Exception as e:
            return 'N'


if  __name__ == '__main__':
    data = {
    'nome': ['ana', 'Maria', 'joão','antonio','kelly'],
    'idade': [18, 20, 25,36,20]
    }

    df = pd.DataFrame(data=data)

    def sexo(nome):
        return GeneroPorNome(nome).classifica()

    df['sexo'] = df['nome'].apply(sexo)
    print(df)