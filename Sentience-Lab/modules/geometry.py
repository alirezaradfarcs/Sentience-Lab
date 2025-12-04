import torch
import pandas as pd
from sklearn.decomposition import PCA
from transformers import AutoModel, AutoTokenizer

class GeometryEngine:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
    
    def get_3d_projection(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state[0].numpy()
        tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        pca = PCA(n_components=3)
        coords = pca.fit_transform(embeddings)
        df = pd.DataFrame(coords, columns=['x', 'y', 'z'])
        df['Token'] = tokens
        return df
