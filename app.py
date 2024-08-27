import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
import string
import pyperclip


def generate_password():
    tamanho_senha = int(length_entry.get())
    letras_maiusculas = uppercase_var.get()
    letras_minusculas = lowercase_var.get()
    numeros = numbers_var.get()
    simbolos = symbols_var.get()
    usage = usage_entry.get()

    caracteres = ""
    if letras_maiusculas:
        caracteres += string.ascii_uppercase
    if letras_minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if caracteres:
        senha = "".join(random.choice(caracteres) for _ in range(tamanho_senha))
        password_output.config(state="normal")
        password_output.delete(0, tk.END)
        password_output.insert(0, senha)
        password_output.config(state="readonly")
    else:
        messagebox.showwarning(
            "Seleção Inválida", "Selecione pelo menos um tipo de caractere."
        )


def copy_to_clipboard():
    pyperclip.copy(password_output.get())
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")


def save_to_file():
    password = password_output.get()
    usage = usage_entry.get()
    if password and usage:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            with open(file_path, "a") as file:  # "a" para acrescentar ao arquivo
                file.write(f"{usage}: {password}\n")
            messagebox.showinfo("Salvo", f"Senha salva em {file_path}")
    else:
        messagebox.showwarning(
            "Erro", "Nenhuma senha gerada para salvar ou campo de uso está vazio."
        )


def clear_fields():
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")
    password_output.config(state="normal")
    password_output.delete(0, tk.END)
    password_output.config(state="readonly")
    usage_entry.delete(0, tk.END)
    uppercase_var.set(True)
    lowercase_var.set(True)
    numbers_var.set(True)
    symbols_var.set(True)


# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas Seguras")

root.iconphoto(False, tk.PhotoImage(file="icone.png"))

# Frame para o comprimento da senha
frame_length = tk.Frame(root)
frame_length.pack(pady=5)
tk.Label(frame_length, text="Quantos caracteres a sua SENHA deve ter? ").pack(
    side=tk.LEFT
)
length_entry = tk.Entry(frame_length, width=5)
length_entry.pack(side=tk.LEFT)
length_entry.insert(0, "10")

# Frame para as opções de caracteres
frame_options = tk.Frame(root)
frame_options.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame_options, text="Letras Maiúsculas", variable=uppercase_var).pack(
    anchor=tk.W
)
tk.Checkbutton(frame_options, text="Letras Minúsculas", variable=lowercase_var).pack(
    anchor=tk.W
)
tk.Checkbutton(frame_options, text="Números", variable=numbers_var).pack(anchor=tk.W)
tk.Checkbutton(frame_options, text="Símbolos", variable=symbols_var).pack(anchor=tk.W)

# Frame para campo de uso da senha
frame_usage = tk.Frame(root)
frame_usage.pack(pady=5)
tk.Label(frame_usage, text="Local de uso da senha (ex: Gmail):").pack(side=tk.LEFT)
usage_entry = tk.Entry(frame_usage, width=30)
usage_entry.pack(side=tk.LEFT)

button_font = ("Helvetica", 12, "bold")

# Botão para gerar a senha
generate_button = tk.Button(
    root,
    text="Gerar Senha",
    command=generate_password,
    bg="black",
    fg="white",
    font=button_font,
)
generate_button.pack(pady=10)

# Campo de saída para a senha gerada
password_output = tk.Entry(root, width=50, state="readonly")
password_output.pack(pady=5)

# Frame para botões de copiar, salvar e limpar
frame_actions = tk.Frame(root)
frame_actions.pack(pady=5)

copy_button = tk.Button(
    frame_actions,
    text="Copiar Senha",
    command=copy_to_clipboard,
    bg="green",
    fg="white",
    font=button_font,
)
copy_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(
    frame_actions,
    text="Salvar Senha",
    command=save_to_file,
    bg="orange",
    fg="black",
    font=button_font,
)
save_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(
    frame_actions,
    text="Limpar",
    command=clear_fields,
    bg="red",
    fg="white",
    font=button_font,
)
clear_button.pack(side=tk.LEFT, padx=5)

# Inicia a aplicaçãoT
root.mainloop()
