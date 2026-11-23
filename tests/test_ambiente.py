from ambiente import resumo_ambiente


def test_versao_python_e_313():
    assert resumo_ambiente()["python"].startswith("3.13")
