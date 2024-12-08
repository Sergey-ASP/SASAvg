import SasViewRunner as sv
import os
import sasavg.sas.qtgui.Plotting as pt
import numpy as np
import matplotlib.pyplot as plt

# import sasview.src.sas.qtgui.Plotting.Plotter2D as pt

filename = 'filename.omf'

model = sv.Model()
model.LoadFile(".\\" + filename)

model.rotationAvg(dtheta=8, dphi=22.5, bins=50, QxMax=0.12)

# change to what you want the file to be called
model.save(".\REMTestParams_C37_90rotate7.dat")
# model.plot()
print("done")
