# CDT-Summer-School-2021

## Setup
* read docs to assemble and connect the hardware https://github.com/TheMemoryDealer/CDT-Summer-School-2021/blob/main/SUMMER%20SCHOOL%20Robotic%20Kit%20Instructions%20Final%20Version.pdf.

* Create a Python virtual environment
```
conda create -n detectron2 python=3.8 -y && conda activate detectron2
```

* More setup
```
pip install pyyaml==5.1 && pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html && pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html
```

* Do this to see if torch installed correctly and cuda is enabled
``` 
python - <<EOF
import torch, torchvision
print(torch.__version__, torch.cuda.is_available())
import cv2 as cv
print(cv.__version__)
EOF
```
expected output:
```
1.7.1 True
4.5.1
```
* Running `python webcam.py` with dummy image **./input.jpg** will give give somethign like:
