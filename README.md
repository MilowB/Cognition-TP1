Mickael Bettinelli
Theo Jaunet

# Cognition-Projet

This project was made on Python 3.x

Python 3.x pip requirements :


numpy
pygame

``` sh

pip install numpy
pip install pygame
```

 > you may need to use pip3 instead depending on your python configuration.
 
 
 ## How to use it ?
 
 The initialisation is made on main.py. If you want to change the initial configuration, you can comment and un comment few lines.
 
 to illustrate, if you want to run an agent in an environement where the agent need to alter his actions, you need to use 
 
 ``` python
  # Creation of the environnement and of motivation system
  env,motivation =init_alter_task()
  
  # method to get result of an action . Be carefull, this is not a reward !
  result = env.getResult(str(action)) 

```
 
  ### Change the maze 
  
  First of all, you to be sure that the following lines are uncommented in main.py main() function. 
  Any other line initalising the environnement or the result in the main function must be commented
  
  
   ``` python
  # Creation of the environnement and of motivation system
 agents, env, motivation = init_maze_task()
  
  # method to get result of an action . Be carefull, this is not a reward !
 result = env.step(agents[0], action)

```

Then, in the ini_maze_task method , you can choose between {"env1","large_maze","line","long_maze","maze","small_maze"}

to set your choice , you must change the environement affectation, as described down bellow.

``` python

   __ENVIRONMENT__ = "maze"

```
### Change the agent

In order to switch the agent, you need to comment the actual agent and uncomment the wanted one, as described bellow

``` python

    agent = DullAgent(strat, ["▲", "■", "▶", "◀"])
    #agent = TotalRecall(strat, ["▲", "■", "▶", "◀"])
    #agent = CartesianAgent(strat, ["▲", "■", "▶", "◀"])
    #agent = BasicAgent(strat, ["▲", "■", "▶", "◀"])
    #agent = SmartAgent(strat, 100, ["▲", "■", "►", "◄"])

```

> Here DullAgent is seleted. Please note that the second argument is to produce the trace. You may want to change some symbols to fit your needs.
  the second argument on SmartAgent is the memory length it may be changed to see any agent behaviour evolution.

### Display the trace

To display the execution, you need 2 lines. Some agents may not have this possibility yet. But to display it, you must make sure the two following lines are uncommented in main.py

``` python
#in main()
agent.tracer(reward, i)

#in describe()
 agent.show_trace()

```

### Misc

You may want to set some argument like number of steps or the level of prompt to configure the desired output.
as described bellow. The default steps is 700 and the debug is off.

``` sh

python3 main.py --steps=900 --debug=True

```

> this command may change with your Os and python configuration. Please note that here , we made the agent do 900 iterations and display the debug output.
