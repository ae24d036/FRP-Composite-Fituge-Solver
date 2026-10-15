from frp_fatigue import SNModel, predict_blocks

# Synthetic parameters only: not measured FRP material properties.
model = SNModel(reference_stress_mpa=300, reference_cycles=100_000, slope=8)
blocks = [(250, 10000), (220, 20000), (200, 30000)]
for row in predict_blocks(blocks, model):
    print(f"Stress: {row['stress_mpa']} MPa | Nf: {row['predicted_life_cycles']:.0f} | D: {row['cumulative_damage']:.5f}")
