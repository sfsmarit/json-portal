# json-portal
Streamlit template for creating a portal site by parsing JSON.
The portal site includes a JSON editor, allowing any user to modify the source file directly on the site.

## Demo Page
https://dummy-json.streamlit.app/

## Settings
### Source file specification
config.py

### Streamlit settings
.streamlit/config.toml

## Prerequisites
- Python 3.10+
- Streamlit
- Git installed


## Steps
```bash
# For the first time, create and activate python venv
python -m venv <envname>
source <envname>/bin/activate.csh

# Clone the repository:
git clone https://github.com/sfsmarit/design-portal.git
cd design-portal

# Install required packages
pip install -r requirements.txt

# If installation fails, try using the binary option
pip install --only-binary=:all: -r requirements.txt

# Run
../<envname>/bin/streamlit run main.py
```
