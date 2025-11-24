from beal_pipeline.core.lte import lte_check

def test_lte_placeholder():
    out = lte_check(12,18,3,3)
    assert "note" in out
