# agent.py

import random


class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']


    def sense_and_act(self, percept: dict) -> str:

        pos = percept['agent_pos']

        return random.choice(self.actions_pool)




# Simple Reflex Agent
class SimpleReflexAgent:
    """
    Simple Reflex Agent using condition-action rules.
    """

    def sense_and_act(self, percept: dict) -> str:

        # IF food exists THEN collect food
        if percept["food_here"]:
            return "Suck"


        # IF wall ahead THEN turn left
        elif percept["wall_ahead"]:
            return "Left"


        # ELSE move right
        else:
            return "Right"





# Model Based Agent
class ModelBasedAgent:
    """
    Model-Based Agent with internal memory state.
    """

    def __init__(self):

        # Memory of visited cells
        self.visited_cells = set()

        # Previous action memory
        self.last_action = None




    def sense_and_act(self, percept: dict) -> str:


        # Current position
        current_position = tuple(percept["agent_pos"])


        # Update memory
        self.visited_cells.add(current_position)



        # Rule 1: Food found
        if percept["food_here"]:

            action = "Suck"



        # Rule 2: Wall ahead
        elif percept["wall_ahead"]:


            possible_actions = [
                "Up",
                "Down",
                "Left",
                "Right"
            ]


            action = "Left"


            for move in possible_actions:


                if move == "Up":

                    next_position = (
                        current_position[0],
                        current_position[1] + 1
                    )


                elif move == "Down":

                    next_position = (
                        current_position[0],
                        current_position[1] - 1
                    )


                elif move == "Left":

                    next_position = (
                        current_position[0] - 1,
                        current_position[1]
                    )


                else:

                    next_position = (
                        current_position[0] + 1,
                        current_position[1]
                    )



                # Select unvisited direction
                if next_position not in self.visited_cells:

                    action = move
                    break





        # Rule 3: Normal movement using memory
        else:


            possible_actions = [
                "Right",
                "Up",
                "Left",
                "Down"
            ]


            action = "Right"



            for move in possible_actions:


                if move == "Right":

                    next_position = (
                        current_position[0] + 1,
                        current_position[1]
                    )


                elif move == "Left":

                    next_position = (
                        current_position[0] - 1,
                        current_position[1]
                    )


                elif move == "Up":

                    next_position = (
                        current_position[0],
                        current_position[1] + 1
                    )


                else:

                    next_position = (
                        current_position[0],
                        current_position[1] - 1
                    )



                if next_position not in self.visited_cells:

                    action = move
                    break




        # Remember last action
        self.last_action = action


        return action