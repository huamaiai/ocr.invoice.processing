#!/bin/bash

set -e

echo "🔧 Starting full setup for OCR Invoice Processing..."

# 1. System Dependencies
echo "📦 Installing system packages: poppler-utils, tesseract-ocr, Docker, docker-compose..."
sudo apt update
sudo apt install -y poppler-utils tesseract-ocr docker.io docker-compose

# 2. Enable Docker service (if not already)
echo "🛠️ Ensuring Docker service is running..."
sudo systemctl enable docker
sudo systemctl start docker

# 3. Setup Python virtual environment
echo "🐍 Creating and activating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# 4. Install Python dependencies
echo "📥 Installing Python packages from requirements.txt..."
pip install -r requirements.txt

# 5. Generate missing folders if needed
echo "📂 Creating expected directories..."
mkdir -p data/sample_invoices logs

# 6. Generate .env if missing
if [ ! -f .env ]; then
  echo "🔐 Creating .env file..."
  cat <<EOF > .env
MYSQL_HOST=localhost
MYSQL_ROOT_PASSWORD=rootpass
MYSQL_DATABASE=invoice_db
MYSQL_USER=invoice_user
MYSQL_PASSWORD=invoice_pass
MYSQL_PORT=3306

MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=ocr_logs
EOF
else
  echo "⚠️ .env file already exists — skipping"
fi

# 7. Docker: Spin up MySQL and MongoDB
echo "🐳 Spinning up MySQL and MongoDB containers via Docker Compose..."
docker-compose up -d

echo "✅ Setup Complete!"
echo "🔍 Next Steps:"
echo "1. Activate your virtualenv: source .venv/bin/activate"
echo "2. Run your test suite: PYTHONPATH=\$(pwd) pytest tests/"
echo "3. Upload invoices to: data/sample_invoices/"
echo "4. Use FastAPI endpoints (when implemented) to interact with the system."
