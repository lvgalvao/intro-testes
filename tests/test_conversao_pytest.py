from app.conversao import converte_f_para_c, converte_c_para_f


def test_converte_deve_retornar_0_quando_receber_32():
    assert converte_f_para_c(32) == 0


def test_converte_deve_retornar_40_quando_receber_40():
    assert converte_f_para_c(-40) == -40


def test_converte_deve_retornar_32_quando_receber_0():
    assert converte_c_para_f(0) == 32.0


def test_converte_deve_retornar_50_quando_receber_10():
    assert converte_c_para_f(10) == 50
