"""
Implementation of a basic PID controller

Alex Tong

"""
DEBUG = True

def bound(val, min, max):
    """ asserts that val is between min and max by truncation """

    if val > max:
        val = max
    if val < min:
        val = min
    return val

class PID:
    """ start with P, add I, then maybe D """
    def __init__(self, P = 1.0, I = 0.0, D = 0.0, I_max = 1.0, I_min = -1.0):
        self.wP = P
        self.wI = I
        self.wD = D
        self.I_max  = I_max
        self.I_min  = I_min
        self.prev_D = 0.0
        self.prev_I = 0.0

        self.target = 0.0
        self.current = 0.0
        self.error = 0.0

    def update(self, current):
    
        prev = self.current
        self.current = current
        err = self.target - self.current
        
        self.P_val  = self.wP * (err)
        self.D_val  = self.wD * (err - self.prev_D) # over time?
        self.prev_D = err
        self.prev_I = bound(self.prev_I + err, self.I_min, self.I_max)
        self.I_val  = self.wI * self.prev_I

        out = self.P_val + self.D_val + self.I_val
         
        print "=========="
        print "UPDATING PID"
        print "Target:", self.target, "Previous:", prev, "Current:", current
        print "P_val:", self.P_val, "D_val:", self.D_val, "I_val:", self.I_val, "Output:", out
        print "=========="

        return out

    def __repr__(self):
        return "<PID: Target: " + str(self.target) + " Current: " + str(self.current) + ">"



if __name__ == "__main__":
    a = PID()
    a.update(5.0)







