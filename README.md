# Totus

Totus is a lightweight platform that hosts large language models (LLMs) and generates dynamic HTML content for an "everything site" based on URL paths. It uses the LLaMA model to create long HTML documents dynamically, allowing users to load different LLM models and generate site content seamlessly.

## Features

- Hosts multiple LLM models (currently configured with LLaMA GGUF format)

- Generates full HTML documents based on requested URL paths

- Returns plain HTML responses without markdown or additional text


Designed for an "everything site" — a site that dynamically serves content based on the path
Simple Flask API for easy integration and extensibility

## How It Works

When a GET request is made to the server (e.g., /some/path), Totus uses the path as a prompt to the loaded LLaMA model. The model generates an HTML document based on the prompt. The server then returns the generated HTML directly to the client.

## Getting Started

### Prerequisites

- Python 3.8+

- A GGUF format LLaMA model (example path: /home/CIN/tcl/projeto/model/Llama-3.2-3B-Instruct-Q6_K.gguf)

- GPU support if available (configurable via n_gpu_layers parameter)

### Installation

Clone the repository:
```sh
git clone https://github.com/tomclima/Totus
cd Totus
```


(Optional) Create a virtual environment:
```sh
python3 venv ./.venv
```

Install dependencies:
```sh
pip install -r requirements.txt
```

