"""
This module consists of constant classes in the L-system.
"""


class KOCH_CURVE:
    VARIABLES = ['F']
    CONSTANTS = ['-', '+']
    THETA = 90
    AXIOM = 'F'
    PRODUCTION_RULES = {
        'F': 'F+F-F-F+F'
    }


class HILBERT_CURVE:
    VARIABLES = ['X', 'Y']
    CONSTANTS = ['-', '+']
    THETA = 90
    AXIOM = 'X'
    PRODUCTION_RULES = {
        'X': '+YF-XFX-FY+',
        'Y': '-XF+YFY+FX-'
    }


class HILBERT_CURVE_II:
    VARIABLES = ['X', 'Y']
    CONSTANTS = ['-', '+']
    THETA = 90
    AXIOM = 'X'
    PRODUCTION_RULES = {
        'X': 'XFYFX+F+YFXFY-F-XFYFX',
        'Y': 'YFXFY-F-XFYFX+F+YFXFY'
    }


class PEANO_GOSPER_CURVE:
    VARIABLES = ['X', 'Y']
    CONSTANTS = ['-', '+']
    THETA = 60
    AXIOM = 'X'
    PRODUCTION_RULES = {
        'X': 'X+YF++YF-FX--FXFX-YF+,',
        'Y': '-FX+YFYF++YF+FX--FX-Y'
    }


class SIERPINSKI_TRIANGLE:
    VARIABLES = ['F', 'X']
    CONSTANTS = ['-', '+']
    THETA = 60
    AXIOM = 'X'
    PRODUCTION_RULES = {
        'F': 'FF',
        'X': '--FXF++FXF++FXF--'
    }

