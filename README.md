# continuous-optimizer &mdash; Optimization on n-dimensional functions

continuous-optimizer applies the particle swarm algorithm to find the global minima in a set of mathematical functions.

## Quicklinks

  - [Installation](#installation)
  - [Results](#results)
    - [Rosenbrock](#rosenbrock)
    - [Goldstein and Price](#goldstein-and-price)
    - [Michalewicz](#michalewicz)
    - [De Jong 1](#de-jong-1)
    - [De Jong 2](#de-jong-2)
    - [De Jong 3](#de-jong-3)
    - [Rastrigin](#rastrigin)
    - [Schwefel](#schwefel)
    - [Zakharov](#zakharov)
    - [Easom](#easom)
    - [Six Hump Camel Back](#six-hump-camel-back)
    - [Ackley Path](#ackley-path)
  - [Analysis](#analysis)
    - [Influence of the number of particles](#influence-of-the-number-of-particles)
    - [Influence of the initial speed variation coefficient](#influence-of-the-initial-speed-variation-coefficient)
    - [Influence of the mobility of the particles](#influence-of-the-mobility-of-the-particles)

## Installation

continuous-optimizer uses `numpy` out of convenience to compute the mathematical operations (not sure if it's really necessary and maybe everything could be found in the `math` module, but `numpy` is so much more fun !)

It also uses `matplotlib` for the graphical representation of the functions in 3D, especially the `mplot3d` module.

There are several parameters that can be passed to the script:

  - `dim` is the number of dimensions on which you want to run the optimization. Keep in mind that the higher the dimension, the harder the optimization problem.
  - `function` is the name of a function to optimize. All supported function can be found in the `functions.py` file. The value passed must match the class name, and the case doesn't matter. For example, to run optimization on the Zakharov function, you can see that there is a class called `Zakharov` so you could pass in a string like `zakharov`.
  - `num-particles` is the number of particles you want to use for your optimization. Defaults to 25.
  - `iterations` is the maximum number of iterations after which the algorithm will stop if it has not converged. Avoid infinite loops.
  - `verbose` is the verbose level which is a positive number more than or equal to 0. The higher the verbose, the more details you will see. At 0 there will be no details, 1 will display the initial and final functions, and 2 will display the functions at each iteration.
  - `phi` is the initial speed variation coefficient.
  - `K` is the mobility of the particles.

For a complete list of all parameters available, you can use the help menu:

    python particle_swarm -h
    Usage: particle_swarm [options]

    Options:
      -h, --help            show this help message and exit
      -d DIM, --dim=DIM     dimension of the function to optimize
      -f FUNCTION, --function=FUNCTION
                            name of the function to optimize
      -n PARTICLES, --num-particles=PARTICLES
                            number of particles in the swarm
      -i ITERATIONS, --iterations=ITERATIONS
                            max number of iterations
      -v VERBOSE, --verbose=VERBOSE
                            verbose level
      -p PHI, --phi=PHI     initial speed variation coefficient
      -k K                  mobility of the particles

## Results

The results of the particle swarm algorithm will be described on each of the functions supported in the `functions.py` file. These functions have very different properties and topology, so it is a good indication to see how well the particle swarm algorithm performs.

### Rosenbrock

The [Rosenbrock](http://en.wikipedia.org/wiki/Rosenbrock_function) function is a non-convex function whose minima is found in a parabolic valley.

It is defined by:

![equation](http://latex.codecogs.com/gif.latex?(1-x\)^2+100(y-x^2\)^2)

Applying particle swarm gives us the minima in (1, 1) like shown below:

![minima](/data/rosenbrock.png)

### Goldstein and Price

The Goldstein and Price function has a minima in (0, -1):

![minima](/data/goldstein.png)

### Michalewicz

![minima](/data/michalewicz.png)

### De Jong 1

![minima](/data/dejong1.png)

### De Jong 2

The De Jong 2 function is just another name for the [Rosenbrock](#rosenbrock) function.

### De Jong 3

![minima](/data/dejong3.png)

### Rastrigin

![minima](/data/rastrigin.png)

### Schwefel

![minima](/data/schwefel.png)

### Zakharov

![minima](/data/zakharov.png)

### Easom

![minima](/data/easom.png)