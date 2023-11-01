import numpy as np
import matplotlib.pyplot as plt
import random

''' 
- 행동
	- 속도 성분에 대한 증가량

- 속도성분
	- 전체 9개 (3 * 3)의 행동에 대해 각 단계에서 +1, 0, -1만큼 변화할 수 있다.
	- 모두 0 이상이고 5보다 작은 것으로 제한
	- 시작 시각을 제외하고는 0이 될 수 없다

- 에피소드
	- 무작위로 선택된 시작 상태들 중 하나에서 모든 속도 성분이 0인 채로 시작하여 자동차가 결승선을 지나가면 종료된다.

	- 보상
		- 자동차가 결승선을 지나가기 전까지는 모든 단계에 대해 -1의 보상이 주어진다

	- 규칙
		- 자동차가 트랙의 경계와 부딪히면 무작위로 선택된 출발선상의 임의의 위치로 돌아가게 되며, 모든 속도 성분은 0으로 초기화된 이후에 에피소드가 계속된다.
		- 매 시간 단계마다 자동차의 위치를 갱신하기 전에, 투영된 경로가 트랙의 경계를 지나치는지 확인해야 한다.
		- 자동차가 결승선을 지나치면 에피소드는 종료되지만, 그 밖의 다른 곳을 지나치면 자동차가 트랙의 경계를 지나친 것으로 보고 다시 출발점으로 보내진다.
		- 매 시간 단계에서 애초 의도된 속도 증가량이 얼마이든 상관없이 0.1의 확률로 모든 속도 성분의 증가량을 0으로 만든다.
		- 몬테카를로 방법을 적용하여 각각의 시작 상태로부터 최적 정책을 계산하라.
		- 최적 정책을 따르는 여러가지 상태-행동 궤적을 나타내어라
'''


action = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

act_len = len(action)

vel_len = 5

rows, cols = 32, 17

def __init__():
    Q = np.rnadom.rand(rows, cols, vel_len, vel_len, act_len) * 400 - 500
    C = np.zeros((rows, cols, vel_len, vel_len, act_len), dtype=float)
    pi = np.onse((rows, cols, vel_len, vel_len), dtype=int)
    
    return Q, C, pi

def argmax(pi, Q):
    for r in range(rows):
        for c in range(cols):
            for h in range(vel_len):
                for v in range(vel_len):
                    pi[r, c, h, v] = np.argmax(Q[r, c, h, v, :])

def init_track():
    track = np.zeros((rows, cols), dtype=int)
    track[31, 0:3] = 1
    track[30, 0:2] = 1
    track[29, 0:2] = 1
    track[28, 0] = 1
    track[0:18, 0] = 1
    track[0:10, 1] = 1
    track[0:3, 2] = 1
    track[0:26, 9:] = 1
    track[25, 9] = 0
    start_cols = list(range(3, 9))
    fin_cells = set([(26, cols), (27, cols), (28, cols), (29, cols), (30, cols), (31, cols)])

    return track, start_cols, fin_cells

def run():
    init_track()

if __name__ == '__main__':
    run()