# Name: Pranav Elavarthi
# Period: 5

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
    ''' your code goes here '''
    for i in vars:
        if i not in assignment: return False

    for i in assignment:
        if(i in adjs):
            for j in adjs[i]:
                if assignment[j] == assignment[i]: return False
    return True

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
    ''' your code goes here '''
    min = ""
    val = 999
    for i in vars:
        if(len(vars[i]) < val and len(vars[i]) != 0):
            min = i
            val = len(vars[i])
    return None if min == "" else min
   
def isValid(value, var, assignment, variables, adjs):
    # value is consistent with assignment
    # check adjacents to check 'var' is working or not.
    ''' your code goes here '''
    if var not in adjs: return True
    for i in adjs[var]:
        if value in assignment and value in assignment[i]: return False
    return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
    ''' your code goes here '''
    if check_complete(assignment, variables, adjs):
        for t in assignment:
            draw_shape(shapes[t], frame, assignment[t])
        return assignment
    const = select_unassigned_var(assignment, variables, adjs)
    for i in variables[const]:
        if isValid(i, const, assignment, variables, adjs):
            assignment[const] = i
            d = dict(variables)
            d[const] = {}
            if const in adjs:
                for j in adjs[const]:
                    if i in d[j]: d[j].remove(i)
            back = recursive_backtracking(assignment, d, adjs, shapes, frame)
            if back != None: return back
            assignment.pop(const)
    return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
    regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
    ''' your code goes here '''
    fr = open("mcNodes.txt","r")
    regions = [l.strip() for l in fr.readlines()]

   # Fill variables by using regions list -- no additional code for this part
    for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
    ''' your code goes here '''
    for line in open('mcEdges.txt', 'r'):
      line = line.strip().split()
      if line[0] not in adjacents: adjacents[line[0]] = [line[1]]
      else: adjacents[line[0]].append(line[1])

      if line[1] not in adjacents: adjacents[line[1]] = [line[0]]
      else: adjacents[line[1]].append(line[0])
   # Set graphics -- no additional code for this part
    frame = GraphWin('Map', 300, 300)
    frame.setCoords(0, 0, 299, 299)
    shapes = read_shape("mcPoints.txt")
    for s, points in shapes.items():
        draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
    solution = backtracking_search(variables, adjacents, shapes, frame)
    print (solution)
   
    mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''