from tkinter import *
import tkinter.filedialog
import sys
import json
import tiledraw
import tilecompositor
import screendesigner
import tilepacker

# All project data stored here
PROJECT = None

def createEmptyProject():
    return {
        "tiles": {},
        "metaTiles": {},
        "nameTable": {}
    }

def validTile(tile):
    if not isinstance(tile, str):
        return False
    if len(tile) != 32:
        return False
    for c in tile:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']:
            return False
    return True

def validMetaTile(metatile):
    return True

def validNameTable(nametable):
    return True

def validProject(project):
    for key in project:
        if key == "tiles":
            for tileID in project[key]:
                if not (isinstance(tileID, str) and validTile(project[key][tileID])):
                    return False
        elif key == "metaTiles":
            for metaTileID in project[key]:
                if not (isinstance(metaTileID, str) and validMetaTile(project[key][metaTileID])):
                    return False
        elif key == "nameTable":
            if not (project[key] and validNameTable(project[key])):
                return False
        else:
            return False
    return True    

def loadProject(filename):
    global PROJECT
    if filename:
        with open(filename, 'r') as f:
            project = json.loads(f.read())
            if not validProject(project):
                raise ValueError("Invalid project file")
            else:
                PROJECT = project
    else:
        PROJECT = createEmptyProject()

def saveProject(filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(PROJECT))

def launchProjectLoad():
    loadProject(tkinter.filedialog.askopenfilename())

def launchProjectSaveAs():
    saveProject(tkinter.filedialog.asksaveasfilename())

def launchNAT(filename=None):
    loadProject(filename)
    root = Tk()
    root.title("NES Art Tool")
    Button(root, text="Load", command=launchProjectLoad).grid(column=0, row=0)
    Button(root, text="Save As", command=launchProjectSaveAs).grid(column=1, row=0)
    Button(root, text="Tile Draw", command=tiledraw.launchTileDraw).grid(column=0, row=1)
    Button(root, text="Tile Compositor", command=tilecompositor.launchTileCompositor).grid(column=1, row=1)
    Button(root, text="Screen Designer", command=screendesigner.launchScreenDesigner).grid(column=2, row=1)
    Button(root, text="Tile Packer", command=tilepacker.launchTilePacker).grid(column=3, row=1)
    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for fname in sys.argv[1:]:
            launchNAT(fname)
    else:
        launchNAT()