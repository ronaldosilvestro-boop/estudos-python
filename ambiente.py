import platform
import sys
from datetime import datetime

import pandas as pd


def resumo_ambiente() -> dict[str, str]:
    """Retorna informações básicas do ambiente Python atual."""
    return {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "python": platform.python_version(),
        "sistema": platform.platform(),
        "pandas": pd.__version__,
        "executavel": sys.executable,
    }


if __name__ == "__main__":
    for chave, valor in resumo_ambiente().items():
        print(f"{chave:<12}{valor}")
