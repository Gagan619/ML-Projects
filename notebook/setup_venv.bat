@echo off
echo ================================
echo 🔧 Setting up virtual environment
echo ================================

REM Step 1: Create venv if not already created
if not exist "venv\" (
    python -m venv venv
)

REM Step 2: Activate venv
call venv\Scripts\activate

REM Step 3: Upgrade pip, setuptools, wheel
python -m pip install --upgrade pip setuptools wheel

REM Step 4: Install requirements
python -m pip install -r requirements.txt

REM Step 5: Confirm Python being used
echo ================================
echo ✅ Setup Complete!
python -c "import sys; print('Using Python:', sys.executable)"
