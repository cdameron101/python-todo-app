import time
from pathlib import Path

import FreeSimpleGUI as sg

import functions


IMAGE_DIR = Path(__file__).resolve().parent
FONT = ("Helvetica", 20)

# Create an empty file on first launch without erasing existing tasks.
Path("todos.txt").touch(exist_ok=True)
todos = functions.get_todos()

sg.theme("DarkTeal1")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button(
    size=(2, 1),
    image_source=str(IMAGE_DIR / "add.png"),
    mouseover_colors="LightBlue2",
    tooltip="Add to-do",
    key="Add",
)
list_box = sg.Listbox(
    values=todos,
    key="todos",
    enable_events=True,
    size=(45, 10),
)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [
    [clock],
    [label, input_box],
    [add_button],
    [list_box, edit_button],
    [complete_button, exit_button],
]
window = sg.Window("My To Do App", layout, font=FONT)

try:
    while True:
        event, values = window.read(timeout=200)

        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        clock.update(time.strftime("%b %d, %Y %H:%M:%S"))

        if event == "todos":
            if values["todos"]:
                input_box.update(values["todos"][0].rstrip("\r\n"))
            continue

        if event not in ("Add", "Edit", "Complete"):
            continue

        if event in ("Edit", "Complete"):
            selected_rows = list_box.get_indexes()
            if not selected_rows:
                sg.popup("Please select an item first.", font=FONT)
                continue
            row = selected_rows[0]

        if event in ("Add", "Edit"):
            text = values["todo"].strip()
            if not text:
                sg.popup("Please enter a to-do.", font=FONT)
                continue

        if event == "Add":
            todos.append(text + "\n")
        elif event == "Edit":
            todos[row] = text + "\n"
        else:
            del todos[row]

        functions.write_todos(todos)
        list_box.update(values=todos)
        input_box.update("")
finally:
    window.close()