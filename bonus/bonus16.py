import PySimpleGUI as sg

label1 = sg.Text("Select Files to Compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Select File")

label2 = sg.Text("Select Destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Select Folder")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2]])

window.read()
window.close()