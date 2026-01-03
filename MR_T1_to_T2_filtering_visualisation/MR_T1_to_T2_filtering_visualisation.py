import cv2
import numpy as np

# ======================================================
# T2‑like contrast simulation to outline fluids better.
# ======================================================


def simulate_t2_contrast(img):
    # Normalize to float [0,1]
    img_float = cv2.normalize(img.astype("float32"),
                              None, 0.0, 1.0, cv2.NORM_MINMAX)

    # Gamma < 1 brightens dark regions (CSF), darkens bright regions (white matter)
    t2_mapped = np.power(img_float, 0.6)

    # Rescale back to 0–255
    t2_sim = cv2.normalize(t2_mapped, None, 0, 255,
                           cv2.NORM_MINMAX).astype("uint8")
    return t2_sim


# image load: image provided in the folder is 512 x 512 for better visualisation
# ======================================================
# change to own path
path = r"C:\Users\dmitr\Desktop\MR_T1_to_T2_filtering_visualisation\brain_normal_midline_high.jpg"
# ======================================================
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError(
        f"Could not load image at: {path}")  # if cant be found

print("Loaded image shape:", img.shape)

# Normalize original
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype("uint8")

# Apply T2 simulation
t2_sim = simulate_t2_contrast(img_norm)


# Add labels to each image on the viewer
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.7
color = (255,)  # white text
thickness = 2

img_labeled = img_norm.copy()
t2_labeled = t2_sim.copy()

cv2.putText(img_labeled, "Original", (10, 30), font,
            scale, color, thickness, cv2.LINE_AA)
cv2.putText(t2_labeled, "T2 Simulated", (10, 30),
            font, scale, color, thickness, cv2.LINE_AA)


# Combine and display using numpy
combined = np.hstack((img_labeled, t2_labeled))

cv2.imshow("Comparison", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save processed image to the same folder ^ Check path above
output_file = "t2_simulated.png"
cv2.imwrite(output_file, t2_sim)
print("Saved:", output_file)
