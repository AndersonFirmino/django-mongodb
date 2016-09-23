# coding=utf-8
import binascii
import os


def make_secret_key():
    print("Criando a secret_key")
    diretorio = os.getcwd()
    file = None

    with open("{0}/{{ cookiecutter.nome_do_projeto }}/settings.py".format(diretorio), "r") as f:
        file = f.read()

    secret_key = binascii.hexlify(os.urandom(24))

    file = file.replace("SECRET", secret_key, 1)

    with open("{0}/{{ cookiecutter.nome_do_projeto }}/settings.py".format(diretorio), "w") as f:
        f.write(file)
    print("Secret Key ok")


make_secret_key()
