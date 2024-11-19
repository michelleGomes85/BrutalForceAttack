# Ataque de Força Bruta

Este é um programa que utiliza ataques de dicionário híbrido e força bruta para descobrir senhas baseadas em seus hashes MD5. Ele combina técnicas eficientes de processamento paralelo para verificar possíveis variações de senhas em uma wordlist e combinações geradas.

---

## 🔧 Funcionalidades

- **Ataque de Dicionário Híbrido**: Gera variações de palavras de uma wordlist, incluindo substituições de caracteres, adição de números, símbolos e capitalização.
- **Fallback para Ataque de Força Bruta**: Caso o ataque de dicionário falhe, tenta todas as combinações possíveis até um comprimento definido.
- **Processamento Paralelo**: Usa todos os núcleos disponíveis da CPU para verificar combinações rapidamente.
- **Compatibilidade com Wordlists**: Fácil integração com arquivos de wordlists existentes.

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x
- Uma wordlist com possíveis senhas (`wordlist.txt`)

### Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/BrutalForceAttack.git
   cd BrutalForceAttack
   ```

2. Prepare sua wordlist

- Certifique-se de que o arquivo `wordlist.txt` esteja no mesmo diretório que o script.
- O arquivo deve conter uma palavra por linha.

3. Configure a senha a ser encontrada no script

- Modifique a variável original_password no início do arquivo para a senha desejada ou forneça o hash MD5 diretamente.

4. Execução

```bash
python brutal_force_attack.py
```

---

## 📄 Estrutura do Projeto

- `brutal_force_attack.py`: Arquivo principal contendo toda a lógica do ataque.
- `wordlist.txt`: Arquivo de texto contendo palavras para o ataque de dicionário (não incluído por padrão).

---

## ⚠️ Aviso Legal

 Projeto é apenas para fins educacionais
