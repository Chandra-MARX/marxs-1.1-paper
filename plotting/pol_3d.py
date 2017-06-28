# The code following code is taken from
# https://marxs.readthedocs.io/en/latest/examples.html
# and just copied here with the addition of output commands
# to write a pdf file.

from copy import copy
from transforms3d import euler
from marxs.source import LabPointSourceCone

from marxs.simulator import Sequence, KeepCol
light = LabPointSourceCone(position=[200., 0., 0.], direction=[-1., 0, 0],
                           half_opening=0.02)
# keep a copy of the position and direction for later
light_pos = light.position.copy()
light_dir = light.dir.copy()

import numpy as np
from marxs.optics import FlatBrewsterMirror, FlatDetector
rot1 = np.array([[2.**(-0.5), 0, -2.**(-0.5)],
                 [0, 1., 0],
                 [2.**(-0.5), 0, 2.**(-0.5)]])
m1 = FlatBrewsterMirror(orientation=rot1,zoom=[1, 10, 30])
# Keep a copy of the initial position for later
m1pos4d = m1.pos4d.copy()

rot2 = np.array([[2.**(-0.5), 0, 2.**(-0.5)],
                 [0, 1., 0],
                 [-2.**(-0.5), 0, 2.**(-0.5)]])
m2 = FlatBrewsterMirror(orientation=rot2,zoom=[1, 10, 30], position=[0, 0, 2e2])
# display is usually set for all objects of a class.
# To change only one mirror, make a copy of this dictionary first.
m2.display = copy(m2.display)
m2.display['color'] = 'blue'
det = FlatDetector(position=[50, 0, 2e2], zoom=[1., 20., 20.])

# Make an object that keeps the photon position after every simulation step
# for later plotting of photon paths.
pos = KeepCol('pos')
experiment = Sequence(elements=[m1, m2, det], postprocess_steps=[pos])
from mayavi import mlab
from marxs.visualization.mayavi import plot_object, plot_rays
fig = mlab.figure()
for i, angle in enumerate(np.arange(0, .5, .15) * np.pi):
  rotmat = np.eye(4)
  rotmat[:3, :3] = euler.euler2mat(angle, 0, 0, 'szxy')
  light.position = np.dot(rotmat, light_pos)
  light.dir = np.dot(rotmat, light_dir)
  m1.pos4d = np.dot(rotmat, m1pos4d)
  rays = light(100)
  pos.data = []
  pos(rays)
  rays = experiment(rays)
  # Now do the plotting
  obj = plot_object(experiment, viewer=fig)
  rout = plot_rays(pos.format_positions())

mlab.view(-60, 140., 525, [70., 60., 60.],roll=250)
mlab.savefig('../3dpol.pdf')
mlab.savefig('../web/3dpol.x3d')
