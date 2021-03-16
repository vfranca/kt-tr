from kt_tr import kt_tr as tr


def test_calcula_range_da_lateralidade():
    assert tr.range(100.0, 10.0) == 90.0
