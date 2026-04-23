from core import PhaseRotationalEncoder
from analysis import MHSFilter
from attention import ResonantAttention
from recursive import PhaseSlipIntegrator
from ingestion import MelbourneProtocol
from scheduler import SolarMidnightScheduler
import numpy as np

def run_ris_protocol():
    print("--- Initializing RIS Protocol ---")
    
    # 1. Core: Mayan Gearbox
    encoder = PhaseRotationalEncoder()
    encoder.add_source("TOI-178b", 0.523)
    encoder.add_source("TOI-178c", 0.312)
    print(f"Great Handshake Window (Hg): {encoder.get_great_handshake():.4f}")

    # 2. Ingestion: Melbourne Protocol
    ingestor = MelbourneProtocol()
    print("Melbourne Protocol Active. Monitoring resonant chains...")

    # 3. Scheduling
    scheduler = SolarMidnightScheduler()
    scheduler.schedule_listen()

    # 4. Analysis & Attention (Simulation for demo)
    print("\n--- Running Real-time Signal Alignment ---")
    mhs = MHSFilter()
    attn = ResonantAttention(schrodinger_threshold=0.7)
    integrator = PhaseSlipIntegrator()

    # Synthetic stream
    t = np.linspace(0, 1, 100)
    data = np.random.normal(0, 0.05, 100) + 0.02 * np.sin(2 * np.pi * 5 * t)
    
    analysis_results = mhs.extract_ordered_noise(data, photon_count=1000)
    print(f"Resonance Detected: {analysis_results['is_resonant']}")
    
    if analysis_results['is_resonant']:
        # Attempt Phase Alignment
        query_phi = encoder.encode(0.5, "TOI-178b")
        key_phi = encoder.encode(0.5, "TOI-178c")
        
        attn_results = attn.compute(query_phi, key_phi)
        print(f"Attention Event: {attn_results['event']} (Strength: {attn_results['alignment_strength']:.4f})")
        
        # Drift Correction
        drift_results = integrator.analyze_signal(query_phi, key_phi, elapsed_days=365)
        print(f"Drift Analysis: {drift_results['status']}")

    print("\n--- RIS Protocol Operational ---")

if __name__ == "__main__":
    run_ris_protocol()
