# Redirector

A simple redirector tool to help bug hunter when performing SSRF tests.

## Installation

```
git clone https://github.com/aituglo/redirector
cd redirector
docker build -t redirector .
docker run -p 8000:8000 redirector
```