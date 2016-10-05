import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import thread
import random
import sys


def measuare():
    current = list()
    voltage = list()
    power = list()
    set_current_array = np.linspace(0, 0.020, 550)
    for i in range(0, len(set_current_array)):
        current.append(set_current_array[i])
        voltage.append(2*set_current_array[i])
        power.append(set_current_array[i]**2)
        J = np.array(current, dtype=float)
        V = np.array(voltage, dtype=float)
        L = np.array(power, dtype=float)
        np.savetxt('data.txt', zip(J, V, L), fmt='%1.12e', header=' J [A] \t V \t L [w] ')
        time.sleep(0.1)


def real_time_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()
    def animate(*args):
        try:
            current, voltage, power = np.loadtxt("data.txt", unpack=True, skiprows=1)
            ax1.clear()
            ax2.clear()
            ax1.plot(current, voltage, 'bo')
            ax2.plot(current, power, 'ro')
            ax1.set_xlabel("J [A]")
            plt.grid(True)
        except Exception:
            pass

    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()


try:
    thread.start_new_thread(measuare, ())
except:
    print("Error, unable to start thread")

time.sleep(4)
real_time_plot()
start = time.time()
while 1:
    end = time.time()
    if end-start > 20:
        print(end)
        sys.exit(0)