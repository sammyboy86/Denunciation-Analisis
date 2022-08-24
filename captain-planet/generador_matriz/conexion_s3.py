import os
import pandas as pd
import numpy as np
import s3fs
import configparser

config = configparser.ConfigParser()
# Este archivo se creará cuando se instale el AWS command line interface.
# Seguir estas instrucciones: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
# ES OBLIGATORIO instalar este componente antes de continuar esta ejecución.
config.read(os.getenv("userprofile") + '/.aws/credentials')

aws_credentials = {'key': config["cdas-itam"]["aws_access_key_id"],'secret': config["cdas-itam"]["aws_secret_access_key"]}

df = pd.read_csv(f"s3://captain-planet-denuncias-paot/clean/clean_denuncias_paot.csv", storage_options=aws_credentials)

matriz = pd.read_csv(r'C:\Users\samue\OneDrive\Documents\GitHub\captain_planet_sammy\captain-planet\data\clean\matriz_con_carpetas.csv')

matriz.to_csv(f's3://captain-planet-denuncias-paot/clean/matriz_con_carpetas.csv', storage_options=aws_credentials)

