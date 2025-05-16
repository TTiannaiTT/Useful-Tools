import json
import matplotlib.pyplot as plt
import numpy as np
import os

# Load training history from JSON file
json_path = r'D:\GitHub\Useful-Tools\Academic_Painting\data\base\training_history.json'

with open(json_path, 'r') as f:
    history = json.load(f)

# Extract training and test accuracy data
train_acc = history['train_acc'][0:34]
test_acc = history['test_acc'][0:34]
epochs = range(1, len(train_acc) + 1)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_acc, 'b-', linewidth=2, label='Training Accuracy')
plt.plot(epochs, test_acc, 'r-', linewidth=2, label='Validation Accuracy')

# Add a vertical line where overfitting starts to occur
# Looking at the data, around epoch 20 the gap starts widening
overfitting_epoch = 20
# plt.axvline(x=overfitting_epoch, color='gray', linestyle='--', alpha=0.7)
# plt.text(overfitting_epoch+0.5, 0.5, 'Overfitting begins', rotation=90, alpha=0.7)

# Fill the gap between curves to highlight overfitting
plt.fill_between(epochs, train_acc, test_acc, where=(np.array(train_acc) > np.array(test_acc)),
                 color='lightgray', alpha=0.5, label='Overfitting Gap')

# Add labels and title
plt.xlabel('Epochs', fontsize=14)
plt.ylabel('Accuracy', fontsize=14)
plt.title('Training and Validation Accuracy Curve (w/o EvAug)', fontsize=16)
plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.7)

# Set y-axis limits for better visualization
plt.ylim(0.3, 1.05)

# Annotate the maximum test accuracy
max_test_acc_epoch = np.argmax(test_acc) + 1
max_test_acc = max(test_acc)
plt.scatter(max_test_acc_epoch, max_test_acc, c='red', s=100, zorder=5)
plt.annotate(f'Max Test Acc: {max_test_acc:.4f}',
             (max_test_acc_epoch, max_test_acc),
             xytext=(max_test_acc_epoch-5, max_test_acc-0.1),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

# Save the figure
save_path =  './overfitting_curve.png'
plt.tight_layout()
plt.savefig(save_path, dpi=300)
plt.show()