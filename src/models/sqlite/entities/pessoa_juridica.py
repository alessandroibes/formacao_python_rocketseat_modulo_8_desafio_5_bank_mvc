from sqlalchemy import BIGINT, Column, REAL, String

from src.models.sqlite.settings.base import Base


class PessoaJuridica(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self) -> str:
        return f"Nome Fantasia: {self.nome_fantasia}, Idade: {self.idade}, Saldo: {self.saldo}"

    def to_dict(self) -> dict:
        return {
            "id" : self.id,
            "faturamento" : self.faturamento,
            "idade" : self.idade,
            "nome_fantasia" : self.nome_fantasia,
            "celular" : self.celular,
            "email_corporativo" : self.email_corporativo,
            "categoria" : self.categoria,
            "saldo" : self.saldo
        }
