import cv2
import pandas as pd
import numpy as np

# Configuration
IMAGE_PATH = "sample.jpg"
COLOR_VALUE_CSV = "color_value.csv"
WINDOW_NAME = "Color Detection"

# loading and reading color csv file
colors_df = pd.read_csv(COLOR_VALUE_CSV)

# Renaming features
colors_df.rename(columns={
    "Color": "color",
    "Color Name": "color_name",
    "hexadecimal value": "hex",
    "Red": "R",
    "Green": "G",
    "Blue": "B"
}, inplace=True)

# converting RGB to numeric values
colors_df[["R", "G", "B"]] = colors_df[["R", "G", "B"]].astype(int)

# loading sample image
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

image = cv2.resize(image, (800, 600))

# global state variables
clicked = False
click_x = click_y = 0
r = g = b = 0

# color detecion function
def detect_color(R, G, B):

    min_dist = float("inf")
    detected_color = "Unknown"

    R, G, B = int(R), int(G), int(B)

    for _, row in colors_df.iterrows():
        dist = (
            abs(R - row["R"]) +
            abs(G - row["G"]) +
            abs(B - row["B"])
        )
        if dist < min_dist:
            min_dist = dist
            detected_color = row["color_name"]

    return detected_color

# mouse click function
def mouse_event(event, x, y, flags, param):
    global clicked, r, g, b, click_x, click_y

    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        click_x, click_y = x, y
        b, g, r = image[y, x]

# loop function
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, mouse_event)

while True:
    clone_img = image.copy()

    if clicked:
        # color rectangle preview
        cv2.rectangle(
            clone_img,
            (20, 20),
            (600, 70),
            (int(b), int(g), int(r)),
            -1
        )

        color_name = detect_color(r, g, b)
        text = f"{color_name} | R={r} G={g} B={b}"

        # handling extreme values
        brightness = int(r) + int(g) + int(b)
        text_color = (0, 0, 0) if brightness > 500 else (255, 255, 255)

        cv2.putText(
            clone_img,
            text,
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            text_color,
            2,
            cv2.LINE_AA
        )

    cv2.imshow(WINDOW_NAME, clone_img)

    # press esc to exit
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()