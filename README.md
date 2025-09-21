# Black-Scholes Implied Volatility Surface

![Image](https://github.com/user-attachments/assets/c9b7b912-346d-463a-aa76-d7d09bb38c23)

*This repository contains a Python implementation for generating and interpolating an implied volatility (IV) surface using the Black-Scholes model.*
---

## ✈️Overview

- Computes European call option prices using the Black-Scholes formula.
- Calculates implied volatility from option prices.
- Creates a synthetic volatility surface and interpolates it for arbitrary strikes and maturities.
- Visualizes the resulting 3D implied volatility surface.

---

## ⛏️Features

- BlackScholes pricing: `bs_call_price(S, K, T, r, sigma)`
- Implied volatility calculation `implied_vol(price, S, K, T, r)`
- Synthetic vol surface generation using a sine + exponential model.
- 3D visualization of strikes, maturities, and interpolated IV.

---

## 🛣️Roadmap

1) American Options Support
2) Exotic options (Asian/Barrier etc)
3) Better UI
4) Live market feed
5) Crypto support

---

## ❤️Contribution
- Please feel free to contribute and add new features or fix bugs! Just fork + a new branch and you are good to go!

---

## Dependencies

```bash
pip install numpy scipy matplotlib
```

## ❗🙏🏼Disclaimer

This code is for educational and research purposes only :).  
It does not constitute financial advice and should **not be used for live trading or investment decisions.**  
The author is *not responsible for any financial losses* resulting from the use of this code.
