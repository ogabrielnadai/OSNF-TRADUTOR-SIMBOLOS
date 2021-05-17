import PySimpleGUI as sg

'''
By: Odontlus
'''
SIMBOLOS = []

SIMBOLOS_CHAR_SIMPLES = {
  "Z": "Z",
  "Y": "Y",
  "X": "X",
  "W": "W",
  "V": "V",
  "U": "U",
  "T": "T",
  "S": "S",
  "R": "R",
  "Q": "Q",
  "P": "P",
  "O": "O",
  "N": "N",
  "M": "M",
  "L": "L",
  "K": "K",
  "J": "J",
  "I": "I",
  "H": "H",
  "G": "G",
  "F": "F",
  "E": "E",
  "D": "D",
  "C": "C",
  "B": "B",
  "A": "A"
}

SIMBOLOS_CHAR_SIMPLES_INVERSO = {
  "Z": "Z",
  "Y": "Y",
  "X": "X",
  "W": "W",
  "V": "V",
  "U": "U",
  "T": "T",
  "S": "S",
  "R": "R",
  "Q": "Q",
  "P": "P",
  "O": "O",
  "N": "N",
  "M": "M",
  "L": "L",
  "K": "K",
  "J": "J",
  "I": "I",
  "H": "H",
  "G": "G",
  "F": "F",
  "E": "E",
  "D": "D",
  "C": "C",
  "B": "B",
  "A": "A"
}

for char in SIMBOLOS_CHAR_SIMPLES:
    SIMBOLOS.insert(0, sg.Button("" + char + "", key="" + char + "",  font=("AFonteParanormal", 31)))


def TraduzirSimbolosParaAlfabeto(input):
    traduzido = ""
    for char in input:
        if char in SIMBOLOS_CHAR_SIMPLES.keys():
            traduzido += (SIMBOLOS_CHAR_SIMPLES.get(char))
        elif char == "":
            traduzido += ""
        else:
            traduzido += ""
    return traduzido


def TraduzirAlfabetoParaSimbolos(input):
    traduzido = ""
    for char in input:
        if char in SIMBOLOS_CHAR_SIMPLES_INVERSO.keys():
            traduzido += (SIMBOLOS_CHAR_SIMPLES_INVERSO.get(char))
        elif char == "":
            traduzido += ""
        else:
            traduzido += ""
    return traduzido

buttons = [
    SIMBOLOS,
]

frame_resultados = [
    [sg.Text('Entrada Simbolos', size=(15, 0)), sg.InputText(size=(110, 5), font=("AFonteParanormal", 25), key='entrada_simbolos_para_alfabeto')],
    [sg.Text('Saida Alfabeto', size=(15, 0)), sg.InputText(size=(236, 5), key='saida_simbolos_para_alfabeto')],
    [sg.RealtimeButton('submit', key='enviar_simbolos_para_alfabeto')]
]
frame_resultados_inv = [
    [sg.Text('Entrada Alfabeto', size=(15, 0)), sg.InputText(size=(236, 5), key='entrada_alfabeto_para_simbolos')],
    [sg.Text('Saida Simbolos', size=(15, 0)), sg.InputText(size=(110, 5), font=("AFonteParanormal", 25), key='saida_alfabeto_para_simbolos')],
    [sg.RealtimeButton('submit', key='enviar_alfabeto_para_simbolos')]
]

layout = [
    [sg.Frame('SIMBOLOS', buttons, key='buttons')],
    [sg.Frame('Resultado - Simbolos para Alfabeto', frame_resultados)],
    [sg.Frame('Resultado - Alfabeto para Simbolos', frame_resultados_inv)],
    [sg.Quit(), ]
]

window = sg.Window("SIMBOLOS OSNF CONVERSOR 1.0 (BY:ODONTLUS FONT BY: rafa el @whypuzzles )", layout, return_keyboard_events=False,
                   use_default_focus=False)

while True:
    event, values = window.Read()

    if event in ('Quit', None):
        break

    elif event in ('enviar_simbolos_para_alfabeto', None):
        output = TraduzirSimbolosParaAlfabeto(values['entrada_simbolos_para_alfabeto'])
        window['saida_simbolos_para_alfabeto'].update(output)

    elif event in ('enviar_alfabeto_para_simbolos', None):
        output = TraduzirAlfabetoParaSimbolos(values['entrada_alfabeto_para_simbolos'].upper())
        window['saida_alfabeto_para_simbolos'].update(output)

    elif buttons:
            value = values['entrada_simbolos_para_alfabeto'] + event
            window['entrada_simbolos_para_alfabeto'].update(value)
