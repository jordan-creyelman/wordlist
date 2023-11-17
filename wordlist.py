import itertools
import string
import time

def generate_wordlist(min_length, max_length, characters):
    wordlist = []

    for length in range(min_length, max_length + 1):
        combinations = itertools.product(characters, repeat=length)
        words = [''.join(combination) for combination in combinations]
        wordlist.extend(words)

    return wordlist

# Caractères à inclure dans la wordlist (lettres minuscules, majuscules, chiffres et caractères spéciaux)
character_set = string.ascii_letters + string.digits + string.punctuation

start_time = time.time()  # Enregistrez le temps de début

# Générer la wordlist de longueur 1 à 6 avec caractères spéciaux
min_length = int(input("entrer le minimum"))
max_length = int(input("entrer le maximu"))
wordlist = generate_wordlist(min_length, max_length, character_set)

end_time = time.time()  # Enregistrez le temps de fin
execution_time = end_time - start_time  # Calculez le temps total d'exécution

# Enregistrer la wordlist dans un fichier
with open('wordlist.txt', 'w') as file:
    file.write('\n'.join(wordlist))

print(f'Wordlist générée avec succès ({len(wordlist)} mots).')
print(f'Le script a mis {execution_time} secondes pour s\'exécuter.')
