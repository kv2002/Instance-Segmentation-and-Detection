# Imports
import torchvision.transforms as trans


class FlipImage(object):
    """
        Flips the image.
    """

    def __init__(self, flip_type='horizontal'):
        """
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        """
        if flip_type == 'vertical':
            self.flip = trans.RandomVerticalFlip(p=1.0)
        else:
            self.flip = trans.RandomHorizontalFlip(p=1.0)
        # Write your code here

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        """
        return self.flip(image)
        # Write your code here
