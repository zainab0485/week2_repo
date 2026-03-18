
# Week 2 - Text Generation using Hugging Face

## Student
Zainab Omar

## Description
In this project, I used a pre-trained model from Hugging Face (distilgpt2) to generate text based on a given prompt.

## Model
The model used is distilgpt2, which is a lightweight version of GPT-2 for text generation tasks.

## How it works
The model takes an input prompt and generates a continuation of the text. I adjusted some parameters to improve the output:
- temperature = 0.7
- top_k = 50
- top_p = 0.9
- repetition_penalty = 1.2

## Example
Prompt: "Give advice on how to be happy"

The model generates a response based on this input.

## How to run
1. Activate the virtual environment:
   source venv/bin/activate

2. Run the code:
   python main.py

## Libraries
- transformers
- torch
