import os, sys, inspect

#Pour inclure les fichiers de l'environnement, plot et stat
cmd_subfolder_grid = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"Grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

import argparse
from Strategy import *
from Agent import *
from env import *
from envBuilder import *
from grid import *


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
    agent = Agent(strat)

    #TODO: modifier la maniere donc est gere l'environnement
    #r2 doit etre retourne uniquement apres une alternance e1 / e2
    env1 = Env({'0': "1", '1': "2"})
    steps = FLAGS.steps
    i = 0

    result = 0
    while i < steps:
        action = agent.chooseExperience(result, i, steps)
        #print("action choisie : " + str(action)) # @debug
        result = env1.getResult(action)
        #print("result  : " + str(result)) # @debug
        agent.get_reward(result)
        i += 1
    
    print("sequences : ", agent.sequences)
    for seq in agent.sequences:
        print(seq)
    '''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=30,
                        help='number of steps')
    FLAGS, unparsed = parser.parse_known_args()
    main()
