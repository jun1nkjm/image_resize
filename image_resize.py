import cv2
import os

# 画像をbicubic補間でリサイズする関数
def resize_images(input_folder, output_folder, scale_factor=4):
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 入力フォルダ内の全ファイルを処理
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 画像ファイルを読み込む
            img = cv2.imread(os.path.join(input_folder, filename))
            
            # 新しいサイズを計算
            new_size = (img.shape[1] * scale_factor, img.shape[0] * scale_factor)
            
            # 画像をbicubic補間でリサイズ
            resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)
            
            # 新しいファイル名で出力フォルダに保存
            # new_filename = f"resized_{filename}"
            # 別のフォルダなら、そのままのファイル名で保存
            new_filename = filename
            cv2.imwrite(os.path.join(output_folder, new_filename))
            print(f"Resized and saved {filename} as {new_filename}")

 if __name__ == "__main__":
    # 使用例
    input_folder = 'input_images'
    output_folder = 'output_images'
    resize_images(input_folder, output_folder)
