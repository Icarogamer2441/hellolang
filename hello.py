import sys

def interpret(code):
    lines = code.split("\n")
    hellonum = 0
    worldnum = 0

    for line in lines:
        tokens = line.split() or line.split("\t")

        for token in tokens:
            if token == "hello":
                hellonum += 1
            elif token == "world":
                worldnum += 1
        
        if hellonum == 1:
            if worldnum == 1:
                print("a", end="")
            elif worldnum == 2:
                print("b", end="")
        elif hellonum == 2:
            if worldnum == 2:
                print("c", end="")
            if worldnum == 3:
                print("d", end="")
            if worldnum == 4:
                print("e", end="")
        elif hellonum == 3:
            if worldnum == 1:
                print("f", end="")
            elif worldnum == 2:
                print("g", end="")
            elif worldnum == 3:
                print("h", end="")
            elif worldnum == 4:
                print("i", end="")
            elif worldnum == 5:
                print("j", end="")
        elif hellonum == 4:
            if worldnum == 1:
                print("k", end="")
            elif worldnum == 2:
                print("l", end="")
            elif worldnum == 3:
                print("m", end="")
            elif worldnum == 4:
                print("n", end="")
        elif hellonum == 5:
            if worldnum == 1:
                print("o", end="")
            elif worldnum == 2:
                print("p", end="")
            elif worldnum == 3:
                print("q", end="")
            elif worldnum == 4:
                print("r", end="")
            elif worldnum == 5:
                print("s", end="")
            elif worldnum == 6:
                print("t", end="")
            elif worldnum == 7:
                print("u", end="")
        elif hellonum == 6:
            if worldnum == 1:
                print("v", end="")
            elif worldnum == 2:
                print("w", end="")
            elif worldnum == 3:
                print("x", end="")
            elif worldnum == 4:
                print("y", end="")
            elif worldnum == 5:
                print("z", end="")
        elif hellonum == 7:
            if worldnum == 1:
                print("")
            elif worldnum == 2:
                print(" ", end="")
            elif worldnum == 3:
                print("?", end="")
            elif worldnum == 4:
                print("!", end="")
            elif worldnum == 5:
                print(".", end="")
            elif worldnum == 6:
                print(",", end="")
            elif worldnum == 7:
                print("'", end="")
            elif worldnum == 8:
                print(";", end="")
        elif hellonum == 8:
            if worldnum == 1:
                print(":", end="")
            elif worldnum == 2:
                print("%", end="")
            elif worldnum == 3:
                print("$", end="")
            elif worldnum == 4:
                print("*", end="")
            elif worldnum == 5:
                print("/", end="")
            elif worldnum == 6:
                print(">", end="")
            elif worldnum == 7:
                print("<", end="")
            elif worldnum == 8:
                print("+", end="")
            elif worldnum == 9:
                print("-", end="")
            elif worldnum == 10:
                print("(", end="")
            elif worldnum == 11:
                print(")", end="")
        elif hellonum == 9:
            if worldnum == 1:
                print("[", end="")
            elif worldnum == 2:
                print("]", end="")
            elif worldnum == 3:
                print("{", end="")
            elif worldnum == 4:
                print("}", end="")
            elif worldnum == 5:
                print("\"", end="")
            elif worldnum == 6:
                print("`", end="")
            elif worldnum == 7:
                print("´", end="")
            elif worldnum == 8:
                print("ç", end="")
            elif worldnum == 9:
                print("^", end="")
            elif worldnum == 10:
                print("~", end="")
            elif worldnum == 11:
                print("@", end="")
        hellonum = 0
        worldnum = 0

if __name__ == "__main__":
    version = "1.0"
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <command>")
        print("commands:")
        print("-v            show the current version of the language you're using")
        print("<file>        execute you file")
    else:
        command = sys.argv[1]

        if command == "-v":
            print("hello Esolang made by: josé icaro. made with: python")
            print(f"hellolang version: {version}")
        else:
            if command.endswith(".hello"):
                with open(command, "r") as f:
                    interpret(f.read())
            else:
                print("Use .hello file extension")
