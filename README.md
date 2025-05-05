# Foundation-sec-8B Web Chat Interface

This project provides a simple web-based frontend using **Flask** and **HTML** to interact with a locally hosted **Foundation-sec-8B** security LLM via the [vLLM OpenAI-compatible API server](https://github.com/vllm-project/vllm).

## Features

- Secure and local forensic chat assistant
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
