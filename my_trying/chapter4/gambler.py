import numpy as np
import matplotlib.pyplot as plt
import csv

'''
상태 : 도박사가 보유한 자금의 액수 1 ~ 99
행동 : 내기에 거는 돈의 액수 0 ~ 가능한 돈
ph = 동전의 앞면이 나올 확률
보상 -> 돈이 늘어나면 : +1, else : 0
앞면이 나오면 : 자기가 건만큼 돈을 얻음
뒷면 : 돈을 잃음
정책 : 보유한 자금의 액수와 도박사가 내거는 돈의 액수 사이의 관계를 규정
최적 정책 : 도박사가 목표에 도달할 확률을 최대로 만듬
'''

STATE = [i for i in range(1, 100)]
REWARD_SUCCESS = 1
REWARD_FAILED = 0
REWARD = [REWARD_SUCCESS, REWARD_FAILED]

def calc_value(ph=0.4, s=None, value_list=None):
    # @ph : 동전의 앞면이 나올 확률
    # @s : 현재 상태
    # @gamma : 할인률
    # @value_list : 현재 계산된 모든 상태에 대한 value값 리스트
 
    max_value_list = []
    action = [i for i in range(0, min(s, 100 - s) + 1)]
    
    for a in action:
        success_value = ph * (value_list[s + a])
        fail_value = (1 - ph) * (value_list[s - a])
        max_value_list.append(success_value + fail_value)
    
    return max(max_value_list)

def calc_policy(value_list=None, ph=0.4):
    # @value_list : 현재 계산된 모든 상태에 대한 value값 리스트
    # @gamma : 할인률

    argmax_action_list = []
    
    for s in STATE:
        argmax_value_list = []
        action_list = [i for i in range(0, min(s, 100 - s) + 1)]
        for a in action_list:
            success_value = ph * (value_list[s + a])
            fail_value = (1 - ph) * (value_list[s - a])
            argmax_value_list.append(success_value + fail_value)
        index = argmax_value_list.index(max(argmax_value_list))
        argmax_action_list.append(action_list[index])

    return argmax_action_list

def value_repeat(theta=0.000001, ph=0.4, times=1000000, file_name=None):
    # @value_list = [0(0개), ..., 1(100개)]
    
    _ = 10 * theta
    value_list = [0 for i in range(100)]
    value_list.append(1)

    value_list_all = []

    for i in range(1, times + 1):
        while _ > theta:
            _ = 0
            for s in STATE: # s : 1 ~ 99
                v = value_list[s]
                value_list[s] = calc_value(ph=ph, s=s, value_list=value_list)
                _ = max(_, abs(v - value_list[s]))
        value_list_all.append(value_list)

    policy_list = calc_policy(value_list=value_list, ph=ph)

    f = open(f'C:/Codes/python/ReinforceLearning/my_trying/chapter4/csv/value_{file_name}.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerows(value_list_all)
    f.close()

    g = open(f'C:/Codes/python/ReinforceLearning/my_trying/chapter4/csv/policy_{file_name}.csv', 'w', newline='')
    writer = csv.writer(g)
    writer.writerow(policy_list)
    g.close()
        
def run():
    value_repeat(theta=0.000001, ph=0.25, times=100, file_name=0.25)
    value_repeat(theta=0.000001, ph=0.4, times=100, file_name=0.4)
    value_repeat(theta=0.000001, ph=0.55, times=100, file_name=0.55)


if __name__ == '__main__':
    run()

