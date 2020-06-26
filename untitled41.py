import time
'''
def zig_zag():
    print("********")

def zig_zag1():
    print(" ********")

def zig_zag2():
    print("  ********")

def zig_zag3():
    print("   ********")

def zig_zag4():
    print("    ********")

def zig_zag5():
    print("   ********")

def zig_zag6():
    print("  ********")

def zig_zag7():
    print(" ********")

    
while True:
    zig_zag()
    time.sleep(0.6)
    zig_zag1()
    time.sleep(0.6)
    zig_zag2()
    time.sleep(0.6)
    zig_zag3()
    time.sleep(0.6)
    zig_zag4()
    time.sleep(0.6)
    zig_zag5()
    time.sleep(0.6)
    zig_zag6()
    time.sleep(0.6)
    zig_zag7()
    time.sleep(0.6)
'''
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:
        # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
        # Change direction:
                indentIncreasing = False
        else:
        # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
        # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()