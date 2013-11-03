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