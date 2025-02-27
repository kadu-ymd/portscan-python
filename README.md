# Escaneamento de portas utilizando um programa em Python

Atividade de desenvolvimento de um *portscanner* em Python para a disciplina de Tecnologias Hacker - Engenharia da Computação - Insper 2025.1

## Desenvolvedores

**Nome**: Carlos Eduardo Porciuncula Yamada

## Modo de utilização

Para executar o código, basta digitar no terminal um comando com a seguinte sintaxe:

```bash
python main.py
	[-t;-u]
	[-n;-h]
	[-v4;-v6]
	[network_ip;host_ip]
	[port_range=start,end(default=1,1000)]
	[ip_range=start,end(default=1,255)]
```

### Legenda

- `[-t;-u]`: Escaneamento de portas TCP (`-t`) ou UDP (`-u`);
- `[-n;-h]`: Escaneamento de um host (`-h`) ou rede (`-n`);
- `[network_ip;host_ip]`: Endereço a ser escaneado, seguindo o formato **X.X.X.X** para host e **X.X.X** para rede¹;
- `[port_range=start,end(default=1,1000)]`: *Range* de portas a serem escaneadas (*opcional*);
- `[ip_range=start,end(default=1,255)]`: *Range* de IPs a serem escaneados (*opcional*; para quando o escaneamento é da rede).


¹Assume-se que a máscara da rede é 255.255.255.0 (prefixo /24).

___

## Implementações

- [x] Interface amigável (*user-friendly interface*)
- [x] Escaneamento de um *host* ou de uma rede
- [x] Permitir que o usuário insira um *range* de portas a serem escaneadas
- [x] *Prints* contendo número da porta e o serviço associado a ela (para *Well-Known ports*)
- [x] Detecção dos estados das portas (*open*, *closed*, *filtered*, etc.)
- [ ] Opção de escaneamento de portas UDP
- [ ] Descobrir OS através de *banner grabbing*
- [x] Suporte para IPv6

**OBS 1**.: o escaneamento da rede funciona apenas para endereços IPv4 (não foi implementada essa funcionalidade para endereços IPv6);

**OBS 2**.: a implementação do escaneamento de portas UDP existe, mas não funciona corretamente. Logo, pode ser testada, mas nada pode ser concluído a partir dos *prints*.
