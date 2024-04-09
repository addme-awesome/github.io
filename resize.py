from PIL import Image

def resize_to_match(input_path, target_path, output_path):
    """
    将输入图像调整到与目标图像相同的大小，并保存到输出路径
    :param input_path: 输入图像路径
    :param target_path: 目标图像路径，用于获取目标大小
    :param output_path: 输出图像路径
    """
    # 打开输入图像和目标图像
    with Image.open(input_path) as input_img, Image.open(target_path) as target_img:
        # 获取目标图像的尺寸
        target_size = target_img.size
        # 调整输入图像的大小为目标尺寸
        resized_input_img = input_img.resize(target_size)
        # 保存调整后的图像
        resized_input_img.save(output_path)

# 示例用法
input_image_path = "D:\BaiduSyncdisk\git仓库\Addme\page\images\edit_4.jpg"  # 输入图像路径
target_image_path = "D:\BaiduSyncdisk\git仓库\Addme\page\images\gt_4.jpg"  # 目标图像路径
output_image_path = "D:\BaiduSyncdisk\git仓库\Addme\page\images\edit_4.jpg"  # 输出图像路径

resize_to_match(input_image_path, target_image_path, output_image_path)
