import matplotlib.pyplot as plt
# num_party = range(2, 9)
#
# glob_data = [177.083, 531.003, 1061.76, 1769.36, 2653.8, 3715.08, 4953.19]
#
# data_send = [88.5414, 177.083, 265.625, 354.167, 442.71, 531.253, 619.796]
#
# delay = [1.60504, 2.29217, 4.01555, 5.78745, 9.27596, 13.1339, 18.9638]
#
# plt.figure(figsize=(20,10))
# plt.subplot(1,3,1)
# plt.plot(num_party, glob_data)
# plt.subplot(1,3,2)
#
# plt.plot(num_party, data_send)
# plt.subplot(1,3,3)
#
# plt.plot(num_party, delay)
# plt.show()
#
# glob = [6111.44, 7278.64, 9613.05, 15437.9, 27087.5, ]
# data = [764.578, 910.479, 1202.28, 1930.39, 3386.6, ]
# time = [39.3272, 69.1549, 130.92, 254.596, ]
# mpc_time = []
#
# # 10000
#
#
#
# size_len = [10000,20000,40000,80000,160000]
# glob = [4953.19,6118.16,8448.09,13107.9]
# data = [619.796,765.418,1056.66,1639.14]
# time = [19.6794,32.7911,58.3617,107.661]
# mpc_time = [6.32799,6.25578,6.30273,6.15904,6.12756]

import numpy as np
# from tdqm import tqdm

# data gen script
for i in (range(8)):
    a = sorted(np.random.random(int(262144)) * 1000)
    with open('./mp-spdz-0.2.0/Player-Data/Input-P'+str(i)+'-0', 'w') as fd:
        for num in a:
            # print(num)
            fd.write(str(num)+' ')
        fd.write('\n')



size_party = 2
size_len = int(262144/2)
data = np.empty((size_party, size_len))
for i in range(size_party):
    with open('./mp-spdz-0.2.0/Player-Data/Input-P'+str(i)+'-0', 'r') as fd:
        for line in fd:
            reals = line.split()
            for j in range(size_len):
                data[i][j] = reals[j]
            break

# weight_total = sum(data[0])
# print(weight_total)
# result = sum(sum(data[p][n] * data[0][n] for n in range(size_len)) for p in
#              range(size_party)) / weight_total / (size_party-1)
# print('weighted avg of first ', size_party, 'x', size_len, ' = ', result)

all = []
for i in range(size_party):
    all.append(data[i])
    print(sum(data[i]))
print(size_party, ' x ', size_len, np.median(all))



# n_party = [2**i for i in range(3,11)]
#
# mpc_t = [6.08736,
# 8.93649,
# 15.2222,
# 27.3375,
# 51.6139,
# 100.539,
# 200.488,397.547]
#
# glob_d = [4021.43,
# 5825.58,
# 9433.88,
# 16650.5,
# 31985.5,
# 61302.9,
# 121290 ,239913]
#
# sent_d = [
# 805.187,
# 1166.48,
# 1889.07,
# 3334.26,
# 6405.13,
# 12276.2,
# 24289 ,48043.9]
# plt.figure(figsize=(15,5))
# plt.subplot(1,2,1)
# plt.plot(n_party, mpc_t)
# plt.scatter(n_party, mpc_t)
# plt.xlabel('data size in each player')
# plt.ylabel('MPC time for weighted average/s')
# plt.subplot(1,2,2)
#
# plt.plot(n_party, np.array(sent_d)/1024)
# plt.scatter(n_party, np.array(sent_d)/1024)
# plt.ylabel('Data sent from each player/GB')
# plt.xlabel('data size in each player')
# plt.suptitle('weighted average computation of 4 player in different data size')
# plt.show()
# plt.subplot(1,3,3)
#
# plt.plot(n_party, sent_d)
# plt.scatter(n_party, sent_d)
# plt.ylabel('MPC time for weighted average/s')


'''
8
weighted avg 494.246
Stopped timer 1 at 6.08736
Time = 7.7849 seconds 
Time1 = 6.08736 seconds 
Data sent = 805.187 MB
Global data sent = 4021.43 MB

16
weighted avg 478.819
Stopped timer 1 at 8.93649
Time = 10.6268 seconds 
Time1 = 8.93649 seconds 
Data sent = 1166.48 MB
Global data sent = 5825.58 MB

32
weighted avg 468.011
Stopped timer 1 at 15.2222
Time = 16.9798 seconds 
Time1 = 15.2222 seconds 
Data sent = 1889.07 MB
Global data sent = 9433.88 MB

64
weighted avg 478.886
Stopped timer 1 at 27.3375
Time = 29.1817 seconds 
Time1 = 27.3375 seconds 
Data sent = 3334.26 MB
Global data sent = 16650.5 MB

128
weighted avg 470.856
Stopped timer 1 at 51.6139
Time = 53.4858 seconds 
Time1 = 51.6139 seconds 
Data sent = 6405.13 MB
Global data sent = 31985.5 MB

256
weighted avg 487.645
Stopped timer 1 at 100.539
Time = 102.482 seconds 
Time1 = 100.539 seconds 
Data sent = 12276.2 MB
Global data sent = 61302.9 MB

512
Starting timer 1 at 0 after 5.131e-06
weighted avg 503.809
Stopped timer 1 at 200.488
Time = 202.393 seconds 
Time1 = 200.488 seconds 
Data sent = 24289 MB
Global data sent = 121290 MB

1024
weighted avg 499.297
Stopped timer 1 at 397.547
Time = 399.492 seconds 
Time1 = 397.547 seconds 
Data sent = 48043.9 MB
Global data sent = 239913 MB

'''



