import numpy as np
import random
import matplotlib.pyplot as plt

# number of race track rows and columns
rows, cols = 32, 17

ε = 0.1
γ = 1

# action can be horizontal and vertical with value 0, 1 or -1
# represented by 1 to 9
actions = [
    (0, 0),
    (0, 1),
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1),
]
act_len = len(actions)

# 5 velocity values 0 to 4, represented by 1 to 5
vel_len = 5

# initialise Q, C and π
# state is 4-tuple: (row, col, velocity_horizontal, verlocity_vertical)
Q = np.random.rand(rows, cols, vel_len, vel_len, act_len) * 400 - 500
C = np.zeros((rows, cols, vel_len, vel_len, act_len), dtype=float)
π = np.ones((rows, cols, vel_len, vel_len), dtype=int)
for r in range(rows):
    for c in range(cols):
        for h in range(vel_len):
            for v in range(vel_len):
                π[r, c, h, v] = np.argmax(Q[r, c, h, v, :])

# set up the 1st race track map
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

# valid actions for each velocity combination
# Both velocity components are restricted to be nonnegative and less than 5,
# and they cannot both be zero.
valid_acts = [
    [idx for idx, a in enumerate(actions) if (h + a[1]) in range(5) and (v + a[1]) in range(5) and not ((h + a[1]) == 0 and (v + a[1]) == 0)]
    for h in range(vel_len)
    for v in range(vel_len)
]

# pre-allocated state, action, probability trajectory array
S = [(1, random.choice(start_cols), 1, 1)] * 10**6
A = [None] * 10**6
B = [None] * 10**6

def make_trajectory(ε, noise=True):
    t = 0

    # start state
    s = S[t]

    while True:
        # get all valid actions for current velocity
        acts = valid_acts[s[2] * 5 + s[3] - 6]
        num_acts = len(acts)

        # choose next action using ε-greedy policy if πa is valid
        # otherwise choose randomly, and save its probability
        s_s = [0, 0, 0, 0]
        for i in range(4):
            s_s[i] = s[i]

        s_s[2] -= 1
        s_s[3] -= 1
        πa = π[s_s]
        πa_valid = πa in acts
        if random.random() >= ε:
            if πa_valid:
                a = πa
                b = 1 - ε + ε / num_acts
            else:
                a = random.choice(acts)
                b = 1 / num_acts
        else:
            a = random.choice(acts)
            b = (1 - ε) if πa_valid else 1 / num_acts

        # add some noise
        if noise and random.random() < 0.1:
            a = 0
            b = 0.1

        A[t] = a
        B[t] = b
        act = actions[a]

        # next state
        vel = (s[2] + act[0], s[3] + act[1])
        next_s = (s[0] + vel[1] - 1, s[1] + vel[0] - 1, vel[0], vel[1])

        # check if car hits finish line
        path = {(min(s[0] + i, next_s[0]), min(s[1] + i, next_s[1])) for i in range(max(vel) + 1)}
        if path & fin_cells:
            return t

        if next_s[0] < 0 or next_s[0] >= rows or next_s[1] < 0 or next_s[1] >= cols or track[next_s[0], next_s[1]] == 1:
            s = (1, random.choice(start_cols), 1, 1)
        else:
            s = next_s

        t += 1
        S[t] = s

def run_episode(T):
    G, W, R = 0.0, 1.0, -1

    for t in range(T - 1, -1, -1):
        s = S[t]
        sa = (*s, A[t])

        G = γ * G + R
        C[sa] += W
        Q[sa] += W * (G - Q[sa]) / C[sa]

        acts = valid_acts[s[2] * 5 + s[3] - 6]
        π[s[:2]] = acts[np.argmax(Q[(*s, acts)], axis=-1)]
        if A[t].any() != π[s[:2]]:
            return t

        W /= B[t]

    return 0

def output_trajectories():
    for i in range(1, 4):
        T = make_trajectory(0.0, noise=False)
        print("\noptimal trajectory #{}:".format(i))
        print("S:", S[:T])
        print("A:", A[:T])
        print("R:", -T)

def main():
    episode_num = 10**5
    rewards = []

    for i in range(episode_num):
        T = make_trajectory(ε)
        t = run_episode(T)
        print("episode {}: {}, {}, {}".format(i, T, t, T - t))

        if i % 9 == 0:
            T = make_trajectory(0.0)
            rewards.append(-T)

    plt.plot(rewards)
    output_trajectories()

if __name__ == "__main__":
    main()
