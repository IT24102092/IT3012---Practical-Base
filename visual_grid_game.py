# visual_grid_game.py

import random
import tkinter as tk


class VisualGridHuntGame:
    """
    Pacman-style grid environment.
    Supports partial observability for Simple Reflex and Model-Based agents.
    """

    def __init__(self, width=10, height=10, num_food=10, num_opponents=2, custom_walls=None):

        self.width = width
        self.height = height

        # Agent starting position
        self.agent_pos = [0, 0]

        # Agent facing direction
        self.direction = "Up"


        if custom_walls is not None:
            self.walls = set(custom_walls)

        else:
            self.walls = {
                (2, 2),
                (2, 3),
                (5, 5),
                (6, 5),
                (3, 7)
            }



        # Generate food positions
        self.food_positions = set()

        while len(self.food_positions) < num_food:

            fx = random.randint(0, self.width - 1)
            fy = random.randint(0, self.height - 1)

            position = (fx, fy)

            if position != (0, 0) and position not in self.walls:
                self.food_positions.add(position)



        # Generate opponents
        self.opponents = []

        while len(self.opponents) < num_opponents:

            ox = random.randint(0, self.width - 1)
            oy = random.randint(0, self.height - 1)

            opponent = [ox, oy]


            if (
                tuple(opponent) != (0, 0)
                and tuple(opponent) not in self.walls
                and tuple(opponent) not in self.food_positions
            ):
                self.opponents.append(opponent)



        self.score = 0
        self.steps = 0
        self.collision = False




    def get_percept(self) -> dict:

        x, y = self.agent_pos


        # Find cell in front of agent

        front_x = x
        front_y = y


        if self.direction == "Up":
            front_y += 1

        elif self.direction == "Down":
            front_y -= 1

        elif self.direction == "Left":
            front_x -= 1

        elif self.direction == "Right":
            front_x += 1



        # Check wall ahead

        wall_ahead = (
            (front_x, front_y) in self.walls
            or front_x < 0
            or front_x >= self.width
            or front_y < 0
            or front_y >= self.height
        )



        # Limited percept for agent

        return {

            # Needed for Model-Based memory
            "agent_pos": list(self.agent_pos),

            # Current sensors
            "wall_ahead": wall_ahead,

            "food_here": tuple(self.agent_pos) in self.food_positions
        }




    def execute_action(self, action: str):

        # Update facing direction
        self.direction = action


        self.steps += 1


        new_pos = list(self.agent_pos)



        if action == "Up":

            new_pos[1] = min(
                self.height - 1,
                new_pos[1] + 1
            )


        elif action == "Down":

            new_pos[1] = max(
                0,
                new_pos[1] - 1
            )


        elif action == "Left":

            new_pos[0] = max(
                0,
                new_pos[0] - 1
            )


        elif action == "Right":

            new_pos[0] = min(
                self.width - 1,
                new_pos[0] + 1
            )



        # Wall collision

        if tuple(new_pos) in self.walls:

            self.score -= 5


        else:

            self.agent_pos = new_pos




        # Food collection

        current_position = tuple(self.agent_pos)


        if current_position in self.food_positions:

            self.food_positions.remove(current_position)

            self.score += 20




        # Move opponents

        for opponent in self.opponents:


            move = random.choice(
                [
                    "Up",
                    "Down",
                    "Left",
                    "Right",
                    "Stay"
                ]
            )


            if move == "Up" and opponent[1] < self.height - 1:
                opponent[1] += 1


            elif move == "Down" and opponent[1] > 0:
                opponent[1] -= 1


            elif move == "Left" and opponent[0] > 0:
                opponent[0] -= 1


            elif move == "Right" and opponent[0] < self.width - 1:
                opponent[0] += 1



            if opponent == self.agent_pos:

                self.score -= 50

                self.collision = True




    def is_done(self) -> bool:

        return (
            len(self.food_positions) == 0
            or self.steps >= 60
            or self.collision
        )





class GridGameGUI:

    def __init__(self, root, width=10, height=10, num_food=12, num_opponents=2):

        self.root = root

        self.root.title(
            "IT3012 - Multi Agent Grid Hunt"
        )


        self.env = VisualGridHuntGame(
            width,
            height,
            num_food,
            num_opponents
        )



        self.cell_size = 50


        self.canvas = tk.Canvas(
            root,
            width=self.env.width * self.cell_size,
            height=self.env.height * self.cell_size,
            bg="white"
        )


        self.canvas.pack()



        self.label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 14)
        )

        self.label.pack()



        self.draw_grid()




    def draw_grid(self):

        self.canvas.delete("all")


        for x in range(self.env.width):

            for y in range(self.env.height):

                x1 = x * self.cell_size

                y1 = (
                    self.env.height - 1 - y
                ) * self.cell_size


                x2 = x1 + self.cell_size

                y2 = y1 + self.cell_size


                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    outline="black"
                )



        # Draw food

        for fx, fy in self.env.food_positions:

            self.canvas.create_oval(
                fx*self.cell_size+15,
                (self.env.height-1-fy)*self.cell_size+15,
                fx*self.cell_size+35,
                (self.env.height-1-fy)*self.cell_size+35,
                fill="orange"
            )



        # Draw agent

        ax, ay = self.env.agent_pos

        self.canvas.create_oval(
            ax*self.cell_size+10,
            (self.env.height-1-ay)*self.cell_size+10,
            ax*self.cell_size+40,
            (self.env.height-1-ay)*self.cell_size+40,
            fill="blue"
        )





if __name__ == "__main__":

    root = tk.Tk()

    app = GridGameGUI(
        root,
        width=12,
        height=12,
        num_food=15,
        num_opponents=0
    )

    root.mainloop()