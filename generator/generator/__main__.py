# __main__.py

from.redi import Redi
import copy
import anytree
from anytree import Node
from anytree.exporter import JsonExporter


FACES = (1, 3, 4, 5)

def rotate_clockwise(cube, face):
    cube_temp = Redi()
    cube_temp.cube = copy.deepcopy(cube.cube)
    cube_temp.rotate(face, "up", 1)
    return cube_temp.cube

def rotate_counter_clockwise(cube, face):
    cube_temp = Redi()
    cube_temp.cube = copy.deepcopy(cube.cube)
    cube_temp.rotate(face, "up", -1)
    return cube_temp.cube

def populate(root, cube, parent, depth=1):
    cube_temp = Redi()
    cube_temp.cube = copy.deepcopy(cube)
    
    if depth <= 10:
        for face in FACES:
            rota = rotate_clockwise(cube_temp, face)
            if anytree.search.find_by_attr(root, rota) is None:
                a = Node(rota, parent=parent)
                populate(root, rota, a, depth=depth+1)
            rota = rotate_counter_clockwise(cube_temp, face)
            if anytree.search.find_by_attr(root, rota) is None:
                b = Node(rota, parent=parent)
                populate(root, rota, b, depth=depth+1)
        

if __name__ == '__main__':
    print("Quick test")
    testcube =  Redi()
    root = Node(testcube.cube)
    populate(root, testcube.cube, root)
    exporter = JsonExporter(indent=2, sort_keys=True)
    f = open("exit.json", "a")
    f.write(exporter.export(root))
    f.close()
