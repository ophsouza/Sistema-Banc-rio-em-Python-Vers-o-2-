# 🏦 Sistema Bancário em Python (Versão 2)

Este é um projeto de um **sistema bancário simples**, feito em Python, com foco em modularização e boas práticas de programação. Ele permite que usuários realizem operações de **depósito**, **saque**, **visualização de extrato**, **cadastro de usuários** e **contas bancárias**.

---

## ✅ Funcionalidades

- Criar **usuário** com CPF único  
- Criar **conta corrente** vinculada a um usuário  
- Realizar **depósitos**  
- Realizar **saques** com:  
  - Limite de valor por saque  
  - Limite diário de saques  
- Exibir **extrato bancário**  
- Listar **todas as contas criadas**

---

## ⚙️ Como funciona

- Cada usuário é identificado por seu **CPF** (sem pontos ou traços)  
- Cada conta tem uma agência padrão (`0001`) e número sequencial  
- As operações financeiras (depósito, saque, extrato) são feitas em memória  
- O código está todo **modularizado em funções**

---

## ▶️ Como executar

1. Certifique-se de ter o **Python 3.10+** instalado  
2. Salve o código em um arquivo, por exemplo `banco.py`  
3. Execute o programa no terminal:

```bash
python banco.py
```

---

## 📄 Exemplo de uso

```text
===== MENU =====
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> nu

Informe o CPF (somente números): 12345678900  
Informe o nome completo: Maria Silva  
Informe a data de nascimento (dd-mm-aaaa): 01-01-1990  
Informe o endereço (logradouro, nro - bairro - cidade/UF): Rua A, 123 - Centro - São Paulo/SP

✅ Usuário criado com sucesso!
```

---

## 📚 Estrutura de Dados

**Usuário:**
```python
{
    "nome": "Maria Silva",
    "data_nascimento": "01-01-1990",
    "cpf": "12345678900",
    "endereco": "Rua A, 123 - Centro - São Paulo/SP"
}
```

**Conta Bancária:**
```python
{
    "agencia": "0001",
    "numero": 1,
    "usuario": <usuário associado>
}
```

---

## 🔒 Regras do sistema

- Um CPF pode ser usado para **apenas um usuário**  
- Um usuário pode ter **várias contas**  
- Saques têm um **limite de R$500 por operação**  
- São permitidos **até 3 saques por dia**

---


