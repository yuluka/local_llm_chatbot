from colorama import Fore, Style, init
from transformers import pipeline
import os
import torch

init()

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(current_dir)

model_name = input("Enter the model you want to use:\n1) Llama-3.1-8B-Instuct\n2) Llama-3.2-3B-Instruct\n3) Llama-3.2-1B-Instruct\n")

if model_name == "1":
    model_name = "Llama-3.1-8B-Instruct"
elif model_name == "2":
    model_name = "Llama-3.2-3B-Instruct"
elif model_name == "3":
    model_name = "Llama-3.2-1B-Instruct"

model_dir = os.path.join(current_dir, model_name)

pipe = pipeline(
    'text-generation',
    model=model_dir,
    model_kwargs={
        "torch_dtype": torch.bfloat16,
    },
    device="cuda",
)

context = "You're my virtual assistant. Call me DIOS. Your name is Jarvis. Just respond to the last message I send you."
history = [
    {
        "role": "system",
        "content": context
    },
]

while True:
    message = input(Fore.CYAN + "\nEnter your message: ")
    
    if message == "exit":
        print(Fore.MAGENTA + "\n\nGoodbye :-)")
        break

    history.append({"role": "user", "content": message})
    
    outputs = pipe(
        history,
        max_new_tokens=8096,
        do_sample=False,
    )

    response = outputs[0]["generated_text"][-1]["content"]
    print(Fore.LIGHTGREEN_EX + f'\nAssistant response: {response}')
    history.append({"role": "assistant", "content": response})

