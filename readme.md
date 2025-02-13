# Loading backend
deactivate
cd backend/
source lib/.venv/bin/activate
uvicorn app.main:app --reload 

# Loaging web_app
deactivate
cd web_app/
npm run dev

const API_BASE_URL = import.meta.env.VITE_API_URL;

'http://127.0.0.1:8000'