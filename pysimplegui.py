import os
import PySimpleGUI as sg

def get_file_path():
    layout = [[sg.Text('Select a file')],
              [sg.Input(), sg.FileBrowse()],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('File Selector').Layout(layout)
    event, values = window.Read()
    window.Close()

    if event == 'OK':
        return values[0]
    else:
        return None

file_path = get_file_path()

if file_path:
    print(f'Selected file: {file_path}')
else:
    print('No file selected')
