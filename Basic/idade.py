idade_pessoa = input('digite sua idade em anos e meses (exp: 15.4): ')

anos, meses = map(int, idade_pessoa.split('.'))

idade_meses = anos * 12 + meses


print('sua idade em meses é:', idade_meses, 'meses')