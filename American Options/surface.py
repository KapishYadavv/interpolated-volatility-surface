import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq #scipy not used yet
from scipy.interpolate import RectBivariateSpline

def american_option_binomial(S, K, T, r, sigma, N=200, option_type="put"):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u                                      #CRR/ Binomial 
    q = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)


    ST = np.array([S * (u**j) * (d**(N-j)) for j in range(N+1)])

    
    if option_type == "call":
        V = np.maximum(ST - K, 0)
    else:
        V = np.maximum(K - ST, 0)

    
    for i in range(N-1, -1, -1):
        ST = ST[:i+1] / u  
        V = disc * (q * V[1:i+2] + (1-q) * V[:i+1])
        if option_type == "call":
            V = np.maximum(V, ST - K)  # see the problem here is that american options have earlys exercise
        else:                          #so its quite alot more tricky to make than european options
            V = np.maximum(V, K - ST)

    return V[0]


#THIS IS NOT COMPLETE!!! I WILL WORK ON UPDATING THIS I JUST WANTED THE FORMULA OUT.
#Version 0.9.1 