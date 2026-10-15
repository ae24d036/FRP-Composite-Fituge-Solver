# FRP Composite Fatigue Solver

An open-source **research prototype** for estimating cyclic fatigue life and cumulative damage in fibre-reinforced polymer (FRP) composite coupons.

## Current scope (v0.1)
- Constant-amplitude stress-life (S–N) prediction using a calibrated power-law relationship.
- Variable-amplitude block loading using linear Palmgren–Miner damage accumulation.
- Unit-tested Python API and runnable example.

**Important limitations:** The sample coefficients are synthetic, not experimentally validated. The current model assumes a single calibrated material configuration, laminate layup, environment, loading mode, and stress ratio R. It does **not** resolve ply stresses, account for stress-ratio effects, predict stiffness degradation, or simulate progressive damage/delamination. Do not use for safety-critical design decisions.

## Model
At a fixed stress ratio R, maximum applied stress S (MPa), and calibrated positive exponent b:

`Nf = Nref * (Sref / S)^b`

Miner's linear damage index: `D = sum(n_i / Nf_i)`. `D >= 1` is a simple screening threshold, not a guaranteed failure criterion.

## Quick start
```bash
python -m pip install -e '.[dev]'
python examples/run_example.py
pytest -q
```

## Example
```python
from frp_fatigue import SNModel, miner_damage
model = SNModel(reference_stress_mpa=300, reference_cycles=100_000, slope=8)
print(model.cycles_to_failure(250))
print(miner_damage([(250, 10000), (220, 20000)], model))
```

## Planned research roadmap
1. Import measured fatigue test data (CSV), fit S–N curves, and quantify uncertainty.
2. Add stress-ratio-dependent fatigue models and mean-stress corrections where supported by FRP data.
3. Add classical laminate theory to compute ply-level stresses for specified layups.
4. Evaluate composite-specific residual stiffness/strength degradation models.
5. Benchmark against published and user-provided experimental fatigue datasets.
6. Add plots, reports, and reproducible validation cases.

## Contributing
Issues, tests, benchmark datasets with clear permissions, and model documentation are welcome. Please provide laminate layup, fibre/matrix, manufacturing process, test standard, stress ratio, environment, and loading frequency when sharing results.

## License
MIT. See LICENSE.
