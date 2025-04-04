import cv2
import os
import argparse
from tqdm import tqdm

# 画像をbicubic補間でリサイズする関数
def resize_images(input_folder, output_folder, scale_factor):
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 入力フォルダ内の全ファイルを処理
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'))]
    for filename in tqdm(files, desc="Resizing images"):
        try:
            # 画像ファイルを読み込む
            img = cv2.imread(os.path.join(input_folder, filename))
            if img is None:
                tqdm.write(f"Failed to read {filename}")
                continue
            
            # 新しいサイズを計算
            new_size = (img.shape[1] * scale_factor, img.shape[0] * scale_factor)
            
            # 画像をbicubic補間でリサイズ
            resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)
            
            # 新しいファイル名で出力フォルダに保存（PNG形式）
            new_filename = f"resized_{os.path.splitext(filename)[0]}.png"
            cv2.imwrite(os.path.join(output_folder, new_filename), resized_img)
            tqdm.write(f"Resized and saved {filename} as {new_filename}")
        except Exception as e:
            tqdm.write(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resize images using bicubic interpolation.')
    parser.add_argument('input_folder', type=str, help='Path to the input folder containing images.')
    parser.add_argument('output_folder', type=str, help='Path to the output folder to save resized images.')
    parser.add_argument('--scale_factor', type=int, default=4, help='Scale factor for resizing images.')
    
    args = parser.parse_args()
    
    resize_images(args.input_folder, args.output_folder, args.scale_factor)
