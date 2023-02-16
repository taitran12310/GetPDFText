# Get PDF Text
## Packages
- fulltext Package
https://pypi.org/project/fulltext/
- pdftotext Package
https://pypi.org/project/pdftotext/

## Guide
- Install 「poppler」 before install package 「pdftotext」
```sh
# macos
brew install pkg-config poppler python

# Windows
## Install the Microsoft Visual C++ Build Tools
## Install poppler through conda
conda install -c conda-forge poppler
```

- Install require package
```sh
# Install virtualenv
pip install virtualenv

# Create and active virtualenv
python3 -m venv .venv
source ./venv/bin/activate

# Install require package
pip install -r requirements.txt
```

- Run
```sh
  # method: [getText1, getText2]
  # file_path: Path of PDF file
  # password: Password of PDF file (only getText2 method)
  # Ex. python3 getPdfText.py -m "getText2" -f "./pdf/sample_password.pdf" -p "123456"
  python3 getPdfText -m <method> -f <file_path> -p <password>

```