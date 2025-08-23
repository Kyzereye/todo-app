import functions
import FreeSimpleGUI as FSG
import time

FSG.theme('DarkTanBlue')
clock = FSG.Text('', key = 'clock')
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
                    layout=[[clock],
                            [label], 
                            [input_box, add_button], 
                            [list_box, edit_button, completed_button], 
                            [exit_button]], 
                    font=('Helvetica', 20))


while True:

  event, values = window.read(timeout = 500)
  window['clock'].update(value=time.strftime("%b %d, %Y %H:%M %S"))

  match event:
    case "Add":
      todos = functions.get_todos()
      new_todo = values['todo']
      todos.append(new_todo)
      functions.write_todos(todos)
      window['todos'].update(values=todos)

      
    case "Edit":
      try:
        todo_to_edit = values['todos'][0]
        edited_todo = values['todo']
        todos = functions.get_todos()
        index_to_edit = todos.index(todo_to_edit)
        todos[index_to_edit] = edited_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)
      except IndexError:
        FSG.popup("Please select an item to edit")

    case "Completed":
      try: 
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
      except IndexError:
        FSG.popup("Please select an item to delete")

    case 'todos':
      window['todo'].update(value=values['todos'][0])

    
    case "Exit":
      break
    
    case FSG.WIN_CLOSED:
      break
      
window.close()




