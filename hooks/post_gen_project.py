# coding=utf-8
from cookiecutter.main import cookiecutter
import binascii
import os


cookiecutter(
    'https://github.com/AndersonFirmino/django-mongodb',
    extra_context={'secret_key': binascii.hexlify(os.urandom(24)) }
)
