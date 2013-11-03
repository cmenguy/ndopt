from numpy import *

# RosenBrock function
class RosenBrock:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-2.048, max=2.048):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)-1):
            res += (1.-pos[i])**2 + 100.*(pos[i+1]-pos[i]**2)**2;
        return res;
    
    def getName(self):
        return 'RosenBrock'

# Goldstein and Price function
class GoldStein:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-2, max=2):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        return (1 + (1 + pos[0] + pos[1])**2 * (19 - 14*pos[0] + 3*pos[0]*pos[0] - 14*pos[1] + 6*pos[0]*pos[1] + 3*pos[1]*pos[1]))*(30 + (2*pos[0] - 3*pos[1])**2 * (18 - 32*pos[0] + 12*pos[0]*pos[0] + 48*pos[1] - 36*pos[0]*pos[1] + 27*pos[1]*pos[1]))
    
    def getName(self):
        return 'GoldStein'

# Michalewicz function
class Michalewicz:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=0, max=pi):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += -sin(pos[i])*(sin((i+1)*pos[i]*pos[i]/pi))**20
        return res;
    
    def getName(self):
        return 'Michalewicz'

# De Jong 1 function
class DeJong1:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5.12, max=5.12):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += pos[i]*pos[i];
        return res;
    
    def getName(self):
        return 'DeJong1'

# De Jong 2 function
class DeJong2:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-2.048, max=2.048):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        return (1.-pos[0])**2 + 100.*(pos[1]-pos[0]**2)**2;
    
    def getName(self):
        return 'DeJong2'

# De Jong 3 function
class DeJong3:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5.12, max=5):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += floor(pos[i]);
        return res;
    
    def getName(self):
        return 'DeJong3'

# Hyper Ellipsoid function
class Ellipsoid:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-65.536, max=65.536):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            subres = 0;
            for j in range(i):
                subres += pos[j];
            res += subres*subres;
        return res;
    
    def getName(self):
        return 'HyperEllipsoid'

# RastRigin function
class RastRigin:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5.12, max=5.12):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += pos[i]*pos[i] - 10.*cos(2.*pi*pos[i]);
        return 10*len(pos) + res;
    
    def getName(self):
        return 'RastRigin'

# Schwefel function
class Schwefel:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-500, max=500):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += -pos[i]*sin(sqrt(abs(pos[i])));
        return res;
    
    def getName(self):
        return 'Schwefel'