import torch
import numpy as np
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from scipy.stats import entropy

class BrainScanner:
    def __init__(self, model_name='gpt2'):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, output_hidden_states=True).to(self.device)
        self.model.eval()

    def scan_layers(self, text):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        hidden_states = outputs.hidden_states 
        layer_data = []
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        for layer_idx, layer_tensor in enumerate(hidden_states):
            activation_variance = torch.var(layer_tensor).item()
            mean_activation = torch.mean(layer_tensor).item()
            layer_data.append({"Layer": layer_idx, "Activation Variance": activation_variance, "Mean Activity": mean_activation})
        return pd.DataFrame(layer_data), tokens

    def get_token_entropy(self, text):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs, labels=inputs["input_ids"])
            logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=-1)
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        entropy_data = []
        for i, token in enumerate(tokens):
            if i == 0: continue
            token_entropy = entropy(probs[0, i-1].cpu().numpy())
            entropy_data.append({"Token": token, "Entropy": token_entropy})
        return pd.DataFrame(entropy_data)
