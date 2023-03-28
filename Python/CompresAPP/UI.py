import PySimpleGUI as sg  

layout = [ [sg.Text("Select The Text to compres", size=(20,1)), sg.Input(size=(20,1)) , sg.Button("Choose")],
           [sg.Text("Select Destination Path" ,size=(20,1)), sg.Input(size=(20,1)) , sg.Button("Choose")],
           [sg.Button("Compres")]
          ]

window=sg.Window("THE Compresion App",layout)

window.read()

window.close()


