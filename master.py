# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:36:07 2016

@author: lafosse
"""

import numpy as np

# define dictionary to store all parameters
params = {
'time':1000,
'tstep':0.01,
'motors':5000,
'filaments':1000,

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

# init_vals = init(J,X,Z) #init.py called to evaluate initial conditions
# init_vals = list of lists (i.e. [[J], [X], [Z]] )


def init(J,X,Z):
    horizontal_radius = 2.0
    vertical_radius = 2.0
    x_poly = horizontal_radius*np.array([-1,1,1,-1,-1])
    y_poly = vertical_radius*np.array([1,1,-1,-1,1])
    boundary = np.pi*np.array([.75,.25,-.25,-.75,-1.25])
    
    for i in range(1,params['filaments'])
        while 1
            x = horizontal_radius*rand;
            y = vertical_radius*rand;
            if (inpolygon(x,y,xpol,ypol)) == 1
                Z(1,i) = x;
                Z(2,i) = y;
                break;
        

    return




'''
write/plot initial data
'''
#out = sim(initial)