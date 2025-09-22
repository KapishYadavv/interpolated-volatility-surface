import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt


#there is some insane maths stuff here please! dont touch it. lol jk its just the black scholes model
def bs_call_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def implied_vol(price, S, K, T, r):
    try:
        return brentq(lambda sigma: bs_call_price(S, K, T, r, sigma) - price, 1e-5, 5)
    except ValueError:
        return np.nan

#uh i might change these later -kapish 
spot = 100
r = 0.01
true_vol_surface = lambda K, T: 0.2 + 0.05 * np.sin(K / 10) * np.exp(-T)  # synthetic vol model

strikes = np.linspace(80, 120, 15)
maturities = np.linspace(0.05, 1.5, 15)

option_prices = np.array([
    [bs_call_price(spot, K, T, r, true_vol_surface(K, T)) for K in strikes]
    for T in maturities
])

iv_surface = np.array([
    [implied_vol(option_prices[i, j], spot, strikes[j], maturities[i], r) 
     for j in range(len(strikes))]
    for i in range(len(maturities))
])


iv_interpolator = RectBivariateSpline(maturities, strikes, iv_surface)

def get_iv(K, T):
    return iv_interpolator(T, K)[0, 0]

test_K = 105
test_T = 0.4
iv_result = get_iv(test_K, test_T)
print(f"Interpolated IV at K={test_K}, T={test_T}: {iv_result:.4f}")


X, Y = np.meshgrid(strikes, maturities)
Z = iv_surface

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
ax.set_title("Interpolated Implied Volatility Surface")
ax.set_xlabel("Strikes")
ax.set_ylabel("Maturity (In years)")
ax.set_zlabel("Implied Volatility")
plt.tight_layout()
plt.show()


#version 0.9 // NSE specfic values NOT added yet.