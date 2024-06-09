from PIL import Image, ImageDraw, ImageFont
import imageio

# 帧数和图像尺寸
frame_count = 10
width, height = 200, 200

# 创建图像帧的列表
frames = []

# 设置文本内容
text = "Hello!"

# 创建一个说话过程中不同嘴部状态的变换图
for i in range(frame_count):
    # 创建一个空白图像
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 画脸
    face_radius = 80
    face_center = (width // 2, height // 2)
    draw.ellipse((face_center[0] - face_radius, face_center[1] - face_radius,
                  face_center[0] + face_radius, face_center[1] + face_radius), fill=(255, 255, 0), outline=(0, 0, 0))

    # 画眼睛
    eye_radius = 10
    left_eye_center = (width // 2 - 30, height // 2 - 30)
    right_eye_center = (width // 2 + 30, height // 2 - 30)
    draw.ellipse((left_eye_center[0] - eye_radius, left_eye_center[1] - eye_radius,
                  left_eye_center[0] + eye_radius, left_eye_center[1] + eye_radius), fill=(0, 0, 0))
    draw.ellipse((right_eye_center[0] - eye_radius, right_eye_center[1] - eye_radius,
                  right_eye_center[0] + eye_radius, right_eye_center[1] + eye_radius), fill=(0, 0, 0))

    # 画嘴，根据当前帧确定嘴的位置
    mouth_width = 40
    mouth_height = (i % 2) * 10  # 交替改变嘴的高度
    mouth_top_left = (width // 2 - mouth_width // 2, height // 2 + 20)
    mouth_bottom_right = (width // 2 + mouth_width // 2, height // 2 + 20 + mouth_height)
    draw.ellipse((mouth_top_left[0], mouth_top_left[1],
                  mouth_bottom_right[0], mouth_bottom_right[1]), fill=(0, 0, 0))

    # 添加文本
    draw.text((width // 2 - 30, height // 2 + 50), text, fill=(0, 0, 0))

    # 将图像加入到帧列表
    frames.append(img)

# 保存动画为GIF
output_file = "talking_face.gif"
imageio.mimsave(output_file, frames, format='GIF', duration=0.8)

print(f'动画已保存为 {output_file}')