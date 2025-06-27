"""
random_walk_simulation.py: Simulate 1D, 2D, and 3D random walks with customizable probabilities and optional animation.

Functions:
    - random_walk_1d
    - random_walk_2d
    - random_walk_3d

Each function returns the traversal coordinates as a list of tuples.
The walk implementations are by myself but the animation plotting done with AI so feel free to modify if problem arise.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


def random_walk_1d(num_steps: int = 50, p_forward: float = 0.5, p_backward: float = 0.5, 
                   show_animation: bool = False, random_state=None, initial_location: int = 0) -> list:
    
    """
    Simulate a 1D random walk.

    Args:
        num_steps (int): Number of steps in the walk.
        p_forward (float): Probability of moving forward (positive direction).
        p_backward (float): Probability of moving backward (negative direction).
        show_animation (bool): If True, display an animated plot of the walk.
        random_state (int or None): Seed for reproducibility.
        initial_location (int): Starting position of the walk.

    Returns:
        list of tuples: Visited positions as a list of (position,) tuples.
    """
    
    if not np.isclose(p_forward + p_backward, 1.0):
        raise ValueError("p_forward and p_backward must sum to 1.")

    if random_state is not None:
        np.random.seed(random_state)

    steps = np.where(np.random.rand(num_steps) < p_forward, 1, -1)
    positions = np.concatenate(([initial_location], np.cumsum(steps) + initial_location))
    trajectory = [(int(p),) for p in positions]

    if show_animation:
        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2, color='blue')
        points, = ax.plot([], [], 'd', color='red')
        current, = ax.plot([], [], 'o', color='forestgreen')

        ax.set_xlim(0, num_steps)
        ax.set_ylim(positions.min() - 1, positions.max() + 1)
        ax.set_title("1D Random Walk")
        ax.set_xlabel("Step")
        ax.set_ylabel("Position")

        def _animate(i):
            x_vals = np.arange(i + 1)
            y_vals = positions[:i + 1]
            line.set_data(x_vals, y_vals)
            points.set_data(x_vals, y_vals)
            current.set_data([x_vals[-1]], [y_vals[-1]])
            return line, points, current

        ani = FuncAnimation(fig, _animate, frames=num_steps + 1, interval=500, blit=True)
        plt.show()

    return trajectory


def random_walk_2d(num_steps: int = 50, p_right: float = 0.25, p_left: float = 0.25, p_up: float = 0.25, 
                   p_down: float = 0.25, show_animation: bool = False, random_state=None, initial_location: tuple = (0, 0)) -> list:
    
    """
    Simulate a 2D random walk.

    Args:
        num_steps (int): Number of steps in the walk.
        p_right (float): Probability of moving right (+x).
        p_left (float): Probability of moving left (-x).
        p_up (float): Probability of moving up (+y).
        p_down (float): Probability of moving down (-y).
        show_animation (bool): If True, display an animated plot of the walk.
        random_state (int or None): Seed for reproducibility.
        initial_location (tuple): Starting position (x, y) of the walk.

    Returns:
        list of tuples: Visited positions as a list of (x, y) tuples.
    """
    
    total = p_right + p_left + p_up + p_down
    if not np.isclose(total, 1.0):
        raise ValueError("Sum of probabilities must equal 1.")

    if random_state is not None:
        np.random.seed(random_state)

    probs = [p_right, p_left, p_up, p_down]
    moves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    steps_idx = np.random.choice(4, size=num_steps, p=probs)
    steps = moves[steps_idx]
    positions = np.vstack((initial_location, np.cumsum(steps, axis=0) + initial_location))
    trajectory = [tuple(p) for p in positions]

    if show_animation:
        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2, color='blue')
        points, = ax.plot([], [], 'd', color='red')
        current, = ax.plot([], [], 'o', color='forestgreen')

        ax.set_xlim(positions[:, 0].min() - 1, positions[:, 0].max() + 1)
        ax.set_ylim(positions[:, 1].min() - 1, positions[:, 1].max() + 1)
        ax.set_title("2D Random Walk")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        def _animate(i):
            x_vals = positions[:i + 1, 0]
            y_vals = positions[:i + 1, 1]
            line.set_data(x_vals, y_vals)
            points.set_data(x_vals, y_vals)
            current.set_data([x_vals[-1]], [y_vals[-1]])
            return line, points, current

        ani = FuncAnimation(fig, _animate, frames=num_steps + 1, interval=500, blit=True)
        plt.show()

    return trajectory


def random_walk_3d(num_steps: int = 50, p_posx: float = 0.2, p_negx: float = 0.2, p_posy: float = 0.2, 
                   p_negy: float = 0.2, p_posz: float = 0.1, p_negz: float = 0.1, 
                   show_animation: bool = False, random_state=None, initial_location: tuple = (0, 0, 0)) -> list:
    
    """
    Simulate a 3D random walk.

    Args:
        num_steps (int): Number of steps in the walk.
        p_posx (float): Probability of moving +x.
        p_negx (float): Probability of moving -x.
        p_posy (float): Probability of moving +y.
        p_negy (float): Probability of moving -y.
        p_posz (float): Probability of moving +z.
        p_negz (float): Probability of moving -z.
        show_animation (bool): If True, display an animated 3D plot.
        random_state (int or None): Seed for reproducibility.
        initial_location (tuple): Starting position (x, y, z) of the walk.

    Returns:
        list of tuples: Visited positions as a list of (x, y, z) tuples.
    """
    
    total = p_posx + p_negx + p_posy + p_negy + p_posz + p_negz
    if not np.isclose(total, 1.0):
        raise ValueError("Sum of probabilities must equal 1.")

    if random_state is not None:
        np.random.seed(random_state)

    probs = [p_posx, p_negx, p_posy, p_negy, p_posz, p_negz]
    moves = np.array([
        [1, 0, 0], [-1, 0, 0],
        [0, 1, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1]
    ])
    steps_idx = np.random.choice(6, size=num_steps, p=probs)
    steps = moves[steps_idx]
    positions = np.vstack((initial_location, np.cumsum(steps, axis=0) + initial_location))
    trajectory = [tuple(p) for p in positions]

    if show_animation:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        def _animate(i):
            ax.clear()
            ax.plot3D(positions[:i + 1, 0], positions[:i + 1, 1], positions[:i + 1, 2], lw=2, color='blue')
            ax.scatter(positions[:i + 1, 0], positions[:i + 1, 1], positions[:i + 1, 2], c='red', marker='d')
            ax.scatter(positions[i, 0], positions[i, 1], positions[i, 2], c='forestgreen', marker='o', s=50)
            ax.set_xlim(positions[:, 0].min() - 1, positions[:, 0].max() + 1)
            ax.set_ylim(positions[:, 1].min() - 1, positions[:, 1].max() + 1)
            ax.set_zlim(positions[:, 2].min() - 1, positions[:, 2].max() + 1)
            ax.set_title("3D Random Walk")

        ani = FuncAnimation(fig, _animate, frames=num_steps + 1, interval=500, blit=False)
        plt.show()

    return trajectory

if __name__ == "__main__":
    
    coords_1d = random_walk_1d(num_steps=30, p_forward=0.6, p_backward=0.4, show_animation=False, random_state=42, initial_location=10)
    print("1D Path:\n", coords_1d)

    coords_2d = random_walk_2d(num_steps=30, p_right=0.3, p_left=0.2, p_up=0.3, p_down=0.2, show_animation=True, random_state=123, initial_location=(10, 5))
    print("2D Path:\n", coords_2d)

    coords_3d = random_walk_3d(num_steps=30, p_posx=0.15, p_negx=0.25, p_posy=0.2, p_negy=0.2, p_posz=0.1, p_negz=0.1, show_animation=True, random_state=7, initial_location=(10, 5, 3))
    print("3D Path:\n", coords_3d)

# Why did the random walk go to therapy?
# Because it couldn’t find its direction in life! 😄