# coding=utf-8
import binascii
import os


def make_secret_key():
    print("[!] Criando hash para SECRET_KEY")
    diretorio = os.getcwd()
    file = None

    with open("{0}/{{ cookiecutter.nome_do_projeto }}/settings.py".format(diretorio), "r") as f:
        file = f.read()

    secret_key = binascii.hexlify(os.urandom(24))

    file = file.replace("CHANGE_ME", secret_key)

    with open("{0}/{{ cookiecutter.nome_do_projeto }}/settings.py".format(diretorio), "w") as f:
        f.write(file)

    print("[!] Hash para SECRET_KEY ok.")


make_secret_key()
