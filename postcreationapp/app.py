from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import datetime
import pytz

app = Flask(__name__)
CORS(app)

# Directory paths (adjust as needed)
BASE_DIR = "../content/posts"
ARCHETYPE_PATH = "../archetypes/posts/index.md"

# Load the archetype template
def load_archetype():
    with open(ARCHETYPE_PATH, 'r') as file:
        return file.read()

# Save the new article
def save_article(slug, metadata, content):
    article_dir = os.path.join(BASE_DIR, slug)
    os.makedirs(article_dir, exist_ok=True)
    article_path = os.path.join(article_dir, "index.md")

    with open(article_path, 'w') as file:
        file.write(metadata + "\n" + content)

# Generate metadata based on user input
def generate_metadata(title, tags, aliases, description, canonicalURL, cover):
    archetype = load_archetype()
    metadata = archetype

    # Get the current time with timezone (Asia/Tehran)
    timezone = pytz.timezone('Asia/Tehran')
    now = datetime.datetime.now(timezone)
    formatted_date = now.strftime('%Y-%m-%dT%H:%M:%S%z')  # Format the date with timezone offset

    # Replace placeholders in the metadata
    metadata = metadata.replace('"{{ replace .Name "-" " " | title }}"', title)
    metadata = metadata.replace("{{ .Date }}", formatted_date)
    metadata = metadata.replace("[\"first\"]", str(tags))
    metadata = metadata.replace('# aliases: ["/first"]', f'aliases: {str(aliases)}')
    metadata = metadata.replace("Desc Text.", description)
    metadata = metadata.replace("https://canonical.url/to/page", canonicalURL)
    metadata = metadata.replace("<image path/url>", cover['image'])
    metadata = metadata.replace("<alt text>", cover['alt'])
    metadata = metadata.replace("<text>", cover['caption'])
    metadata = metadata.replace("relative: false", f'relative: {str(cover["relative"]).lower()}')
    metadata = metadata.replace("hidden: false", f'hidden: {str(cover["hidden"]).lower()}')

    return metadata

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_article():
    data = request.json
    title = data.get('title')
    tags = data.get('tags', [])
    # aliases = data.get('aliases', []).split('/')
    aliases = data.get('aliases', [])
    description = data.get('description', '')
    canonicalURL = data.get('canonicalURL', '')
    cover = data.get('cover', {
        'image': '',
        'alt': '',
        'caption': '',
        'relative': False,
        'hidden': False
    })
    content = data.get('content', '')

    slug = title.lower().replace(' ', '-')
    metadata = generate_metadata(title, tags, aliases, description, canonicalURL, cover)

    save_article(title, metadata, content)
    return jsonify({"message": "Article created successfully!", "slug": slug})

if __name__ == '__main__':
    app.run(debug=True)
