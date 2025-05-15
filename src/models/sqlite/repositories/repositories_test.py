import pytest

from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository
from .pessoa_juridica_repository import PessoaJuridicaRepository


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="database integration")
def test_list_pessoas_fisicas():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.list_pessoas_fisicas()
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_criar_pessoa_fisica():
    pessoa_fisica = {
        "renda_mensal": 12000.00,
        "idade": 42,
        "nome_completo": "José Firmino",
        "celular": "1234-4321",
        "email": "josefi@exemplo.com",
        "categoria": "Categoria D",
        "saldo": 45000.00
    }

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.criar_pessoa_fisica(**pessoa_fisica)


@pytest.mark.skip(reason="database integration")
def test_realizar_extrato_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.realizar_extrato(1)
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_buscar_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.buscar_pessoa_fisica(1)
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_sacar_dinheiro_acima_do_limite_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    with pytest.raises(ValueError) as error:
        repo.sacar_dinheiro(12001.00, 1)

    assert str(error.value) == "Saque excede o limite de R$ 12000.0"


@pytest.mark.skip(reason="database integration")
def test_sacar_dinheiro_com_saldo_insuficiente_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    with pytest.raises(ValueError) as error:
        repo.sacar_dinheiro(10001.00, 1)

    assert str(error.value) == "Saldo insuficiente."


@pytest.mark.skip(reason="database integration")
def test_sacar_dinheiro_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.sacar_dinheiro(1000.00, 1)
    assert response == "Saque de R$ 1000.0 realizado com sucesso. Saldo restante: R$ 9000.0"


@pytest.mark.skip(reason="database integration")
def test_list_pessoas_juridicas():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.list_pessoas_juridicas()
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_criar_pessoa_juridica():
    pessoa_juridica = {
        "faturamento": 85000.00,
        "idade": 7,
        "nome_fantasia": "Empresa CBA",
        "celular": "1234-9999",
        "email_corporativo": "cba@exemplo.com",
        "categoria": "Categoria E",
        "saldo": 125000.00
    }

    repo = PessoaJuridicaRepository(db_connection_handler)
    repo.criar_pessoa_juridica(**pessoa_juridica)


@pytest.mark.skip(reason="database integration")
def test_realizar_extrato_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.realizar_extrato(1)
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_buscar_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.buscar_pessoa_juridica(1)
    print()
    print(response)


@pytest.mark.skip(reason="database integration")
def test_sacar_dinheiro_acima_do_limite_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    with pytest.raises(ValueError) as error:
        repo.sacar_dinheiro(60001.00, 1)

    assert str(error.value) == "Saque excede o limite de R$ 60000.0"


@pytest.mark.skip(reason="database integration")
def test_sacar_dinheiro_com_saldo_insuficiente_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    with pytest.raises(ValueError) as error:
        repo.sacar_dinheiro(50001.00, 1)

    assert str(error.value) == "Saldo insuficiente."


@pytest.mark.skip(reason="database integration")
def test_sacar_dinheiro_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.sacar_dinheiro(1000.00, 1)
    assert response == "Saque de R$ 1000.0 realizado com sucesso. Saldo restante: R$ 49000.0"
