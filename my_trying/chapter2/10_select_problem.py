import matplotlib.pyplot as plt
import random
'''
10중 선택 문제
실제 보상값 R_t가 평균이 q(A_t)이고 분산이 1인 정규분포로부터 선택된다.
'''

def sample_average(times=1000, epsilon=0.1):

    q_action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    N_action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Q_action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    reward_list = []

    while times:

        for i in range(10): # q_a값 갱신, 비정상적 상황
            q_action[i] += random.normalvariate(mu=0, sigma=0.01)

        if random.random() < epsilon: # 탐험적 행동
            action = random.randint(0, 9)
            reward = random.normalvariate(mu=q_action[action], sigma=1)
            reward_list.append(reward)
            try: # N(a) > 0
                Q_action[action] = Q_action[action] + (reward - Q_action[action]) / N_action[action]
            except: # N(a) = 0
                Q_action[action] = reward
            N_action[action] += 1

        else: # 탐욕적 행동
            max_Q = max(Q_action)
            max_index = []
            
            for i in range(10): # Q_action의 최댓값 인덱스 찾기
                if Q_action[i] == max_Q:
                    max_index.append(i)

            if len(max_index) == 1: # 행동 선택하기
                action = max_index[0]
            else:
                action = max_index[random.randint(1, len(max_index)) - 1]

            reward = random.normalvariate(mu=q_action[action], sigma=1)
            reward_list.append(reward)
            try: # N(a) > 0
                Q_action[action] = Q_action[action] + (reward - Q_action[action]) / N_action[action]
            except: # N(a) = 0
                Q_action[action] = reward
            N_action[action] += 1

        times -= 1

    return reward_list
            
def weight_average(times=1000, epsilon=0.1, alpha=0.1):

    q_action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    N_action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Q_action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    reward_list = []

    while times:

        for i in range(10): # q_a값 갱신, 비정상적 상황
            q_action[i] += random.normalvariate(mu=0, sigma=0.01)

        if random.random() < epsilon: # 탐험적 행동
            action = random.randint(0, 9)
            reward = random.normalvariate(mu=q_action[action], sigma=1)
            reward_list.append(reward)
            try: # N(a) > 0
                Q_action[action] = Q_action[action] + alpha * (reward - Q_action[action])
            except: # N(a) = 0
                Q_action[action] = reward
            N_action[action] += 1

        else: # 탐욕적 행동
            max_Q = max(Q_action)
            max_index = []
            
            for i in range(10): # Q_action의 최댓값 인덱스 찾기
                if Q_action[i] == max_Q:
                    max_index.append(i)

            if len(max_index) == 1: # 행동 선택하기
                action = max_index[0]
            else:
                action = max_index[random.randint(1, len(max_index)) - 1]

            reward = random.normalvariate(mu=q_action[action], sigma=1)
            reward_list.append(reward)
            try: # N(a) > 0
                Q_action[action] = Q_action[action] + alpha * (reward - Q_action[action])
            except: # N(a) = 0
                Q_action[action] = reward
            N_action[action] += 1

        times -= 1

    return reward_list

def visualize(first, second):
    plt.plot(first, label='sample, e = 0.0')
    plt.plot(second, label='sample, e = 0.1')
    '''plt.plot(third, label='weight, e = 0.0')
    plt.plot(fourth, label='weight, e = 0.1')'''

    plt.xlabel('steps')
    plt.ylabel('avg reward')
    plt.legend()

    plt.show()

def averaging_result(sum_result_list):
    
    result = []
    length_first = len(sum_result_list)
    length_second = len(sum_result_list[0])

    for i in range(length_second):
        result.append(0)
    
    for i in range(length_second):
        for j in range(length_first):
            result[i] = sum_result_list[j][i]

    for i in range(len(result)):
        result[i] = result[i] / len(result)

    return result

def run1():

    sample_average_e_is_0 = []
    sample_average_e_is_01 = []
    weight_average_e_is_0 = []
    weight_average_e_is_01 = []

    for i in range(2000):
        sample_average_e_is_0.append(sample_average(epsilon=0.0))
        sample_average_e_is_01.append(sample_average(epsilon=0.1))
        weight_average_e_is_0.append(sample_average(epsilon=0.0))
        weight_average_e_is_01.append(sample_average(epsilon=0.1))

    sample_average_e_is_0 = averaging_result(sample_average_e_is_0)
    sample_average_e_is_01 = averaging_result(sample_average_e_is_01)
    weight_average_e_is_0 = averaging_result(weight_average_e_is_0)
    weight_average_e_is_01 = averaging_result(weight_average_e_is_01)

    visualize(first=sample_average_e_is_0, second=sample_average_e_is_01, third=weight_average_e_is_0, fourth=weight_average_e_is_01)

def run2():
    sample_average_e_is_01 = sample_average(times=10000)
    weight_average_e_is_01 = weight_average(times=10000)
    visualize(first=sample_average_e_is_01, second=weight_average_e_is_01)

if __name__ == '__main__':
    run2()