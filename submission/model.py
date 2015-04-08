#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of Nicolas P. Rougier nor the names of its
#   contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------
#
# References:
# -----------
#
# * Gurney, K. N., Prescott, T. J. & Redgrave, P. (2001) A computational model
#   of action selection in the basal ganglia I: A new functional anatomy,
#   Biological Cybernetics 84: 401-410
#
# * Gurney, K. N., Prescott, T. J. & Redgrave, P. (2001) A computational model
#   of action selection in the basal ganglia II: Analysis and simulation of
#   behaviour, Biological Cybernetics 84: 411-423.
#
# -----------------------------------------------------------------------------
from dana import *

figs = {}

def draw_group(name, data, title=''):
    ''' '''
    axes = plt.gca()
    x = np.arange(len(data))
    axes.grid()
    rects = axes.bar(left=x,height=np.ones_like(data),
                     width=.75, align='center', alpha=0.5)
    axes.set_ylim([0,1])
    plt.xticks(x)
    axes.set_title(title, fontsize=10)
    for label in axes.get_xticklabels() + axes.get_yticklabels():
        label.set_fontsize(10)
    figs[name] = axes,rects

def update_group(name, data):
    ''' '''
    axes,rects = figs[name]
    for rect,h in zip(rects,data):
        rect.set_height(h)

def draw_plot(name, title=''):
    ''' '''
    axes = plt.gca()
    axes.grid()
    line, = axes.plot([1],[1])
    axes.set_xlim([0,10])
    axes.set_ylim([-0.1,+0.7])
    axes.set_title(title, fontsize=10)
    for label in axes.get_xticklabels() + axes.get_yticklabels():
        label.set_fontsize(10)
    plt.xlabel('Time (s)', fontsize=10)
    figs[name] = axes,line

def update_plot(name, x, y):
    ''' '''
    axes, line = figs[name]
    line.set_xdata(x)
    line.set_ydata(y)


# Number of channels
n = 6

# Time constant
tau  =  0.04

# Resting levels
eSt1 = +0.20
eSt2 = +0.20
eSTN = -0.25
eGPe = -0.20
eGPi = -0.20
eVLT = +0.00
ePFC = +0.00
eTRN = +0.00

# Connections strength
D1 = 0.2
D2 = 0.2

STN_GPe = +0.9
St2_GPe = -1.0

STN_GPi = +0.9
GPe_GPi = -0.3
St1_GPi = -1.0

GPe_STN = -1.0
PFC_STN = +0.5
PC_STN  = +0.5

PFC_St1 = +0.5*(1+D1)
PC_St1  = +0.5*(1+D1)

PFC_St2 = +0.5*(1-D2)
PC_St2  = +0.5*(1-D2)

GPi_VLT = -1.0
PFC_VLT = +1.0
TRN_VLT = -0.4
TRN_VLT_self = -0.125

PFC_TRN = +1.0
GPi_TRN = -0.2
VLT_TRN = +1.0

VLT_PFC = +1.0


# Posterior Cortex
PC  = zeros(n, '''V''')

# Striatum D1: medium spiny neurons of the striatum with D1 dopamine receptors
St1 = zeros(n, '''dU/dt = 1/tau*(-U + PC_ + PFC_)
                   V    = np.minimum(np.maximum(U-eSt1,0),1)
                   PC_; PFC_''')

# Striatum D2: medium spiny neurons of the striatum with D2 dopamine receptors
St2 = zeros(n, '''dU/dt = 1/tau*(-U + PC_ + PFC_)
                   V    = np.minimum(np.maximum(U-eSt2,0),1)
                   PC_; PFC_''')

# Sub-Thalamic Nucleus
STN = zeros(n, '''dU/dt = 1/tau*(-U + PC_ + PFC_ + GPe_)
                   V    = np.minimum(np.maximum(U-eSTN,0),1)
                   PC_; PFC_; GPe_''')

# External Globus Pallidus
GPe = zeros(n, '''dU/dt = 1/tau*(-U + STN_ + St2_)
                   V    = np.minimum(np.maximum(U-eGPe,0),1)
                   STN_; St2_''')

# External Globus Pallidus
GPi = zeros(n, '''dU/dt = 1/tau*(-U + STN_ + St1_ + GPe_)
                   V    = np.minimum(np.maximum(U-eGPi,0),1)
                   STN_; St1_; GPe_''')

#  Ventro-Lateral Thalamus
VLT = zeros(n, '''dU/dt = 1/tau*(-U + PFC_ + TRN_ + GPi_)
                   V    = np.minimum(np.maximum(U-eVLT,0),1)
                   PFC_; TRN_; GPi_''')

# Prefrontal Cortex
PFC = zeros(n, '''dU/dt = 1/tau*(-U + PC_ + VLT_)
                   V    = np.minimum(np.maximum(U-ePFC,0),1)
                   PC_; VLT_''')

# Thalamic Reticular Nucleus
TRN = zeros(n, '''dU/dt = 1/tau*(-U + PFC_ + VLT_ + GPi_)
                   V    = np.minimum(np.maximum(U-eTRN,0),1)
                   PFC_; VLT_; GPi_''')

