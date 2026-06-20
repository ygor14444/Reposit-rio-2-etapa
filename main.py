import os
import time
import requests
from supabase import create_client, Client

SUPABASE_URL = ""
SUPABASE_KEY = ""
ZAPI_INSTANCE_ID = "" 
ZAPI_TOKEN = ""
ZAPI_CLIENT_TOKEN = ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

if not all([SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE_ID, ZAPI_TOKEN]):
    print("[ERRO] Erro crítico: Variáveis de ambiente faltando no arquivo .env!")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"


def buscar_contatos_supabase():
    """Busca os contatos cadastrados na tabela 'contatos' do Supabase."""
    print("[INFO] Buscando contatos no Supabase...")
    try:
        response = supabase.table("contatos").select("nome, telefone").limit(3).execute()
        return response.data
    except Exception as e:
        print(f"[ERRO] Falha ao conectar ou buscar dados no Supabase: {e}")
        return []


def enviar_mensagem_zapi(nome, telefone):
    """Envia a mensagem exata exigida pelo desafio via Z-API."""
    mensagem_exata = f"Olá, {nome} tudo bem com você?"
    
    payload = {
        "phone": telefone,
        "message": mensagem_exata
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    if ZAPI_CLIENT_TOKEN:
        headers["Client-Token"] = ZAPI_CLIENT_TOKEN

    try:
        print(f"[INFO] Enviando mensagem para {nome} ({telefone})...")
        response = requests.post(ZAPI_URL, json=payload, headers=headers, timeout=10)
        
        if response.status_code in [200, 201]:
            print(f"[SUCESSO] Mensagem enviada para {nome}!")
            return True
        else:
            print(f"[AVISO] Z-API retornou status {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Erro na requisição HTTP da Z-API para {nome}: {e}")
        return False


def main():
    print("--- INICIANDO FLUXO B2BFLOW ---")
    
    contatos = buscar_contatos_supabase()
    
    if not contatos:
        print("[AVISO] Nenhum contato encontrado ou erro na busca. Encerrando.")
        return

    print(f"[INFO] Encontrado(s) {len(contatos)} contato(s).")

    for index, contato in enumerate(contatos):
        nome = contato.get("nome")
        telefone = contato.get("telefone")
        
        if nome and telefone:
            enviar_mensagem_zapi(nome, telefone)
            
            if index < len(contatos) - 1:
                print("[INFO] Aguardando 3 segundos para o próximo envio...")
                time.sleep(3)
        else:
            print(f"[AVISO] Contato com dados incompletos encontrado: {contato}")

    print("--- FLUXO FINALIZADO ---")


if __name__ == "__main__":
    main()