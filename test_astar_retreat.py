# Task 4.2: Test A* Retreat Tile Skipping

from agent import SearchAgent


def test_retreat_tile_is_skipped():
    # Create the search agent
    agent = SearchAgent()

    # Simple 3x3 grid with no walls
    start = (0, 0)
    goal = (2, 0)
    walls = set()
    grid_size = (3, 3)

    # Opponent is placed on the direct candidate tile
    opponents = [(1, 0)]

    # Agent has Dust
    has_dust = True

    # Bloodseeker is missing
    bloodseeker_present = False

    # Run A* with the safety information
    plan = agent.astar_search(
        start,
        goal,
        walls,
        grid_size,
        opponents,
        has_dust,
        bloodseeker_present,
        heuristic_type="manhattan"
    )

    # The direct tile (1, 0) should be avoided
    assert plan != ["Right", "Right"], \
        "Test Failed: A* used the Retreat tile"

    print("A* Retreat Tile Skipping Test Passed!")


if __name__ == "__main__":
    test_retreat_tile_is_skipped()