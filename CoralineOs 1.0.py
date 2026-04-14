import random
from rich import print
import datetime
from datetime import datetime
import time

title = r'''
_________                     .__  .__              ________          
\_   ___ \  ________________  |  | |__| ____   ____ \_____  \   ______
/    \  \/ /  _ \_  __ \__  \ |  | |  |/    \_/ __ \ /   |   \ /  ___/
\     \___(  <_> )  | \// __ \|  |_|  |   |  \  ___//    |    \\___ \ 
 \______  /\____/|__|  (____  /____/__|___|  /\___  >_______  /____  >
        \/                  \/             \/     \/        \/     \/   1.0                                                     
        '''
while True:
    now = datetime.now()

    date = now.strftime("%D    %H : %M")
    print(date, end="\r")
    time.sleep(1)
    print(f"[red]{title}[/red]")
    greetings = ["Welcome to CoralineOs! Choose an option: ", "Greetings to CoralineOs! Choose an option: "]
    greeting = random.choice(greetings)
    print(f"[red]{greeting}[/red]")
    print("[red]╔═════════════════════════╗[/red]")
    print("[red]║1: Calculator, 2: Dices  ║[/red]")
    print("[red]╚═════════════════════════╝[/red]")
    options = float(input("Options: "))
    if options == 1:
        then = print('''[red]░░  █▀▀ █▀█ █   █▀▀ █ █ █   █▀█ ▀█▀ █▀█ █▀█
░░  █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█  █  █▄█ █▀▄[/red]''')
        x = float(input("> Insert a number: "));
        y = float(input("> Insert another number: "));
        m = f'''[red] ╔══════════════ RESULTS: ══════════════╗
> Addizzione: {x + y}
> Sottrazione: {x - y}
> Moltiplicazione: {x * y}
> Divisione: {x / y}
> Potenza: {x ** y}[/red]
'''
        print(m)
    elif options == 2:
        L = r'''
 _____     __     ______     ______     ______    
/\  __-.  /\ \   /\  ___\   /\  ___\   /\  ___\   
\ \ \/\ \ \ \ \  \ \ \____  \ \  __\   \ \___  \  
 \ \____-  \ \_\  \ \_____\  \ \_____\  \/\_____\ 
  \/____/   \/_/   \/_____/   \/_____/   \/_____/ 
                                                  
'''
        print(f"[red]{L}[/red]")
        numbers = [1, 2, 3, 4, 5, 6]
        dice = random.choice(numbers)
        print("[red]Your number is...[/red]");
        print(f"[red]{dice}[/red]")
        
    else:
        print("Invalid option, try again.");
    print("\n")   
    input("Press Enter to go back to the menu")
    print("\033c", end="")
