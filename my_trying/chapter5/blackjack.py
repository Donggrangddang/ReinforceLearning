import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

ACTION_HIT = 1 # 한 장 더받음
ACTION_STAND = 0 # 더 안받음
ACTIONS = [ACTION_HIT, ACTION_STAND]

# 플레이어의 정책
POLICY_PLAYER = np.zeros(22, dtype=int)
for i in range(12, 20):
    POLICY_PLAYER[i] = ACTION_HIT
POLICY_PLAYER[20] = ACTION_STAND
POLICY_PLAYER[21] = ACTION_HIT

# 딜러의 정책
POLICY_DEALER = np.zeros(22, dtype=int)
for i in range(12, 17):
    POLICY_DEALER[i] = ACTION_HIT
for j in range(17, 22):
    POLICY_DEALER[i] = ACTION_STAND

# 카드 뽑기
def get_card():
    card = np.random.randint(1, 14)
    card = min(10, card)
    return card

def card_value(card_id):
    return 11 if card_id == 1 else card_id


# 게임 플레이
# policy_player : 딜러 or 플레이어
# initial_state : [사용가능 에이스 유무, 게임 참여자가 보유한 숫자의 합, 딜러가 보여주는 하나의 카드]
# initial_action : 그냥 행동
def play(policy_player, initial_state=None, initial_action=None):
    
    player_sum = 0
    player_trajectory = []
    usable_ace_player = False

    dealer_card1 = 0
    dealer_card2 = 0
    usable_ace_dealer = False

    if initial_state == None:
        # 두 장을 뽑게하기
        while player_sum < 12:
            card = get_card()
            player_sum += card_value(card)

            # 플레이어의 점수가 2번 뽑아서 21점을 넘으려면 에이스 두번 뽑기밖에 없음
            if player_sum > 21:
                assert player_sum == 20, 'errorcode1'
                player_sum -= 10
            else:
                usable_ace_player |= (1 == card)
            
        dealer_card1 = get_card()
        dealer_card2 = get_card()