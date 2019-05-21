import matplotlib.pyplot as plt
import h5py
import numpy as np
import matplotlib
import math

# adver_sample_query_file = '32_adver_img_query_500/32_adver_img_query_500.h5'
# query = h5py.File(adver_sample_query_file)
#
# query_L = query['AdvLab'][:]
# query_x = query['AdvImg'][:]
# query_y = query['AdvTag'][:]
#
#
# #
# # plt.subplot(3, 2, 1)
# # plt.plot(range(0,1380), query_y[52,:])
# # plt.subplot(3, 2, 2)
# # plt.plot(range(0,1380), query_y[268,:])
# # plt.subplot(3, 2, 3)
# # plt.plot(range(0,1380), query_y[398,:])
# # plt.subplot(3, 2, 4)
# # plt.plot(range(0,1380), query_y[546,:])
# # plt.subplot(3, 2, 5)
# # plt.plot(range(0,1380), query_y[653,:])
# # plt.subplot(3, 2, 6)
# plt.plot(range(0,1380), query_y[925,:])
# plt.show()


# 1
x = [1,2,3,4]
y = [1.2,2.7,4.5,6.9]
plt.plot(x, y)
plt.show()

# 2
plt.plot(x, y, color="r", linestyle="--", marker="*", linewidth=1.0)
plt.show()

# 3
x = np.arange(-5, 5, 0.02)
y = np.sin(x)
plt.axis([-np.pi, np.pi, -2, 2])
plt.plot(x, y, color="r", linestyle="-", linewidth=1)
plt.show()

# 4
x = np.arange(-2 * math.pi, 2 * math.pi, 0.02)
y = np.sin(x)
plt.axis([-10, 10, -2, 2])
plt.xticks([i * np.pi/2 for i in range(-4, 5)], [str(i * 0.5) + "$\pi$" for i in range(-4, 5)])
plt.yticks([i * 0.5 for i in range(-4, 5)])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, color="r", linestyle="-", linewidth=1)
plt.show()

# 5
x = np.arange(-1, 1, 0.1)
y1 = np.exp(x)
y2 = np.exp(2 * x)
plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 6
x = np.arange(-1, 1, 0.1)

y1 = np.exp(x)
y2 = np.exp(2 * x)
y3 = np.exp(1.5 * x)

plt.figure(1)
plt.subplot(1, 2, 1)
plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)

plt.xlabel("x")
plt.ylabel("y1")

plt.figure(2)
plt.plot(x, y2, color="k", linestyle="-", marker="s", linewidth=1)

plt.xlabel("x")
plt.ylabel("y2")

plt.figure(1)
plt.subplot(1, 2, 2)
plt.plot(x, y3, color="b", linestyle="-", marker="v", linewidth=1)

plt.xlabel("x")
plt.ylabel("y3")

plt.show()


# 7

x = np.arange(-1, 1, 0.1)

y1 = np.exp(x)
y2 = np.exp(2 * x)

plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1, label="y1")
plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1, label="y2")

plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))

plt.title("Figure 1")

plt.show()

# 8
x = np.arange(-1, 1, 0.1)

y = [2 * i for i in x]

plt.plot(x, y, color="r", linestyle="-", marker="^", linewidth=1)

plt.grid(color="k", linestyle=":")
plt.show()

# 9
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.1)

y1 = np.exp(x)
y2 = np.exp(2 * x)

plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

# plt.text(-0.5, 3, "exp functions", fontsize=10)
plt.annotate('A', xy=(0, 1), xytext=(-0.5, 2.5), arrowprops=dict(facecolor='k', headwidth=10, width=2))
plt.show()