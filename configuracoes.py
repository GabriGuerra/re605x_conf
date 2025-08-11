from automacao import configurar_re605x_com_selenium, detectar_navegador

def configurar_repetidor(ssid, senha):
    print(f"Iniciando configuração com SSID: {ssid}")
    configurar_re605x_com_selenium(ssid, senha)