LIMITS = {
    "high": 30,
    "normal": 120,
    "low": 480
}

def is_overdue(elapsed_time, priority="normal"):
    # Проверка на корректность ввода (потребуется в Паре 3)
    if elapsed_time < 0:
        raise ValueError("Elapsed time cannot be negative")
    if priority not in LIMITS:
        raise ValueError("Unknown priority level")
        
    # Базовое правило: просрочка строго больше лимита
    return elapsed_time >= LIMITS[priority]
