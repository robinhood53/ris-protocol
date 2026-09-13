import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def run_tame_healing_simulation():
    print("--- RIS Protocol: TAME Healing Simulation (Mars Life Support) ---")
    
    # 1. Initialize the SNN (Synthetic Tissue)
    num_nodes = 100
    target_pressure = 100.0  # The morphological "goal state" (e.g., O2 pressure)
    
    # Create a random graph to represent the neuromorphic chip's synaptic connections
    G = nx.erdos_renyi_graph(num_nodes, 0.1)
    
    # Initialize node weights (each node contributes equally initially)
    for i in G.nodes():
        G.nodes[i]['weight'] = target_pressure / num_nodes
        
    def calculate_system_output(graph):
        return sum(nx.get_node_attributes(graph, 'weight').values())

    # 2. Setup the Timeline
    timesteps = 200
    gcr_strike_time = 50
    nodes_to_kill = 35 # 35% of the chip is scrambled by cosmic radiation
    
    time_series = np.arange(timesteps)
    system_output_history = []
    active_nodes_history = []
    
    # 3. TAME Loop (The Simulation)
    for t in time_series:
        # A. Check for GCR Strike
        if t == gcr_strike_time:
            print(f"[{t}] ALERT: GCR Strike Detected. {nodes_to_kill} nodes destroyed.")
            nodes = list(G.nodes())
            dead_nodes = np.random.choice(nodes, size=nodes_to_kill, replace=False)
            G.remove_nodes_from(dead_nodes)
            
        # B. Measure Current Output
        current_output = calculate_system_output(G)
        system_output_history.append(current_output)
        active_nodes_history.append(G.number_of_nodes())
        
        # C. TAME Healing (Bio-electric Plasticity)
        # If output is below the target state, surviving nodes dynamically increase their weight to compensate
        if t > gcr_strike_time and current_output < target_pressure:
            deficit = target_pressure - current_output
            # Plasticity rate (how fast the system heals)
            healing_factor = 0.05 
            compensation_per_node = (deficit * healing_factor) / G.number_of_nodes()
            
            for i in G.nodes():
                G.nodes[i]['weight'] += compensation_per_node
                
    # 4. Visualization (Edward Tufte style - high data-ink ratio)
    print("\nSimulation complete. Plotting TAME recovery...")
    
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
    
    # Plot 1: System Output (O2 Pressure)
    ax1.plot(time_series, system_output_history, color='#00ffcc', linewidth=2.5, label='System Output (O2 Pressure)')
    ax1.axhline(y=target_pressure, color='white', linestyle='--', alpha=0.5, label='TAME Target State (Homeostasis)')
    ax1.axvline(x=gcr_strike_time, color='#ff3333', linestyle=':', linewidth=2, label='GCR Strike (Hardware Damage)')
    
    ax1.set_title("The Odyssey Protocol: TAME Healing in SNN Life Support", fontsize=14, loc='left', pad=15)
    ax1.set_ylabel("Oxygen Pressure (%)", fontsize=10)
    ax1.grid(True, alpha=0.1)
    ax1.legend(loc='lower right')
    
    # Annotations
    ax1.annotate('Catastrophic Hardware Failure', xy=(gcr_strike_time, 75), xytext=(gcr_strike_time + 10, 85),
                 arrowprops=dict(facecolor='red', arrowstyle='->'), color='#ff3333')
    ax1.annotate('Autonomous TAME Recovery', xy=(150, 99), xytext=(120, 90),
                 arrowprops=dict(facecolor='#00ffcc', arrowstyle='->'), color='#00ffcc')

    # Plot 2: Active Nodes (Hardware Integrity)
    ax2.fill_between(time_series, 0, active_nodes_history, color='#444444', alpha=0.5)
    ax2.plot(time_series, active_nodes_history, color='#888888', linewidth=1.5, label='Active Neuromorphic Nodes')
    ax2.set_ylabel("Node Count", fontsize=10)
    ax2.set_xlabel("Mission Timeline (Timesteps)", fontsize=10)
    ax2.set_ylim(0, 110)
    ax2.legend(loc='lower right')
    
    plt.tight_layout()
    plt.savefig("tame_healing_simulation.png", dpi=300, bbox_inches='tight')
    print("\nVisualization saved as 'tame_healing_simulation.png'")

if __name__ == "__main__":
    run_tame_healing_simulation()
