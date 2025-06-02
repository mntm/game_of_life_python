"""
Initial state
----------
----------
----------
-----1----
------1---
----111---
----------
----------
----------
---------- 
À chaque itération, l'état d’une cellule est entièrement déterminé par l’état de ses huit cellules voisines, selon les règles suivantes :

Une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît) ;
Une cellule vivante ne possédant pas exactement deux ou trois cellules voisines vivantes meurt.

tableau 10 elt [0 1 2 3 4 5 6 7 8 9]
for (int index = 0; index < 10; index++) {}

for valeur in tableau

for index in range(10)
"""

matrix_cell = [
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

def print_matrix () :
    for row in matrix_cell:
        text = ""
        for cell in row:
            text += "A" if cell == 1 else "."
        print(text)

print_matrix();

