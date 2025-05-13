from sqlalchemy import BIGINT, Column, REAL, String

from src.models.sqlite.settings.base import Base


class PessoaJuridica(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"Nome Fantasia: {self.nome_fantasia}, Idade: {self.idade}, Saldo: {self.saldo}"
