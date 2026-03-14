# Assignment 2 — Foundation Models for Visual Brain Encoding

## Overview

This project studies how well different visual and multimodal model representations explain fMRI responses in visual brain regions.

It progresses from standard CNN baselines to modern vision-language models and layer-wise transformer analysis.

## What this project covers

### 1. CNN-based encoding baselines
Compared multiple deep visual architectures such as:
- ResNet-50
- EfficientNet
- SqueezeNet

Pipeline:
- extracted image features
- selected ROI-specific vertices
- trained encoding models per ROI
- evaluated predicted vs true neural responses using correlation-based metrics

### 2. Vision-language and semantic brain encoding
Extended beyond CNN-only encoders by incorporating:
- visual embeddings from modern VLMs
- semantic embeddings from captions or model-generated descriptions
- visual-only, semantic-only, and joint encoding models

Also included:
- exact prompt design
- prompt-family ablations
- analysis of which ROIs benefit from semantic supervision

### 3. Layer-wise transformer-to-brain mapping
Tested the hypothesis that deeper transformer layers align with later stages of the visual hierarchy by:
- extracting features from multiple intermediate depths
- training layer-wise encoding models
- comparing representational alignment across ROIs
- plotting encoding performance as a function of layer depth

## Data-science / NeuroAI skills demonstrated

- feature extraction from CNNs, VLMs, and transformers
- multimodal representation comparison
- ridge-based encoding model construction
- ablation-driven analysis
- ROI-wise evaluation of model–brain alignment
- layer-wise representation analysis

## Representative outputs

This project includes:
- ROI-wise encoding comparisons
- baseline vs VLM vs joint-feature evaluation
- prompt-ablation analysis
- layer-depth performance curves
- representational alignment plots

## Why this matters

This project reflects a modern NeuroAI workflow: testing whether visual and semantic representations from foundation models better explain brain responses than standard CNN baselines, and identifying where language-aware representations help most.
