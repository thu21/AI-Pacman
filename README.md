![alt](http://ai.berkeley.edu/projects/release/search/v1/001/maze.png)
## Introduction
In this project, your Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. You will build general search algorithms and apply them to Pacman scenarios.
 
## Language
  Python version 2.7
## Search
  1. Depth First Search
      
      ` python pacman.py -l tinyMaze -p SearchAgent`
	  
	   `python pacman.py -l mediumMaze -p SearchAgent`
	   
	   `python pacman.py -l bigMaze -z .5 -p SearchAgent`
  2. Breadth First Search
  
       `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`
  
       `python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5`
  
  3. Varying the Cost Function
  
      `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`
  
      `python pacman.py -l mediumDottedMaze -p StayEastSearchAgent`
  
      `python pacman.py -l mediumScaryMaze -p StayWestSearchAgent`
  
  4. A* search
  
      `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`
  
  5. Finding All the Corners
  
     `python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`
  
     `python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`
  
  6.Corners Problem: Heuristic
  
     `python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`
 

