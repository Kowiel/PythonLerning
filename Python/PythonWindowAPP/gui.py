import sys
sys.path.insert(0,"C:\\Users\\Michal\\Documents\\GitHub\PythonLerning\\Python")
import Functions 
import PySimpleGUI as sg  

layout = [ [sg.Text("Type Your To-Do")],
          [sg.Input() , sg.Button("Add To-Do")]
          ]

window=sg.Window("The To-Do App",layout)

events , values = window.read()

print(f"Will Eventualy add {values[0]} as a To do")

window.close()



