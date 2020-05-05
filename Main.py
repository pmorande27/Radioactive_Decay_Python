from Radioactive_Decay_Python.animate import animate


def main():
    d = animate(10, 0.02775,0.01)
    d.animateDecay()
    d.displayIsotope()

main()