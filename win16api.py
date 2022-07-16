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

# external stuff
wingdefile = folder + "wingde.exports"
bc450rtlfile = folder + "bc450rtl.exports"

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
wingde = []
bc450rtl = []

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
