import sys

def check(blocks, token) -> bool:
    result = []
    
    # Aqui debes escribir el codigo de la solucion
    
    return result
    
def main():
    # Enviamos datos desordenados para testear el resultado
    result = check(["f319", "3720", "4e3e", "46ec", "c7df", "c1c7", "80fd", "c4ea"], "b93ac073-eae4-405d-b4ef-bb82e0036a1d");
    
    # Esperamos que el resultado sea como este array
    expected = ["f319", "46ec", "c1c7", "3720", "c7df", "c4ea", "4e3e", "80fd"];

    if result == expected:
        print("`Lo resolviste correctamente!")
    else:
        print("`Todavia puedes intentarlo!")


main()
