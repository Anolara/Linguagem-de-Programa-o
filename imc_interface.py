import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        altura = float(entry_altura.get())
        peso = float(entry_peso.get())
        altura_m = altura / 100

        imc = peso / (altura_m ** 2)

        if imc < 17:
            status = "Muito abaixo do peso"
        elif imc < 25:
            status = "Peso normal"
        elif imc < 30:
            status = "Acima do peso"
        else:
            status = "Obesidade"

        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END,
            f"Classificação: {status}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Preencha altura e peso com números válidos.")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_text.delete("1.0", tk.END)

def sair():
    janela.destroy()


#interface
janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")
janela.geometry("800x350")

tk.Label(janela, text="Nome do Paciente:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_nome = tk.Entry(janela, width=50)
entry_nome.grid(row=0, column=1, padx=10)

tk.Label(janela, text="Endereço Completo:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_endereco = tk.Entry(janela, width=50)
entry_endereco.grid(row=1, column=1, padx=10)

tk.Label(janela, text="Altura (cm)").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_altura = tk.Entry(janela, width=15)
entry_altura.grid(row=2, column=1, sticky="w")

tk.Label(janela, text="Peso (Kg)").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_peso = tk.Entry(janela, width=15)
entry_peso.grid(row=3, column=1, sticky="w")

resultado_text = tk.Text(janela, width=35, height=10, borderwidth=2, relief="groove")
resultado_text.grid(row=2, column=2, rowspan=3, padx=15)

btn_calcular = tk.Button(janela, text="Calcular", width=12, command=calcular_imc)
btn_calcular.grid(row=5, column=0, padx=10, pady=15)

btn_reiniciar = tk.Button(janela, text="Reiniciar", width=12, command=reiniciar)
btn_reiniciar.grid(row=5, column=1, padx=10)

btn_sair = tk.Button(janela, text="Sair", width=12, command=sair)
btn_sair.grid(row=5, column=2, padx=10)

janela.mainloop()
