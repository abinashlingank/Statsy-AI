import torch
import transformers

from transformers import LlamaForCausalLM, LlamaTokenizer

import os
import shutil
from Variables import prompt
import pandas as pd

# clearing the output images directory before next plots
if os.path.exists("output"):
    shutil.rmtree("output")
os.makedirs("output", exist_ok=True)

# loading the data
data = pd.read_csv('data.csv')
data = data.head(10)

# Loading the model

model_dir = "./llama-2-7b-chat-hf"
model = LlamaForCausalLM.from_pretrained(model_dir)

# Adding data to prompt
prompt += data.to_string()

print(prompt)

# Defining and instantiating the tokenizer and pipeline

tokenizer = LlamaTokenizer.from_pretrained(model_dir)

pipeline = transformers.pipeline(
                            "text-generation",

                            model=model,

                            tokenizer=tokenizer,

                            torch_dtype=torch.float16,

                            device_map="auto",

                            )
while not os.listdir('output'): # run the model untill we get output images in the directory
    sequences = pipeline(
                    prompt,

                    do_sample=True,

                    top_k=10,

                    num_return_sequences=1,

                    eos_token_id=tokenizer.eos_token_id,

                    max_length=400,

                    )
    response = ""
    for seq in sequences:
        response += seq['generated_text']

    # Parsing the content

    prompt2 = '''parse and give me only python code by removing unneccasary words and lines from thie follwing response:
    "'''
    prompt2+=response

    prompt2+='''"

    Your output should be in the following format.
    # code:
    # ```python
    # <parsed python code>
    # ```
    '''
    sequences2 = pipeline(
                    prompt2,

                    do_sample=True,

                    top_k=10,

                    num_return_sequences=1,

                    eos_token_id=tokenizer.eos_token_id,

                    max_length=400,

                    )
    response2 = ""
    for seq in sequences:
        response2 += seq['generated_text']

    start = response2.find("```python")
    if start == -1:
        start = response2.find("```")
        start += 3
    else:
        start += 9
    end = response2.find("```", start)

    python_code = response[start:end]

    with open("plot.py", "w") as file:
        file.write(python_code)