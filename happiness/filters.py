def find_country(data, name):
    """Vyhledá zemi podle názvu (case-insensitive)."""
    return [r for r in data if name.lower() in r["Country name"].lower()]

def filter_by_region(data, region):
    """Vrátí všechny země v daném regionu."""
    return [r for r in data if r["Regional indicator"] == region]

def filter_by_score_range(data, min_score, max_score):
    """Filtr podle hodnoty štěstí."""
    def to_float(x):
        try:
            return float(x)
        except:
            return None
    return [r for r in data if (v:=to_float(r["Ladder score"])) and min_score <= v <= max_score]
