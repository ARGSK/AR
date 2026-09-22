from processing.frame_extractor import extract_frames
from models.detector import detect_objects
from shared.utils import seconds_to_timestamp


def process_video(video_name):
    frames = extract_frames(video_name)

    print("\nProcessing results :")

    for frame_number in frames:
        objects = detect_objects(frame_number)

        timestamp = seconds_to_timestamp(frame_number)

        print(
            f"Frame number: {frame_number} | "
            f"Timestamp: {timestamp} | "
            f"Objects: {objects}"
        )