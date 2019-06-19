"""
Petrophysics equations
testing testing
"""


def gardner(vp, alpha=310, beta=0.25):
    """
    Compute bulk density (in kg/m^3) from vp (in m/s)
    """
    return alpha * vp**beta


def impedance(vp, rho):
    """
    Compute impedance from vp (in m/s) and bulk density (in kg/m^3)
    """
    return vp * rho
