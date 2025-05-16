from typing import List

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from .listar_pessoas_juridicas_controller import ListarPessoasJuridicasController


pessoa_juridica_1 = {
    "id" : 1,
    "faturamento" : 100000.00,
    "idade" : 7,
    "nome_fantasia" : "Empresa 1",
    "celular" : "1234-5678",
    "email_corporativo" : "pjuridica@example.com",
    "categoria" : "Categoria Teste",
    "saldo" : 250000.00
}


pessoa_juridica_2 = {
    "id" : 2,
    "faturamento" : 150000.00,
    "idade" : 12,
    "nome_fantasia" : "Empresa 1",
    "celular" : "9999-8888",
    "email_corporativo" : "pjuridica2@example.com",
    "categoria" : "Categoria Teste 2",
    "saldo" : 320000.00
}


class MockPessoaJuridicaRepository():
    def list_pessoas_juridicas(self) -> List[PessoaJuridica]:
        return [
            PessoaJuridica(
                id=pessoa_juridica_1["id"],
                faturamento=pessoa_juridica_1["faturamento"],
                idade=pessoa_juridica_1["idade"],
                nome_fantasia=pessoa_juridica_1["nome_fantasia"],
                celular=pessoa_juridica_1["celular"],
                email_corporativo=pessoa_juridica_1["email_corporativo"],
                categoria=pessoa_juridica_1["categoria"],
                saldo=pessoa_juridica_1["saldo"]
            ),
            PessoaJuridica(
                id=pessoa_juridica_2["id"],
                faturamento=pessoa_juridica_2["faturamento"],
                idade=pessoa_juridica_2["idade"],
                nome_fantasia=pessoa_juridica_2["nome_fantasia"],
                celular=pessoa_juridica_2["celular"],
                email_corporativo=pessoa_juridica_2["email_corporativo"],
                categoria=pessoa_juridica_2["categoria"],
                saldo=pessoa_juridica_2["saldo"]
            )
        ]


def test_listar_pessoas_juridicas():
    controller = ListarPessoasJuridicasController(MockPessoaJuridicaRepository())
    pessoas_juridicas = controller.listar_pessoas_juridicas()

    expected_result = [pessoa_juridica_1, pessoa_juridica_2]

    assert expected_result == pessoas_juridicas
