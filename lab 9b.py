from numpy import random

class Agent:
    def __init__(self, world, same_pref):
        self.world = world
        self.same_pref = same_pref
        self.location = None

    def move(self):
        pass  # Simplified for brevity

class World:
    def __init__(self, params):
        self.params = params
        self.grid = {(i, j): None for i in range(params['world_size'][0]) for j in range(params['world_size'][1])}
        self.agents = [Agent(self, params['same_pref']) for _ in range(params['num_agents'])]
        random.shuffle(self.agents)
        self.init_world()

    def init_world(self):
        for agent in self.agents:
            loc = self.find_vacant()
            self.grid[loc] = agent
            agent.location = loc

    def find_vacant(self):
        empties = [loc for loc, occupant in self.grid.items() if occupant is None]
        return random.choice(empties)

    def run(self):
        for iteration in range(self.params['max_iter']):
            random.shuffle(self.agents)
            for agent in self.agents:
                agent.move()
            # Simplified output for demonstration
            if iteration % 10 == 0:  # Output every 10 iterations
                print(f'Iteration {iteration}: Running simulation...')

params = {
    'world_size': (20, 20),
    'num_agents': 10,
    'same_pref': 0.4,
    'max_iter': 100,
}

world = World(params)
world.run()
