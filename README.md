## Sobre
 
O `BruteTok` lê uma lista de senhas de um arquivo de texto e testa cada uma contra o endpoint de autenticação configurado, parando quando encontra uma credencial válida (ou ao esgotar a lista). O objetivo é **medir a resistência de senhas** em um ambiente controlado,por exemplo, validar que a política de senha de uma aplicação que você desenvolveu realmente bloqueia senhas fracas e aplica rate limiting.
 
## Funcionalidades
 
- **Wordlist configurável:** basta apontar para outro arquivo `.txt` para trocar completamente o conjunto de senhas testadas, uma senha por linha.
- **Alvo e payload configuráveis:** URL do endpoint, nome do campo de usuário e de senha ajustáveis para casar com a aplicação de teste.
- **Controle de ritmo (rate limiting):** intervalo configurável entre tentativas, para não derrubar o ambiente de teste e respeitar os limites acordados no escopo.
- **Log claro de resultados:** cada tentativa é registrada com seu status, e uma credencial válida é destacada ao final.
## Requisitos
 
- Python 3.9+
- Biblioteca `requests`
## Instalação
 
```bash
git clone <https://github.com/pedr432/BruteTok.git>
cd BruteTok
pip install -r requirements.txt
```
 
Se preferir, instale a dependência diretamente:
 
```bash
pip install requests
```
 
## Configuração
 
Abra o `script.py` e ajuste as variáveis de configuração para apontar para o **seu** alvo de teste:
 
```python
TARGET_URL = "http://localhost:8080/login"   # endpoint da SUA aplicação de laboratório
USERNAME   = "usuario_de_teste"               # conta de teste que você criou para a avaliação
WORDLIST   = "wordlist.txt"                    # arquivo com as senhas a testar
DELAY      = 1.0                               # segundos entre tentativas (respeite o escopo)
```
 
> Defina `TARGET_URL` apenas para um sistema que você controla ou está autorizado a testar. Nunca aponte para um serviço de produção de terceiros.
 
## Uso
 
```bash
python script.py
```
 
A ferramenta percorre a wordlist, testa cada senha contra o alvo configurado e informa o resultado de cada tentativa. Ao encontrar uma credencial válida, ela destaca a senha e encerra.
 
## Trocando a wordlist
 
O recurso principal da ferramenta é poder substituir a wordlist com facilidade. Basta:
 
1. Criar ou baixar um arquivo de texto com **uma senha por linha**.
2. Apontar a variável `WORDLIST` (ou o parâmetro correspondente) para o novo arquivo.
```text
123456
senha123
qwerty
P@ssw0rd!
...
```
 
Wordlists comuns para fins de treino acompanham distribuições como a Kali Linux (ex.: `rockyou.txt`) e são úteis para avaliar o quanto uma política de senha fraca ficaria exposta.
 
## Boas práticas de teste
 
- **Use sempre contas de teste**, criadas especificamente para a avaliação — nunca contas reais de usuários.
- **Respeite o rate limit acordado** no escopo; aumente o `DELAY` se o ambiente for sensível.
- **Documente tudo:** alvo, data/hora, wordlist usada e resultados, para incluir no relatório.
- **Reporte** as senhas fracas encontradas ao responsável pelo sistema e recomende correções (política de senha forte, MFA, bloqueio após N tentativas, detecção de ataques automatizados).
## O que um bom sistema deve ter (o outro lado)
 
Testar credenciais só faz sentido se você souber o que recomendar depois. Um login bem defendido costuma ter: política de senha forte, autenticação multifator (MFA), rate limiting e bloqueio temporário após várias falhas, e monitoramento de tentativas anômalas. Se a sua ferramenta de teste consegue avançar sem esbarrar em nenhuma dessas barreiras, esse é exatamente o achado a reportar.
 
 ## Fé fé ✌🏻✌🏻
