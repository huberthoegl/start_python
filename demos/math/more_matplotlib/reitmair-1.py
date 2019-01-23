# From: Daniel Reitmair <daniel.reitmair@gmx.de>
# Hochschule Augsburg, WS0708

import sys
import cmath
import pylab

if __name__=="__main__":
    LGrund = []
    LGrundabs = []
    LOber1 = []
    LOber2 = []
    LOber3 = []
    LGesabs = []
    LGes = []
    LX1 = []
    LX2 = []
    LX3 = []
    LxAchse =[]
    w = 2 * cmath.pi * 50
    t = 0.00

    while t <= 0.02:
        LGrundabs.append(abs(cmath.sin(w*t)))
        LGesabs.append(abs(cmath.sin(w*t)-0.25*cmath.sin(3*w*t)))
        if t <= 0.01:
            LOber1.append(-0.25*cmath.sin(3*w*t))
            LX2.append(t)
        if t >= 0.01:
            LGrund.append(cmath.sin(w*t))
            LOber2.append(-0.25*cmath.sin(3*w*t))
            LOber3.append(0.25*cmath.sin(3*w*t))
            LGes.append(cmath.sin(w*t)-0.25*cmath.sin(3*w*t))
            LX3.append(t)       
        LX1.append(t)
        LxAchse.append(0)
        t = t + 0.0001
    
    pylab.title('Leiterspannungen Kurvenverlauf')
    pylab.xlabel('Zeit [ms]')
    pylab.ylabel('Spannung [V]')    
    
    pylab.plot(LX3,LGrund,'g--',LX3,LGes,'b:',LX1,LxAchse,'k-')
    pylab.plot(LX1,LGrundabs,'g-',LX1,LGesabs,'b-')
    pylab.plot(LX3,LOber2,'m-.',LX2,LOber1,'m-', LX3, LOber3,'m-')
    
    pylab.show()
