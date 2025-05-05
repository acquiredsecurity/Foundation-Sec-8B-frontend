# Foundation-sec-8B Web Chat Interface

This project provides a simple web-based frontend using **Flask** and **HTML** to interact with a locally hosted [**Foundation-sec-8B**](https://huggingface.co/fdtn-ai/Foundation-Sec-8B) security LLM via the [vLLM OpenAI-compatible API server](https://github.com/vllm-project/vllm).

<img width="1429" alt="image" src="https://github.com/user-attachments/assets/b1348981-0d51-4005-b082-d4199991bffa" />


## Features

- Easily prompt Foundation Sec 8B chat assistant when running it locally via web ui
- HTML-based frontend with a prompt box and response display
- Queries `Foundation-sec-8B` through vLLM’s `/v1/completions` endpoint
- Designed for analyst-style interactions (forensics, threat detection, incident response)

## Requirements

- Python 3.8+
- Flask
- requests
- Running vLLM server with Foundation-sec-8B loaded (on port `8000` by default)

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/acquiredsecurity/foundation-sec-webchat.git
cd foundation-sec-webchat
