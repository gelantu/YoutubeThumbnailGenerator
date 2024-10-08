from flask import Flask, request, jsonify, render_template
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import os
import logging
import random

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Initialize Stable Diffusion client
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # Your API Key
    verbose=True,
)

@app.route('/')
def index():
    app.logger.info("Rendering index page")
    return render_template('index.html')

@app.route('/generate_thumbnail', methods=['POST'])
def generate_thumbnail():
    app.logger.info("Generating thumbnail")
    try:
        script = request.form['script']
        theme = request.form['theme']
        
        # Generate image using Stable Diffusion API
        prompt = f"Create a YouTube thumbnail for a video about {theme}"
        answers = stability_api.generate(
            prompt=prompt,
            seed=random.seed(),
            steps=30,
            cfg_scale=8.0,
            width=1280,
            height=720,
            samples=1,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )

        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    app.logger.warning("Your request activated the API's safety filters and could not be processed.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    
                    # Add text to the image
                    draw = ImageDraw.Draw(img)
                    try:
                        font = ImageFont.truetype("arial.ttf", 36)
                    except IOError:
                        font = ImageFont.load_default()
                    draw.text((10, 10), theme, font=font, fill=(255, 255, 255))
                    
                    # Save the image
                    img_path = os.path.join("static", "generated_thumbnail.png")
                    img.save(img_path)
        
        # Generate a title using OpenAI (you might want to replace this with a different method)
        title = generate_title(script)
        
        app.logger.info(f"Thumbnail generated successfully. Title: {title}")
        return render_template('index.html', title=title, thumbnail_url=img_path)
    except Exception as e:
        app.logger.error(f"Error generating thumbnail: {str(e)}")
        return render_template('index.html', error=str(e))

def generate_title(script):
    # You might want to implement a different method for title generation
    # This is just a placeholder
    return f"Video about {script[:30]}..."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)