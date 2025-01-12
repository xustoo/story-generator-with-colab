from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_model.storyModel import BASE_DIR, StoryGenerator  # StoryGenerator sınıfını ithal et
import os  # os modülünü ekleyin

MODEL_PATH = os.path.join(BASE_DIR, "../models/storyModel.h5")

app = Flask(__name__)
CORS(app, resources={r"/generate-story": {"origins": "*"}})  # Allow all origins

@app.route('/')
def home():
    return "Story Generator API is running."

@app.route('/generate-story', methods=['POST'])
def generate_story_endpoint():
    data = request.get_json()
    keywords = data.get('keywords', [])
    max_length = data.get('max_length', 100)  # max_length parametresini ekledik, varsayılan olarak 100 alıyoruz
    
    if not keywords or not isinstance(keywords, list):
        return jsonify({"error": "Invalid or missing keywords"}), 400

    try:
        story_generator = StoryGenerator()  # StoryGenerator sınıfından bir örnek oluştur
        if not os.path.exists(MODEL_PATH):  # Model yoksa eğit
            story_generator.train_model()
        
        # Hikaye üretme: max_length parametresini de geçiyoruz
        story = story_generator.generate_story(keywords, max_length)  
        
        return jsonify({"story": story})
    except Exception as e:
        print(f"Error generating story: {e}")
        return jsonify({"error": f"Story generation failed: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Portu 5000 olarak ayarlayın
