from __future__ import division

import imp
import os

from pyrl          import utils
from pyrl.figtools import Figure

#=========================================================================================
# Files
#=========================================================================================

here   = utils.get_here(__file__)
parent = utils.get_parent(here)

# Paths
scratchpath = os.environ.get('SCRATCH')
if scratchpath is None:
    scratchpath = os.path.join(os.environ['HOME'], 'scratch')
trialspath   = os.path.join(scratchpath, 'work', 'pyrl')
analysispath = os.path.join(parent, 'examples', 'analysis')
modelspath   = os.path.join(parent, 'examples', 'models')

# analysis/rdm
rdm_analysisfile = os.path.join(analysispath, 'rdm.py')
rdm_analysis     = imp.load_source('rdm_analysis', rdm_analysisfile)

# analysis/mante
mante_analysisfile = os.path.join(analysispath, 'mante.py')
mante_analysis     = imp.load_source('mante_analysis', mante_analysisfile)

# analysis/multisensory
multisensory_analysisfile = os.path.join(analysispath, 'multisensory.py')
multisensory_analysis     = imp.load_source('multisensory_analysis',
                                            multisensory_analysisfile)

# analysis/romo
romo_analysisfile = os.path.join(analysispath, 'romo.py')
romo_analysis     = imp.load_source('romo_analysis',romo_analysisfile)

# models/mante
mante_modelfile  = os.path.join(modelspath, 'mante.py')
mante_model      = imp.load_source('mante_model', mante_modelfile)
mante_behavior   = os.path.join(trialspath, 'mante', 'trials_behavior.pkl')
mante_activity   = os.path.join(trialspath, 'mante', 'trials_activity.pkl')

# models/multisensory
multisensory_modelfile = os.path.join(modelspath, 'multisensory.py')
multisensory_model     = imp.load_source('multisensory_model', multisensory_modelfile)
multisensory_behavior  = os.path.join(trialspath, 'multisensory', 'trials_behavior.pkl')
multisensory_activity  = os.path.join(trialspath, 'multisensory', 'trials_activity.pkl')

# models/romo
romo_modelfile = os.path.join(modelspath, 'romo.py')
romo_model     = imp.load_source('romo_model', romo_modelfile)
romo_behavior  = os.path.join(trialspath, 'romo', 'trials_behavior.pkl')
romo_activity  = os.path.join(trialspath, 'romo', 'trials_activity.pkl')

#=========================================================================================
# Figure setup
#=========================================================================================

w   = utils.mm_to_inch(174)
r   = 0.97
fig = Figure(w=w, r=r, axislabelsize=9, labelpadx=4, labelpady=6,
             thickness=0.8, ticksize=3, ticklabelsize=7.5, ticklabelpad=2)

w_behavior = 0.19
h_behavior = 0.15

w_activity = 0.16
h_activity = h_behavior

xleft = 0.1
ybot  = 0.06
DX    = 0.09
dx    = 0.06
dy    = 0.08
DY    = 0.08

fig.add('romo-behavior', [xleft, ybot, w_behavior, w_behavior/r])
fig.add('ms-behavior', [xleft, fig['romo-behavior'].top+DY, w_behavior, h_behavior])
fig.add('mante-c', [xleft, fig['ms-behavior'].top+DY, w_behavior, h_behavior])
fig.add('mante-m', [xleft, fig['mante-c'].top+dy, w_behavior, h_behavior])

w_mante = 0.1
h_mante = 0.07

pad_mante = 0.07
x0_mante  = fig['mante-m'].right + DX + pad_mante
y0_mante  = fig['mante-m'].top - h_mante
dx_mante  = (3*w_activity+2*dx - pad_mante - 4*w_mante)/3
dy_mante  = (2*h_behavior+DY - 4*h_mante)/3

fig.add('mante-choice-0',         [x0_mante, y0_mante, w_mante, h_mante])
fig.add('mante-motion-choice-0',  [x0_mante, fig['mante-choice-0'].y-dy_mante-h_mante, w_mante, h_mante])
fig.add('mante-color-choice-0',   [x0_mante, fig['mante-motion-choice-0'].y-dy_mante-h_mante, w_mante, h_mante])
fig.add('mante-context-choice-0', [x0_mante, fig['mante-color-choice-0'].y-dy_mante-h_mante, w_mante, h_mante])
for i in xrange(1, 4):
    fig.add('mante-choice-{}'.format(i),         [fig['mante-choice-{}'.format(i-1)].right+dx_mante, fig['mante-choice-0'].y, w_mante, h_mante])
    fig.add('mante-motion-choice-{}'.format(i),  [fig['mante-choice-{}'.format(i-1)].right+dx_mante, fig['mante-motion-choice-0'].y, w_mante, h_mante])
    fig.add('mante-color-choice-{}'.format(i),   [fig['mante-choice-{}'.format(i-1)].right+dx_mante, fig['mante-color-choice-0'].y, w_mante, h_mante])
    fig.add('mante-context-choice-{}'.format(i), [fig['mante-choice-{}'.format(i-1)].right+dx_mante, fig['mante-context-choice-0'].y, w_mante, h_mante])

