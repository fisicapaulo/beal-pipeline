from beal_pipeline.core.pinch_height_radical import pinch_metrics

def test_pinch_metrics():
    out = pinch_metrics(3,6,3,3,3,3)
    assert "H" in out and "R" in out and "ratio" in out
