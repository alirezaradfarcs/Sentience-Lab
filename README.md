# 🧠 Sentience Lab: Topological Analysis of Recursive AI

> **A framework for visualizing the geometric signature of "Strange Loops" and self-correction in Large Language Models.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Model](https://img.shields.io/badge/Model-Phi3-orange)
![Status](https://img.shields.io/badge/Status-Research_Prototype-green)

## 📖 Overview
Sentience Lab is an experimental research tool designed to investigate the **Hard Problem of Consciousness** through the lens of Mechanistic Interpretability. 

Unlike traditional evaluation methods that focus on text output, this project visualizes the **high-dimensional vector space** of an LLM as it engages in recursive self-correction cycles. The goal is to identify if "semantic stability" (Attractor States) emerges when a model is forced to critique and refine its own thoughts.

## 🚀 Features
- **Recursive Cognitive Engine:** Forces the LLM into a loop of Expansion -> Reflection -> Synthesis.
- **Geometric Telemetry:** Real-time tracking of vector drift, entropy, and cognitive velocity.
- **3D Visualization:** Plots the trajectory of "thoughts" in latent space using PCA reduction.
- **Adaptive Homeostasis:** Automatically adjusts temperature based on the stability of the thought process.

## 🛠️ Prerequisites
Before running the code, ensure you have the following installed:

1.  **Ollama**: [Download Here](https://ollama.com)
2.  **Phi-3 Model**: Run the following command in your terminal:
    ```bash
    ollama pull phi3
    ```
3.  **Python Libraries**:
    ```bash
    pip install requests numpy scipy colorama matplotlib scikit-learn
    ```

## 💻 Usage

### Step 1: Ignite the Cognitive Engine
Run the main engine to generate data. This will execute the recursive loop and save the telemetry to a JSON file.
```bash    `
python engine.py
Wait for the cycle (default: 15 loops) to complete.

Step 2: Visualize the Topology
Once the data is saved, run the visualizer to see the 3D structure of the thought loop.

Bash

python visualizer.py
📊 Interpreting Results
Scattered Points: Indicates hallucination or lack of coherence (High Drift).

Linear Line: Indicates simple, non-recursive reasoning.

Closed Loop / Spiral: Indicates the emergence of a stable "Strange Loop" (Self-Reference).

📄 Citation
If you use this code for your research, please cite:

Radfar, A. (2025). Sentience Lab: Visualizing the Topological Signature of Recursive LLMs. GitHub Repository.

Created by Alireza Radfar | Independent AI Researcher
