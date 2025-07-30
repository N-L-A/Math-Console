from decimal import Decimal as d
from decimal import getcontext as dec_settings
from fractions import Fraction as f
from os import system
from random import choice as pick
from random import choices as dist

pi = 3.14
e = 2.71

__REPL_history__ = ""
__REPL_load_history__ = ""

def hlp():
    print("""
        >>> Important Commands <<<
             +=== Syntax ===+
    - fa/b for a/b fractions
    - d0.0 for 0.0 decimals
             
            +=== Constants ===+
    - pi
    - e
    
            +=== Commands ===+
    - hlp() print the documentation for all non-builtin features 
    - clr() clear the console
    - stdc(prec: int) set decimal precission to prec (positive int above 0)
    - save_history() open a file explorer wizard and select where to save current console history 
    - save_history(path:str = None) save current console history on the specified file path
    - load_history() open a file explorer wizard and select a history log to load 
    - load_history(path:str = None) load logged history from the specified file path
    
           +=== Functions ===+
    - rand() returens a random decimal in range [0, 1)
    - rand(num: int) returns a random integer between 0 and num
    - rand(num: int, step=s) for s being a float, returns a random decimal between 0 and num with s steps.
    - rand(min: int/float, max: int/float, step=1) returns a random decimal in [min, max] for the specified steps
        * Note: use loop=x decleration in rand to return a list of x random decimals instead of one
        ** Note: if step=0, rand will return a continiouse decimal between specified parameters
    - is_ogre(text: str) scans a string for ogre traces. returns the level of ogreish fury as an int within [0, inf), or -1 if no ogre was detected.
""")

def clr():
    system("cls")

def load_history(path=None):
    global __REPL_load_history__

    if path:
        __REPL_load_history__ = path
        return

    import tkinter
    from tkinter import filedialog

    # init - making hidden tkinter root for the messages
    root = tkinter.Tk()
    root.title("Dialogs root")
    root.withdraw()
    root.lift()
    root.attributes('-topmost', 1)   # Keep it on top (temporarily)
    # init end
    
    __REPL_load_history__ = filedialog.askopenfilename(title="Open a history log", initialdir=None, filetypes=[('Math Console Files', '*.mcls'), ('Text Files', '*.txt'), ('Python Files', '*.py')])

    root.destroy()


def save_history(path=None):

    if path == None:
        import tkinter
        from tkinter import filedialog

        # init - making hidden tkinter root for the messages
        root = tkinter.Tk()
        root.title("Dialogs root")
        root.withdraw()
        root.lift()
        root.attributes('-topmost', 1)   # Keep it on top (temporarily)
        # init end
        
        path = filedialog.asksaveasfilename(title="Save your history log", initialdir=None, filetypes=[('Math Console Files', '*.mcls')])

        root.destroy()
    
    try:
        file = open(path+".mcls", "w")
        file.write(__REPL_history__)
        file.close()
    except Exception as exception:
        print("cannot save at", path, "["+str(exception)+"]")
     

def rand(min=None, max=None, step=1, loop=0):
    import random
    if min == None:
        return d(str(random.random()))
    
    if max == None:
        return rand(0, min, step)
    
    if min > max:
        tmp = min
        min = max
        max = tmp
        del tmp
    
    if loop > 0:
        res = []
        for i in range(loop):
            res.append(rand(min, max, step, 0))
        return res
    
    if step == 0:
        return d(str(random.uniform(min, max)))
    
    step = abs(step)

    return random.randint(int(min/step), int(max/step))*d(str(step))

def stdc(prec=28):
    global pi, e
    dec_settings().prec = prec
    pi = d("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278"[:min(prec+2, 1026)])
    e = d("2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354021234078498193343210681"[:min(prec+2, 1026)])

stdc() # reset global vars

def parse(text: str) -> str:
    import re

    # 1. fN/M  => f(N,M)
    text = re.sub(r'\bf(\d+)/(\d+)', r'f(\1,\2)', text)

    # Regular expression pattern to match the numbers
    pattern = r'([d])([+-]?\d*\.?\d+)(?=\s|$|\t|[^a-zA-Z0-9])'  # Match 'd' followed by an optional sign, number, and decimal
    
    # Replace matched patterns with the desired format
    return re.sub(pattern, r'\1("\2")', text)

def get_level(text:str) -> int:
    level = 0
    while text.startswith("\t"):
        level += 1
        text = text[1:]
    
    return level

def execution(code:str) -> str:
    level = get_level(code)
    return f"{r'   '*level}tmp = {parse(code.replace(r'    ', ''))}\n{r'   '*level}if tmp != None:\n\t{r'   '*level}print(tmp)"

def is_ogre(text: str) -> int:
    """Check if a string translates to Ogrish
    Retruns an int describing how angry the ogre is
    Returns -1 if no ogre was found"""
    result = -1
    text = text.removeprefix("tmp = ").removesuffix("\nif tmp != None:\n\tprint(tmp)")

    if text.replace("R", "").replace("A", "").replace("!", "") == "" and text.startswith("RAR"):
        result = max(0, text.count("R")-5 + text.count("!")**2)
    
    return result

if __name__ == "__main__":
    while True:

        if __REPL_load_history__ != "":
            inp = "None"
            try:
                hist = open(__REPL_load_history__, "r")
                inp = hist.read()
                hist.close()
                inp += "\n" # auto return
                # print(inp.replace("\n", "\n... "))

            except Exception as exception:
                print("cannot open path:", __REPL_load_history__)
            
            __REPL_load_history__ = ""
        
        else:
            inp = input(">>> ")
        
        lines = inp.split("\n")
        while lines[-1].endswith(":") or lines[-1].startswith("\t"):
            lines += input("... ").split("\n")
            
        __skip_history__ = len(lines) == 1 and (lines[0].startswith("load_history(") or lines[0].startswith("save_history(")) # do not save load or save history commands, unless they are a part of a block

        level = 0
        collecting_function = -1
        collected = ""
        for line in lines:
            if line.replace(" ", "").replace("\t", "") == "":
                None
            else:
                if collecting_function > -1 and collecting_function < get_level(line):
                    collected += "\n" + line
                
                else:
                    tmp = line.replace("\t", "")

                    if tmp.startswith("def "):
                        collecting_function = get_level(line)
                        collected += "\n" + line
                        
                    elif tmp.replace(" ", "").endswith(":") or tmp.startswith(("import", "from", "raise", "break", "pass", "continue", "print(")) or tmp.count("=") > tmp.count("==")*2:
                        collected += "\n" + line
                    
                    else:
                        collected += "\n" + execution(line)

        while len(collected) > 0 and collected[0] == "\n":
            collected = collected[1:] # remove first character if is \n

        # print(parse(collected))
        inp = "\n".join(lines) # used for history management so you can store blocks
        if is_ogre(collected) > 64:
            collected = "raise OverflowError('System is Overwhelmed by Ogreish Fury')"
            inp = collected
        elif is_ogre(collected) > 1:
            collected = "hlp()" # help the user in case of uncontrollable fury
            inp = collected
        

        try:
            exec(parse(collected))

            if not __skip_history__:
                __REPL_history__ += "\n" + inp
        except Exception as exception:
            print("["+type(exception).__name__+"]", exception)
