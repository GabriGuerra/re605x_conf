import tkinter as tk
from tkinter import ttk
import subprocess
from configuracoes import configurar_repetidor, detectar_navegador

def obter_redes_wifi():
    try:
        resultado = subprocess.check_output(["netsh", "wlan", "show", "networks"], encoding="utf-8")
        redes = []
        for linha in resultado.split("\n"):
            linha = linha.strip()
            if linha.startswith("SSID "):
                partes = linha.split(":", 1)
                if len(partes) == 2:
                    ssid = partes[1].strip()
                    if ssid and ssid not in redes:
                        redes.append(ssid)
        return redes
    except Exception as e:
        print("Erro ao obter redes Wi-Fi:", e)
        return []

def configurar_repetidor_interface():
    ssid = combo_redes.get()
    senha = entrada_senha.get()
    if ssid and senha:
        status_label.config(text=f"Iniciando configuração com SSID: {ssid}")
        janela.update()
        configurar_repetidor(ssid, senha)
        status_label.config(text="Configuração concluída.")
    else:
        status_label.config(text="Selecione uma rede e digite a senha.")

def atualizar_navegador_detectado():
    navegador = detectar_navegador()
    if navegador:
        label_navegador.config(text=f"Navegador detectado: {navegador.capitalize()}")
    else:
        label_navegador.config(text="Nenhum navegador compatível encontrado")

# Interface
janela = tk.Tk()
janela.title("🔧 Configurar RE605X")
janela.geometry("360x400")
janela.configure(bg="#0f172a")  # fundo escuro estilo tech

# Estilo moderno
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#0f172a", foreground="#94a3b8", font=("Segoe UI", 10))
style.configure("TButton", background="#1e293b", foreground="#38bdf8", font=("Segoe UI", 10, "bold"), padding=6)
style.map("TButton", background=[("active", "#0ea5e9")])
style.configure("TCombobox", fieldbackground="#1e293b", background="#1e293b", foreground="#e2e8f0", font=("Segoe UI", 10))

# Título
tk.Label(janela, text="Configuração de Repetidor", font=("Segoe UI", 14, "bold"), bg="#0f172a", fg="#38bdf8").pack(pady=10)

# Combo de redes
tk.Label(janela, text="Selecione a rede Wi-Fi:").pack(pady=5)
redes_disponiveis = obter_redes_wifi()
combo_redes = ttk.Combobox(janela, values=redes_disponiveis)
combo_redes.pack(pady=5)

# Campo de senha
tk.Label(janela, text="Senha da rede Wi-Fi:").pack(pady=5)
entrada_senha = tk.Entry(janela, show="*", font=("Segoe UI", 10), bg="#1e293b", fg="#e2e8f0", insertbackground="#e2e8f0")
entrada_senha.pack(pady=5)

# Navegador detectado
label_navegador = tk.Label(janela, text="Navegador detectado: ...", bg="#0f172a", fg="#94a3b8", font=("Segoe UI", 9))
label_navegador.pack(pady=5)

# Botão configurar
botao_configurar = ttk.Button(janela, text="Configurar", command=configurar_repetidor_interface)
botao_configurar.pack(pady=10)

# Status
status_label = tk.Label(janela, text="", bg="#0f172a", fg="#38bdf8", font=("Segoe UI", 10))
status_label.pack(pady=10)

atualizar_navegador_detectado()
janela.mainloop()