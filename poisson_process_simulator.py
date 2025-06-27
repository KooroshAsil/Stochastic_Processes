import numpy as np
import matplotlib.pyplot as plt

def poisson_process(total_time: int = 10, rate: float = 1.0, random_state=None) -> list:
    
    """
    Simulate a Poisson process with fixed unit time intervals and plot event counts per interval
    along with cumulative events.

    Args:
        total_time (int): Total number of discrete time units to simulate (e.g., seconds, days).
        rate (float): Event rate λ, meaning expected number of events per one unit time interval.
        random_state (int or None): Seed for reproducibility.

    Returns:
        list of tuples: Each tuple contains (time, event_flag, cumulative_count), where
                        event_flag is 1 if at least one event occurred in that interval, else 0.
    """
    
    if random_state is not None:
        np.random.seed(random_state)

    num_steps = total_time
    events = np.random.poisson(rate, size=num_steps)
    times = np.arange(1, total_time + 1)
    cumulative_counts = events.cumsum()
    
    # event_flag is 1 if any event occurred in that second, else 0
    event_flags = (events > 0).astype(int)
    
    trajectory = list(zip(times, event_flags, cumulative_counts))

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(times, events, width=0.8, color='royalblue', edgecolor='black', label='Events per Interval')
    ax.plot(times, cumulative_counts, marker='o', color='tomato', linewidth=2, label='Cumulative Events')

    ax.set_xlim(0, total_time + 1)
    ax.set_ylim(0, max(events.max(), cumulative_counts.max()) + 3)
    ax.set_xlabel("Time (unit intervals)", fontsize=12)
    ax.set_ylabel("Number of Events", fontsize=12)
    ax.set_title(f"Poisson Process Simulation (λ={rate} events per unit time)", fontsize=14)

    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

    ax.set_xticks(times)
    ax.set_xticklabels([str(t) for t in times], rotation=45, fontsize=9)

    ax.legend()

    plt.tight_layout()
    plt.show()

    return trajectory


if __name__ == "__main__":
    
    poisson_events = poisson_process(total_time=10, rate=1.5, random_state=42)
    print("Poisson Process Event Counts (time, event_flag, cumulative):\n", poisson_events)