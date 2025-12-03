import os
from PIL import Image

# Cartella dello script (e quindi dove ci sono anche le immagini)
input_folder = os.path.dirname(os.path.abspath(__file__))

extensions = (".webp", ".jpg", ".jpeg")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(extensions):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(input_folder, output_filename)

        if os.path.exists(output_path):
            print(f"{output_filename} già esiste, salto.")
            continue

        try:
            with Image.open(input_path) as img:
                img.save(output_path, "WEBP")
            print(f"Convertito {filename} -> {output_filename}")
        except Exception as e:
            print(f"Errore convertendo {filename}: {e}")
