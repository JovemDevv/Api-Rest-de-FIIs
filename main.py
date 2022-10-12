import PySimpleGUI as sg
from cotacao import pegar_cotacoes

sg.theme('Reds')

layout = [
    [sg.Text("Moeda", font = 'arial 12 bold')],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button('Cotação', font = 'arial 10 bold'), sg.Button("Cancelar", font = 'arial 10 bold')],
    [sg.Text("", key='texto_cotacao'), sg.Text("Desenvolvido por Ana Caroline Vasconcellos", font="arial 8")],
    
]

janela = sg.Window("Sistema de Cotações",  layout)

#requisição
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Cotação":
        codigo_cotacao = valores["nome_cotacao"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela["texto_cotacao"].update(f"A cotação do {codigo_cotacao} é de R${cotacao}")

janela.close()