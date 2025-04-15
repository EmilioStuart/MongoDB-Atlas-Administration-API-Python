# Author: EmilioStuart
# Date: 15-04-2025
# Description: Script para gerenciar IPs no MongoDB Atlas usando a API REST
# Requirements: requests, python-dotenv
# Usage: python script.py
# Note: Certifique-se de ter um arquivo .env com as variáveis de ambiente necessárias

# Importar as bibliotecas necessárias
import os
import requests
from requests.auth import HTTPDigestAuth
from pprint import pprint
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env


# Função para mostrar todos os IPs
def mostrar_todos_IPs():
    # Faz a requisição GET
    response = requests.get(base_url, auth = auth, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        print(pprint(response.json()))
    else:
        print(f"Erro na requisição GET: {response.status_code}")


# Função para mostrar IPs por chave e valor
# Exemplo: mostrar_IP("Comentário", "Meu IP")
def mostrar_IP(key, value):
    # Faz a requisição GET
    response = requests.get(base_url, auth = auth, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        for item in response.json()['results']:
            if item[key] == value:
                print(f"{key} encontrado com o valor {value}: {item['ipAddress']}")
                break
    else:
        print(f"Erro na requisição GET: {response.status_code}")


# Função para adicionar um IP
def adicionar_IP(comment, ipAddress):
    # Define o payload da requisição (JSON)
    # Exemplo: payload = [{"ipAddress": "Meu IP", "comment": "Meu Comentário"}]
    payload = [
        {
            "ipAddress": ipAddress,
            "comment": comment,
        }
    ]

    # Faz a requisição POST
    response = requests.post(base_url, auth = auth, headers=headers, json=payload)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 201:
        print(f"IP {ipAddress} adicionado com sucesso!")
    else:
        print(f"Erro na requisição POST: {response.status_code}")
        print(f"Resposta: {response.text}")

# Função para remover IPs por endereço IP
def remover_por_IP(ipAddress):
    # Faz a requisição DELETE
    response = requests.delete(f"{base_url}/{ipAddress}", auth = auth, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 204:
        print(f"IP {ipAddress} removido com sucesso!")
    elif response.status_code == 404:
        print(f"IP {ipAddress} não encontrado.")
    else:
        print(f"Erro na requisição DELETE: {response.status_code}")


# Função para remover IPs por comentário (descrição do IP)
def remover_por_comment(comment):
    # Faz a requisição GET
    response = requests.get(base_url, auth = auth, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        for item in response.json()['results']:
            if item["comment"] == comment:
                ipAddress = item['ipAddress']
                break
    else:
        print(f"Nao foi possível encontrar: {response.status_code}")


    # Faz a requisição DELETE
    response = requests.delete(f"{base_url}/{ipAddress}", auth = auth, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 204:
        print(f"{comment} removido com sucesso!")
    elif response.status_code == 404:
        print(f"{comment} não encontrado.")
    else:
        print(f"Erro na requisição DELETE: {response.status_code}")


base_url = "https://cloud.mongodb.com/api/atlas/v2/groups/" + os.getenv("PROJECT_ID") + "/accessList"

# Define o header do HTTP 
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.atlas.2024-08-05+json' 
}

public_key = os.getenv("PUBLIC_KEY")
private_key = os.getenv("PRIVATE_KEY")
auth = HTTPDigestAuth(public_key, private_key)