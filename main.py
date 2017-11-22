import os, sys, inspect

#Pour inclure les fichiers de l'environnement, plot et stat
cmd_subfolder_grid = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"Grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

import argparse
from Strategy import *
from Agent import *
from SmartAgent import *
from env import *
from envBuilder import *
from grid import *
from env_dif import *


def main():
    __ENVIRONMENT__ = "maze"
    #Afficher ou non l'interface
    __GUI__ = True

    #Instanciation des builders
    envbuilder = EnvBuilder(__ENVIRONMENT__)
    gui, map, agents = envbuilder.build()
    #Creation de la grille
    env = Grid(gui, map, agents, __GUI__, "maze")

    motivation = {"1": -1, "2": 1}
    strat = Strategy(motivation)
    agent = SmartAgent(strat, 100, ["▲", "▼", "►", "◄"])

    env1 = Env({'0': "1", '1': "2"})
    envd = Env_Dif()

    steps = FLAGS.steps
    i = 0

    result = 0
    while i < steps:

        action = agent.chooseExperience(i, steps)
        #result = envd.getResult(str(action))
        result = env.step(agents[0], action)
        reward = agent.get_reward(result)
        agent.memory()
        if FLAGS.debug:
            print("--------------------------")
            print("J'ai choisis : e" + str(action))
            print("J'ai eu : r" + str(result))
            print("Pour : " + str(reward) + " pts")
            agent.pres()

        i += 1    
    agent.tracer(reward, i)

    print(agent.best_seq)
    agent.show_trace()

    templ = []
    print("---- Test succes rate ----")
    for it in range(0, 300):
        templ += agent.best_seq
    n = 0

    for action in templ:
        if agent.get_reward(envd.getResult(action)) > 0:
            n += 1
    print("Success rate is :" + str(round((n/len(templ)*100),0))+" %")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=3000,
                        help='number of steps')
    parser.add_argument('--debug', type=bool, default=False,
                        help='Put the debug display')

    FLAGS, unparsed = parser.parse_known_args()

    main()
