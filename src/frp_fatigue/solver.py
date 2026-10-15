"""Illustrative log-log S-N model; parameters must be experimentally calibrated."""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class SNModel:
    reference_stress_mpa: float
    reference_cycles: float
    slope: float

    def __post_init__(self):
        if min(self.reference_stress_mpa, self.reference_cycles, self.slope) <= 0:
            raise ValueError("S-N parameters must be positive")

    def cycles_to_failure(self, max_stress_mpa: float) -> float:
        """N = Nref * (Sref/Smax)^slope, at fixed stress ratio R."""
        if max_stress_mpa <= 0 or not math.isfinite(max_stress_mpa):
            raise ValueError("Maximum stress must be finite and positive")
        return self.reference_cycles * (self.reference_stress_mpa / max_stress_mpa) ** self.slope


def miner_damage(blocks, model: SNModel) -> float:
    """Sum n_i/N_i. Blocks are (maximum_stress_MPa, applied_cycles)."""
    total = 0.0
    for stress, cycles in blocks:
        if cycles < 0 or not math.isfinite(cycles):
            raise ValueError("Cycle counts must be finite and nonnegative")
        total += cycles / model.cycles_to_failure(stress)
    return total


def predict_blocks(blocks, model: SNModel):
    """Return each block's life and cumulative Miner damage."""
    result, cumulative = [], 0.0
    for stress, cycles in blocks:
        life = model.cycles_to_failure(stress)
        if cycles < 0 or not math.isfinite(cycles):
            raise ValueError("Cycle counts must be finite and nonnegative")
        cumulative += cycles / life
        result.append({"stress_mpa": stress, "applied_cycles": cycles,
                       "predicted_life_cycles": life, "cumulative_damage": cumulative})
    return result
