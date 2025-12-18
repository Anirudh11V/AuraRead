AuraRead: PDF Loud Reader

AuraRead is a web-based tool built with Python and Django that allows users to upload PDF documents, select a specific page range, and convert that text into audible speech. It's designed to help students, professionals and the visually impaired consume written content effortlessly.

Features:
    Current(MVP):
        - Secure File Upload: Users can upload PDF documents safely.
        - Precise Range Selection: Custom page range selection to avoid reading unwanted headers or inidices.
        - High-Quality TTS: Powered by Google Text-to-Speech (gTTS) for natural-sounding audio.
        - Instant Playback - Built-in HTML5 audio player for immediate listenting.
        - Offline Access: Downloadable MP3 files for listening on the go.

    Planned(Enhanced):
        - Background Processing: Integration with Celery & Redis for faster, non-blocking audio generation.
        - Visual PDF Viewer: integration with PDF.js to allow text highlighting for selection.
        - Voice Customization: Options to change voice speed, gender and accent.
        - Automatic Cleanup: Periodic task to delete old media files to save storage.

Tech Stack:
    - Backend: Django
    - Database: SQLite (Development)
    - PDF Parsing: pypdf
    - Text-to-Speech: gTTS (Google Text-to-Speech)
    - Environment Management: python-dotenv

Installation & Setup:
    * Follow these steps to get your local development environment running:
    1. Clone the repository
        git clone https://github.com/Anirudh11V/AuraRead.git
        cd AuraRead
    
    2. Set up a Virtual Environment
        py -m venv venv

        <!-- Windows -->
        venv\Scripts\activate

        <!-- Mac/Linux -->
        source venv\bin\activate

    3. Install Dependencies
        pip install -r requirements.txt

    4. Environment Variables
        * Create a .env file in the root directory and add your secret keys:
        DJANGO_SECRET_KEY = your_sceret_key_here 
        DJANGO_DEBUG = True
        DJANGO_ALLOWED_HOSTS = 127.0.0.1, localhost

    5. Run Migrations
        python manage.py makemigrations
        python manage.py migrate

    6. Start Server
        python manage.py runserver

    visit http://127.0.0.1:8000/ in your browser.

Contributing:
    Contributions are welcome. If you have ideas to improve the speed of text extraction or UI enhancements, feel free to fort this repo and submit a Pull Request.

License:
    This project is open-source and available under the MIT License.