fig.add('ms-0', [fig['ms-behavior'].right+DX, fig['ms-behavior'].y, w_activity, h_activity])
fig.add('ms-1', [fig['ms-0'].right+dx, fig['ms-behavior'].y, w_activity, h_activity])
fig.add('ms-2', [fig['ms-1'].right+dx, fig['ms-behavior'].y, w_activity, h_activity])

fig.add('romo-0', [fig['romo-behavior'].right+DX, fig['romo-behavior'].y, w_activity, h_activity])
fig.add('romo-1', [fig['romo-0'].right+dx, fig['romo-behavior'].y, w_activity, h_activity])
fig.add('romo-2', [fig['romo-1'].right+dx, fig['romo-behavior'].y, w_activity, h_activity])

#=========================================================================================
# Annotations
#=========================================================================================

plot = fig['mante-m']
plot.text_upper_center(r'\textbf{Behavior}', fontsize=9.5, dy=0.13)
plot.text_upper_center(r'\textbf{Neural activity}', fontsize=9.5, dx=2.5, dy=0.13)

#=========================================================================================

kwargs = dict(ms=5, lw=1)
mante_analysis.psychometric(mante_behavior, {'m': fig['mante-m'], 'c': fig['mante-c']},
                            **kwargs)

plot = fig['mante-m']
plot.xlabel('Percent motion coherence')
plot.ylabel('Percent right choices')

plot = fig['mante-c']
plot.xlabel('Percent color coherence')

#=========================================================================================

units     = [7, 10, 17, 43]
all_plots = []
for i in xrange(len(units)):
    plots = {
        'choice':         fig['mante-choice-'+str(i)],
        'motion-choice':  fig['mante-motion-choice-'+str(i)],
        'color-choice':   fig['mante-color-choice-'+str(i)],
        'context-choice': fig['mante-context-choice-'+str(i)]
        }
    all_plots.append(plots)

tmin, tmax = 0, 750
mante_analysis.sort(mante_activity, all_plots, units=units, tmin=tmin, tmax=tmax)

for plots in all_plots:
    for plot in plots.values():
        plot.xticks([tmin, tmax])
        plot.xticklabels()
        plot.xlim(tmin, tmax)

# Time axis
plot = fig['mante-context-choice-0']
plot.xticks([tmin, tmax])
plot.xticklabels([tmin, tmax])
plot.xlim(tmin, tmax)
plot.xlabel('Time (ms)')

# Rate axis
lims = {
    'choice':         5,
    'motion-choice':  6,
    'color-choice':   6,
    'context-choice': 5
    }

for k, v in lims.items():
    for i in xrange(len(units)):
        plot = fig['mante-{}-{}'.format(k, i)]
        plot.yticks([0, v])
        plot.ylim(0, v)

def custom_axislabel(name, s1, s2, color2='k'):
    plot = fig[name]
    plot.text(-0.8, 0.5+0.13, s1, ha='center', va='center', fontsize=7,
              transform=plot.transAxes)
    plot.text(-0.8, 0.5-0.13, s2, ha='center', va='center', fontsize=7, color=color2,
              transform=plot.transAxes)

custom_axislabel('mante-choice-0', 'choice', r'\textit{all trials}')
custom_axislabel('mante-motion-choice-0', 'motion \& choice', r'\textbf{motion context}',
                 'k')
custom_axislabel('mante-color-choice-0', 'color \& choice', r'\textbf{color context}',
                 Figure.colors('darkblue'))
custom_axislabel('mante-context-choice-0', 'context \& choice', r'\textit{all trials}')

#=========================================================================================

plot = fig['ms-behavior']

kwargs = dict(ms=5, lw=1)
multisensory_analysis.psychometric(multisensory_behavior, fig['ms-behavior'], **kwargs)

plot.xlabel('Rate (events/s)')
plot.ylabel('Percent high choices')

#=========================================================================================

kwargs = {}

units = [17, 6, 14]
plots = [fig['ms-'+str(i)] for i in xrange(len(units))]
multisensory_analysis.sort(multisensory_activity, plots, units=units)

for p in ['ms-0', 'ms-1', 'ms-2']:
    plot = fig[p]
    plot.xticks([-300, 0, 1000])
    plot.xlim(-300, 1000)

plot = fig['ms-0']
plot.xlabel('Time from stimulus onset (ms)')

#=========================================================================================

kwargs = dict(r=2.2, fontsize=6.5, lw=0.8)
romo_analysis.performance(romo_behavior, fig['romo-behavior'], **kwargs)

plot = fig['romo-behavior']
plot.xlabel('$f_1$ (Hz)')
plot.ylabel('$f_2$ (Hz)')

#=========================================================================================

kwargs = {}

units = [0, 15, 18]
plots = [fig['romo-'+str(i)] for i in xrange(len(units))]
romo_analysis.sort(romo_activity, plots, units=units)

for p in ['romo-0', 'romo-1', 'romo-2']:
    plot = fig[p]
    plot.xticks([0, 1, 2, 3, 4])
    plot.xlim(-0.5, 4)

plot = fig['romo-0']
plot.xlabel('Time from $f_1$ onset (sec)')
plot.ylabel('Firing rate (a.u.)')

#=========================================================================================

fig.save()
