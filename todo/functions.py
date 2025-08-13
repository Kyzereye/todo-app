import time
from datetime import datetime

FILEPATH = "todo.txt"

def get_todos(filename="todos.txt"):
  with open(filename, 'r') as file_local:
    todos_local = file_local.readlines()
  file_local.close()
  todos_local = [todo.replace('\n', '') for todo in todos_local]
  print(todos_local)
  return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    todos =[ todo + '\n' for todo in todos_arg]
    with open(filepath, 'w') as file:
      file.writelines(todos) 

now = datetime.now()
date_time = now.strftime("%H:%m%p %a %b %d, %Y")

nowtime = time.strftime("%H")
# print(nowtime)
# print(f"It is now {date_time}")


if __name__ == "__main__":
   print("hello me")      