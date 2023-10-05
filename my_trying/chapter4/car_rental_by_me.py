from math import exp, factorial
import random

def init(): # 초기화
    state = [] # State [[A, B], [A, B] ...]
    value_s = [0 for i in range(441)] # V(s) 설정
    pi_s = [0 for i in range(441)] # pi(s) 설정

    for car_A in range(21): # 모든 상태 설정
        for car_B in range(21):
            state.append([car_A, car_B])

    return state, value_s, pi_s

def poisson(lam=4): # 푸아송 분포, 확률이 나온다
    poisson_list = [(lam ** n) * exp(-lam) / factorial(n) for n in range(21)]
    
    return poisson_list

def value_calc(state, s, a, value_s, gamma=0.9): # 시그마 어쩌구 값이 나온다
    result = 0
    car_A = s[0]
    car_B = s[1]
    poisson_list_A_rent = poisson(lam=3)
    poisson_list_A_return = poisson(lam=4)
    poisson_list_B_rent = poisson(lam=3)
    poisson_list_B_return = poisson(lam=2)

    for A_rent in range(21):
        for A_return in range(21):
            for B_rent in range(21):
                for B_return in range(21):
                    p = poisson_list_A_rent[A_rent] * poisson_list_A_return[A_return] * poisson_list_B_rent[B_rent] * poisson_list_B_return[B_return]
                    r = abs(a) * (-2) + (min(A_rent, car_A - a) + min(B_rent, car_B - a)) * 10

                    if (car_A < a) or (car_B + a < 0): # action을 취할 수 없는 상태
                        break
                    else: # action을 취할 수 있는 상태
                        if car_A - a - A_rent + A_return < 0 or car_B + a - B_rent + B_return < 0:
                            break
                        else:
                            s_ = [car_A - a - A_rent + A_return, car_B + a - B_rent + B_return]
                            for i in range(2): # 차가 20개 초과 되었을 때
                                if s_[i] > 20:
                                    s_[i] = 20

                    index_s_ = state.index(s_)
                    result += p * (r + gamma * value_s[index_s_])

    return result

def argmax(state, s, value_s): # 최적의 a값 반환

    result_list = []
    
    for a in range(-5, 1, 6):
        result_list.append(value_calc(state, s, a, value_s))

    result_max_index = result_list.index(max(result_list)) - 5
    return result_max_index

def policy_evaluate(state, value_s, pi_s, theta=0.1): # 정책 평가 value_s, pi_s 반환

    times = 1
    _ = theta + 1

    while _ > theta:
        print(f'delta = {_}, times = {times}\npi_s = {pi_s}\nvalue_s = {value_s}')
        _ = 0

        for s in state: # 모든 상태에 대해서 반복
            index_s = state.index(s)
            v = value_s[index_s]
            value_s[index_s] = value_calc(state, s, pi_s[index_s], value_s)
            _ = max(_, abs(v - value_s[index_s]))
        times += 1

    return value_s, pi_s

def policy_improve():

    pi_s_list = []
    dummy = init()
    state = dummy[0]
    value_s = dummy[1]
    pi_s = dummy[2]

    while True:
        print('gogogo')
        policy_evaluate_result = policy_evaluate(state, value_s, pi_s)

        value_s = policy_evaluate_result[0]
        pi_s = policy_evaluate_result[1]

        stable_policy = True

        for s in state:
            index_s = state.index(s)
            action_before = pi_s[index_s]
            pi_s[index_s] = argmax(state, s, value_s)
            if action_before != pi_s[index_s]:
                stable_policy = False
        
        if stable_policy:
            return pi_s_list, pi_s
        else:
            pi_s_list.append(pi_s)
        
if __name__ == '__main__':
    print(policy_improve())





