from beal_pipeline.core.zsigmondy import zsigmondy_barrier

def test_trivial_exception():
    out = zsigmondy_barrier(5,5,3)
    assert out["exception"] is True
