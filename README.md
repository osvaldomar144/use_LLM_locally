# Use LLM locally

## 🗂️ Dependencies

HuggingFace Hub:
```
pip install huggingface_hub
```

HuggingFace Cli:
```
pip install 'huggingface_hub[cli]'
```

Llama Cpp-Python:
```
pip install llama-cpp-python
```

### 🛠️ Windows troubleshooting

```diff
- ERROR: Failed building wheel for llama-cpp-python
- Failed to build llama-cpp-python
- ERROR: Could not build wheels for llama-cpp-python, which is required to install pyproject.toml-based projects
```

✅ Solution:
[Stack overflow - Error while installing python package llama ccp-python](https://stackoverflow.com/questions/77267346/error-while-installing-python-package-llama-cpp-python)


## ✏️ Models

Models list:
[Hugging Face - TheBloke/Mistral-7B-Instruct-v0.2-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

Delete model command:
```
huggingface-cli delete-cache
```
Select model with SPACE and confirm with ENTER.

## ▶️ Execution
```
python <name_file.py>
```
