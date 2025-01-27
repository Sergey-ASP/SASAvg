import SasViewRunner as sv

filename ='.\\magnaTestData_radius_30A.omf'

model = sv.Model()
model.LoadFile(filename)

model.rotationAvg(dtheta=8, dphi=22.5, bins=50, QxMax=0.12)

# change to what you want the file to be called
model.save(".\SavedFileName.dat")
# model.plot()
print("done")
