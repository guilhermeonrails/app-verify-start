import os
import requests
from datetime import datetime

def validate_url(url):
    if not url.startswith("https://"):
        url = "https://" + url

    if not url.startswith("https://api."):
        url = url.replace("https://", "https://api.")

    if "scratch.mit.edu" not in url:
        restante_url = url.split("https://api.")[1]
        url = "https://api.scratch.mit.edu/" + restante_url
    return url

def make_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        project_data = response.json()
        history_info = project_data.get("history", {})
        created_at = history_info.get("created", "")
        modified_at = history_info.get("modified", "")
        shared_at = history_info.get("shared", "")
    
        created_at_formatted = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y")
        modified_at_formatted = datetime.strptime(modified_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y")
        shared_at_formatted = datetime.strptime(shared_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y - %H:%M")

        print("\nHistórico do Projeto\n")
        print(f"Criado:         {created_at_formatted}")
        print(f"Modificado:     {modified_at_formatted}")
        print(f"Compartilhado:  {shared_at_formatted}\n")
    else:
        print('url inválida!')

def clear_screen():
    # Verifica o sistema operacional e chama o comando de limpar tela apropriado
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        url = input('Digite a URL -> ')
        url = validate_url(url)
        make_request(url)

        resposta = input('Digite a letra (u) para inserir uma nova URL ou (Enter) para continuar e (s) para sair: ')
        
        if resposta.lower() == 's':
            clear_screen()
            print('bye')
            break
        elif resposta.lower() == 'u':
            clear_screen()

if __name__ == "__main__":
    main()
