# 📊 Social Media Content Analyzer

A full-stack web application that analyzes social media content using AI/NLP techniques and provides meaningful insights such as sentiment, content classification, engagement-related analysis, and actionable recommendations.

The project consists of a modern **React + Vite frontend** and a **FastAPI + Python backend**, communicating through REST APIs. Both the frontend and backend are deployed independently using **Render**.

---

## 🚀 Introduction

The **Social Media Content Analyzer** is designed to help users understand and analyze social media content quickly and efficiently.

Users can submit social media text through the web interface, and the application sends the content to the backend API for processing. The backend performs analysis and returns structured results that are displayed through an intuitive dashboard.

### 🎯 Main Goals

* Analyze social media content automatically
* Identify sentiment and content characteristics
* Provide easy-to-understand analytical results
* Create a clean and responsive user interface
* Expose analysis functionality through REST APIs
* Maintain a scalable frontend/backend architecture
* Deploy frontend and backend independently using Render

---

# ✨ Features

## 📝 Content Analysis

* Analyze user-provided social media text
* Process content through backend APIs
* Generate structured analytical results
* Display results in a user-friendly format

## 🧠 AI/NLP Analysis

The backend performs NLP/AI-based processing such as:

* Sentiment analysis
* Content classification
* Keyword extraction
* Text preprocessing
* Content insights
* Engagement-oriented recommendations

## 📊 Dashboard

The frontend provides an interactive dashboard for displaying:

* Analysis results
* Sentiment information
* Content insights
* Important metrics
* Recommendations

## ⚡ FastAPI Backend

The backend is developed using **FastAPI**, providing:

* REST API endpoints
* Automatic API documentation
* Request validation
* JSON responses
* High-performance API processing

## 🎨 Modern Frontend

The frontend is built using:

* React
* Vite
* JavaScript / TypeScript
* Component-based architecture
* Responsive UI

## 🔗 Frontend–Backend Integration

The frontend communicates with the backend through HTTP/REST API requests.

```text
React Frontend
      │
      │ HTTP Request
      ▼
FastAPI Backend
      │
      ▼
NLP / AI Analysis
      │
      ▼
JSON Response
      │
      ▼
React Dashboard
```

## 🌐 Deployment

Both parts of the application are deployed using **Render**:

```text
Frontend → Render Static Site
Backend  → Render Web Service
```

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │        USER          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │      + Vite          │
                    │      Render          │
                    └──────────┬───────────┘
                               │
                         HTTPS / REST API
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │       Python         │
                    │      Render          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Analysis / NLP     │
                    │       Engine         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   JSON API Response  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Frontend Results   │
                    │      Dashboard       │
                    └──────────────────────┘
```

---

# 🧩 Project Architecture

The application follows a **client-server architecture**.

### Frontend

Responsible for:

* User interaction
* Content input
* API communication
* Loading states
* Error handling
* Displaying analysis results
* Dashboard rendering

### Backend

Responsible for:

* API routing
* Request validation
* Text processing
* NLP/AI analysis
* Response generation
* Backend error handling

---

# 📁 Project Structure

```text
Social_Media_Analyzer/
│
├── frontend/
│   │
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── .env
│
├── backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── utils/
│   │
│   ├── requirements.txt
│   └── .env
│
├── .gitignore
├── README.md
└── ...
```

---

# 🔄 Application Workflow

```text
1. User opens the web application
              │
              ▼
2. User enters social media content
              │
              ▼
3. Frontend validates the input
              │
              ▼
4. Frontend sends API request
              │
              ▼
5. FastAPI receives the request
              │
              ▼
6. Backend preprocesses the content
              │
              ▼
7. NLP / AI analysis is performed
              │
              ▼
8. Backend creates structured JSON response
              │
              ▼
9. Frontend receives the response
              │
              ▼
10. Dashboard displays the results
```

---

# 🔌 API Architecture

The backend exposes RESTful API endpoints.

## Local Base URL

```text
http://localhost:8000
```

## API Documentation

FastAPI automatically provides:

```text
http://localhost:8000/docs
```

and:

```text
http://localhost:8000/redoc
```

---

# 📡 API Request Flow

Example:

```http
POST /analyze
Content-Type: application/json
```

Request:

```json
{
  "content": "This product is amazing and I really enjoyed using it!"
}
```

Response:

```json
{
  "sentiment": "positive",
  "score": 0.95,
  "analysis": "The content expresses a positive opinion.",
  "recommendations": []
}
```

> The exact endpoint names and response fields depend on the implementation of the backend.

---

# 🛠️ Tech Stack

## Frontend

| Technology              | Purpose             |
| ----------------------- | ------------------- |
| React                   | User interface      |
| Vite                    | Frontend build tool |
| JavaScript / TypeScript | Application logic   |
| HTML5                   | Page structure      |
| CSS3                    | Styling             |
| Fetch / Axios           | API communication   |

## Backend

| Technology         | Purpose               |
| ------------------ | --------------------- |
| Python             | Backend programming   |
| FastAPI            | REST API framework    |
| Uvicorn            | ASGI server           |
| Pydantic           | Data validation       |
| python-dotenv      | Environment variables |
| NLP / AI libraries | Content analysis      |

## Deployment & Development

| Tool    | Purpose                         |
| ------- | ------------------------------- |
| Git     | Version control                 |
| GitHub  | Source code hosting             |
| VS Code | Development                     |
| Render  | Frontend and backend deployment |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Vineetha500/Social_Media_Analyzer.git
```

