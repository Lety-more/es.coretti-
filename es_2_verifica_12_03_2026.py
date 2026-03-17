g=9.81
def posizione(t, v0=0, a=g, s0=0):
    spostemento=0
    spostemento=s0 + v0*t + 0.5 * a * (t**t)
    return spostemento

def velocita(t, v0=0, a=g):
    veloce=0
    veloce=v0 + a*t
    return veloce

def t(tempo,posizione):
    

pos=posizione(4)
print(pos)
vel=velocita(4,5)
print(vel)
