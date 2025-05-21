
import json

input_file = "dataset.jsonl"           # JSONL dosya adın
output_file = "prepared_dataset.txt"   # Yeni oluşturulacak dosya

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        try:
            data = json.loads(line)
            prompt = data.get("prompt", "").strip()
            response = data.get("response", "").strip()

            # Eğer prompt ve response boş değilse yaz
            if prompt and response:
                combined = f"{prompt} {response}"
                outfile.write(combined + "\n")
        except json.JSONDecodeError:
            print("Hatalı satır atlandı:", line)