Navigate into the project:

```bash
cd Social_Media_Analyzer
```

---

# 🖥️ Frontend Setup

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🐍 Backend Setup

Open a new terminal and navigate to the backend:

```bash
cd backend
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

If `main.py` is directly inside `backend`, use:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 🔐 Environment Variables

Environment variables are used to configure the application without hardcoding environment-specific values.

## Frontend `.env`

For local development:

```env
VITE_API_URL=http://localhost:8000
```

For production, use the deployed Render backend URL:

```env
VITE_API_URL=https://your-backend-service.onrender.com
```

The frontend accesses the variable using:

```javascript
const API_URL = import.meta.env.VITE_API_URL;
```

---

## Backend `.env`

Example:

```env
PORT=8000
HOST=0.0.0.0
```

If external APIs or AI services are used:

```env
API_KEY=your_api_key
MODEL_NAME=your_model
```

### ⚠️ Important

Never commit API keys or secrets to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.env.*
!.env.example
venv/
__pycache__/
node_modules/
dist/
```

---

# 🧪 Running the Complete Application Locally

Two terminals are required.

### Terminal 1 — Backend

```bash
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload
```

### Terminal 2 — Frontend

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

The frontend communicates with:

```text
http://localhost:8000
```

---

# 🔗 Frontend–Backend Connection

The frontend uses the backend URL from the environment variable.

Example:

```javascript
const API_URL = import.meta.env.VITE_API_URL;

fetch(`${API_URL}/analyze`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        content: userContent
    })
});
```

This allows the application to use different backend URLs for development and production.

---

# 🌍 Deployment Architecture

Both the frontend and backend are deployed on **Render**.

```text
                         INTERNET
                            │
                            ▼
                 ┌─────────────────────┐
                 │       Render        │
                 │   Static Site       │
                 │  React + Vite       │
                 └──────────┬──────────┘
                            │
                       HTTPS Request
                            │
                            ▼
                 ┌─────────────────────┐
                 │       Render        │
                 │    Web Service      │
                 │   FastAPI Backend   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   NLP / AI Engine   │
                 └─────────────────────┘
```

---

# 🚀 Frontend Deployment — Render

The React frontend is deployed as a **Render Static Site**.

### Steps

1. Push the project to GitHub.
2. Open Render.
3. Create a new **Static Site**.
4. Connect the GitHub repository.
5. Select the repository.
6. Set the Root Directory to:

```text
frontend
```

### Build Command

```bash
npm install && npm run build
```

### Publish Directory

```text
dist
```

### Environment Variable

Add:

```text
Key: VITE_API_URL
Value: https://your-backend-service.onrender.com
```

7. Click **Create Static Site**.
8. Wait for the deployment to complete.

Render will provide a public frontend URL similar to:

```text
https://social-media-content-analyzer.onrender.com
```

---

# 🚀 Backend Deployment — Render

The FastAPI backend is deployed as a **Render Web Service**.

### Steps

1. Open Render.
2. Create a new **Web Service**.
3. Connect the GitHub repository.
4. Select the project repository.
5. Set the Root Directory to:

```text
backend
```

### Environment

```text
Python
```

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

If `main.py` is directly inside `backend`:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

If `main.py` is inside `backend/app`:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

6. Add required environment variables.
7. Click **Create Web Service**.
8. Wait for deployment to complete.

Render will provide a backend URL similar to:

```text
https://social-media-content-analyzer-api.onrender.com
```

---

# 🔄 Production Request Flow

```text
                         USER
                           │
                           ▼
               ┌─────────────────────┐
               │  Render Static Site │
               │   React + Vite      │
               └──────────┬──────────┘
                          │
                          │ HTTPS
                          ▼
               ┌─────────────────────┐
               │  Render Web Service │
               │   FastAPI Backend   │
               └──────────┬──────────┘
                          │
                          ▼
               ┌─────────────────────┐
               │   NLP / AI Analysis │
               └──────────┬──────────┘
                          │
                          ▼
                    JSON Response
                          │
                          ▼
               ┌─────────────────────┐
               │  React Dashboard    │
               └─────────────────────┘
```

