from bruhanimate.bruhscreen import Screen
from bruhanimate.bruhffer import Buffer

def view(screen: Screen, file: str):
    back_buffer = Buffer(screen.width, screen.height)
    view_buffer = Buffer(screen.width, screen.height)
    with open(file, 'r') as f:
        lines = [line for line in f.readlines()]
        for i, line in enumerate(lines):
            back_buffer.put_at(0, i, line, False)
        
        changes = view_buffer.get_buffer_changes(back_buffer)
        for y, x, val in changes:
            screen.print_at(val, x, y, 1)
        input()
        screen.close()

        


def shell():
    while (file_to_open := input(">> Enter the path to the file you want to open:\n>> ")) != "q":
        print(file_to_open)
        Screen.show(view, args=(file_to_open,))

