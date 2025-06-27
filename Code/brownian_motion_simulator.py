"""
This Python script simulates and visualizes 1D, 2D, and 3D Brownian motion. It offers options for both animated and static plots, 
customizable parameters like starting position, step size, and the number of moves, and provides statistical output for the generated paths.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def brownian_motion_1d(start=0, thetha=1, num_moves=100, show=True,
                    line_color="blue", marker_color="red", marker_style="D",
                    marker_size=3, save_path=None, random_state=None, animated=True):
    """
    Simulate 1D Brownian motion.

    Parameters:
    - start (float): initial position.
    - thetha (float): std dev of Gaussian steps.
    - num_moves (int): number of steps.
    - show (bool): whether to plot.
    - line_color (str): color of connecting line.
    - marker_color (str): color of points.
    - marker_style (str): style of point markers.
    - save_path (str or None): file path to save plot.
    - random_state (None or Int): if one want's to generate repeatable result
    - animated (bool): if True, plot an animation; otherwise, plot a static image.

    Returns:
    - np.ndarray: positions including start.
    """
    
    if num_moves <= 0:
        raise ValueError("num_moves must be positive")
    if thetha < 0:
        raise ValueError("thetha must be non-negative")
    if random_state is not None:
        np.random.seed(random_state)

    steps = np.random.normal(loc=0, scale=thetha, size=num_moves)
    positions = np.concatenate(([start], start + np.cumsum(steps)))
    steps_axis = np.arange(num_moves + 1)

    def plot_motion(steps_axis, points):
        fig, ax = plt.subplots()
        ax.set_xlabel("Step")
        ax.set_ylabel("Position")
        ax.set_title("Brownian Motion")
        ax.grid(True)
        ax.set_xlim(0, num_moves)
        ax.set_ylim(np.min(points) - thetha, np.max(points) + thetha)

        if animated:
            line, = ax.plot([], [], color=line_color)
            marker, = ax.plot([], [], marker=marker_style, linestyle="", color=marker_color, markersize=marker_size)

            def update(frame):
                line.set_data(steps_axis[:frame], points[:frame])
                marker.set_data(steps_axis[frame-1:frame], points[frame-1:frame])
                return line, marker

            ani = animation.FuncAnimation(fig, update, frames=len(steps_axis), blit=True, interval=100)

        else:
            ax.plot(steps_axis, points, color=line_color)
            ax.plot(steps_axis, points, marker=marker_style, linestyle="", color=marker_color, markersize=marker_size)
            
        if save_path:
            if animated:
                ani.save(save_path, writer='pillow')
            else:
                plt.savefig(save_path)
        else:
            plt.show()

    if show:
        plot_motion(steps_axis, positions)
        print(f"Final position: {positions[-1]:.4f}")
        print(f"Mean position: {positions.mean():.4f}")
        print(f"Variance: {positions.var():.4f}")

    return positions

def brownian_motion_2d(start=(0, 0), thetha=1, num_moves=100, show=True,
                       line_color="blue", marker_color="red", marker_style="D",
                       marker_size=3, save_path=None, random_state=None, animated=True):
    """
    Simulate 2D Brownian motion.

    Parameters:
    - start (tuple of float): initial position (x, y).
    - thetha (float): std dev of Gaussian steps.
    - num_moves (int): number of steps.
    - show (bool): whether to plot.
    - line_color (str): color of connecting line.
    - marker_color (str): color of points.
    - marker_style (str): style of point markers.
    - marker_size (int): size of point markers.
    - save_path (str or None): file path to save plot.
    - random_state (None or int): seed for reproducibility.
    - animated (bool): if True, plot an animation; otherwise, plot a static image.

    Returns:
    - np.ndarray: array of shape (num_moves+1, 2) with 2D positions.
    """
    
    if num_moves <= 0:
        raise ValueError("num_moves must be positive")
    if thetha < 0:
        raise ValueError("thetha must be non-negative")
    if random_state is not None:
        np.random.seed(random_state)

    steps = np.random.normal(loc=0, scale=thetha, size=(num_moves, 2))
    positions = np.vstack([start, start + np.cumsum(steps, axis=0)])

    def plot_motion(points):
        fig, ax = plt.subplots()
        ax.set_xlabel("X Position")
        ax.set_ylabel("Y Position")
        ax.set_title("2D Brownian Motion")
        ax.grid(True)
        ax.set_aspect("equal")
        
        ax.set_xlim(np.min(points[:, 0]) - thetha, np.max(points[:, 0]) + thetha)
        ax.set_ylim(np.min(points[:, 1]) - thetha, np.max(points[:, 1]) + thetha)

        if animated:
            line, = ax.plot([], [], color=line_color)
            marker, = ax.plot([], [], marker=marker_style, linestyle="", 
                              color=marker_color, markersize=marker_size)

            def update(frame):
                line.set_data(points[:frame, 0], points[:frame, 1])
                marker.set_data(points[frame-1:frame, 0], points[frame-1:frame, 1])
                return line, marker

            ani = animation.FuncAnimation(fig, update, frames=len(points), blit=True, interval=100)

        else:
            ax.plot(points[:, 0], points[:, 1], color=line_color)
            ax.plot(points[:, 0], points[:, 1], marker=marker_style, linestyle="", 
                    color=marker_color, markersize=marker_size)

        if save_path:
            if animated:
                ani.save(save_path, writer='pillow')
            else:
                plt.savefig(save_path)
        else:
            plt.show()

    if show:
        plot_motion(positions)
        final_x, final_y = positions[-1]
        print(f"Final position: ({final_x:.4f}, {final_y:.4f})")
        print(f"Mean position: ({positions[:,0].mean():.4f}, {positions[:,1].mean():.4f})")
        print(f"Variance: ({positions[:,0].var():.4f}, {positions[:,1].var():.4f})")

    return positions

def brownian_motion_3d(start=(0, 0, 0), thetha=1, num_moves=100, show=True,
                       line_color="blue", marker_color="red", marker_style="D",
                       marker_size=3, save_path=None, random_state=None, animated=True):
    """
    Simulate 3D Brownian motion.

    Parameters:
    - start (tuple of float): initial (x, y, z) position.
    - thetha (float): std dev of Gaussian steps.
    - num_moves (int): number of steps.
    - show (bool): whether to plot.
    - line_color (str): color of connecting line.
    - marker_color (str): color of points.
    - marker_style (str): style of point markers.
    - marker_size (int): size of point markers.
    - save_path (str or None): file path to save plot.
    - random_state (None or int): seed for reproducibility.
    - animated (bool): if True, plot an animation; otherwise, plot a static image.

    Returns:
    - np.ndarray: array of shape (num_moves+1, 3) with 3D positions.
    """

    if num_moves <= 0:
        raise ValueError("num_moves must be positive")
    if thetha < 0:
        raise ValueError("thetha must be non-negative")
    if random_state is not None:
        np.random.seed(random_state)

    steps = np.random.normal(loc=0, scale=thetha, size=(num_moves, 3))
    positions = np.vstack([start, start + np.cumsum(steps, axis=0)])

    def plot_motion_3d(points):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        ax.set_xlabel("X Position")
        ax.set_ylabel("Y Position")
        ax.set_zlabel("Z Position")
        ax.set_title("3D Brownian Motion")
        ax.grid(True)
        
        ax.set_xlim(np.min(points[:, 0]) - thetha, np.max(points[:, 0]) + thetha)
        ax.set_ylim(np.min(points[:, 1]) - thetha, np.max(points[:, 1]) + thetha)
        ax.set_zlim(np.min(points[:, 2]) - thetha, np.max(points[:, 2]) + thetha)

        if animated:
            line, = ax.plot([], [], [], color=line_color)
            marker, = ax.plot([], [], [], marker=marker_style, linestyle="", 
                               c=marker_color, markersize=marker_size)

            def update(frame):
                line.set_data(points[:frame, 0], points[:frame, 1])
                line.set_3d_properties(points[:frame, 2])
                marker.set_data(points[frame-1:frame, 0], points[frame-1:frame, 1])
                marker.set_3d_properties(points[frame-1:frame, 2])
                return line, marker

            ani = animation.FuncAnimation(fig, update, frames=len(points), blit=False, interval=100)

        else:
            ax.plot(points[:, 0], points[:, 1], points[:, 2], color=line_color)
            ax.scatter(points[:, 0], points[:, 1], points[:, 2],
                       c=marker_color, marker=marker_style, s=marker_size)

        if save_path:
            if animated:
                ani.save(save_path, writer='pillow')
            else:
                plt.savefig(save_path)
        else:
            plt.show()

    if show:
        plot_motion_3d(positions)
        final = positions[-1]
        print(f"Final position: ({final[0]:.4f}, {final[1]:.4f}, {final[2]:.4f})")
        print(f"Mean position: ({positions[:,0].mean():.4f}, {positions[:,1].mean():.4f}, {positions[:,2].mean():.4f})")
        print(f"Variance: ({positions[:,0].var():.4f}, {positions[:,1].var():.4f}, {positions[:,2].var():.4f})")

    return positions


if __name__ == "__main__":    
    pos1d = brownian_motion_1d(start=0, thetha=1, num_moves=100, random_state=42, animated=False)
    pos2d= brownian_motion_2d(start=(0, 0), thetha=2, num_moves=100, random_state=42, animated=True)
    pos3d= brownian_motion_3d(start=(0, 0, 0), thetha=3, num_moves=100, random_state=42, animated=True)
    # i would now like a brownie to eat 
