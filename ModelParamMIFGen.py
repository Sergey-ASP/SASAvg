import micromagneticmodel as mm  
import discretisedfield as df 
import matplotlib.pyplot as plt
import k3d as k3d
import magna.utils as mu
import SasViewRunner as sv
import fileinput


##  INITIAL VALUES  ##
_layers = 4
_layer_radius = 4
_particle_radius = 3.5e-9

##  FOR FILE NAME AND MAGNA-U PARAMS ONLY ##
_centers_per_layer = 37          # make sure that layer radius corresponds to this value!
_spin_flip_background = .05
_sld = 1.0                       # in e-6 A^-2


#  use r_tuple to specify radius of spheres
magna = mu.MNP(id=-1, name="test", n_layers=_layers, layer_radius=_layer_radius, discretizations=(1,1,1), r_tuple=(4e-9, _particle_radius, _particle_radius), form='hcp')
mu.MNP.initialize(self=magna, m0=(0,0,1), fields='m')
M = magna.m_field
magna.save_fields()

# uncomment if you want to see the field generated
# M.sel('z').mpl()
# M.sel('x').mpl()
# M.sel('y').mpl()
plt.show()

filename = "REMTestParams_C{0}_L{1}_SLD{2}_R{3}_SFB{4}.omf".format(_centers_per_layer, _layers, _sld, _particle_radius, _spin_flip_background)
magna.m_field.to_file(filename, representation="txt")


# changing file to fit sasview expected format
file = open(filename, mode="r+")
file.repl



model = sv.Model()
model.LoadFile(".\\" + filename)

model.rotationAvg(dtheta=8, dphi=22.5, bins=50, QxMax=0.12)
model.save(".\REMTestParams_C37_90rotate7.dat")
model.plot()
print("done")
