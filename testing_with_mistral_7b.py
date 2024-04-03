from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# define model name and file
model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
model_file = "mistral-7b-instruct-v0.2.Q8_0.gguf"

model_path = hf_hub_download(model_name, filename=model_file)

model_kwargs = {
  "n_ctx":4096,    # Context length to use
  "n_threads":4,   # Number of CPU threads to use
  "n_gpu_layers":0,# Number of model layers to offload to GPU. value = 0 beacuse use only CPU
}

## Instantiate model from downloaded file
llm = Llama(model_path=model_path, **model_kwargs)

## Generation kwargs
generation_kwargs = {
    "max_tokens":200, # Max number of new tokens to generate
    "stop":["<|endoftext|>", "</s>"], # Text sequences to stop generation on
    "echo":False, # Echo the prompt in the output
    "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

## Run inference
prompt = "The meaning of life is "
res = llm(prompt, **generation_kwargs) # Res is a dictionary

## Unpack and the generated text from the LLM response dictionary and print it
print(res["choices"][0]["text"])