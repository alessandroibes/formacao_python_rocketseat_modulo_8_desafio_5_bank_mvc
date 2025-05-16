from abc import ABC, abstractmethod
from typing import List


class ListarPessoasFisicasControllerInterface(ABC):

    @abstractmethod
    def listar_pessoas_fisicas(self) -> List[dict]:
        pass
