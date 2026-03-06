import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


print("=== Gerador de Senhas ===")

tamanho = int(input("Digite o tamanho da senha: "))

senha = gerar_senha(tamanho)

print("Senha gerada:", senha)
