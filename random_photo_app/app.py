import os
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import boto3
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pictures.db'
db = SQLAlchemy(app)

# AWS S3 Configuration
S3_BUCKET = 's3-bucket-name'
S3_ACCESS_KEY = 'access-key'
S3_SECRET_KEY = 'secret-key'
S3_REGION = 'region'

s3_client = boto3.client('s3', 
                          aws_access_key_id=S3_ACCESS_KEY,
                          aws_secret_access_key=S3_SECRET_KEY,
                          region_name=S3_REGION)

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_type = db.Column(db.String(50))
    url = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/save_picture', methods=['POST'])
def save_picture():
    data = request.json
    animal_type = data.get('animal_type')
    num_pictures = data.get('num_pictures', 1)

    urls = []
    for _ in range(num_pictures):
        # Fetch a random image
        response = requests.get("https://place.dog/200/200")
        
        if response.status_code == 200:
            # Create a unique filename
            image_name = f"{animal_type}_{_}.jpg"
            try:
                # Upload to S3
                s3_client.put_object(Bucket=S3_BUCKET, Key=image_name, Body=response.content)
                url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{image_name}"
                
                # Save to database
                new_picture = Picture(animal_type=animal_type, url=url)
                db.session.add(new_picture)
                urls.append(url)

            except NoCredentialsError:
                return jsonify({"message": "Credentials not available"}), 403

    db.session.commit()
    return jsonify({"message": "Pictures saved", "urls": urls})

@app.route('/last_picture/<animal_type>', methods=['GET'])
def last_picture(animal_type):
    picture = Picture.query.filter_by(animal_type=animal_type).order_by(Picture.id.desc()).first()
    if picture:
        return jsonify({"url": picture.url})
    return jsonify({"message": "No pictures found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
