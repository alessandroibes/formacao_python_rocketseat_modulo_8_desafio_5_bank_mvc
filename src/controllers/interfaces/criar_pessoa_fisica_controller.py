from abc import ABC, abstractmethod


class CriarPessoaFisicaControllerInterface(ABC):

    @abstractmethod
    def criar(self, pessoa_fisica: dict) -> dict:
        pass
