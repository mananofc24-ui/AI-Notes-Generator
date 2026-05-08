# AI Notes Generator 📝

A full-stack AI-powered web application that automates the creation of concise study notes from PDF documents. Built with **Streamlit**, **Docker**, **MySQL**, and integrated with **Hugging Face's** large language models.

## 🚀 Features
- **User Authentication:** Secure registration and login system backed by MySQL.
- **PDF Processing:** Automated text extraction from uploaded PDF files.
- **AI-Powered Summarization:** Generates intelligent, bulleted notes using Mistral/Zephyr models.
- **Persistent Sessions:** Keeps your generated notes visible even during UI refreshes.
- **Export Options:** Download your generated notes as `.txt` files instantly.
- **Dockerized Environment:** Fully containerized setup for consistent deployment across any machine.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Database:** MySQL 8.0
- **AI Orchestration:** Hugging Face Inference API
- **Containerization:** Docker & Docker Compose
- **Language:** Python 3.10+

## 📦 Installation & Setup

### Prerequisites
- [Docker Desktop](https://docker.com) installed.
- A [Hugging Face API Token](https://huggingface.co).

### Step 1: Clone the Repository
```bash
git clone https://github.com
cd AI-Notes-Generator
```

### Step 2: Configure Environment Variables
Create a `.env` file in the root directory and add your credentials:
```text
HF_TOKEN=your_huggingface_api_token_here
```

### Step 3: Launch with Docker
Run the following command to build the images and start the services:
```bash
docker compose up --build
```
The application will be available at `http://localhost:8501`.

## 📂 Project Structure
- `app.py`: Main Streamlit application logic.
- `Dockerfile`: Configuration for the Python/Streamlit container.
- `docker-compose.yml`: Orchestrates the Streamlit app and MySQL database services.
- `requirements.txt`: Python dependencies.
- `.env`: (Hidden) Secure storage for API keys.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
