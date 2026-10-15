import pytest
from frp_fatigue import SNModel, miner_damage, predict_blocks

def test_reference_point():
    m = SNModel(300, 100000, 8)
    assert m.cycles_to_failure(300) == pytest.approx(100000)

def test_miner_damage():
    m = SNModel(300, 100000, 8)
    assert miner_damage([(300, 25000), (300, 25000)], m) == pytest.approx(0.5)

def test_invalid_stress():
    with pytest.raises(ValueError):
        SNModel(300, 100000, 8).cycles_to_failure(0)

def test_cumulative():
    rows = predict_blocks([(300, 10000), (300, 20000)], SNModel(300, 100000, 8))
    assert rows[-1]['cumulative_damage'] == pytest.approx(0.3)
