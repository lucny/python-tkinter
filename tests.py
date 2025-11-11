from happiness.data_loader import load_data
from happiness.filters import find_country, filter_by_region, filter_by_score_range, to_float


def test_load_data(data):
    """Test načítání dat ze souboru CSV."""
    # Ověření, že data jsou načtena jako seznam
    assert isinstance(data, list)
    # Ověření, že seznam není prázdný
    assert len(data) > 0
    # Ověření, že první prvek seznamu je slovník s očekávanými klíči
    assert isinstance(data[0], dict)
    # Ověření, že klíče "Country" a "Happiness score" jsou přítomny
    assert "Country" in data[0]
    # Ověření, že klíč "Happiness score" je přítomen
    assert "Happiness score" in data[0]


def test_find_country(data, country_name="Czechia"):
    """Test vyhledávání země podle názvu."""
    # Vyhledání dat pro Českou republiku
    result = find_country(data, country_name)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že první záznam odpovídá České republice
    assert result[0]["Country"] == country_name


def test_filter_by_region(data, region_name="Western Europe"):
    """Test filtrování podle regionu."""
    # Filtrování dat pro region "Western Europe"
    result = filter_by_region(data, region_name)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že všechny záznamy patří do správného regionu
    for r in result:
        assert r["Regional indicator"] == region_name


def test_filter_by_score_range(data, min_score=7.0, max_score=8.0, score_key="Happiness score"):
    """Test filtrování podle rozsahu skóre."""
    # Filtrování dat podle skóre v rozsahu 7.0 až 8.0
    result = filter_by_score_range(data, min_score, max_score, score_key)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že všechny záznamy mají skóre v zadaném rozsahu
    for r in result:
        score = to_float(r[score_key])
        assert min_score <= score <= max_score


if __name__ == "__main__":
    # Načtení dat pro testy
    try:
        csv_data = load_data("happiness/world_happiness_2023.csv", delimiter=';')
        test_load_data(csv_data)
        test_find_country(csv_data)
        test_filter_by_region(csv_data)
        test_filter_by_score_range(csv_data, score_key="Happiness score")
        print("Všechny testy proběhly úspěšně.")
    except FileNotFoundError:
        print("Chyba: Soubor nebyl nalezen.")
