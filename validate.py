import os

videos_path = 'full_dataset_100f'
images_path = 'full_image_dataset_100f'


def validate_video():
    count = 0
    files = os.listdir(videos_path)
    for f in files:
        f = os.path.join(videos_path, f)
        s = os.path.getsize(f)
        if(s < 1024*14):
            count += 1
            print(f)
    print(count, "Videos falharam!")
    print(len(files), "Videos gerados corretamente!")

def validate_images():
    v_files = os.listdir(videos_path)
    files = os.listdir(images_path)

    print(len(v_files) - len(files), "Imagens falharam!")
    print(len(files), "Imagens geradas corretamente!")



print("-------------------------------------------")
print("Validando vídeos")
if os.path.exists(videos_path):
    validate_video()

print("-------------------------------------------")
print("Validando imagens")
if os.path.exists(videos_path):
    validate_images()
print("-------------------------------------------")