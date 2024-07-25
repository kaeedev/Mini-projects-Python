#--- Pedimos datos por pantalla
burger = input('Elige que tipo de hamburguesa quieres, clasica o vegana: ')

#--- Hacemos las condicionales
if burger.lower() == 'clasica':  #Condicional del primer tipo de burger con sus ingredientes
    ingredientesClasica= input('Los ingredientes extra son: -Queso Idiazabal -Bacon -Huevo. Elija SOLAMENTE UNO de ellos: ')
    if ingredientesClasica.lower() == 'queso idiazabal':
        print('Has elegido la hamburguesa clasica con el ingrediente extra:', ingredientesClasica.title())
    elif ingredientesClasica.lower() == 'bacon':
        print('Has elegido la hamburguesa clasica con el ingrediente extra:', ingredientesClasica.title())
    elif ingredientesClasica.lower()== 'huevo':
        print('Has elegido la hamburguesa clasica con el ingrediente extra:', ingredientesClasica.title())
    else: #Mensaje de error si no introduce un ingrediente extra valido
        print('No se va a añadir ningun ingrediente extra a tu hamburguesa clasica')
elif burger.lower() == 'vegana': #Segunda condicional con el otro tipo de burger y sus ingredientes
    ingredientesVegana= input('Los ingredientes extra son: -Tofu -Cebolla caramelizada. Elija SOLAMENTE UNO de ellos: ')
    if ingredientesVegana.lower() == 'tofu':
        print('Has elegido la hamburguesa vegana con el ingrediente extra:', ingredientesVegana.title())
    elif ingredientesVegana.lower() == 'cebolla caramelizada':
        print('Has elegido la hamburguesa vegana con el ingrediente extra:', ingredientesVegana.title())
    else: #Mensaje de error si no introduce un ingrediente extra valido
        print('No se va a añadir ningun ingrediente extra a tu hamburguesa vegana')
else: #Mensaje de error por si no introduce algun tipo de burger
    print('Introduzca un tipo de hamburguesa valida la proxima vez, por favor')
    