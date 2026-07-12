# headerspoof

Testa cabeçalhos de host/spoofing em seu próprio servidor.

## O que faz

Esta ferramenta de **ofensiva** apenas em aplicacoes suas ou engajamento autorizado. Testa cabeçalhos de host/spoofing em seu próprio servidor. O codigo e
testavel localmente (sem dependencias de rede para os testes unitarios).

> **Aviso etico:** uso exclusivo para fins educacionais e testes em ambientes
> que voce **possui** ou tem **autorizacao expressa** para auditar. Nunca a
> utilize contra sistemas de terceiros. O autor nao se responsabiliza por uso
> indevido.

## Instalacao

```bash
git clone https://github.com/Diogo-Damasceno/headerspoof.git
cd headerspoof
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

## Uso

Verifique como seu app reage a Host/CORS forjados.

## Exemplos reais

```bash
$ header-spoof http://127.0.0.1:8080
# {"cors_acao": "*"}
```

## Como funciona (resumo)

O modulo principal implementa a logica em funcoes puras e testaveis; a CLI e
apenas a casca de argumentos. Os testes em `tests/` (Python) ou `CoreTest.java`
(Java) cobrem os casos principais e rodam offline.

## O que NAO faz

- Nao executa ataques contra terceiros.
- Nao exfiltra dados.
- Nao substitui uma solucao comercial de seguranca.

## Licenca

MIT — ver `LICENSE`.
