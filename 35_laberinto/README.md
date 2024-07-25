<p align="center">INFORMACIÓN</p>

ESP:

Juego del laberinto.

Imagina que eres parte de un equipo de desarrollo de IA que se encarga de
crear un sistema para que un robot resuelva laberintos. 

El laberinto está
representado por una matriz, donde ciertos valores indican caminos permitidos
( 0 ), paredes ( 1 ), y la salida ( 9 ). La tarea es implementar una función
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.

Toma en cuenta los siguientes puntos:
1. La matriz representa el laberinto, donde los valores son:
0 : Camino permitido.
1 : Pared, no se puede atravesar.
9 : Salida del laberinto.
2. La función resolver_laberinto utiliza recursividad
para encontrar la ruta más corta desde una posición inicial hasta la salida.
3. La función debe devolver una lista de coordenadas que representan la ruta
desde la posición inicial hasta la salida.
4. Lista de movimientos posibles: arriba ( (-1, 0) ), abajo( (1,
0) ), izquierda ( (0, -1) ), derecha ( (0, 1) ).




---

ENG:

Maze Game.

Imagine you are part of an AI development team tasked with creating a system for a robot to solve mazes.

The maze is represented by a matrix, where certain values indicate allowed paths (0), walls (1), and the exit (9). The task is to implement a recursive function that finds the shortest path for the robot to exit the maze.

Consider the following points:

The matrix represents the maze, where the values are:
0: Allowed path.
1: Wall, cannot be traversed.
9: Exit of the maze.
The function solve_maze uses recursion to find the shortest path from a starting position to the exit.
The function should return a list of coordinates representing the path from the starting position to the exit.
List of possible moves: up ((-1, 0)), down ((1, 0)), left ((0, -1)), right ((0, 1)).

