from transformers import pipeline 

print("step 1: starting...")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("step 2: model loaded")

result = generator(
    "Give advice on how to be happy:",
    max_new_tokens=60,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    repetition_penalty=1.2,
    do_sample=True
)

print("step 3: generation done")
print(result[0]["generated_text"])
