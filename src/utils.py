# Вспомогательные функции
def format_currency(value: float, precision: int = 2) -> str:
    return f"{value:.{precision}f}"