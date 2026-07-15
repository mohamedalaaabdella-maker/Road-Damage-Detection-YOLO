# 🛣️ Road Damage Detection using YOLO

A Computer Vision project for automatic road damage detection using the YOLO (You Only Look Once) object detection algorithm.

The project focuses on training and comparing multiple YOLO models to identify the best balance between detection accuracy and inference speed for real-world applications.

---

# 📌 Project Overview

Road damage detection is an important task for smart transportation systems and infrastructure maintenance.

In this project, multiple YOLO models were trained and evaluated on a road damage dataset to detect different types of road defects.

The models were compared based on detection performance and inference speed to determine the most suitable model for deployment.

---

# 📂 Dataset

The dataset contains annotated road images with bounding boxes representing different road damage categories.

The dataset was divided into:

- Training Set
- Validation Set
- Test Set

---

# 🧹 Data Preparation

The following preprocessing steps were applied:

- Image verification
- Dataset organization
- YOLO annotation format
- Train / Validation / Test split

---

# 🤖 Models Trained

Three YOLO models were trained and compared:

- YOLO11n
- YOLO11s
- YOLO11m

Each model was trained using the same dataset and training configuration for a fair comparison.

---

# 📊 Model Evaluation

The models were evaluated using:

- mAP@50
- mAP@50-95
- Precision
- Recall
- Inference Time
- FPS (Frames Per Second)

A performance benchmark was also conducted on randomly selected test images to compare real-world inference speed.

---

# 🏆 Best Model

After comparing all models, the best-performing model was selected based on the trade-off between:

- Detection Accuracy
- Speed
- Computational Cost

---

# 🖼️ Inference Results

The trained model can:

- Detect road damages in images
- Draw bounding boxes around detected damages
- Display confidence scores
- Process images efficiently

---

# 🛠️ Technologies Used

- Python
- Ultralytics YOLO
- PyTorch
- OpenCV
- NumPy
- Matplotlib
- Pandas

---


# 🚀 Future Improvements

- Train on larger road damage datasets
- Real-time video detection
- Deploy using Streamlit
- Edge device optimization
- Road inspection dashboard

---

# 👨‍💻 Author

**Mohamed Alaa Abdella**

Computer Engineering Student

AI & Machine Learning Enthusiast

Interested in:

- Computer Vision
- Deep Learning
- Object Detection
- Autonomous Systems
