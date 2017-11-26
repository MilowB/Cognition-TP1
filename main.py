import os, sys, inspect

# Pour inclure les fichiers de l'environnement, plot et stat
cmd_subfolder_grid = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "Grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

import argparse
from Strategy import *
from OldStrat import *
from Agent import *
from SmartAgent import *
from cartesianAgent import *
from totalRecall import *
from dull import *
from env import *
from envBuilder import *
from grid import Grid
import time
from env_dif import *


def init_maze_task():

    __ENVIRONMENT__ = "maze"

    # Afficher ou non l'interface
    __GUI__ = True

    # Instanciation des builders
    envbuilder = EnvBuilder(__ENVIRONMENT__)
    gui, map, agents = envbuilder.build()

    # Creation de la grille
    env = Grid(gui, map, agents, __GUI__, __ENVIRONMENT__)

    motivation = {"01": -5, "02": 10, "11": -1, "12": -1, "22": -3, "32": -3}

    return agents, env, motivation


def init_simple_task():
    env = Env({'0': "1", '1': "2"})
    motivation = {"01": -1, "02": 1, "11": -1, "12": 1}
    return env, motivation


def init_alter_task():
    env = Env_Dif()
    motivation = {"01": -1, "02": 1, "11": -1, "12": 1}
    return env, motivation


def main():
    agents, env, motivation = init_maze_task()
    #env,motivation = init_simple_task()
    #env,motivation = init_alter_task()

    strat = Strategy(motivation)


    ''' First envs'''
    #strat = OldStrategy()

    agent = DullAgent(strat, ["▲", "■", "▶", "◀"])
    #agent = TotalRecall(strat, ["▲", "■", "▶", "◀"])
    #agent = CartesianAgent(strat, ["▲", "■", "▶", "◀"])

    #Exécuter cet agent pour les premiers environnements (nombre d'actions différent)
    ''' Firsts Env'''
    #agent = SmartAgent(strat,100,  ["►", "◄"])

    i = 0

    while i < FLAGS.steps:
        if i > FLAGS.steps - 20:
            time.sleep(0.3)

        action = agent.chooseExperience(i, FLAGS.steps)
        #result = env.getResult(str(action)) # To use if the task is not a Maze
        result = env.step(agents[0], action)  # To use if the task is a  Maze
        reward = agent.get_reward(result)

        if agent._name != "cartesian":
            agent.memory() # TODO : ------- > comment this line to see memory usage efficiency
        #agent.tracer(reward, i)

        if FLAGS.debug:
            print("--------------------------")
            print("J'ai choisis : " + agent.symb[action])
            print("J'ai eu : r" + str(result))
            print("Pour : " + str(reward) + " pts")

        i += 1
    describe(agent)

def describe(agent):
    # print(agent.max_inter(agent.interactions))
    # agent.show_inter()
    # print(agent.best_seq)

    if agent._name != "cartesian":
        agent.show_trace()
        print(agent.motiv)

    #agent.print_interactions()  # @debug


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #Dans le cas du CartesianAgent, monter le nombre default d'iterations à 10.000
    parser.add_argument('--steps', type=int, default=7000,
                        help='number of steps')
    parser.add_argument('--debug', type=bool, default=False,
                        help='Put the debug display')

    FLAGS, unparsed = parser.parse_known_args()

    main()
