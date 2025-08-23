import functions
import FreeSimpleGUI as FSG

label = FSG.Text('Type in a todo')
input_box = FSG.InputText(tooltip = "  Enter Todo  ", key="todo")
add_button = FSG.Button("Add")
complete_button = FSG.Button('Complete')
edit_button = FSG.Button('Edit')
exit_button = FSG.Button('Exit')
completed_button = FSG.Button('Completed')
list_box = FSG.Listbox(values=functions.get_todos(), key='todos', 
                       enable_events=True, size=[45,10])


window = FSG.Window('My ToDo App', 
                    layout=[[label], 
                            [input_box, add_button], 
                            [list_box, edit_button, completed_button], 
                            [exit_button]], 
                    font=('Helvetica', 20))


while True:
  event, values = window.read()
  # print(1, event)
  # print(2, values)
  # print(3, values['todos'])
  # print('====')

  match event:
    case "Add":
      todos = functions.get_todos()
      new_todo = values['todo']
      todos.append(new_todo)
      print(todos)
      functions.write_todos(todos)
      window['todos'].update(values=todos)

      
    case "Edit":
      todo_to_edit = values['todos'][0]
      edited_todo = values['todo']
      todos = functions.get_todos()
      index_to_edit = todos.index(todo_to_edit)
      todos[index_to_edit] = edited_todo
      functions.write_todos(todos)
      window['todos'].update(values=todos)

    case "Completed":
      todo_to_complete = values['todos'][0]
      todos = functions.get_todos()
      todos.remove(todo_to_complete)
      functions.write_todos(todos)
      window['todos'].update(values=todos)

    case 'todos':
      window['todo'].update(value=values['todos'][0])

    
    case "Exit":
      break
    
    case FSG.WIN_CLOSED:
      break
      
window.close()




