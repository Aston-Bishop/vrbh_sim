This is just thinking aloud for the simple algorithm - 

This should be run on a list of nodes representing the edges of the searched nodes in the graph
```
y pos = y position of Node (current node being searched)
x pos = x position of the Node
R = Robot (which will be fixed at this point)
Rx = Robot x position
Ry = Robot y 
iter-n = The number of iterations so far (3rd iteration, 4th etc)


if y pos == iter-n from Ry: 
	Node is EITHER a top node or a bottom node (checking should probably be implemented)
	Node has 3 edges to search next
if x pos < Rx: 
	Node is to the left of the Robot
	Therefore 
	1 edge to search next in -ve direction from Robot
if x pos > Rx: 
	Node is to the right of the robot
	therefore
	1 edge to search in +ve direction from the Robot

```