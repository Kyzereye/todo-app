# from todo_functions import *
import functions as tf


while True:
  main_text = "Type add, show, edit, done, or exit:"

  todos = tf.get_todos()
  user_action = input(main_text)
  user_action = user_action.strip()

  if user_action.startswith('add'):
    todos.append(user_action[4:])
    tf.write_todos(todos)

  elif user_action.startswith('show'):
    for index, item in enumerate(todos):
      row = f"{index +1}: {item}"

  elif user_action.startswith('edit'):
    try:
      number = int(user_action[5:])
      number -= 1
      exiting_todo = todos[number]
      new_todo = input('Enter change to todo: ')

      # todos[number] = new_todo
      todos.__setitem__(number, new_todo)
      tf.write_todos(todos)

    except(ValueError):
      print("Your command is not valid.")
      print("Type edit with the number of the todo to edit")
  
  elif user_action.startswith('done'):
    try:
      number = int(user_action[5:])
      if number > 0:
        todos.pop(number - 1)
        tf.write_todos(todos)
      else:
        print("Number must be positive")

    except IndexError:
      print("number was too high")


  elif user_action.startswith('exit'):
    tf.write_todos(todos)
    break

  else:
    print("not the rigth option")



