from optparse import Values
import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Login', layout=layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senhac = '123'
        usuarioc = 'marcos'
        usuario = value['usuario']
        senha = value['senha']
        if senha == senhac and usuario == usuarioc:
            window['mensagem'].update('login feito com sucesso')
        else:
            window['mensagem'].update('senha ou usuario incorreto')
