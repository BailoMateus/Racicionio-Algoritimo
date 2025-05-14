import random
import string


caracteres = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
captcha = ''.join(random.choices(caracteres, k=6))


print("CAPTCHA:", captcha)


entrada = input("Digite o CAPTCHA exatamente como exibido: ")


if entrada == captcha:
    print(" CAPTCHA correto! Acesso permitido.")
else:
    print(" CAPTCHA incorreto! Acesso negado.")
