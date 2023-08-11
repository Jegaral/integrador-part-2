def main():
    print("Presiona la tecla ↑ para salir.")
    
    while True:
        key = input()
        
        if key == "↑":
            print("Saliendo del bucle...")
            break
        else:
            print("Tecla presionada:", key)

if __name__ == "__main__":
    main()
