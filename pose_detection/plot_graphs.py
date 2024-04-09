import numpy as np
import matplotlib.pyplot as plt

not_live = False

if not_live:
    # Load the saved NumPy arrays
    left_hip_coords = np.load('left_hip_coords.npy')
    right_hip_coords = np.load('right_hip_coords.npy')
    left_knee_coords = np.load('left_knee_coords.npy')
    right_knee_coords = np.load('right_knee_coords.npy')
    left_ankle_coords = np.load('left_ankle_coords.npy')
    right_ankle_coords = np.load('right_ankle_coords.npy')
else:
    # Load the saved NumPy arrays
    left_hip_coords = np.load('left_hip_coords_live.npy')
    right_hip_coords = np.load('right_hip_coords_live.npy')
    left_knee_coords = np.load('left_knee_coords_live.npy')
    right_knee_coords = np.load('right_knee_coords_live.npy')
    left_ankle_coords = np.load('left_ankle_coords_live.npy')
    right_ankle_coords = np.load('right_ankle_coords_live.npy')


# Plot the x, y, and z coordinates for each landmark
fig, axs = plt.subplots(3, 2, figsize=(15, 10))

# Left Hip
axs[0, 0].plot(left_hip_coords[:, 0], label='X')
axs[0, 0].plot(left_hip_coords[:, 1], label='Y')
axs[0, 0].plot(left_hip_coords[:, 2], label='Z')
axs[0, 0].set_title('Left Hip Coordinates')
axs[0, 0].legend()

# Right Hip
axs[0, 1].plot(right_hip_coords[:, 0], label='X')
axs[0, 1].plot(right_hip_coords[:, 1], label='Y')
axs[0, 1].plot(right_hip_coords[:, 2], label='Z')
axs[0, 1].set_title('Right Hip Coordinates')
axs[0, 1].legend()

# Left Knee
axs[1, 0].plot(left_knee_coords[:, 0], label='X')
axs[1, 0].plot(left_knee_coords[:, 1], label='Y')
axs[1, 0].plot(left_knee_coords[:, 2], label='Z')
axs[1, 0].set_title('Left Knee Coordinates')
axs[1, 0].legend()

# Right Knee
axs[1, 1].plot(right_knee_coords[:, 0], label='X')
axs[1, 1].plot(right_knee_coords[:, 1], label='Y')
axs[1, 1].plot(right_knee_coords[:, 2], label='Z')
axs[1, 1].set_title('Right Knee Coordinates')
axs[1, 1].legend()

# Left Ankle
axs[2, 0].plot(left_ankle_coords[:, 0], label='X')
axs[2, 0].plot(left_ankle_coords[:, 1], label='Y')
axs[2, 0].plot(left_ankle_coords[:, 2], label='Z')
axs[2, 0].set_title('Left Ankle Coordinates')
axs[2, 0].legend()

# Right Ankle
axs[2, 1].plot(right_ankle_coords[:, 0], label='X')
axs[2, 1].plot(right_ankle_coords[:, 1], label='Y')
axs[2, 1].plot(right_ankle_coords[:, 2], label='Z')
axs[2, 1].set_title('Right Ankle Coordinates')
axs[2, 1].legend()

# Adjust layout
plt.tight_layout()
plt.show()
