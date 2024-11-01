import hashlib
from multiprocessing import Pool, cpu_count
from itertools import product
import string

# Função para verificar se o hash MD5 de uma palavra corresponde ao hash alvo
def check_hash(word_hash_tuple):
    
    word, target_hash = word_hash_tuple
    word = word.strip()
    
    attempt_hash = hashlib.md5(word.encode()).hexdigest()
    
    if attempt_hash == target_hash:
        return word 
    
    return None

# Função para gerar variações de uma palavra para ataque de dicionário híbrido
def generate_variations(word):
    
    variations = [word]
    
    # Adiciona números ao final da palavra (e.g., 'senha1', 'senha2', ...)
    for i in range(10):
        variations.append(word + str(i))
    
    # Substitui letras comuns por símbolos (e.g., 'a' por '@', 's' por '$')
    substitutions = {'a': '@', 's': '$', 'o': '0', 'i': '1', 'e': '3'}
    for letter, symbol in substitutions.items():
        variations.append(word.replace(letter, symbol))
        
    # Adiciona uma variação com a primeira letra maiúscula
    variations.append(word.capitalize())
    
    # Adiciona símbolos ao início e ao final da palavra
    symbols = ['@', '#', '$', '!', '%', '*']
    for symbol in symbols:
        variations.append(symbol + word)     # Adiciona o símbolo no início
        variations.append(word + symbol)     # Adiciona o símbolo no final

    return variations

# Função para carregar e processar as palavras da wordlist
def load_wordlist(wordlist_file):
    
    try:
        with open(wordlist_file, 'r') as f:
            words = [line.strip() for line in f]
        return words
    except FileNotFoundError:
        print(f"File '{wordlist_file}' not found.")
        return None

# Função que cria uma lista de todas as variações de palavras na wordlist
def create_variation_list(words, target_hash):
    variation_list = []
    
    for word in words:
        variations = generate_variations(word)
        variation_list.extend([(variation, target_hash) for variation in variations])
        
    return variation_list

# Função de ataque de força bruta
def brute_force_attack(target_hash, max_length=4):
    characters = string.ascii_lowercase + string.digits
    pool = Pool(processes=cpu_count())

    # Gera combinações e verifica o hash para cada combinação
    for length in range(1, max_length + 1):
        combinations = product(characters, repeat=length)
        combination_list = [(''.join(comb), target_hash) for comb in combinations]

        # Executa a função check_hash em paralelo
        for result in pool.imap_unordered(check_hash, combination_list):
            if result is not None:  # Senha encontrada
                print(f'Password found via brute force: {result}')
                pool.terminate()
                return result

    pool.close()
    pool.join()
    print("Senha não encontrada no ataque de força bruta")
    return None

# Função principal que realiza o ataque de dicionário híbrido
def hybrid_dictionary_attack(target_hash, wordlist_file):
    
    words = load_wordlist(wordlist_file)
    
    if words is None:
        return None

    pool = Pool(processes=cpu_count())
    
    variation_list = create_variation_list(words, target_hash)

    for result in pool.imap_unordered(check_hash, variation_list):
        if result is not None: 
            print(f'Senha encontrada: {result}')
            pool.terminate() 
            return result

    pool.close()
    pool.join() 
    
    print('Senha não encontrada no ataque dicionario hibrido. Iniciando ataque de força bruta ...')
    return brute_force_attack(target_hash)

if __name__ == '__main__':
    
    # Hash MD5 da senha que queremos descobrir
    original_password = "cr1wdZrm"
    target_hash = hashlib.md5(original_password.encode()).hexdigest()
    print(f"MD5 Senha a ser encontrada: {target_hash}")

    wordlist_file = 'wordlist.txt' 

    # Executa o ataque de dicionário híbrido com fallback para força bruta
    hybrid_dictionary_attack(target_hash, wordlist_file)
