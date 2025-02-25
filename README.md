# Escaneamento de portas utilizando um programa em Python

Atividade de desenvolvimento de um portscanner em Python para a disciplina de Tecnologias Hacker - Engenharia da Computação - Insper 2025.1

## Modo de utilização

Para executar o código, basta digitar no terminal um comando com a seguinte sintaxe:

```bash
python main.py 
	[-t;-u]
	[-n;-h]
	[network;host]
	[port_range=start,end(default=1,1000)]
	[ip_range=start,end(default=1,255)]
```

Exemplo 1 (host): escaneamento do host X.X.X.X

```bash
python main.py -h X.X.X.X
```

ou ainda

```bash
python main.py -h X.X.X.X port_range=100,500
```

Exemplo 2 (rede): escaneamento do host X.X.X

```bash
python main.py -n X.X.X
```

ou ainda

```bash
python main.py -h X.X.X ip_range=100,255
```

e assim por diante.
