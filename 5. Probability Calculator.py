import random
from copy import deepcopy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        experiment_hat = deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        drawn_balls_count = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}
        if all(drawn_balls_count.get(color, 0) >= count for color, count in expected_balls.items()):
            successes += 1
    return successes / num_experiments

# Example usage:
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000)
print(probability)