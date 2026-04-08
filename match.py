#vamos a usar el metodo match para encontrar coincidencias en una variable

letra = "b"

match letra:
    case "a":
        print("empieza con vocal")
    case "e":
        print("Empieza con vocal")
    case "i":
        print("Empieza con vocal")
    case "o":
        print("Empieza con vocal")
    case "u":
        print("Empieza con vocal")
    case _:
        print("No empieza con vocal")