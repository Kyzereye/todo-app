import functions
import FreeSimpleGUI as FSG

label = FSG.Text('Type in a todo')
input_box = FSG.InputText(tooltip = "  Enter Todo  ")
add_button = FSG.Button("Add")
complete_button = FSG.Button('Complete')
edit_button = FSG.Button('Edit')


window = FSG.Window('My ToDo App', layout=[[label], [input_box, add_button], ])
window.read()
window.close()




