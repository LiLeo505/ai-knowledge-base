# AI Knowledge Base

An intelligent Q&A system that leverages AI models to answer questions based on provided knowledge base content.

## Overview

This project is an AI-powered knowledge base system built with Python. It integrates with the DashScope API to provide intelligent answers based on custom knowledge base content stored in the `knowledge` directory.

## Features

- Custom knowledge base integration
- AI-powered question answering
- Uses Alibaba Cloud's DashScope API
- Supports text file knowledge sources

## Requirements

- Python 3.8+
- DashScope API key

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API key:
   ```
   DASHSCOPE_API_KEY=your_api_key_here
   ```

## Usage

1. Add your knowledge base files to the `knowledge` directory (as .txt files)
2. Run the application:
   ```bash
   python main.py
   ```
3. Enter your question when prompted

## Configuration

The application uses a `config.py` file to load the API key from environment variables.

## Project Structure

- `main.py`: Main application logic
- `config.py`: Configuration and API key loading
- `requirements.txt`: Python dependencies
- `knowledge/`: Directory for knowledge base files
- `.env`: Environment variables (not included in version control)

## License

This project is licensed under the MIT License.