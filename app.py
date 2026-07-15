# ==========================================
# Import Libraries
# ==========================================
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
import cv2
from fastapi import FastAPI
from ultralytics import YOLO

app = FastAPI()

model = YOLO("bestv11s.pt")

@app.get("/")
def home():

    return {

        "message":"Road Damage Detection API"

    }


# ==========================================
# Upload Video
# ==========================================

@app.post("/predict-video")
async def predict_video(file: UploadFile = File(...)):

    input_path = f"uploads/{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ==========================
    # Read Video
    # ==========================

    cap = cv2.VideoCapture(input_path)
    # ==========================================
    # Video Properties
    # ==========================================

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = "outputs/output.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(

    output_path,

    fourcc,

    fps,

    (width, height))
    
    frame_count = 0

    while True:

        success, frame = cap.read()

        if not success:
            break
        frame_count+=1

    # ==========================
    # YOLO Prediction
    # ==========================

        results = model(

            frame,

            verbose=False)


        annotated_frame = results[0].plot()

        writer.write(annotated_frame)

    cap.release()
    writer.release()

    return FileResponse(

    path=output_path,

    media_type="video/mp4",

    filename="road_damage_detection.mp4"

)
     

# ==========================================
# Predict Image
# ==========================================

@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):

    # Save uploaded image
    input_path = f"uploads/{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read image
    image = cv2.imread(input_path)

    if image is None:
         return {
        "error": "Cannot read image."
        }

    results = model(
       image,
       imgsz=640,
       conf=0.25,
       verbose=False
    )

    annotated_image = results[0].plot()

    output_path = os.path.join(
       "outputs",
       f"pred_{file.filename}"
    )

    cv2.imwrite(output_path, annotated_image)

    return FileResponse(
       output_path,
       media_type="image/jpeg",
       filename=f"pred_{file.filename}"
    )

# model = YOLO('best.pt')

# image = 'China_Drone_000035.png'

# results = model(
#     image,
#     imgsz=640,
#     conf=0.25,
#     verbose=False
# )

# print(len(results[0].boxes))


