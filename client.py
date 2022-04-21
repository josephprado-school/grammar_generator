import gramgen

#BNF grammar syntax
separator = "::="
delimiter = "|"

quit = False

while True:
    try:
        file = input("What is the name of the grammar file (or enter to quit)? ")
        
        if file != "":
            grammar = gramgen.GrammarGenerator(file, separator, delimiter)
        else:
            quit = True
        break
        
    except FileNotFoundError:
        print("\nCannnot locate \"" + file + "\"! Please try again.\n")
        
while not quit:
    symbols = grammar.get_non_terminal_symbols()

    print("\nAvailable symbols to generate are: ")
    print("[" + ", ".join(symbols) + "]")
    
    symbol = input("\nWhat do you want to generate (or enter to quit)? ")
    
    if symbol == "":
        quit = True
    
    elif symbol in symbols:
        while True:
            try:
                n = (int)(input("How many do you want me to generate? "))
                
                print()
                for i in range(n):
                    print(grammar.get_random_phrase(symbol))
                break
            
            except ValueError:
                print("\nPlease enter an integer value!")   
    else:
        print("\n\"" + symbol + "\" is not a valid symbol! Please try again.")
