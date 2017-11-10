import argparse
from Strategy import *
from Agent import *
from SmartAgent import *
from env import *
from env_dif import *


def main():
    strat = Strategy()
    agent = SmartAgent(strat, 20, ["▲", "▼"])
    env1 = Env({'0': "1", '1': "2"})
    envd = Env_Dif()

    steps = FLAGS.steps
    i = 0

    while i < steps:

        action = agent.chooseExperience(i, steps)
        result = envd.getResult(str(action))
        reward = agent.get_reward(result)
        agent.memory()
        if FLAGS.debug:
            print("--------------------------")
            print("J'ai choisis : e" + str(action))
            print("J'ai eu : r" + str(result))
            print("Pour : " + str(reward) + " pts")
            agent.pres()

        agent.tracer(reward, i)
        i += 1

    print(agent.best_seq)
    agent.show_trace()

    templ = []
    print("---- Test succes rate ----")
    for it in range(0, 100):
        templ += agent.best_seq
    n = 0

    for action in templ:
        if agent.get_reward(envd.getResult(action)) > 0:
            n += 1
    print("Success rate is :" + str(round((n/len(templ)*100),0))+" %")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=500,
                        help='number of steps')
    parser.add_argument('--debug', type=bool, default=False,
                        help='Put the debug display')

    FLAGS, unparsed = parser.parse_known_args()

    main()
