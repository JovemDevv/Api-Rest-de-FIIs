import PySimpleGUI as sg

layout = [
    [sg.Text("Pegar cotação da bolsa")],
    [sg.InputText()],
    [sg.Button("Pegar cotação"), sg.Button("Cancelar")],
    [sg.text("")],
]