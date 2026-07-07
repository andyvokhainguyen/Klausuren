import sys
import getopt

def hilfe():
    print("Verwendung:")
    print("Summe: python myscript.py --add -x <zahl> -y <zahl>")
    print("Produkt: python myscript.py --multiply -x <zahl> -y <zahl>")
    print("Hilfe: python myscript.py -h")

def main(argv):
    operation = ""
    x = None
    y = None

    try:
        opts, args = getopt.getopt(
            argv, "hamx:y:",
            ["help", "add", "multiply", "zahlx=", "zahly="]
        )
    except getopt.GetoptError:
        print("Fehler: Ungültige Option oder ungültiges Argument.")
        hilfe()
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            hilfe()
            sys.exit()
        elif opt in ("-a", "--add"):
            operation = "add"
        elif opt in ("-m", "--multiply"):
            operation = "multiply"
        elif opt in ("-x", "--zahlx"):
            x = int(arg)
        elif opt in ("-y", "--zahly"):
            y = int(arg)

    if operation == "" or x is None or y is None:
        print("Fehler: Operation (--add/--multiply) sowie -x und -y sind erforderlich.")
        hilfe()
        sys.exit(2)

    if operation == "add":
        print(x + y)
    elif operation == "multiply":
        print(x * y)

if __name__ == "__main__":
    main(sys.argv[1:])





import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Addiert oder multipliziert zwei Zahlen."
    )

    parser.add_argument(
        "-a", "--add",
        action="store_true",
        help="Addiert zwei Zahlen"
    )

    parser.add_argument(
        "-m", "--multiply",
        action="store_true",
        help="Multipliziert zwei Zahlen"
    )

    parser.add_argument(
        "-x",
        type=int,
        required=True,
        help="Erste Zahl"
    )

    parser.add_argument(
        "-y",
        type=int,
        required=True,
        help="Zweite Zahl"
    )

    args = parser.parse_args()

    if args.add:
        print(args.x + args.y)
    elif args.multiply:
        print(args.x * args.y)
    else:
        print("Fehler: Bitte --add oder --multiply angeben.")

if __name__ == "__main__":
    main()
