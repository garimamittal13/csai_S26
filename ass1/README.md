# Assignment 1 — fMRI and EEG/MEG Preprocessing and Decoding

## Overview

This project builds an end-to-end understanding of neuroimaging preprocessing and classification across multiple modalities:
- **fMRI** (mandatory)
- exactly one of **EEG** or **MEG**

The goal is to move from raw or pre-extracted scientific data to interpretable binary decoding pipelines with modality-appropriate visualizations.

## What this project covers

### 1. fMRI decoding (mandatory)
Built ROI-specific decoding pipelines using the Haxby visual object recognition dataset.

Key elements:
- worked with voxel time-series features from ventral temporal (VT) and an assigned ROI
- decoded binary stimulus contrasts such as face vs house and face vs non-house
- used session-aware evaluation with Leave-One-Group-Out cross-validation
- compared decoding performance across ROI conditions
- visualized brain regions to contextualize model interpretation

### 2. EEG or MEG pipeline
Completed exactly one additional modality pipeline:

- **EEG option:** raw `.mat` loading, preprocessing, feature extraction, and task classification
- **MEG option:** BIDS-based loading with MNE-BIDS, epoch construction, preprocessing, feature extraction, and story vs word-list decoding

## Data-science / scientific skills demonstrated

- loading raw scientific file formats
- preprocessing noisy neural signals
- feature engineering for classification
- leakage-aware evaluation
- cross-validation with grouped scientific data
- modality-appropriate interpretation using brain visualizations or topographic maps

## Representative outputs

This project includes:
- classification accuracy summaries
- ROI-wise comparisons
- confusion matrices
- PSD / preprocessing diagnostic plots
- topographic maps or fMRI visualizations

## Why this matters

This project demonstrates my ability to build scientifically grounded pipelines from real neuroimaging data rather than relying only on pre-cleaned benchmark features.
