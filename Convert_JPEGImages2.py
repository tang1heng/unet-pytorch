# 图片二值化
from PIL import Image
import os
from tqdm import tqdm

origin_path = "VOCdevkit/VOC2007/SegmentationClass"
output_path = "VOCdevkit/VOC2007/SegmentationClass"
threshold = 10

if __name__ == "__main__":
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_names = os.listdir(origin_path)

    print("正在遍历全部图片。")
    for image_name in tqdm(image_names):
        image = Image.open(os.path.join(origin_path, image_name))
        image = image.convert('L')
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        photo = image.point(table, '1')
        photo.save(os.path.join(output_path, os.path.splitext(image_name)[0] + '.png'))