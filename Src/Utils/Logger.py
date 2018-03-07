__author__ = 'losos'

errPre = "[ ERROR ] "
infPre = "[ INFO  ] "
dbgPre = "[ DEBUG ] "

enabled = True
dbgM = True

def turnOn():
    global enabled
    enabled = True

def turnOff():
    global enabled
    enabled = False

def dbgMode(on = True):
    global dbgM
    dbgM = on

def internalPrinter(msg):
    if enabled:
        print(msg)

def raw(msg):
    print(msg,)

def rawNl(msg):
    internalPrinter(msg)

def err(msg):
    internalPrinter(errPre + msg)

def inf(msg):
    internalPrinter(infPre + msg)

def dbg(msg):
    global dbgM
    if dbgM:
        internalPrinter(dbgPre + msg)