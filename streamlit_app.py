import functions
import streamlit as st


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos = functions.get_todos()
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()
st.text_input(
    label="Add a new task",
    label_visibility="collapsed",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)
