# agent.py

import random
import math
from collections import deque
import heapq


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
    

class SearchAgent:

    def __init__(self):
        self.plan = []
        self.active_algo = "BFS"

    def manhattan_distance(self, pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def euclidean_distance(self, pos, goal):
        return math.sqrt(
            (pos[0] - goal[0]) ** 2 +
            (pos[1] - goal[1]) ** 2
        )

    def astar_search(
        self,
        start_pos,
        goal_pos,
        walls,
        grid_size,
        heuristic_type='manhattan'
    ):
        # Priority queue: (f_cost, g_cost, current_pos, path_taken)
        if heuristic_type == 'manhattan':
            h_cost = self.manhattan_distance(start_pos, goal_pos)
        else:
            h_cost = self.euclidean_distance(start_pos, goal_pos)

        frontier = [(h_cost, 0, start_pos, [])]
        reached_states = set()

        while frontier:
            f_cost, g_cost, current_pos, path_taken = heapq.heappop(frontier)

            if current_pos == goal_pos:
                return path_taken

            if current_pos in reached_states:
                continue

            reached_states.add(current_pos)

            x, y = current_pos

            neighbors = [
                ((x, y + 1), "Up"),
                ((x, y - 1), "Down"),
                ((x - 1, y), "Left"),
                ((x + 1, y), "Right")
            ]

            for next_pos, action in neighbors:
                nx, ny = next_pos

                if (
                    0 <= nx < grid_size[0]
                    and 0 <= ny < grid_size[1]
                    and next_pos not in walls
                    and next_pos not in reached_states
                ):
                    g_new = g_cost + 1

                    if heuristic_type == 'manhattan':
                        h_new = self.manhattan_distance(
                            next_pos,
                            goal_pos
                        )
                    else:
                        h_new = self.euclidean_distance(
                            next_pos,
                            goal_pos
                        )

                    f_new = g_new + h_new

                    heapq.heappush(
                        frontier,
                        (
                            f_new,
                            g_new,
                            next_pos,
                            path_taken + [action]
                        )
                    )

        return None

    def bfs_search(self, start, goal, walls, grid_size):

        queue = deque([(start, [])])
        reached = {start}

        while queue:

            current, path = queue.popleft()

            if current == goal:
                return path

            x, y = current

            neighbors = [
                ((x, y + 1), "Up"),
                ((x, y - 1), "Down"),
                ((x - 1, y), "Left"),
                ((x + 1, y), "Right")
            ]

            for next_pos, action in neighbors:

                nx, ny = next_pos

                if (
                    0 <= nx < grid_size[0]
                    and 0 <= ny < grid_size[1]
                    and next_pos not in walls
                    and next_pos not in reached
                ):
                    reached.add(next_pos)

                    queue.append(
                        (next_pos, path + [action])
                    )

        return None

    def dfs_search(self, start, goal, walls, grid_size):

        stack = [(start, [])]
        reached = {start}

        while stack:

            current, path = stack.pop()

            if current == goal:
                return path

            x, y = current

            neighbors = [
                ((x, y + 1), "Up"),
                ((x, y - 1), "Down"),
                ((x - 1, y), "Left"),
                ((x + 1, y), "Right")
            ]

            for next_pos, action in neighbors:

                nx, ny = next_pos

                if (
                    0 <= nx < grid_size[0]
                    and 0 <= ny < grid_size[1]
                    and next_pos not in walls
                    and next_pos not in reached
                ):
                    reached.add(next_pos)

                    stack.append(
                        (next_pos, path + [action])
                    )

        return None

    def ucs_search(self, start, goal, walls, grid_size):

        frontier = [(0, start, [])]
        reached = {start: 0}

        while frontier:

            cost, current, path = heapq.heappop(frontier)

            if current == goal:
                return path

            x, y = current

            neighbors = [
                ((x, y + 1), "Up", 1),
                ((x, y - 1), "Down", 1),
                ((x - 1, y), "Left", 1),
                ((x + 1, y), "Right", 1)
            ]

            for next_pos, action, step_cost in neighbors:

                nx, ny = next_pos

                if (
                    0 <= nx < grid_size[0]
                    and 0 <= ny < grid_size[1]
                    and next_pos not in walls
                ):
                    new_cost = cost + step_cost

                    if (
                        next_pos not in reached
                        or new_cost < reached[next_pos]
                    ):
                        reached[next_pos] = new_cost

                        heapq.heappush(
                            frontier,
                            (
                                new_cost,
                                next_pos,
                                path + [action]
                            )
                        )

        return None

    def sense_and_act(self, percept):

        if not self.plan:

            start = tuple(percept["agent_pos"])

            food_positions = percept["all_food"]

            if not food_positions:
                return "Stay"

            # Find the closest food
            goal = min(
                food_positions,
                key=lambda food:
                    abs(food[0] - start[0]) +
                    abs(food[1] - start[1])
            )

            walls = set(percept["walls"])
            grid_size = percept["grid_size"]

            if self.active_algo == "BFS":

                self.plan = self.bfs_search(
                    start,
                    goal,
                    walls,
                    grid_size
                )

            elif self.active_algo == "DFS":

                self.plan = self.dfs_search(
                    start,
                    goal,
                    walls,
                    grid_size
                )

            elif self.active_algo == "UCS":

                self.plan = self.ucs_search(
                    start,
                    goal,
                    walls,
                    grid_size
                )

            elif self.active_algo == "AStar":

                self.plan = self.astar_search(
                    start,
                    goal,
                    walls,
                    grid_size,
                    heuristic_type="manhattan"
                )

            if self.plan is None:
                return "Stay"

        return self.plan.pop(0)