

# Signal Processing visualisation script: Multiple Filter applications + Combined Pipeline
# This is a tool for visualisation, how process signaling is performed at a fundamental level

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import (
    gaussian_filter,
    median_filter,
    uniform_filter,
    laplace
)
from mpl_toolkits.mplot3d import Axes3D  # enables 3D plotting

# 1. Create a 2D coordinate grid, -10 by 10
size = 50
x = np.linspace(-10, 10, size)
y = np.linspace(-10, 10, size)
X, Y = np.meshgrid(x, y)

# 2. Create a clean underlying signal
true_signal = np.exp(-(X**2 + Y**2) / 10)


# 3. Adding noise (simulating real data)
noise = 0.35 * np.random.randn(size, size)
signal_noisy = true_signal + noise

# 4. Individual filters (for comparison)
signal_gaussian = gaussian_filter(signal_noisy, sigma=2.0)
signal_median = median_filter(signal_noisy, size=3)
signal_mean = uniform_filter(signal_noisy, size=3)
signal_gm = median_filter(signal_gaussian, size=3)
signal_mg = gaussian_filter(signal_median, sigma=2.0)
signal_laplacian = laplace(signal_noisy)


# 5. Combined filter pipeline:
# Pipeline order:
#   Median → Gaussian → Mean → Gaussian → Laplacian (light)
#
# Why:
#   Median                → remove impulsive outliers first
#   Gaussian              → smooth remaining noise
#   Mean (box)            → additional averaging
#   Gaussian (light)      → remove box artifacts
#   Laplacian (small)     → restore structure / detail
# This is a very common pattern in imaging & signal processing.

# Step 1: Median filter removes spikes / outliers
combined = median_filter(signal_noisy, size=3)

# Step 2: Gaussian smoothing removes remaining random noise
combined = gaussian_filter(combined, sigma=2.0)

# Step 3: Mean (box) filter adds extra averaging
combined = uniform_filter(combined, size=3)

# Step 4: Light Gaussian to smooth box-filter artifacts
combined = gaussian_filter(combined, sigma=1.0)

# Step 5: Subtract a small Laplacian term to restore detail
combined = combined - 0.2 * laplace(combined)

# 6. Collecting all results
signals = [
    signal_noisy,
    signal_gaussian,
    signal_median,
    signal_mean,
    signal_gm,
    signal_mg,
    signal_laplacian,
    combined
]

titles = [
    "Original (Noisy)",
    "Gaussian Filter",
    "Median Filter",
    "Mean (Box) Filter",
    "Gaussian → Median",
    "Median → Gaussian",
    "Laplacian (Edges)",
    "Combined Pipeline (Final)"
]

# 7. Plotting all 8 results in 3D. Can rotate using mouse LMB+rotate
fig = plt.figure(figsize=(22, 10))

for i, (sig, title) in enumerate(zip(signals, titles), start=1):
    ax = fig.add_subplot(2, 4, i, projection='3d')
    ax.plot_surface(X, Y, sig, cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Amplitude')

plt.tight_layout()
plt.show()
