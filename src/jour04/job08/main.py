# Ouvrir le fichier maze.mz
with open("maze.mz.txt", "r") as f:
    maze = f.readlines()

# Trouver la position de l'entrée et de la sortie du labyrinthe
for i in range(len(maze)):
    if maze[i][0] == ".":
        start_pos = (i, 0)
    if maze[i][-2] == ".":
        end_pos = (i, len(maze[i]) - 3)


# Fonction pour trouver les voisins d'une position donnée dans le labyrinthe
def neighbors(pos):
    row, col = pos
    result = []
    if row > 0 and maze[row - 1][col] == ".":
        result.append((row - 1, col))
    if row < len(maze) - 1 and maze[row + 1][col] == ".":
        result.append((row + 1, col))
    if col > 0 and maze[row][col - 1] == ".":
        result.append((row, col - 1))
    if col < len(maze[row]) - 3 and maze[row][col + 1] == ".":
        result.append((row, col + 1))
    return result


# Algorithme de recherche en largeur pour trouver le chemin le plus court
from queue import Queue

q = Queue()
q.put(start_pos)

visited = set()
visited.add(start_pos)

prev = {}

while not q.empty():
    curr_pos = q.get()
    if curr_pos == end_pos:
        break
    for next_pos in neighbors(curr_pos):
        if next_pos not in visited:
            q.put(next_pos)
            visited.add(next_pos)
            prev[next_pos] = curr_pos

# Construire le chemin le plus court
path = []
curr_pos = end_pos
while curr_pos != start_pos:
    path.append(curr_pos)
    curr_pos = prev[curr_pos]
path.append(start_pos)
path.reverse()

# Afficher le labyrinthe avec le chemin le plus court
maze_out = []
for i in range(len(maze)):
    row = maze[i]
    out_row = ""
    for j in range(len(row)):
        if (i, j) in path:
            out_row += "X"
        else:
            out_row += row[j]
    maze_out.append(out_row)

# Écrire le labyrinthe avec le chemin le plus court dans le fichier maze-out.mz
with open("maze-out.mz.txt", "w") as f:
    for row in maze_out:
        f.write(row)
