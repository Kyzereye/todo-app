import functions
import FreeSimpleGUI as FSG

label = FSG.Text('Type in a todo')
input_box = FSG.InputText(tooltip = "  Enter Todo  ", key="todo")
add_button = FSG.Button("Add")
complete_button = FSG.Button('Complete')
edit_button = FSG.Button('Edit')
exit_button = FSG.Button('Exit')


window = FSG.Window('My ToDo App', 
                    layout=[[label], [input_box, add_button], [exit_button]], 
                    font=('Helvetica', 20))


while True:
  event, values = window.read()



  match event:
    case "Add":
      todos = functions.get_todos()
      new_todo = values['todo']
      todos.append(new_todo)
      print(todos)
      functions.write_todos(todos)
      
    case "Edit":
      print('gpt edit')
    
    case "Exit":
      break
    
    case FSG.WIN_CLOSED:
      break
      
window.close()




