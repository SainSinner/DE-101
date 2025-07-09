def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #используем read() для чтения содержимого файла
        print(text)

def main():
    open_input("text.txt")

if __name__=="__main__":
    main()