# St1 connections
SparseConnection( PC('V'),  St1('PC_'),   PC_St1 * np.ones(1) )
SparseConnection( PFC('V'), St1('PFC_'), PFC_St1 * np.ones(1) )

# St2 connections
SparseConnection( PC('V'),  St2('PC_'),   PC_St2 * np.ones(1) )
SparseConnection( PFC('V'), St2('PFC_'), PFC_St2 * np.ones(1) )

# STN connections
SparseConnection( PC('V') , STN('PC_'),   PC_STN * np.ones(1) )
SparseConnection( PFC('V'), STN('PFC_'), PFC_STN * np.ones(1) )
SparseConnection( GPe('V'), STN('GPe_'), GPe_STN * np.ones(1) )

# GPe connections
DenseConnection(  STN('V'), GPe('STN_'), STN_GPe * np.ones((n,n)) )
SparseConnection( St2('V'), GPe('St2_'), St2_GPe * np.ones(1)     )

# GPi connections
DenseConnection(  STN('V'), GPi('STN_'), STN_GPi * np.ones((n,n)) )
SparseConnection( St1('V'), GPi('St1_'), St1_GPi * np.ones(1)     )
SparseConnection( GPe('V'), GPi('GPe_'), GPe_GPi * np.ones(1)     )

# VLT connections
SparseConnection( PFC('V'), VLT('PFC_'), PFC_VLT * np.ones(1) )
SparseConnection( GPi('V'), VLT('GPi_'), GPi_VLT * np.ones(1) )
K = TRN_VLT * np.ones((n,n))
K[np.arange(n),np.arange(n)] = TRN_VLT_self
DenseConnection(  TRN('V'), VLT('TRN_'), K )

# PFC connections
SparseConnection( VLT('V'), PFC('VLT_'), VLT_PFC * np.ones(1) )
SparseConnection(  PC('V'), PFC('PC_'),            np.ones(1) )

# TRN connections
SparseConnection( PFC('V'), TRN('PFC_'), PFC_TRN * np.ones(1) )
SparseConnection( VLT('V'), TRN('VLT_'), VLT_TRN * np.ones(1) )
SparseConnection( GPi('V'), TRN('GPi_'), GPi_TRN * np.ones(1) )


# Draw figures
plt.ion()
fig = plt.figure(figsize=(15,12))
fig.patch.set_alpha(0.0)

plt.subplot(4,3,1)
draw_group('PC',  PC['V'],  'Posterior Cortex (PC)')
plt.subplot(4,3,2)
draw_group('PFC', PFC['V'], 'Prefrontal Cortex (PFC)')
plt.subplot(4,3,3)
draw_group('STN', STN['V'], 'Sub-Thalamic Nucleus (STN)')
plt.subplot(4,3,4)
draw_group('St1', St1['V'], 'Striatum D1 (St1)')
plt.subplot(4,3,5)
draw_group('St2', St2['V'], 'Striatum D2 (St2)')
plt.subplot(4,3,6)
draw_group('GPe', GPe['V'], 'External globus pallidus (GPe)')
plt.subplot(4,3,7)
draw_group('GPi', GPi['V'], 'Internal globus pallidus (GPi)')
plt.subplot(4,3,8)
draw_group('VLT', VLT['V'], 'Ventro Lateral Thalamus (VLT)')
plt.subplot(4,3,9)
draw_group('TRN', TRN['V'], 'Thalamic Reticular Nucleus (TRN)')
plt.subplot(4,3,10)
draw_plot('GPi_1', 'GPi channel 1')
plt.subplot(4,3,11)
draw_plot('GPi_2', 'GPi channel 2')
plt.subplot(4,3,12)
draw_plot('GPi_3', 'GPi channel 3-6')

GPi_1 = []
GPi_2 = []
GPi_3 = []


@clock.at(2*second)
def update_PC(t):
    PC['V'][0] = .4

@clock.at(4*second)
def update_PC(t):
    PC['V'][1] = .6

@clock.at(6*second)
def update_PC(t):
    PC['V'][0] = .6

@clock.at(8*second)
def update_PC(t):
    PC['V'][0] = .4

# Refresh figures every 10 miliseconds
@clock.every(25*millisecond)
def update_figure(t):

    GPi_1.append(GPi['V'][0])
    GPi_2.append(GPi['V'][1])
    GPi_3.append(GPi['V'][2])

    update_group('PC',  PC['V'])
    update_group('PFC', PFC['V'])
    update_group('STN', STN['V'])
    update_group('St1', St1['V'])
    update_group('St2', St2['V'])
    update_group('GPe', GPe['V'])
    update_group('GPi', GPi['V'])
    update_group('VLT', VLT['V'])
    update_group('TRN', TRN['V'])

    update_plot('GPi_1', np.arange(len(GPi_1))*25*millisecond, GPi_1)
    update_plot('GPi_2', np.arange(len(GPi_2))*25*millisecond, GPi_2)
    update_plot('GPi_3', np.arange(len(GPi_3))*25*millisecond, GPi_3)

    plt.draw()

# Run simulation for 1 second
run(time=10*second, dt=1*millisecond)
plt.ioff()
plt.savefig('Gurney_et_al_2001.pdf')
plt.show()
