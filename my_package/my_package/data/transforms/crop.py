# Imports
import torchvision.transforms as trans


class CropImage(object):
    """
        Performs either random cropping or center cropping.
    """

    def __init__(self, shape, crop_type='center'):
        """
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        """
        if crop_type == "random":
            self.crop = trans.RandomCrop(shape)
        else:
            self.crop = trans.CenterCrop(shape)
        # Write your code here

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        """
        return self.crop(image)
        # Write your code here
