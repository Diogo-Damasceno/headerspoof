# header-spoof

Testa cabeçalhos de host/spoofing em seu próprio servidor.

> **Aviso etico:** ferramenta exclusiva para fins educacionais e testes em
> ambientes que voce possui ou tem autorizacao para auditar. Categoria:
> Ofensiva. Nunca a use contra terceiros.

## Instalacao

```bash
git clone https://github.com/Diogo-Damasceno/header-spoof.git
cd header-spoof
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

## Uso

Verifique como seu app reage a Host/CORS forjados.

Exemplos reais:

```
  $ header-spoof http://127.0.0.1:8080
  {"cors_acao": "*"}```

## Arquitetura

`src/header_spoof/core.py` tem a logica pura (funcoes testaveis); `cli.py` e a
casca de argumentos. Testes em `tests/` cobrem os casos principais.
