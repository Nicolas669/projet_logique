_author_ = 'Lastes Elea'
_Filename_ = 'start'
_Creationdate_ = '11-02-19'

l = [[6, 7, 8], [5], [1, 3, 5, 8, 10, 11], [2, 3], [4, 5], [6, 1], [2, 4, 6], [3, 4]]

def write(liste):
    f = open('outputfile.txt', 'w')
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            string = str(liste[i][j])
            f.write(string + ' ')
        f.write('\n')
    f.close()

write(l)