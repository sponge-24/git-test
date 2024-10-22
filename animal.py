import sys

def default():
    print("hello")

def cat():
    print("Mewo")

def dog():
    print("lol")

def main():
    if sys.argv[1] == "cat":
        cat()
    elif sys.argv[1] == "dog":
        dog()
    else:
        default()

if __name__ == "__main__":
    main()