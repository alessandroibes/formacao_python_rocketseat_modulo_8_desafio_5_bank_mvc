from abc import ABC, abstractmethod


class CriarPessoaJuridicaControllerInterface(ABC):

    @abstractmethod
    def criar(self, pessoa_juridica: dict) -> dict:
        pass
