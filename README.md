# FastAPI Password Validation

API simples desenvolvida com FastAPI para validação de senhas.

## Requisitos

* Python 3.10+
* pip

## Instalação

Clone o repositório:

```bash
git clone https://github.com/piudi2121/PasswordCheck/
cd PasswordCheck
```

Instale os pacotes necessários:

```bash
pip install fastapi uvicorn
```

## Execução

Inicie o servidor:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000
```

## Documentação

A documentação automática pode ser acessada em:

```
http://127.0.0.1:8000/docs
```

## Endpoints

```bash
/check/<password:str>
```

## Rascunho

<img width="1352" height="700" alt="Captura de tela 2026-02-10 014351" src="https://github.com/user-attachments/assets/9a0b779c-360b-4bb3-9d50-58755ae2431c" />

---
