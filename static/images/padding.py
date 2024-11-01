import os
from PIL import Image, ImageOps

def add_padding_to_folder(input_folder, output_folder):
    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_folder, exist_ok=True)
    
    # パディングする色 (#f4f4f4) を指定
    padding_color = (244, 244, 244)  # RGB形式で指定

    # 入力フォルダ内のすべてのPNGファイルに対して処理
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            
            # 幅が800ピクセルであることを確認
            if img.width != 800:
                print(f"{filename} の幅が800ピクセルではありません。スキップします。")
                continue
            
            # 画像の上下にパディングを追加して 800x600 にする
            new_img = ImageOps.pad(img, (800, 600), color=padding_color, centering=(0.5, 0.5))
            
            # 保存先のパス
            output_path = os.path.join(output_folder, filename)
            new_img.save(output_path)
            print(f"{filename} を処理しました。")

# 使用例
input_folder = "input_images"  # 入力フォルダ
output_folder = "output_images"  # 出力フォルダ
add_padding_to_folder(input_folder, output_folder)
