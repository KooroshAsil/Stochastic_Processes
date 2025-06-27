
# 🎲 Stochastic Process Simulations

> *"Exploring randomness through computational mathematics."*

---

## 📂 Repository Overview

This Python suite simulates and visualizes key stochastic processes using scientific computing libraries. It is designed for both educational and research purposes.

```

Stochastic_Processes
├── brownian_motion_simulator.py   # 1D-3D Brownian motion simulations
├── markov_chain_simulator.py      # Animated Markov chain traversals
├── poisson_process_simulator.py   # Event occurrence simulations
├── random_walk_simulator.py       # Multi-dimensional random walks
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

````

---

## 🧩 Simulation Modules

### 1. **Poisson Process Simulator** (`poisson_process_simulator.py`)
**Purpose:** Simulates discrete event occurrences over time.  
**Key Features:**
- Models event counts in continuous time
- Cumulative trajectory plots
- Configurable rate parameter `λ`

**Usage:**
```python
events = poisson_process(total_time=10, rate=1.5, random_state=42)
````

---

### 2. **Random Walk Simulator** (`random_walk_simulator.py`)

**Purpose:** Simulates 1D, 2D, and 3D random walks.
**Key Features:**

* Directional probability tuning
* Optional animation
* Trajectory coordinate output

**Usage:**

```python
trajectory_3d = random_walk_3d(
    num_steps=100,
    p_posx=0.15, p_negx=0.25,
    show_animation=True
)
```

---

### 3. **Brownian Motion Simulator** (`brownian_motion_simulator.py`)

**Purpose:** Models Wiener processes in 1D–3D space.
**Key Features:**

* Gaussian-distributed steps (θ control)
* Both animated and static visualizations
* Statistical path summary

**Usage:**

```python
path = brownian_motion_2d(
    start=(0, 0),
    thetha=0.5,
    num_moves=500,
    animated=True
)
```

---

### 4. **Markov Chain Simulator** (`markov_chain_simulator.py`)

**Purpose:** Simulates discrete-time memoryless state transitions.
**Key Features:**

* Animated directed graph traversal
* Custom transition matrix input
* Trace of visited states

**Usage:**

```python
states = ["Sunny", "Rainy"]
P = [[0.8, 0.2], [0.3, 0.7]]
trajectory = markov_chain(states, P, "Sunny", steps=20)
```

---

## ⚙️ Installation & Setup

```bash
# Install dependencies
pip install -r requirements.txt
```

**Required Libraries:**

* `numpy`
* `matplotlib`
* `networkx`
* `imageio`
* `pillow`

---

## 📊 Output Previews

> a visualization sample*

### Brownian_motion

![Brownian_motion](https://github.com/user-attachments/assets/4ff47f23-c4ff-4283-99bb-54538d970f36)

### Markov Chain

![Markov Chain Traversal](https://github.com/user-attachments/assets/dd37af01-ddd3-48b3-af67-8a0712b9939e)

### Poisson Process

![Poisson Process](https://github.com/user-attachments/assets/d71b5529-b7ba-4b61-8ae7-6e6f5f9e1ca6)

### 3D Random Walk

![3D Random Walk](https://github.com/user-attachments/assets/34ba2788-8dcb-4505-9ea5-f6ece1f19201)

---

## 🎯 Applications

* **Finance**: Simulating stock prices, market jumps
* **Physics**: Diffusion, heat equations
* **Queueing Theory**: Arrival/service time modeling
* **AI/ML**: Reinforcement learning dynamics
* **Education**: Visualization of abstract probability concepts

---

> **Tip:** All modules support animated plotting with `show_animation=True`.
> **Easter Egg:** Look for subtle jokes in the comments – math has a sense of humor too! 😄
