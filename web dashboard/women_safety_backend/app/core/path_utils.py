# app/core/path_utils.py

from typing import List

def refine_path(raw_coords: List[List[float]]):
    """
    Refine a list of [lon, lat] coordinates:
    - Remove consecutive duplicates
    - Round to 6 decimal places
    - Add 'start' and 'end' metadata
    - Return a clean JSON object
    """
    if not raw_coords:
        return {"error": "No coordinates provided"}

    # Round coordinates
    rounded = [[round(lon, 6), round(lat, 6)] for lon, lat in raw_coords]

    # Remove consecutive duplicates
    deduped = [rounded[0]]
    for point in rounded[1:]:
        if point != deduped[-1]:
            deduped.append(point)

    return {
        "start": deduped[0],
        "end": deduped[-1],
        "coordinates": deduped
    }
