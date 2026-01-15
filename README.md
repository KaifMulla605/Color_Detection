Setup
1. Clone the repository:
````
git clone https://github.com/your-username/color-detection-opencv.git
cd color-detection-opencv
````
2. Create and activate a virtual environment (optional but recommended):
````
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
````
3. Install required dependencies:
````
pip install -r requirements.txt
````
4. Ensure the following files are present:
````
sample.jpg (input image)
color_value.csv (color dataset)
````

Usage
1. Run the application:
````
python color_detection.py
````
2. The image window will open.
3. **Double-click** on any pixel in the image to detect its color.
4. The detected color name and RGB values will be displayed on the image.
5. Press ESC to close the application.
