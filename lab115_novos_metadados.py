"""
Novidade da versão 3.8 => podemos verificar a versão de qualquer pacote que estejamos trabalhando

"""

# Trabalhando com metadados -> é necessário realizar o import de metadata

from importlib import metadata

# print(f'A versão do módulo pip é -> {metadata.version("pip")}')   # A versão do módulo pip é -> 20.2.3
#
# # Podemos visualizar também todos os metadados que estão presentes em um pacote -> veja a seguir
#
# metadados_pip = metadata.metadata('pip')
#
# print(f'Os metadados existentes no módulo pip são -> {list(metadados_pip)}')
#
# """
# ['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python']
# """
#
# # Com isso, podemos olhar mais de perto um determinado metadata
# print(f'------------Metadata---------')
# print(f' Vamos ver mais de perto um metadata do método pip -> {metadados_pip["Project-URL"]}')  # Documentation,
# # https://pip.pypa.io
#

# Pode ser que você esteja interessado em saber quantos arquivos estão presentes no seu
# pacote pip no projeto em questão

print(f'Quantos arquivos têm no pacote pip -> {len(metadata.files("pip"))}')  # Quantos arquivos têm no
# pacote pip -> 804

# Você pode querer saber o que o pacote pip requer em sua instalação

print(f'O pacote pip requer alguma instalação neste projeto? -> {metadata.requires("pip")}')  # O pacote pip requer
# alguma instalação neste projeto? -> None

# Vamos agora instalar o Django para simular essa necessidade
print(f'O pacote django requer alguma instalação neste projeto? -> {metadata.requires("django")}')
# O pacote django requer alguma instalação neste projeto? -> ['pytz', 'sqlparse (>=0.2.2)',
# "argon2-cffi (>=16.1.0) ; extra == 'argon2'", "bcrypt ; extra == 'bcrypt'"]
