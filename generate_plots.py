import matplotlib.pyplot as plt
import numpy as np
import os

dirname = os.path.dirname(__file__)


def generate_plot(test_name, x, y):
    plt.plot(x, y)
    plt.xlabel('Timestep')
    plt.ylabel('Fuel Demand [kg]')
    plt.title('Test %s Demand' % test_name)
    plt.axis([0, 15, min(y) - 1, max(y) + 1])
    fn = os.path.join(os.path.dirname(__file__),
                      './docs/do/images/%s' % test_name)
    plt.savefig(fn)


test_name = 'A-const-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 1
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-const-2'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 2
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-grow-1'
x = np.arange(0, 16, step=1)
y = 0.1 * x
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Power Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-decl-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y[0] = 1
y[1] = 1
y[2] = 1
plt.step(x, y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'A-decl-2'
x = np.arange(0, 16, step=1)
y = 2 - 0.1 * x
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.grid()
plt.close()


test_name = 'A-mix-1'
x = np.arange(0, 16, step=1)
y = 0.5 * x
y[7:] = 3 - 0.2 * (x[7:]-6)
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Fuel Demand [kg]')
plt.title('Test %s Fuel Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-const-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 1
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Power demand [GWe]')
plt.title('Test %s Power Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-grow-1'
x = np.arange(0, 16, step=1)
y = 0.1 * x
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Power demand [GWe]')
plt.title('Test %s Power Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-decl-1'
x = np.arange(0, 16, step=1)
y = 2 - 0.1 * x
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Power Demand')
plt.title('Test %s Power Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'B-mix-1'
x = np.arange(0, 16, step=1)
y = 0.5 * x
y[7:] = 3 - 0.2 * (x[7:]-6)
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Power demand [GWe]')
plt.title('Test %s Power Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()


test_name = 'C-const-1'
x = np.arange(0, 16, step=1)
y = np.zeros(16)
y = y + 1
plt.plot(x, y)
plt.xlabel('Timestep')
plt.ylabel('Power demand [GWe]')
plt.title('Test %s Power Demand' % test_name)
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()

test_name = 'C-const-1-waste'
x = np.arange(0, 16, step=1)
y = [1]
for time in x[1:]:
    prev_value = y[-1]
    # if time is a multiple of 7, which is when they decommission
    if time % 7 == 0:
        add = 3
    else:
        add = 1
    now_value = prev_value + add
    y.append(now_value)
plt.step(x, y)
plt.xlabel('Timestep')
plt.ylabel('Cumulative Waste Disposal Demand [kg]')
plt.title('Test %s Waste Disposal Demand' % test_name.replace('-waste', ''))
plt.axis([0, 15, min(y) - 1, max(y) + 1])
fn = os.path.join(os.path.dirname(__file__),
                  './docs/do/images/%s' % test_name)
plt.grid()
plt.savefig(fn)
plt.close()
