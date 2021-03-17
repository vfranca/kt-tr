from kt_tr import kt_tr


def test_calcula_range_da_lateralidade():
    assert kt_tr.range(100.0, 10.0) == 90.0


def test_calcula_a_metade_do_range():
    assert kt_tr.metade(90.0) == 45.0


def test_calcula_o_terco_do_range():
    assert kt_tr.terco(90.0) == 30.0


def test_calcula_o_meio_da_lateralidade():
    assert kt_tr.meio(100.0, 45.0) == 55.0


def test_calcula_o_terco_superior_da_lateralidade():
    assert kt_tr.terco_sup(100.0, 30.0) == 70.0


def test_calcula_o_terco_inferior_da_lateralidade():
    assert kt_tr.terco_inf(10.0, 30.0) == 40.0
