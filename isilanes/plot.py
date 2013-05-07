# coding=utf8

import pylab

# Execution times (s):
times = {
        #'Jose en memoria' : {
        #      100 : 1.25,
        #     1000 : 9.46,
        #    },
        #'Jose v2' : {
        #      100 : 1.2,
        #     1000 : 9.1,
        #    },
        'Jose v3' : {
              100 :  11,
             1000 : 213,
            },
        'Inaki' : {
              100 :  12,
             1000 : 138,
            },
        #'Inaki con buffer (500)' : {
        #      100 :   2.54,
        #     1000 :  18.47,
        #    10000 : 268.8,
        #    },
        'Inaki buffer (5000c)' : {
              100 :   1.90,
             1000 :  18.17,
            10000 : 192.74,
            },
        'Inaki buffer2 (512L)' : {
              100 :   2.78,
             1000 :  13.62,
            10000 : 119.59,
            },
        }

# RES memory (MB):
mems = {
        #'Jose en memoria' : {
        #      100 :  77,
        #     1000 : 676,
        #    },
        #'Jose v2' : {
        #      100 :  50,
        #     1000 : 430,
        #    },
        'Jose v3' : {
              100 : 7.8,
             1000 : 8.2,
            },
        'Inaki' : {
              100 : 8.5,
             1000 : 8.5,
            },
        #'Inaki con buffer (500)' : {
        #      100 : 11,
        #     1000 : 12,
        #    10000 : 12,
        #    },
        'Inaki buffer (5000c)' : {
              100 : 22,
             1000 : 34,
            10000 : 34,
            },
        'Inaki buffer2 (512L)' : {
              100 : 22,
             1000 : 392,
            10000 : 387,
            },
        }

fig = pylab.figure(0, figsize=(12,8), dpi=100)

fig_time = fig.add_subplot(2,1,1)
for id,vals in sorted(times.items()):
    x = []
    y = []
    for nlines in sorted(vals):
        x.append(nlines)
        y.append(vals[nlines])
    fig_time.plot(x, y, 'o--', label=id)
    fig_time.set_ylabel('time (s)')
    fig_time.legend(prop={'size':12}, bbox_to_anchor=(1.0, 0.4))
    #fig_time.set_xscale('log')
    #fig_time.set_yscale('log')

fig_mem = fig.add_subplot(2,1,2)
for id,vals in sorted(mems.items()):
    x = []
    y = []
    for nlines in sorted(vals):
        x.append(nlines)
        y.append(vals[nlines])
    fig_mem.plot(x, y, 'o--', label=id)
    fig_mem.set_xlabel('#lines')
    fig_mem.set_ylabel('mem (MB)')
    fig_mem.legend(prop={'size':12}, bbox_to_anchor=(1.0, 0.5))
    #fig_mem.set_xscale('log')
    #fig_mem.set_yscale('log')

pylab.show()

'''
# Second plot:
x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

test100 = {}
test100['buffer2']  = [  11.69,  6.39,  4.16,  2.58,  2.01,  1.80,  1.79,  2.00,  2.05,  2.06 ]

test1000 = {}
test1000['buffer2'] = [ 150.09, 74.57, 45.00, 22.22, 15.99, 14.29, 15.95, 17.58, 23.80, 38.63 ]

test10000 = {}
test10000['buffer2'] = [ 0, 0, 446.28, 281.17, 196.33, 182.05, 174.15, 192.25, 252.16, 362.86 ]

pylab.figure(1, figsize=(12,8), dpi=100)
pylab.plot(x[2:-1], test100['buffer2'][2:-1], label='100L')
pylab.plot(x[2:-1], test1000['buffer2'][2:-1], label='1000L')
pylab.plot(x[2:-1], test10000['buffer2'][2:-1], label='10000L')
pylab.yscale('log')
pylab.legend()
pylab.show()
'''
