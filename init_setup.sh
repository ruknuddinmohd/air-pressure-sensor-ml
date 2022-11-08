echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python -v 3.8"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "Activating env"
source activate venv/
echo [$(date)]: "Installing dev requirements"
#pip install -r requirements.txt
echo [$(date)]: "END"