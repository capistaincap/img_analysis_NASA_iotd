# NASA Image of the Day Archive (Scraping + Color Analysis)
This learning project scrapes ~120 images from IOTD archive from NASA for feature extraction and visualization purposes.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Scraper

This will:
- Scrape paginated NASA Image of the Day pages  
- Download images into the `images/` directory  
- Generate `img_features.csv`  

```bash
python scraper.py
```

Wait until the download completes.


---

### 5. Run Feature Extraction

```bash
python featureExtraction.py
```

Loads up relevant feature info in a `csv` file.



---

### 6. Run Visualization

```bash
python visualization.py
```

This script loads `img_features.csv` and visualizes extracted image features.

---

## Notes

- `venv/` and `images/` are ignored via `.gitignore`.
- The `images/` directory is generated automatically when running `scraper.py`. (Creating it manually is redundant as it will be overwritten)
- Always activate the virtual environment before running the scripts.

---

## Contributors

- Capistaincap 
- Cometcoder192 (for initial setup)