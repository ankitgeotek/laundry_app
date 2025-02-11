# laundry_app


## **Project Setup Guide**

### **Setting Up the Virtual Environment**
To create a Python virtual environment, run:
```bash
python -m venv backend/lib/.venv
```

#### **Activating the Virtual Environment**
##### **On macOS/Linux:**
```bash
source backend/lib/.venv/bin/activate
```
##### **On Windows (Command Prompt):**
```cmd
backend\lib\.venv\Scripts\activate
```
##### **On Windows (PowerShell):**
```powershell
backend\lib\.venv\Scripts\Activate.ps1
```

---

### **Installing Dependencies**
After activating the environment, install the required packages:
```bash
pip install -r backend/requirements.txt
```

---

### **Running the Backend**
To start the backend service:
```bash
# Deactivate any previously active virtual environment
deactivate

# Navigate to the backend directory
cd backend/

# Activate the virtual environment
source lib/.venv/bin/activate

# Start the FastAPI server
uvicorn app.main:app --reload
```

---

### **Running the Frontend (React Web App)**
To start the frontend application:
```bash
# Deactivate any active virtual environment
deactivate

# Navigate to the web app directory
cd web_app/

# Start the development server
npm run dev
```
