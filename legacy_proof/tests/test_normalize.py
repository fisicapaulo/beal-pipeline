from beal_pipeline.core.normalize import normalize_row
from types import SimpleNamespace

def test_normalize_basic():
    row = SimpleNamespace(id=1, x=6, y=9, z=3, a=3, b=3, c=3)
    out = normalize_row(row)
    assert out["status"] == "ok"
    assert out["x"] == 2 and out["y"] == 3 and out["z"] == 1

def test_discard_exponent():
    row = SimpleNamespace(id=2, x=2, y=3, z=1, a=2, b=3, c=3)
    out = normalize_row(row)
    assert out["status"] == "discard"
