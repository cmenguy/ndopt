from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import *

import matplotlib.pyplot as plt
import pylab as pl

# Particle Swarm algorithm to find optima of a continous 3d function
class ParticleSwarm:

    # functions: array of functions to optimize
    # phi: initial speed variation coefficient
    # K: mobility of the particles
    def __init__(self, functions, phi=4.1, K=1):
        self.functions = functions;
        self.phi = phi;
        self.K = K;
        self.Ki = 2.*self.K/(self.phi - 2. + sqrt(self.phi*self.phi - 4.*self.phi));
        
    # represents 1 particle in the swarm
    class Particle:

        # pos: position of the particle
        # speed: speed of the particle
        # best: best position known to this particle
        def __init__(self, pos, speed, best):
            self.pos = pos;
            self.speed = speed;
            self.best = best;
            
        def setPos(self, newpos):
            self.pos = newpos;
                
        def setSpeed(self, newspeed):
            self.speed = newspeed;
            
        def setBest(self, newbest):
            self.best = newbest;
            
    # initialize the swarm with random positions and set speed to 0
    def initialize(self, function):
        particles = []
        
        for i in range(self.max_particules):
            
            pos = [];
            speed = [];
            
            for rg in range(function.dim):
                pos.append(random.uniform(function.min, function.max));
                speed.append(0);
            
            particles.append(self.Particle(pos, speed, pos));
            
        return particles;
    
    # print the function to optimize as well as particle positions
    def dispFunc(self, function, particles, x, y, z, title='Particles swarm'):
        fig = plt.figure();
        ax = Axes3D(fig); 
                
        step = (function.max - function.min)*10./4.
                
        ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.get_cmap("jet"))
                
        best=0;
        for part in range(len(particles)):
            if function.getValue(particles[best].pos) > function.getValue(particles[part].pos):
                best = part;
            ax.scatter([particles[part].pos[0]], [particles[part].pos[1]], [function.getValue(particles[part].pos)], marker='o', color='black', linewidth=10.)
        ax.scatter([particles[best].pos[0]], [particles[best].pos[1]], [function.getValue(particles[best].pos)], marker='x', color='red', linewidth=30.)
        
        plt.title(title)
        plt.show();
        
    # compute the mean of the particles positions
    def getMeans(self, function, particles):
        m = [];
        v = [];
        for d in range(function.dim):
            tab = []
            for part in range(len(particles)):
                tab.append(particles[part].pos[d]);
            m.append(pl.mean(tab));
            v.append(pl.std(tab));
            
        return m, v;
        
    # main loop of the particle swarm algorithm
    def run(self, verbose=2, step=10, c='blue'):        
        # iterate over every function to optimize
        for i in range(len(self.functions)):
            it = 0;
            
            self.max_particules = self.functions[i].max_particules;
            self.max_it = self.functions[i].max_it;
            
            # initialize particles positions
            particles = self.initialize(self.functions[i]);
                        
            # if verbose more than 1, create the grid
            if verbose >= 1:
                x = arange(self.functions[i].min, self.functions[i].max, 0.05)
                y = arange(self.functions[i].min, self.functions[i].max, 0.05)
                x, y = meshgrid(x, y)
                z = self.functions[i].getValue([x, y])
            
            # if verbose more than 1, display the initial function
            if verbose >= 1:
                self.dispFunc(self.functions[i], particles, x, y, z, 'Initialization : ' + self.functions[i].getName())

            # main loop, iterate until the algorithm has converged
            while it <= self.max_it:
                phi1 = random.uniform(0, 1)*self.phi/2;
                phi2 = random.uniform(0, 1)*self.phi/2;
                
                # if strong verbose, display function every step iteration
                if verbose == 2 and it % step == 0:
                    self.dispFunc(self.functions[i], particles, x, y, z, 'Iteration ' + str(it) + ' : ' + self.functions[i].getName())
                
                # iterate over every particle
                for part in range(len(particles)):                    
                    family = [];
                    bests = [];
                    for ngb in range(len(particles)):
                        family.append(self.functions[i].getValue(particles[ngb].best));
                        bests.append(particles[ngb].best);
                    
                    # compute best position of neighbors
                    pkvoisin = bests[family.index(min(family))];
                    
                    # speed regulation following particles law
                    particles[part].setSpeed(self.Ki*array(particles[part].speed) + phi1*(array(particles[part].best)-array(particles[part].pos)) + phi2*(array(pkvoisin)-array(particles[part].pos)));
                    particles[part].setPos(particles[part].pos + particles[part].speed);
                    
                    # make sure we stay within the research space
                    for dd in range(len(particles[part].pos)):
                        if particles[part].pos[dd] > self.functions[i].max:
                            particles[part].pos[dd] = self.functions[i].max;
                        if particles[part].pos[dd] < self.functions[i].min:
                            particles[part].pos[dd] = self.functions[i].min;
                                        
                    # update the best known position for this particle
                    if self.functions[i].getValue(particles[part].best) > self.functions[i].getValue(particles[part].pos):
                        particles[part].setBest(particles[part].pos);
                    
                it += 1;
                
            # if verbose more than 1, display function after convergence
            if verbose >= 1:
                self.dispFunc(self.functions[i], particles, x, y, z, 'Convergence : ' + self.functions[i].getName())