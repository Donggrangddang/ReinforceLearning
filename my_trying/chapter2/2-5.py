import numpy as np
import matplotlib.pyplot as plt
import random

def visualize(number1, number2, number3, number4):
    plt.plot(number1, label='sample_average, e = 0.0')
    plt.plot(number2, label='sample_average, e = 0.1')
    plt.plot(number3, label='constant_average, e = 0.0')
    plt.plot(number4, label='constant_average, e = 0.1')

    plt.xlabel('steps')
    plt.ylabel('avg reward')
    plt.legend()
    
    plt.show()

def sample_average(q_a, times=2000, epsilon=0.0, time_level=10000):
    number = random.random()
    N_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Q_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    reward = []
    result_Q_a = []

    for k in range(time_level):
        print(k)
        q_a += random.normalvariate(mu=0, sigma=0.01)

        for i in range(times):

            for j in range(10): # 보상 분포
                reward.append(random.normalvariate(mu=q_a, sigma=1))

            if number < epsilon: # 무작위적 행동
                action = random.randint(0, 9)
                if N_times[action] == 0:
                    Q_a[action] = reward[action]
                else:
                    Q_a[action] = Q_a[action] + (reward[action] - Q_a[action]) / N_times[action]
            else: # 탐욕적 행동
                max_Q = max(Q_a)
                if Q_a.count(max_Q) == 1: # 추정값이 같은게 존재 x
                    action = Q_a.index(max_Q)
                    if N_times[action] == 0:
                        Q_a[action] = reward[action]
                    else:
                        Q_a[action] = Q_a[action] + (reward[action] - Q_a[action]) / N_times[action]
                else: # 추정값이 같은게 존재
                    index = [r for r, value in enumerate(Q_a) if value == max_Q]
                    action = index[random.randint(0, len(index) - 1)]
                    if N_times[action] == 0:
                        Q_a[action] = reward[action]
                    else:
                        Q_a[action] = Q_a[action] + (reward[action] - Q_a[action]) / N_times[action]
                        
            N_times[action] += 1

        result_Q_a.append(Q_a)

    return result_Q_a
                
def constant_average(q_a, times=2000, epsilon=0.0, time_level=10000, alpha=0.1):
    number = random.random()
    N_times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Q_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    reward = []
    result_Q_a = []

    for k in range(time_level):
        print(k)
        q_a += random.normalvariate(mu=0, sigma=0.01)

        for i in range(times):

            for j in range(10): # 보상 분포
                reward.append(random.normalvariate(mu=q_a, sigma=1))

            if number < epsilon: # 무작위적 행동
                action = random.randint(0, 9)
                Q_a[action] = Q_a[action] + alpha * (reward[action] - Q_a[action])
                N_times[action] += 1
            else: # 탐욕적 행동
                max_Q = max(Q_a)
                if Q_a.count(max_Q) == 1: # 추정값이 같은게 존재 x
                    action = Q_a.index(max_Q)
                    Q_a[action] = Q_a[action] + alpha * (reward[action] - Q_a[action])
                    N_times[action] += 1
                else: # 추정값이 같은게 존재
                    index = [r for r, value in enumerate(Q_a) if value == max_Q]
                    action = index[random.randint(0, len(index) - 1)]
                    Q_a[action] = Q_a[action] + alpha * (reward[action] - Q_a[action])
                    N_times[action] += 1

        result_Q_a.append(sum(Q_a) / 10)

    return result_Q_a

def run():

    q_a = 0.5

    number1 = sample_average(q_a=q_a, times=2000, epsilon=0, time_level=10000)
    number2 = sample_average(q_a=q_a, times=2000, epsilon=0.1, time_level=10000)
    number3 = constant_average(q_a=q_a, times=2000, epsilon=0, time_level=10000)
    number4 = constant_average(q_a=q_a, times=2000, epsilon=0.1, time_level=10000)

    visualize(number1, number2, number3, number4)

if __name__ == '__main__':
    run()