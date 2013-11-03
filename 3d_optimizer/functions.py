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