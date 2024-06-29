# Breeds_classification
Description:
This project involves using a pre-developed image classifier to identify dog breeds for a citywide dog show. The classifier ensures that only images of actual dogs are registered.

Key Tasks:

Evaluate various image classification algorithms to determine which one most accurately distinguishes between dogs and non-dogs.
Assess the performance of the best algorithm in correctly identifying specific dog breeds.
Measure the runtime of each algorithm, balancing accuracy with computational efficiency.
Technical Details:

Utilized convolutional neural networks (CNNs), specifically AlexNet, VGG, and ResNet architectures, pre-trained on the ImageNet dataset.
Applied a provided classifier function to classify images, ensuring accurate breed identification, even for breeds with similar appearances.

# Running the Project
## Single Run
To classify images from a single run, use the following command:

```python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt```

--dir: The directory containing the images to classify.
--arch: The CNN architecture to use (vgg, alexnet, or resnet).
--dogfile: The file containing the list of dog names.

## Batch Execution
For batch execution, run the following script:

```sh run_models_batch.sh```

This script will automate the process of running multiple classifications in batches.
