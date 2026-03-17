COMMODITIES = ["Wheat", "Coarse Grains", "Rice", "Oilseeds", "Cotton", "Sugar"]
COUNTRIES = ["USA", "Ukraine", "India", "China", "Brazil", "Argentina"]


def detect_metadata(chunk):
    try:
        return {
            "commodity": [c for c in COMMODITIES if c.lower() in chunk.lower()]
            or ["General"],
            "country": [c for c in COUNTRIES if c.lower() in chunk.lower()]
            or ["Global"],
        }
    except Exception as e:
        print("[metadata] failed to detect metadata:", e)
        return {"commodity": ["General"], "country": ["Global"]}
