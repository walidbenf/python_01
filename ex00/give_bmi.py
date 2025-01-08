def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for each height/weight pair
    """
    if not height or not weight or len(height) != len(weight):
        raise ValueError("Lists must be non-empty and of same length")
    
    try:
        return [w / (h * h) for h, w in zip(height, weight)]
    except TypeError:
        raise ValueError("All elements must be numbers")

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values exceed the limit
    """
    if not isinstance(limit, (int, float)):
        raise ValueError("Limit must be a number")
    
    try:
        return [b > limit for b in bmi]
    except TypeError:
        raise ValueError("All BMI values must be numbers")