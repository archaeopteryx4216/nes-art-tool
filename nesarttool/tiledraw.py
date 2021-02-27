from tkinter import *

def launchOpenTile():
    pass

def saveTile():
    pass

def launchExportTile():
    pass

def deleteTile():
    pass

def launchColorPicker(num):
    pass

def setDrawColor(num):
    pass

def launchTileDraw():
    tileDraw = Tk()
    tileDraw.title("Tile Draw")

    topPanel = Frame(tileDraw)

    Button(topPanel, text="Open", command=launchOpenTile).grid(column=0, row=0)
    Button(topPanel, text="Save", command=saveTile).grid(column=1, row=0)
    Button(topPanel, text="Export", command=launchExportTile).grid(column=2, row=0)
    Button(topPanel, text="Delete", command=deleteTile).grid(column=3, row=0)

    topPanel.pack()

    bottomPanel = Frame(tileDraw)

    leftPanel = Frame(bottomPanel)

    Text(leftPanel, height=1, width=32).grid(column=0, row=0)
    Canvas(leftPanel, height=256, width=256, bg="#fff").grid(column=0, row=1)
    leftPanel.grid(column=0, row=0)

    rightPanel = Frame(bottomPanel)

    Canvas(rightPanel, height=25, width=25, bg="#fff").grid(column=0, row=0)
    Text(rightPanel, )
    Label(rightPanel, text="Selected Color").grid(column=2, row=0)

    Label(rightPanel, text="Select Color").grid(column=1, row=1)
    Label(rightPanel, text="Palette Chooser").grid(column=2, row=1)

    Canvas(rightPanel, height=25, width=25, bg="#fff").grid(column=0, row=2)
    Button(rightPanel, text="Transparency", width=12, command=lambda: setDrawColor(0)).grid(column=1, row=2)
    Button(rightPanel, text="...", command=lambda: launchColorPicker(0)).grid(column=2, row=2)

    Canvas(rightPanel, height=25, width=25, bg="#fff").grid(column=0, row=3)
    Button(rightPanel, text="Color 1", width=12, command=lambda: setDrawColor(1)).grid(column=1, row=3)
    Button(rightPanel, text="...", command=lambda: launchColorPicker(1)).grid(column=2, row=3)

    Canvas(rightPanel, height=25, width=25, bg="#fff").grid(column=0, row=4)
    Button(rightPanel, text="Color 2", width=12, command=lambda: setDrawColor(2)).grid(column=1, row=4)
    Button(rightPanel, text="...", command=lambda: launchColorPicker(2)).grid(column=2, row=4)

    Canvas(rightPanel, height=25, width=25, bg="#fff").grid(column=0, row=5)
    Button(rightPanel, text="Color 3", width=12, command=lambda: setDrawColor(3)).grid(column=1, row=5)
    Button(rightPanel, text="...", command=lambda: launchColorPicker(3)).grid(column=2, row=5)

    rightPanel.grid(column=1, row=0)

    bottomPanel.pack()

    tileDraw.mainloop()