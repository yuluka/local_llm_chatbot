# Local LLM Chatbot

## Author

Yuluka Gigante Muriel


## Overview

This repository contains a simple chatbot implementation, via the CLI, using three different local LLMs.

Of course, it is not mandatory to use the models I chose, and you can easily switch to different models of your choice by modifying a few lines in the code:

```python
model_name = input("Enter the model you want to use:\n1) Llama-3.1-8B-Instuct\n2) Llama-3.2-3B-Instruct\n3) Llama-3.2-1B-Instruct\n")

if model_name == "1":
    model_name = "Llama-3.1-8B-Instruct"
elif model_name == "2":
    model_name = "Llama-3.2-3B-Instruct"
elif model_name == "3":
    model_name = "Llama-3.2-1B-Instruct"
```


## How to use it

To use this code you'll need to follow these steps:

1. Install the dependencies listed in 'requirements.txt':

    ```bash
    pip install -r requirements.txt
    ```

    > **Note**: This project is condigured for a system with an NVIDIA GPU using PyTorch (CUDA 11.8) on Windows OS. If you're on a different platform, adjust the installation accordingly by referring to the [PyTorch website](https://pytorch.org).

2. Download the models:

    As I mentioned before, I chose the models:

    - [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
    - [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
    - [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)

    But you can download and use any model and version.

    After downloading, ensure that the models are placed in directories at the same level as the `src` folder, with one folder per model. 
    
    If you choose to use other models, update the `model_name` variable with the name of the folder containing your model.

3. Run the script:

    To start the chatbot, run the following command:

    ```bash
    python ./src/app.py
    ```

    Once the script is running, you'll be prompted to choose a model to interact with. Wait for the model to load on your GPU or CPU, and then start the conversation.


## Notes

- Ensure you have enough GPU memory to store the models. 6GB of VRam was sufficient for Llama 3.2 3B/1B.


I hope you find this useful.