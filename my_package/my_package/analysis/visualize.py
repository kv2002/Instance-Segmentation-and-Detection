# Imports
import torch
import torchvision.transforms as transforms
import torchvision.utils as utils
from matplotlib import pyplot as plt


def plot_visualization(image, boxes, masks, classes, score, output):  # Write the required arguments
    for i in range(len(masks)):
        masks[i] = masks[i] * 255
        masks[i] = masks[i].astype('uint8')
        masks[i] = masks[i].transpose(1, 2, 0)
    img = torch.from_numpy(image)
    img = img * 255
    img = img.to(torch.uint8)
    labels = [cat + " " + acc for cat, acc in zip(classes, score)]
    labels3 = labels[:3]
    boxes3 = torch.stack(boxes[:3])
    imgbox = utils.draw_bounding_boxes(img, boxes=boxes3, labels=labels3,
                                       colors=[(0, 0, 255), (255, 0, 0), (0, 255, 0)],
                                       font_size=20)
    to_pil = transforms.ToPILImage()
    plt.imshow(to_pil(imgbox))
    plt.axis('off')
    plt.savefig(fname=output[0], bbox_inches='tight', pad_inches=0)
    plt.close()
    plt.imshow(to_pil(img))
    colours = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]
    for i, mask in enumerate(masks):
        if i == 3:
            break
        pil_la = to_pil(mask)
        pil_la = pil_la.convert("LA")
        before = pil_la.getdata()
        after = []
        for item in before:
            if item[0] == 0:
                after.append((255, 0))
            else:
                after.append(item)
        pil_la.putdata(after)
        pil_rgba = pil_la.convert("RGBA")
        white = pil_rgba.getdata()
        coloured = []
        for item in white:
            if item[3] != 0:
                coloured.append(colours[i])
            else:
                coloured.append(item)
        pil_rgba.putdata(coloured)
        plt.imshow(pil_rgba, cmap='jet', alpha=0.5)
    plt.axis('off')
    plt.savefig(fname=output[1], bbox_inches='tight', pad_inches=0)
    plt.close()
# The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
