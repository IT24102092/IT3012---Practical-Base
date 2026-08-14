# simulator2.py

from visual_grid_game import VisualGridHuntGame
from agent import ModelBasedAgent


def run_agent_simulation():

    # Create the grid environment
    env = VisualGridHuntGame(
        width=10,
        height=10,
        num_food=10,
        num_opponents=0
    )

    # Create the agent
    agent = ModelBasedAgent()


    print("=== Agent Simulation Started ===")


    while not env.is_done():

        # Get limited percept from environment
        percept = env.get_percept()

        # Agent decides action based on percept
        action = agent.sense_and_act(percept)

        # Apply action in environment
        env.execute_action(action)


        print(
            f"Position: {env.agent_pos} | "
            f"Food Left: {len(env.food_positions)} | "
            f"Score: {env.score} | "
            f"Percept: {percept} | "
            f"Action: {action}"
        )


    print(
        f"\nSimulation Finished! "
        f"Final Score: {env.score} "
        f"after {env.steps} steps."
    )


if __name__ == "__main__":
    run_agent_simulation()