from abc import ABC, abstractmethod
from typing import List


class ListarPessoasJuridicasControllerInterface(ABC):

    @abstractmethod
    def listar_pessoas_juridicas(self) -> List[dict]:
        pass
