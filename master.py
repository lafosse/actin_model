# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:36:07 2016

@author: lafosse
"""
import time
tic = time.time();

import numpy as np
from matplotlib import path

# define dictionary to store all parameters
params = {
'time':1000,
'tstep':0.01,
'filaments':1000,
'motors':5000,

# filament parameters
'fil_length':1.0, #filament length
'p0':1.0, #detachment rate
'p1':0.2, #attachement rate
'p2':0.7, #polymerization rate

# motor parameters
'r':0.3, #radius of search for motor attachment & max stretch for walk
'v':1.0, #velocity of motor
'k':3.0, #stiffness of motor 'spring'
'unbundleRate':1.0,
'bundleRate':0.2,
'activationRate':10.0,
'inactivationRate':1.0,
'motorBundleRadius':1.0 # same as r according to literature
}

# pre-allocate memory for output arrays
J = np.zeros((3,params['motors']))
X = np.zeros((2,params['motors']))
Z = np.zeros((5,params['filaments']))
# J -> motor state output:
#    J(1,:) = progression of motor state
#        0-inactive
#        1-active
#        2-bundled & active
#    J(2,:) = index of motor bundled to
#    J(3,:) = index of filament bound to
#    J(4,:) = bias placeholder if necessary (likely will remove)
# X -> motor position output
#    X(1,:) = x position of motor head
#    X(2,:) = y position of motor head
# Z -> filament output
#    Z(1,:) = x position of filament +end
#    Z(2,:) = y position of filament +end
#    Z(3,:) = angle of orientation (unit circle, CCW)
#    Z(4,:) = Z(1,:) - (fil_length * cos(Z(3,:)))
#    Z(5,:) = Z(2,:) - (fil_length * sin(Z(3,:)))

def initialize_positions(J,X,Z):
    boundary_height = 2.0;
    boundary_width = 2.0;
    boundary = path.Path([(-1*boundary_width,-1*boundary_height),
                          (-1*boundary_width,boundary_height),
                          (boundary_width,boundary_height),
                          (boundary_width,-1*boundary_height)],
                          readonly=True)
#    boundary = np.pi*np.array([.75,.25,-.25,-.75,-1.25])
    
    # assign random positions to plus ends of filaments
    for i in range(0,params['filaments']):
        while 1:
            x_plus_end = boundary_width*np.random.uniform();
            y_plus_end = boundary_height*np.random.uniform();
            # check if plus ends of filament are within boundary
            if boundary.contains_point(np.array([x_plus_end,y_plus_end])):
                Z[0,i] = x_plus_end;
                Z[1,i] = y_plus_end;
                while 1:
                    angle = 2*np.pi*np.random.uniform();
                    x_minus_end = x_plus_end-params['fil_length']*np.cos(angle);
                    y_minus_end = y_plus_end-params['fil_length']*np.sin(angle);
                    # check if minus ends of filament are within boundary
                    if boundary.contains_point(np.array([x_minus_end,y_minus_end])):
                        Z[2,i] = angle;
                        Z[3,i] = x_minus_end;
                        Z[4,i] = y_minus_end;
                        break
                break
            
    # assign random positions to motors       
    for j in range(0,params['motors']):
        while 1:
            x = boundary_width*np.random.uniform();
            y = boundary_height*np.random.uniform();
            if boundary.contains_point(np.array([x,y])):
                X[0,j] = x;
                X[1,j] = y;
                break            
            
    return J,X,Z
 
J,X,Z = initialize_positions(J,X,Z)



toc = time.time() - tic;
'''
write/plot initial data
'''
#out = sim(initial)