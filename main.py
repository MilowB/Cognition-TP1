import argparse
from Strategy import *
from Agent import *

import env


def main():
    strat = Strategy()
    agent = Agent(strat)
    env1 = env.Env({'0': "1", '1': "2"})
    steps = FLAGS.steps
    i = 0

    while i < steps:
        action = agent.chooseExperience(i, steps)
        result = env1.getResult(action)
        agent.get_reward(result)
        i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=30,
                        help='number of steps')
    FLAGS, unparsed = parser.parse_known_args()
    main()