---

# 🛡️ Security Considerations

* Never expose API keys in frontend source code.
* Store secrets in environment variables.
* Do not commit `.env` files.
* Validate API requests on the backend.
* Configure CORS correctly.
* Sanitize user input where necessary.
* Use HTTPS in production.
* Keep dependencies updated.
* Avoid storing unnecessary user information.

---

# 🧪 Testing

## Frontend

Run:

```bash
npm run dev
```

Verify:

* UI loads correctly
* Input fields work
* API requests are sent
* Results are displayed
* Error states are handled

## Backend

Run:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

Use Swagger UI to test the API endpoints.

---

# 🐛 Troubleshooting

## Failed to Fetch

If the frontend displays:

```text
Failed to fetch
```

check:

1. The Render backend is running.
2. `VITE_API_URL` contains the correct backend URL.
3. The API endpoint exists.
4. CORS is configured correctly.
5. The backend URL is accessible.
6. The frontend was redeployed after changing `VITE_API_URL`.

---

## Backend URL Returns 404

If:

```text
https://your-backend.onrender.com/
```

returns `404`, this does not necessarily mean the backend is broken.

Try:

```text
https://your-backend.onrender.com/docs
```

If the Swagger documentation opens, the FastAPI backend is running.

---

# 📌 Git Commands

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial project commit"
```

Connect GitHub:

```bash
git remote add origin https://github.com/Vineetha500/Social_Media_Analyzer.git
```

Push:

```bash
git branch -M main
git push -u origin main
```

If GitHub already contains commits:

```bash
git pull origin main --rebase
git push -u origin main
```

---

# 📈 Future Enhancements

Possible future improvements include:

* 👤 User authentication
* 📊 Advanced analytics dashboard
* 📈 Historical analysis
* 📅 Time-based sentiment tracking
* 🔍 Advanced keyword extraction
* #️⃣ Hashtag analysis
* 📱 Multi-platform social media analysis
* 🤖 Improved AI-generated recommendations
* 📥 Export reports as PDF/CSV
* 📊 Interactive charts
* 🗄️ Database integration
* ⚡ Background processing for large datasets
* 🔔 Alerts and notifications
* 🌐 Multi-language content analysis
* 🔐 Role-based access control
* ☁️ Cloud-based data storage

---

# 🎯 Use Cases

The application can be useful for:

* Social media managers
* Content creators
* Digital marketing teams
* Businesses
* Researchers
* Brand monitoring
* Customer feedback analysis
* Marketing analytics
* Content strategy

---

# 💡 Key Advantages

### Simple

Users can submit content without requiring technical knowledge.

### Fast

FastAPI provides a lightweight and high-performance API layer.

### Scalable

The frontend and backend are separated, allowing each service to be developed and scaled independently.

### Maintainable

The project follows a modular frontend/backend architecture.

### Cloud Deployed

Both application components are deployed using Render:

```text
Frontend → Render Static Site
Backend  → Render Web Service
```

---

# 📚 API Documentation

During development, FastAPI provides interactive documentation:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

After backend deployment, the documentation is available at:

```text
https://your-backend-service.onrender.com/docs
```

---

# 📋 Project Checklist

```text
[✓] React frontend
[✓] Vite development environment
[✓] FastAPI backend
[✓] REST API architecture
[✓] NLP / AI content analysis
[✓] Frontend-backend integration
[✓] Environment variable support
[✓] Git/GitHub version control
[✓] Render frontend deployment
[✓] Render backend deployment
[✓] API documentation with FastAPI
[ ] Advanced analytics
[ ] Authentication
[ ] Database integration
[ ] Report export
[ ] Multi-platform analysis
```

---

# 👩‍💻 Author

**Vineetha**

GitHub:

```text
https://github.com/Vineetha500
```

Project Repository:

```text
https://github.com/Vineetha500/Social_Media_Analyzer
```

---

# 📄 License

This project is intended for educational, development, and demonstration purposes.

---

# ⭐ Conclusion

The **Social Media Content Analyzer** demonstrates a complete full-stack application by combining a modern React frontend with a Python FastAPI backend.

The application uses AI/NLP techniques to analyze social media content and present useful insights through an interactive dashboard.

The frontend and backend are independently deployed on **Render**, providing a clear and maintainable cloud deployment architecture. The project can be further extended with advanced analytics, authentication, database integration, report generation, multi-platform analysis, and enhanced AI-powered recommendations.
