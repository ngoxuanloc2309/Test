import cv2
import os


def detect_and_save_objects(image_path, output_folder):
    # Đọc ảnh đầu vào
    image_path = r"C:\New folder\test\test\output\input.jpg"

    image = cv2.imread(image_path)

    # Thực hiện xác định đối tượng, ở đây sử dụng mô hình object detection của OpenCV
    # Bạn có thể sử dụng mô hình hoặc thư viện phân loại đối tượng mà bạn muốn
    # Đảm bảo cài đặt OpenCV: pip install opencv-python
    # Ví dụ sử dụng mô hình Haarcascades
    cascade_path = r'C:\path\to\your\opencv\build\etc\haarcascades\haarcascade_frontalface_default.xml'

    cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Tạo folder Ket_qua nếu chưa tồn tại
    output_folder_path = os.path.join(output_folder, 'Ket_qua')
    os.makedirs(output_folder_path, exist_ok=True)

    # Lưu đối tượng vào các folder tương ứng
    for (x, y, w, h) in objects:
        label = 'label'  # Đặt label tùy thuộc vào đối tượng được phát hiện
        label_folder_path = os.path.join(output_folder_path, label)
        os.makedirs(label_folder_path, exist_ok=True)

        object_image = image[y:y + h, x:x + w]
        object_path = os.path.join(label_folder_path, f'object_{x}_{y}.jpg')
        cv2.imwrite(object_path, object_image)


if __name__ == "__main__":
    # Thay đổi đường dẫn ảnh và thư mục đầu ra tùy thuộc vào nhu cầu
    input_image_path = r"C:\New folder\test\test\output\input.jpg"
    output_folder_path = r"C:\New folder\test\test\output\KQ"

    detect_and_save_objects(input_image_path, output_folder_path)
