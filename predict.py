from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser(description="VisDrone Object Detection")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

model = YOLO("VisDrone_YOLO_yolov8s.pt")

model.predict(
    source=args.image,
    imgsz=960,
    conf=0.25,
    save=True
)
