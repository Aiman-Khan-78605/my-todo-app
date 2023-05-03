import streamlit as st
import todos_functions

todos=todos_functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo.title()+'\n')
    todos_functions.write_todos(todos)



st.title("My TODO App")
st.subheader("This is my todo App")
st.write("This app is use to increase productivity..")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        todos_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add a new todo..",on_change=add_todo,key='new_todo')