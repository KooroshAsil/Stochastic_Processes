import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyArrowPatch

def markov_chain(states, transition, initial_state, steps=10, random_state=None, show_animation = False):
    
    """
    Simulates a Markov chain traversal.
    Args:
        states (list): List of state labels.
        transition (list[list[float]]): Transition probability matrix.
        initial_state (str): Starting state.
        steps (int): Number of steps to simulate.
        random_state (int, optional): Seed for reproducibility.
    Returns:
        list: Sequence of visited states.
    """
    
    def animate_traversal(states, transitions, transition_matrix):
        
        """
        Helper function Creates an animation of a Markov chain traversal over a directed graph,
        showing transition probabilities as edge weights and omitting zero-probability edges.
        All bidirectional edges are curved equally.
        Args:
            states (list): List of state labels.
            transitions (list): Ordered list of visited states.
            transition_matrix (list[list[float]]): Transition probability matrix.
        Returns:
            FuncAnimation: Matplotlib animation object.
            
        ANIMATAION PLOTTING IS DONE BY AI AFTER A HUGE AMOUNT OF ARGUE 
        i have no interest in writing such confusing codes my self and messing with lots of details
        feel free to change it as you like
        that is why i left the comments.
        """
        
        P = np.array(transition_matrix)
        G = nx.DiGraph()
        G.add_nodes_from(states)

        # Store edge details including curvature and label
        edge_details = {}

        # Determine curvature: self-loops small, bidirectional curved, else straight
        for i, u in enumerate(states):
            for j, v in enumerate(states):
                p = P[i, j]
                if p <= 0:
                    continue
                G.add_edge(u, v)
                if i == j:
                    rad = 0.1
                elif P[j, i] > 0:
                    rad = 0.15
                else:
                    rad = 0.0
                edge_details[(u, v)] = {'label': f"{p:.2f}", 'rad': rad}

        pos = nx.spring_layout(G, seed=42)
        fig, ax = plt.subplots(figsize=(8, 6))

        def draw_edges(ax, edges, color, lw):
            for (u, v), det in edges.items():
                x1, y1 = pos[u]
                x2, y2 = pos[v]
                rad = det['rad']
                if u != v:
                    arrow = FancyArrowPatch(
                        (x1, y1), (x2, y2),
                        connectionstyle=f"arc3,rad={rad}",
                        arrowstyle='-|>',
                        mutation_scale=20,
                        lw=lw,
                        color=color,
                        axes=ax
                    )
                    ax.add_patch(arrow)
                else:
                    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u, v)],
                                        edge_color=color, arrows=True, width=lw)

        def draw_labels(ax):
            for (u, v), det in edge_details.items():
                x1, y1 = pos[u]
                x2, y2 = pos[v]
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                dx, dy = x2 - x1, y2 - y1
                norm = np.hypot(dx, dy)
                rad = det['rad']
                if u == v:
                    x_label, y_label = x1, y1 + 0.12
                elif norm == 0:
                    x_label, y_label = mid_x, mid_y
                else:
                    px, py = -dy / norm, dx / norm
                    offset = 0.15 if rad != 0 else 0.05
                    x_label = mid_x + px * offset
                    y_label = mid_y + py * offset
                ax.text(x_label, y_label, det['label'], ha='center', va='center', fontsize=9,
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

        def update(frame):
            ax.clear()
            # Draw all nodes in base color
            nx.draw_networkx_nodes(G, pos, ax=ax, node_color='palegreen', node_size=600)
            nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold')

            # Draw all edges in gray
            draw_edges(ax, edge_details, color='dimgray', lw=1.5)
            draw_labels(ax)

            path = transitions[:frame+1]
            # Edges visited before current (blue)
            if len(path) > 1:
                past_edges = { (a, b): edge_details[(a, b)] for a, b in zip(path[:-2], path[1:-1]) }
                draw_edges(ax, past_edges, color='blue', lw=2)

                # Current traversed edge in orchid
                current_edge = { (path[-2], path[-1]): edge_details[(path[-2], path[-1])] }
                draw_edges(ax, current_edge, color='darkorchid', lw=3)
                title = f"Step {frame}: {path[-2]} → {path[-1]}"
            else:
                title = f"Step {frame}: start at {path[0]}"

            # Highlight current node in indigo
            nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=[path[-1]], node_color='tomato', node_size=600)

            ax.set_title(title, fontsize=16)
            ax.axis('off')

        ani = FuncAnimation(fig, update, frames=len(transitions), interval=1000, repeat=True)
        update(0)
        return ani

    # done by my self 
    
    if random_state is not None:
        np.random.seed(random_state)
    transition = np.array(transition)
    current = initial_state
    trajectory = [current]
    for _ in range(steps):
        i = states.index(current)
        current = np.random.choice(states, p=transition[i])
        trajectory.append(current)    
    
    if show_animation:
        anim = animate_traversal(states, trajectory, P)
        plt.show()

    return trajectory


if __name__ == "__main__":
    
    states = ["A", "B", "C", "D"]
    P = [
        [0.15, 0.7 , 0.15, 0   ],
        [0.15, 0.05, 0.6 , 0.2 ],
        [0.3 , 0.1 , 0.5 , 0.1 ],
        [0   , 0.4 , 0.1 , 0.5 ]
    ]
    
    trajectory = markov_chain(states, P, states[0], steps=15, random_state=42, show_animation=True)
    print(trajectory)
    # Why did the Markov chain break up with its partner? 
    # Because it had no memory of their relationship. 😅