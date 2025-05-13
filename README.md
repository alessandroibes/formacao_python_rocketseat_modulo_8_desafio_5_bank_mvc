# Bank MVC

Nesse desafio, é apresentado de forma prática, os conceitos sobre arquitetura de software e padrão MVC apresentados durante a Formação Python da Rocketseat.

A ideia desse desafio é criar uma API para um banco contendo operações para as tabelas de Pessoa Jurídica e Pessoa Física.

Criação de um sistema bancário com clientes:

- Pessoas Físicas
- Pessoas Jurídicas

## Regras da aplicação

[ ] A aplicação deve estar conectada a um banco SQLite;

[ ] O projeto deve conter uma interface Cliente, com os métodos: Sacar dinheiro e Realizar extrato.

[ ] As controllers devem possuir testes unitários para garantir que estão funcionando conforme devem funcionar.

[ ] Deverá ser possível criar usuários

[ ] Deverá ser possível listar usuários.

## Regras de negócio

O método “sacar dinheiro” deve possuir um limite máximo menor em Pessoa física do que para pessoa jurídica