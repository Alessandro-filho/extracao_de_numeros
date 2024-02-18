import os
from flask import Flask, jsonify, redirect, url_for
from threading import Thread
from PIL import Image
import pytesseract
import re
from datetime import datetime

app = Flask(__name__)

# Configura Tesseract
pytesseract.pytesseract.tesseract_cmd = r''

# Diretório com as imagens
IMAGE_DIRECTORY = ''

# Variável para armazenar o progresso
progress = {"current": 0, "total": 0, "status": "Not started"}

def process_images_background():
    phone_numbers_set = set()
    filenames = [f for f in os.listdir(IMAGE_DIRECTORY) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    progress["total"] = len(filenames)
    progress["current"] = 0
    progress["status"] = "Processing"
    
    for filename in filenames:
        filepath = os.path.join(IMAGE_DIRECTORY, filename)
        image = Image.open(filepath)
        custom_config = r'--oem 3 --psm 11'
        text = pytesseract.image_to_string(image, config=custom_config)
        phone_number_regex = r'\+\d{2}\s?(\d{2})\s?(\d{4,5})[\-\. ]?(\d{4})'
        numbers_in_image = re.findall(phone_number_regex, text)
        for number in numbers_in_image:
            formatted_number = f'+55 {number[0]} {number[1]}-{number[2]}'
            phone_numbers_set.add(formatted_number)
        progress["current"] += 1
    
    # Salvando os números em um arquivo txt
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'extracted_numbers_{timestamp}.txt'
    with open(filename, 'w') as file:
        for number in sorted(phone_numbers_set):
            file.write(f'{number}\n')
    
    progress["status"] = "Completed"
    progress["current"] = 0
    progress["total"] = 0

@app.route('/')
def index():
    return '''
    <h1>OCR Image Processing</h1>
    <form action="/start_processing" method="post">
        <input type="submit" value="Start Processing">
    </form>
    <p><a href="/progress">Check Progress</a></p>
    '''

@app.route('/start_processing', methods=['POST'])
def start_processing():
    if progress["status"] in ["Not started", "Completed"]:  # Evitar iniciar novamente se já está processando
        thread = Thread(target=process_images_background)
        thread.start()
    return redirect(url_for('index'))

@app.route('/progress')
def show_progress():
    return jsonify(progress)

if __name__ == '__main__':
    app.run(debug=True)
