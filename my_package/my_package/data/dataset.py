# Imports
import json

import numpy as np
from PIL import Image


class Dataset(object):
    """
        A class for the dataset that will return data items as per the given index
    """

    def __init__(self, annotation_file, transforms=None):
        """
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        """
        self.data = []
        self.transforms = transforms
        with open(annotation_file, 'r') as json_file:
            self.json_list = list(json_file)
            for obj in self.json_list:
                self.data.append(json.loads(obj))

    def __len__(self):
        """
            return the number of data points in the dataset
        """
        return len(self.data)

    def __getitem__(self, idx):
        """
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following,
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (won't be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        """
        img = Image.open('./data/' + self.data[idx]['img_fn'])
        png_ann = Image.open('./data/' + self.data[idx]['png_ann_fn'])
        if self.transforms is not None:
            for transform in self.transforms:
                img = transform(img)
        img = np.asarray(img)
        img = img.astype('float32') / 255.0
        img = img.transpose(2, 0, 1)

        png_ann = np.asarray(png_ann)
        png_ann = png_ann.astype('float32') / 255.0
        png_ann = np.expand_dims(png_ann, axis=0)

        gt_bboxes = []
        for bbox in self.data[idx]['bboxes']:
            gt_bboxes.append([bbox['category']] + bbox['bbox'])

        return {'image': img, 'gt_png_ann': png_ann, 'gt_bboxes': gt_bboxes}
