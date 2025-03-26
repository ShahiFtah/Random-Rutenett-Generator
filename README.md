# Conway's Game of Life Simulation - Python

This repository contains the implementation of Conway's Game of Life, a cellular automaton devised by the British mathematician John Conway. The program simulates the evolution of cells on a grid where each cell can either be alive or dead, and its future state is determined by the number of live neighbors it has.

## Purpose
This project was developed as part of the IN1000 course assignment (Fall 2022). The goal was to create a program that simulates the life and death of cells over multiple generations based on the rules of Conway's Game of Life. This project serves as both an educational tool and a demonstration of object-oriented programming in Python.

## Features
- **Generational Evolution**: The program allows users to observe the simulation of cell evolution generation by generation.
- **User Interaction**: The user can interact with the simulation by adjusting the dimensions of the grid and observing how the cell population changes over time.
- **Dynamic Grid**: The simulation works on a grid of customizable size, with each cell having a state of "alive" or "dead" depending on its surrounding cells.

## Game of Life Rules
- A live cell with fewer than two live neighbors dies (underpopulation).
- A live cell with two or three live neighbors remains alive.
- A live cell with more than three live neighbors dies (overpopulation).
- A dead cell with exactly three live neighbors becomes alive (reproduction).

## Files
- **celle.py**: Contains the class definition for individual cells, with methods for updating their state and checking neighbors.
- **rutenett.py**: Manages the grid of cells and handles the simulation of their state changes.
- **verden.py**: Manages the simulation of the entire world, including the tracking of generations and cell updates.
- **hovedprogram.py**: The main program that initializes the simulation and provides an interface for the user to interact with.
