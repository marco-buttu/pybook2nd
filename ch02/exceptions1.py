planets = {
    'Mercurio': 4879, 
    'Venere': 12104,
    'Terra': 12756,
    'Marte': 6787, 
    'Giove': 142984,
    'Saturno': 120536,
    'Urano': 51118,
    'Nettuno': 49528,
}

while True:
    name = input('Inserisci il nome di un pianeta: ')
    print('Diametro in km:', planets[name])
