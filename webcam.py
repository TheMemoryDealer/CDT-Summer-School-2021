import cv2

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break
# cv2.destroyWindow("preview")



# check pytorch installation:
import torch, torchvision
print(torch.__version__, torch.cuda.is_available())
assert torch.__version__.startswith("1.8")   # please manually install torch 1.8 if Colab changes its default version

# Some basic setup:
# Setup detectron2 logger
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random
# from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

window_name = 'image'

im = cv2.imread("./input.jpg")
cv2.imshow(window_name, im)

#waits for user to press any key
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 											# CLICK FUCKIN 0 OR ELSE IT'LL CRASH

#closing all open windows
cv2.destroyAllWindows()


cfg = get_cfg()
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
# Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)
outputs = predictor(im)

# look at the outputs. See https://detectron2.readthedocs.io/tutorials/models.html#model-output-format for specification
print(outputs["instances"].pred_classes)
print(outputs["instances"].pred_boxes)

# We can use `Visualizer` to draw the predictions on the image.
v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imshow(window_name, out.get_image()[:, :, ::-1])
cv2.waitKey(0) 											# CLICK FUCKIN 0 OR ELSE IT'LL CRASH

#closing all open windows
cv2.destroyAllWindows()