'''
3
weighted avg 489.341
Stopped timer 1 at 28.4971
Time = 29.3333 seconds 
Time1 = 28.4971 seconds 
Data sent = 3789.67 MB
Global data sent = 11361.1 MB

4
weighted avg 491.8
Stopped timer 1 at 55.9757
Time = 57.2642 seconds 
Time1 = 55.9757 seconds 
Data sent = 7445.83 MB
Global data sent = 29751.9 MB

5
weighted avg 487.645
Stopped timer 1 at 100.539
Time = 102.482 seconds 
Time1 = 100.539 seconds 
Data sent = 12276.2 MB
Global data sent = 61302.9 MB

6
weighted avg 490.99
Stopped timer 1 at 173.758
Time = 176.244 seconds 
Time1 = 173.758 seconds 
Data sent = 18393.5 MB
Global data sent = 110205 MB

7
weighted avg 492.027
Stopped timer 1 at 275.998
Time = 279.267 seconds 
Time1 = 275.998 seconds 
Data sent = 25594.8 MB
Global data sent = 178893 MB

8
weighted avg 492.245
Stopped timer 1 at 422.278
Time = 426.271 seconds 
Time1 = 422.278 seconds 
Data sent = 34128.4 MB
Global data sent = 272593 MB
'''

n_party=range(2,8)
mpc_t = [28.4971,
55.9757,
100.539,
173.758,
275.998,
422.278]

# glob_d = []

sent_d = [3789.67,
7445.83,
12276.2,
18393.5,
25594.8,
34128.4]

# plt.figure(figsize=(15,5))
# plt.subplot(1,2,1)
# plt.plot(n_party, mpc_t)
# plt.scatter(n_party, mpc_t)
# plt.xlabel('number of player')
# plt.ylabel('MPC time for weighted average/s')
# plt.subplot(1,2,2)
#
# plt.plot(n_party, np.array(sent_d)/1024)
# plt.scatter(n_party, np.array(sent_d)/1024)
# plt.ylabel('Data sent from each player/GB')
# plt.xlabel('number of player')
# plt.suptitle('weighted average computation of different number of parties')
# plt.show()


'''
2**18
50%-rank = 499.463
Stopped timer 1 at 1.83037
Time = 14.4987 seconds 
Time1 = 1.83037 seconds 
Data sent = 719.598 MB
Global data sent = 1439.2 MB

2**17
50%-rank = 498.003
Stopped timer 1 at 1.90382
Time = 8.67982 seconds 
Time1 = 1.90382 seconds 
Data sent = 449.147 MB
Global data sent = 898.294 MB


Starting timer 1 at 0 after 5.826e-06
50%-rank = 0.031311
Stopped timer 1 at 0.838221
Time = 1.34438 seconds 
Time1 = 0.838221 seconds 
Data sent = 88.3922 MB
Global data sent = 176.784 MB

Starting timer 1 at 0 after 5.58e-06
50%-rank = 0.0540009
Stopped timer 1 at 0.843049
Time = 1.34746 seconds 
Time1 = 0.843049 seconds 
Data sent = 88.3959 MB
Global data sent = 176.792 MB

50%-rank = 0.0910339
Stopped timer 1 at 0.847688
Time = 1.35676 seconds 
Time1 = 0.847688 seconds 
Data sent = 88.3997 MB
Global data sent = 176.799 MB


50%-rank = 0.266129
Stopped timer 1 at 1.42316
Time = 1.93178 seconds 
Time1 = 1.42316 seconds 
Data sent = 133.537 MB
Global data sent = 267.074 MB

50%-rank = 0.533188
Stopped timer 1 at 1.43492
Time = 1.95393 seconds 
Time1 = 1.43492 seconds 
Data sent = 133.543 MB
Global data sent = 267.086 MB

Starting timer 1 at 0 after 4.829e-06
50%-rank = 1.99196
Stopped timer 1 at 1.36972
Time = 1.87717 seconds 
Time1 = 1.36972 seconds 
Data sent = 133.562 MB
Global data sent = 267.125 MB




18
Time = 14.8599 seconds 
Time1 = 1.90256 seconds 
Data sent = 719.598 MB
Global data sent = 1439.2 MB

17
Time = 8.64919 seconds 
Time1 = 1.91533 seconds 
Data sent = 449.147 MB
Global data sent = 898.294 MB

16
50%-rank = 124.906
Stopped timer 1 at 1.91095
Time = 5.33261 seconds 
Time1 = 1.91095 seconds 
Data sent = 303.599 MB
Global data sent = 607.197 MB

15
50%-rank = 62.729
Stopped timer 1 at 1.65681
Time = 3.62204 seconds 
Time1 = 1.65681 seconds 
Data sent = 218.595 MB
Global data sent = 437.191 MB

14
50%-rank = 31.3938
Stopped timer 1 at 1.6262
Time = 2.62195 seconds 
Time1 = 1.6262 seconds 
Data sent = 177.045 MB
Global data sent = 354.09 MB

'''
n_party = [2**i for i in range(14, 19)]
mpc_t = [1.6262,1.65681,1.91095,1.91533,1.90256]
sent_d = [177.045,218.595,303.599,449.147,719.598]
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.plot(n_party, mpc_t)
plt.scatter(n_party, mpc_t)
plt.xlabel('number of player')
plt.ylabel('MPC time for weighted average/s')
plt.subplot(1,2,2)

plt.plot(n_party, np.array(sent_d)/1024)
plt.scatter(n_party, np.array(sent_d)/1024)
plt.ylabel('Data sent from each player/GB')
plt.xlabel('number of player')
plt.suptitle('weighted average computation of different number of parties')
plt.show()