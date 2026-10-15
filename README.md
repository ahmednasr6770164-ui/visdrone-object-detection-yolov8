# VisDrone Object Detection using YOLOv8

## Project Overview
This project uses YOLOv8s to detect objects in aerial images from the VisDrone dataset. The model identifies 10 object classes, including pedestrians, people, bicycles, cars, vans, trucks, tricycles, buses, and motorcycles.

## Dataset
- **Dataset:** VisDrone2019-DET
- **Source:** [VisDrone Dataset](https://github.com/VisDrone/VisDrone-Dataset)
- **Classes:** 10
- **Training images:** 6,471
- **Validation images:** 548
- **Test images:** 1,610

The dataset is subject to its original license, **CC BY-NC-SA 3.0 IGO**. Please consult the dataset's terms before redistributing or using it commercially.

## Model and Training
- **Model:** YOLOv8s
- **Framework:** Ultralytics
- **Training image size:** 960 × 960
- **Epochs configured:** 80
- **Batch size:** 8
- **Hardware:** NVIDIA Tesla T4 GPU

## Test Results

| Metric | Score |
|---|---:|
| Precision | 52.7% |
| Recall | 41.9% |
| mAP@50 | 40.1% |
| mAP@50–95 | 23.5% |

The model performs best on the car class. Detecting small and crowded objects remains challenging.

## Model Weights
The trained weights are named `VisDrone_YOLO_yolov8s.pt`.

The weights file may be provided separately if it is too large for a convenient browser upload. See the repository for availability.

## Technologies
- Python
- PyTorch
- Ultralytics YOLOv8
- Computer Vision
- Object Detection

## Limitations
The model may miss objects, especially small or overlapping instances. The reported scores reflect evaluation on the provided test split and should not be interpreted as production-level performance.

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Object Detection

Place `VisDrone_YOLO_yolov8s.pt` in the project directory, then run:

```bash
python predict.py --image path/to/your/image.jpg
```

Replace `path/to/your/image.jpg` with the path to your image.

The output image with bounding boxes will be saved in the `runs/detect/predict` directory (or a numbered variant if that directory already exists).

## Project Structure

```text
visdrone-object-detection-yolov8/
├── README.md
├── predict.py
├── requirements.txt
└── VisDrone_YOLO_yolov8s.pt
```

## Author
Ahmed Nasr
