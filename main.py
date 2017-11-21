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
    
    __ENVIRONMENT__ = "env1"
    #Afficher ou non l'interface
    __GUI__ = True

    ''''''''''''''''''''''''''''''''''''
    ''''''''''''''''''''''''''''''''''''

    strat = Strategy()
    agent = AgentDev(strat)

    #Instanciation des builders
    envbuilder = EnvBuilder(__ENVIRONMENT__)
    gui, map, agents = envbuilder.build()

    #Creation de la grille
    env = Grid(gui, map, agents, __GUI__)
    
    #Pour une question de généricité les valeurs des actions n'ont pas été modifiées dans la grille
    #Action monter = 0, action descendre = 2
    histo = {}
    cpt = 0
    result = 0
    while cpt < 10:
        action = agent.chooseExperience(result, cpt, 20)
        result = env.step(agents[0], action)
        agent.get_reward(result)
        cpt += 1

    print("Final best action : ", agent.best_actions)

    '''
    strat = Strategy()
    agent = SmartAgent(strat, 20, ["▲", "▼"])

    env1 = Env({'0': "1", '1': "2"})
    envd = Env_Dif()

    steps = FLAGS.steps
    i = 0

    result = 0
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
    
    print("sequences : ", agent.sequences)
    for seq in agent.sequences:
        print(seq)
    '''

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
