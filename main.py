from config import APP_NAME
from processing.video_processor import process_video


def main():
    print(f"=== {APP_NAME} ===")

    video_name = "camera_01.mp4"

    process_video(video_name)


if __name__ == "__main__":
    main()