import argparse

import env
import Agent
import Strategy



def main():

    env1 = env.Env({'0': 1, '1': 2})
    a1 = Agent.Agent(Strategy.Strategy())
    steps = FLAGS.steps
    i = 0

    while i < steps:
        print("Salutation, je choisis l'experience")
        a1.chooseExperience(i,steps)
        i += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=30,
                        help='number of steps')
    FLAGS, unparsed = parser.parse_known_args()
    main()
