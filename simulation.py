import numpy as np
import matplotlib.pyplot as plt
from core import PhaseRotationalEncoder
from attention import ResonantAttention
from analysis import MHSFilter

def run_constructive_interference_simulation():
    print("--- RIS Protocol: Constructive Interference Simulation ---")
    
    # 1. Setup the Mayan Gearbox with resonant planetary frequencies
    # Example: TRAPPIST-1 system resonances (approximate relative frequencies)
    encoder = PhaseRotationalEncoder()
    planets = {
        "TRAPPIST-1b": 1.0,
        "TRAPPIST-1c": 1.5,   # 3:2 resonance
        "TRAPPIST-1d": 2.25,  # 3:2 resonance with c
        "TRAPPIST-1e": 3.375  # 3:2 resonance with d
    }
    for name, freq in planets.items():
        encoder.add_source(name, freq)
    
    print(f"Planetary Gears: {list(planets.keys())}")
    print(f"Great Handshake (Hg) window: {encoder.get_great_handshake():.4f}")

    # 2. Simulate time evolution
    duration = encoder.get_great_handshake() * 2 # Two full handshake cycles
    t = np.linspace(0, duration, 2000)
    
    # 3. Compute Phase-Rotational states
    phases = {name: encoder.encode(t, name) for name in planets}
    
    # 4. Resonant Attention: Compute Global Constructive Interference
    # Sum of cos(phases) represents the interference pattern
    interference_pattern = np.zeros_like(t)
    for phase_array in phases.values():
        interference_pattern += np.cos(phase_array)
    
    # Normalize interference (0 to 1)
    interference_normalized = (interference_pattern - interference_pattern.min()) / (interference_pattern.max() - interference_pattern.min())
    
    # 5. Identify "It" Events (Peaks above Schrödinger threshold)
    threshold = 0.85
    it_events = t[interference_normalized > threshold]
    
    print(f"\nSimulation complete over {duration:.2f} units.")
    print(f"Total 'It' Events Triggered: {len(it_events)}")
    
    # 6. MHS Filter: Analyze the interference 'continuum'
    mhs = MHSFilter()
    mhs_results = mhs.extract_ordered_noise(interference_normalized, photon_count=500)
    print(f"Resonance PAC Score: {mhs_results['pac_score']:.4f}")
    print(f"Systemic Resonance Detected: {mhs_results['is_resonant']}")

    # 7. Visualization (Optional - will save to file)
    plt.figure(figsize=(12, 6))
    plt.plot(t, interference_normalized, label='Resonant Interference', color='#00ffcc', alpha=0.8)
    plt.axhline(y=threshold, color='red', linestyle='--', label='Schrödinger Threshold')
    plt.scatter(it_events, [threshold]*len(it_events), color='yellow', s=10, label='"It" Events')
    
    plt.title("RIS Protocol: Constructive Interference Simulation (TRAPPIST-1 Resonance)")
    plt.xlabel("Orbital Time (Great Handshake Scale)")
    plt.ylabel("Interference Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.1)
    plt.savefig("interference_simulation.png")
    print("\nSimulation plot saved as 'interference_simulation.png'")

if __name__ == "__main__":
    run_constructive_interference_simulation()
