# Synthetic Manuscript Generator

## Overview

This project generates synthetic historical manuscript images for Indic scripts using configurable backgrounds, fonts, and manuscript text.

Supported scripts:

- Devanagari
- Modi
- Sharada

Each generated image is accompanied by a Markdown annotation file.

---

## Features

- Modular Python implementation
- Random manuscript background selection
- Random manuscript text selection
- Automatic annotation generation
- Dataset generation
- Train / Validation / Test split
- Supports multiple Indic scripts

---

## Project Structure

```text
backgrounds/
fonts/
scripts/

output/

dataset/
    train/
    validation/
    test/

generate.py
split_dataset.py
renderer.py
effects.py
annotations.py
requirements.txt
README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

Generate dataset

```bash
python generate.py
```

Split dataset

```bash
python split_dataset.py
```

---

## Dataset

Scripts

- Devanagari
- Modi
- Sharada

Images per script

- Train: 85
- Validation: 10
- Test: 5

---

## Hugging Face Dataset

(Add your Hugging Face Dataset URL here)

---

## GitHub Repository

(Add your GitHub Repository URL here)
