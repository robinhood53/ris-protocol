import numpy as np
import math
from functools import reduce

class PhaseRotationalEncoder:
    """
    Core Module: The Mayan Gearbox (Phase-Rotational Encoding)
    Replaces standard positional encodings with phase-rotational logic.
    """
    def __init__(self, frequencies=None):
        """
        frequencies: dict mapping input source (e.g., 'Visual', 'TOI-178b') to Orbital Frequency (omega).
        """
        self.frequencies = frequencies or {}
        self.hg_window = None

    def add_source(self, name, omega):
        self.frequencies[name] = omega
        self._calculate_great_handshake()

    def _calculate_great_handshake(self):
        """
        Calculate the Least Common Multiple (LCM) for all input frequencies 
        to define the 'Great Handshake' (Hg) window.
        
        Hg = LCM(T_i) where T_i = 1 / omega_i
        For practical implementation, we use a precision factor to handle floats.
        """
        if not self.frequencies:
            self.hg_window = 0
            return

        periods = [1.0 / omega for omega in self.frequencies.values()]
        
        # Scaling to integers for LCM calculation (precision of 10^-6)
        precision = 1_000_000
        int_periods = [int(p * precision) for p in periods]
        
        def lcm(a, b):
            if a == 0 or b == 0: return 0
            return abs(a * b) // math.gcd(a, b)
        
        lcm_scaled = reduce(lcm, int_periods)
        self.hg_window = lcm_scaled / precision

    def encode(self, time_steps, source_name):
        """
        Encodes a source as a phase rotation at a given time.
        phi(t) = (omega * t) % (2 * pi)
        """
        omega = self.frequencies.get(source_name)
        if omega is None:
            raise ValueError(f"Source {source_name} not found in frequencies.")
        
        return (omega * time_steps) % (2 * np.pi)

    def get_great_handshake(self):
        return self.hg_window

if __name__ == "__main__":
    # Example usage
    encoder = PhaseRotationalEncoder()
    # Frequencies for TOI-178 system (relative)
    encoder.add_source("TOI-178b", 0.523)
    encoder.add_source("TOI-178c", 0.312)
    print(f"Great Handshake (Hg) window: {encoder.get_great_handshake()}")
