from ghidra.program.model.symbol.SourceType import *
import string

folder = "C:\\temp\\ghidra_exports\\"

fm = currentProgram.getFunctionManager()

# Windows 1.x to 3.x stuff
gdifile = folder + "gdi.exports"
userfile = folder + "user.exports"
kernelfile = folder + "kernel.exports"
shellfile = folder + "shell.exports"
commdlgfile = folder + "commdlg.exports"
win87emfile = folder + "win87em.exports"
commfile = folder + "comm.exports"
displayfile = folder + "display.exports"
mousefile = folder + "mouse.exports"
mmsystemfile = folder + "mmsystem.exports"
soundfile = folder + "sound.exports"
mousefile = folder + "mouse.exports"
keyboardfile = folder + "keyboard.exports"
toolhelpfile = folder + "toolhelp.exports"
verfile = folder + "ver.exports"

# external stuff
wingdefile = folder + "wingde.exports"
bc450rtlfile = folder + "bc450rtl.exports"
msvideofile = folder + "msvideo.exports"
avifilefile = folder + "avifile.exports"

class Func:
    def __init__(self, ordinal, name):
        self.ordinal = ordinal
        self.name = name.strip()

gdi = []
user = []
kernel = []
shell = []
commdlg = []
win87em = []
comm = []
display = []
mouse = []
mmsystem = []
sound = []
mouse = []
keyboard = []
toolhelp = []
ver = []
wingde = []
bc450rtl = []
msvideo = []
avifile = []

for lines in file(gdifile):
    line = lines.split(",")
    ordinal = int(line[0])
    gdi.append(Func(ordinal, line[1]))

for lines in file(userfile):
    line = lines.split(",")
    ordinal = int(line[0])
    user.append(Func(ordinal, line[1]))

for lines in file(kernelfile):
    line = lines.split(",")
    ordinal = int(line[0])
    kernel.append(Func(ordinal, line[1]))

for lines in file(shellfile):
    line = lines.split(",")
    ordinal = int(line[0])
    shell.append(Func(ordinal, line[1]))

for lines in file(commdlgfile):
    line = lines.split(",")
    ordinal = int(line[0])
    commdlg.append(Func(ordinal, line[1]))

for lines in file(mmsystemfile):
    line = lines.split(",")
    ordinal = int(line[0])
    mmsystem.append(Func(ordinal, line[1]))

for lines in file(toolhelpfile):
    line = lines.split(",")
    ordinal = int(line[0])
    toolhelp.append(Func(ordinal, line[1]))

for lines in file(win87emfile):
    line = lines.split(",")
    ordinal = int(line[0])
    win87em.append(Func(ordinal, line[1]))

for lines in file(verfile):
    line = lines.split(",")
    ordinal = int(line[0])
    ver.append(Func(ordinal, line[1]))

for lines in file(msvideofile):
    line = lines.split(",")
    ordinal = int(line[0])
    msvideo.append(Func(ordinal, line[1]))

for lines in file(avifilefile):
    line = lines.split(",")
    ordinal = int(line[0])
    avifile.append(Func(ordinal, line[1]))

for lines in file(keyboardfile):
    line = lines.split(",")
    ordinal = int(line[0])
    keyboard.append(Func(ordinal, line[1]))

ext_fm = fm.getExternalFunctions()
while ext_fm.hasNext():
    ext_func = ext_fm.next()
    ext_func_name = ext_func.toString()
    
    if "GDI::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in gdi:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "USER::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in user:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "KERNEL::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in kernel:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "SHELL::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in shell:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "COMMDLG::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in commdlg:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "MMSYSTEM::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in mmsystem:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "TOOLHELP::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in toolhelp:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "WIN87EM::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in win87em:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "VER::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in ver:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "MSVIDEO::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in msvideo:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "AVIFILE::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in avifile:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break
    
    if "KEYBOARD::" in ext_func_name:
        o = ext_func_name.split("_")
        for x in keyboard:
            if x.ordinal == int(o[1]):
                name = str(x.name)
                ext_func.setName(name,ghidra.program.model.symbol.SourceType.IMPORTED)
                break