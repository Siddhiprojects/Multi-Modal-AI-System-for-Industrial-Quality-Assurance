
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import ollama

# -------------------------------
# Streamlit Configuration
# -------------------------------
st.set_page_config(
    page_title="Industrial Quality Inspection",
    layout="wide"
)

st.title("🏭 AI-Powered Industrial Quality Assurance System")
st.caption(
    "Detect manufacturing defects using YOLOv8 and generate AI maintenance reports with Ollama."
)

# -------------------------------
# Load YOLO Model (Cached)
# -------------------------------
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# -------------------------------
# Choose Image Source
# -------------------------------
option = st.radio(
    "Choose Image Source",
    ["Upload Image", "Take Photo"]
)

image = None

if option == "Upload Image":

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

elif option == "Take Photo":

    camera_image = st.camera_input("Take a Photo")

    if camera_image is not None:
        image = Image.open(camera_image)

# -------------------------------
# Run Detection
# -------------------------------
if image is not None:

    # Resize image for faster inference
    MAX_SIZE = (640, 640)
    image.thumbnail(MAX_SIZE)

    # Convert PIL image to NumPy
    img = np.array(image)

    # Run YOLO
    with st.spinner("Detecting defects..."):
        results = model.predict(
            source=img,
            imgsz=640,
            conf=0.25,
            verbose=False
        )

    annotated = results[0].plot()

    st.subheader("Detection Result")
   # -------------------------------
# Display Original and Detection Side by Side
# -------------------------------

# Convert PIL image to NumPy
img = np.array(image)

# Run YOLO
with st.spinner("Detecting defects..."):
    results = model.predict(
        source=img,
        imgsz=640,
        conf=0.25,
        verbose=False
    )

# Get annotated image
annotated = results[0].plot()

# Display images side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 Original Image")
    st.image(
        image,
        width = 500)

with col2:
    st.subheader("🎯 Detection Result")
    st.image(
        annotated,
        width = 500)

    # -------------------------------
    # Extract Defects
    # -------------------------------
    boxes = results[0].boxes
    defects = []

    if len(boxes) > 0:

        for box in boxes:

            cls = int(box.cls)

            confidence = float(box.conf)

            defect_name = model.names[cls]

            defects.append(
                f"{defect_name} (Confidence: {confidence:.2f})"
            )

    else:
        defects.append("No defects detected.")

    # -------------------------------
    # AI Report Generation
    # -------------------------------
prompt = f"""
You are an experienced industrial maintenance engineer.

The following defects were detected:

{chr(10).join(defects)}

Generate a professional maintenance report.

Include:

1. Inspection Summary
2. Defect Description
3. Possible Causes
4. Severity Assessment
5. Recommended Maintenance Actions
6. Preventive Measures

"""

with st.spinner("Generating AI Maintenance Report..."):
    placeholder = st.empty()
    report = ""
    stream = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}],
    stream=True)
    for chunk in stream:
        report += chunk["message"]["content"]
        placeholder.markdown(report)
