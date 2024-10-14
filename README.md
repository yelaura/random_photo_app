# Random Dog Photo API
## Description
This Flask application allows users to save random pictures of animals (e.g., dogs) to AWS S3 and retrieve the last saved picture of a specified animal type.
## Requirements
- Python 3.7+
- AWS Account (for S3 storage)
- Docker (optional, for containerization)
## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yelaura/random_photo_app.git
   cd random_photo_app
2. **Setup Virtual Environment: (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Setup AWS credentials:**
   ```bash
   export S3_BUCKET=your-bucket-name
   export S3_ACCESS_KEY=your-access-key
   export S3_SECRET_KEY=your-secret-key
   export S3_REGION=your-region
## Running the Application
### Locally
   ```bash
   python app.py
   ```
## In Docker
1. **Build the Docker Image**
   ```bash
   docker build -t random_photo_app .
2. **Run the Docker Image**
   ```bash
   docker run -p 5000:5000 random_photo_app
## API Endpoints
1. **Save Pictures**
   - Endpoint: POST /save_picture
   - Body:
      ```json
      {
      "animal_type": "dog",
      "num_pictures": 5
      }
2. **Get Last Picture**
   - Endpoint: GET /last_picture/dog
   - Retrieves the URL of the last saved picture of the specified animal type.
