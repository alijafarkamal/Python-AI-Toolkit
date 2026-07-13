# Python-AI-Toolkit 🧠🚀

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-%E2%9C%94%EF%B8%8F-brightgreen)
![AI](https://img.shields.io/badge/Artificial%20Intelligence-%F0%9F%A4%96-orange)
![NLP](https://img.shields.io/badge/Natural%20Language%20Processing-%E2%9C%A8-yellow)

## Overview

**Python-AI-Toolkit** is a curated collection of production-style Python mini-projects across:
- Generative AI and NLP
- Computer vision and audio/speech AI
- Data processing and analytics
- API-driven utility tools
- Security/network and load-testing examples

The repository is organized as standalone scripts, so each project can be run independently.

## Engineering Coverage in This Repository

This toolkit demonstrates multiple engineering domains in one codebase:

- **ML/AI engineering**: TensorFlow, PyTorch, Transformers, Whisper, TensorFlow Hub
- **Data engineering**: CSV/PDF ingestion, extraction, transformation, and export workflows
- **Application engineering**: CLI tools, Tkinter desktop GUIs, script-based automation
- **API integration engineering**: REST API consumption with request handling and JSON parsing
- **Vision engineering**: classification, object detection (YOLO + SSD), image processing
- **Audio engineering**: real-time capture, speech-to-text, audio classification
- **Web/data collection engineering**: scraping/search integrations and external data fetchers
- **Security/performance engineering examples**: packet sniffing and Locust load testing

## Tech Stack (Current)

### Core language/runtime
- Python 3.x

### AI/ML and model tooling
- `tensorflow`, `tensorflow_hub`
- `torch`, `torchvision`
- `transformers`
- `huggingface_hub`
- `whisper`
- `textblob`
- `boto3` (AWS Comprehend sentiment)

### Data processing and analytics
- `pandas`, `cudf`
- `matplotlib`, `seaborn`, `mplcursors`
- `pdfplumber`, `camelot`, `fpdf`
- `csv` module (standard library)

### Vision and audio
- `opencv-python` (`cv2`), `numpy`
- `pyaudio`, `speech_recognition`, `wave`
- Pretrained model configs/resources in `configs/`

### API, scraping, and automation
- `requests`
- `beautifulsoup4` (`bs4`)
- `googlesearch`
- `pytrends`
- `instaloader`
- `imdb` / Cinemagoer
- `whois`
- `qrcode`, `folium`, `geopy`
- `locust`, `kamene`

### UI/interaction
- CLI scripts
- Tkinter desktop GUIs (`tkinter`, `scrolledtext`)
- Notebooks (`.ipynb`) in examples

## Databases and Data Storage

### Database status
- There is **no internal relational or NoSQL database layer** in the current repository (no PostgreSQL/MySQL/MongoDB/Redis integration in code).

### Data persistence patterns used
- **File-based storage**:
  - Input datasets in `input_data_files/` (mostly CSV)
  - Generated artifacts in `output_data_files/` (PDF and outputs)
  - Additional generated files in specific utility folders (e.g., HTML maps, images, text outputs)
- **In-memory processing**:
  - DataFrames and tensors for transformation/inference pipelines
- **External data sources**:
  - Public and authenticated APIs (weather, nutrition, books, SpaceX, exchange rates, news, etc.)

## End-to-End Engineering Flow

Most projects follow this reusable flow:

1. **Input acquisition**
   - Local files (CSV/PDF/image/audio), live microphone/camera, or external APIs
2. **Preprocessing**
   - Parsing, formatting, feature extraction, or tokenization depending on modality
3. **Model/inference or business logic**
   - AI model inference (NLP/vision/audio) or utility/business transformation
4. **Output generation**
   - Console output, GUI output, plots, saved files (CSV/PDF/image), or downloadable assets
5. **Iteration**
   - Scripts are modular and can be swapped or extended by domain folder

## Repository Structure

- `ai_models/`  
  Chat, summarization, sentiment, and LLM examples (CLI + GUI)

- `data_processing/`  
  Crypto data analysis, PDF table extraction, PDF-to-CSV conversion, nutrition API analysis, image-to-PDF

- `vision_audio/`  
  Image classification, object detection (YOLO/SSD), image captioning, audio classification, speech-to-text

- `utilities/`  
  Practical utilities: weather, map generation, translation, QR, password generation, search scraping

- `apps_and_examples/`  
  API demos, IMDb/books lookup, currency conversion, Instagram downloader, network sniffer, load testing

- `configs/`  
  Model/config artifacts (`.cfg`, `.names`, `.spec`, assets)

- `input_data_files/` and `output_data_files/`  
  Dataset and generated-output folders for data workflows

## Setup

```bash
git clone https://github.com/alijafarkamal/Python-AI-Toolkit.git
cd Python-AI-Toolkit
```

> This repository currently does not include a single centralized `requirements.txt` or `pyproject.toml`.  
> Install dependencies per script based on its imports and usage.

## Usage

Run any script directly from its folder:

```bash
cd ai_models
python gptneo_chat_gui.py
```

## Contribution

Contributions are welcome. Add new scripts, improve engineering quality, and open a pull request.

## License

MIT License.
