# map-scanner

A python implementation of a map scanner.

Let's think of an embeded agent that exposes the following methods:

* `move()` => returns true if the agent successfully moved forward from one unit.
* `rotate(angle)` => rotate the agent to a specific angle and return nothing.

We want to be able to place this agent into an environment filled with obstacles.
The agent must be able to produce a map of this environment through the following method:

* `scan(agent)` => return a 2d matrix of this environment.

For the purpose of this simulation, this agent will read it's environment from a file stored in environment variable `MAP_FILE`.
