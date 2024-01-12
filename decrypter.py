import os

import pyaes


key = b'testeransomwares'
counter = pyaes.Counter(initial_value=100)

# instancia de AESModeOfOperationCTR com a chave e o contador
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)


#abrir o arquivo a ser descriptografado
file_name ="C:\\kali\\teste.txt.ransomwaretroll"
file = open(file_name,'rb')
file_data = file.read()
file.close()
#remover o arquivo original
#os.remove(file_name)

# definindo a chave de descryptografia
key = b"testeransomwares"
#aes = pyaes.AESModeOperationCTR(key)

#descriptografar o arquivo
decrypt_data = aes.decrypt(file_data)

#remover o arquivo cryptografado
#os.remove(file_name)
#criar um  arquivo descryptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()