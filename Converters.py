# This file contains functions to convert between different currencies. The `usd_to_nep` function converts US dollars to Nepalese rupees, while the `nep_to_usd` function converts Nepalese rupees to US dollars. The `nep_to_inr` function converts Nepalese rupees to Indian rupees, and the `inr_to_nep` function converts Indian rupees to Nepalese rupees. Each function takes an amount as input and returns the converted amount based on the specified conversion rates.
def usd_to_nep(usd):
    return usd * 150

def nep_to_usd(nep):
    return nep / 150

def nep_to_inr(nep):
    return nep * 0.6

def inr_to_nep(inr):
    return inr / 0.6