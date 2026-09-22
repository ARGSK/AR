from config import MIN_CONFIDENCE


def detect_objects(frame_number):
    objects = []

    if frame_number == 20:
        objects.append({
            "class": "person",
            "confidence": 0.92
        })

    if frame_number == 40:
        objects.append({
            "class": "car",
            "confidence": 0.87
        })

    return [
        obj for obj in objects
        if obj["confidence"] >= MIN_CONFIDENCE
    ]