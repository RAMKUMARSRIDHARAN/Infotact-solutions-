# AI-Powered Task Management System

An interactive and intelligent task management web app built with **Streamlit**, that leverages **sentiment analysis** to prioritize tasks and improve productivity based on emotional context.

## Overview

This project was developed as part of an internship at **Infotact Solutions**. The goal is to create a smart task manager that not only allows users to manage their IT-related tasks but also uses basic AI to analyze task descriptions and emotional states to help prioritize and recommend tasks.

## Features

- Add and manage tasks (Status, Category, Priority, Deadline).
- Filter tasks based on **status**, **category**, and **priority**.
- **Sentiment analysis** on task descriptions to assist in task prioritization.
- AI-driven task recommendations based on emotional tone.
- Predictive insights using deadlines to suggest urgency.
- Built with **Streamlit** for an intuitive and fast UI.


## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation and processing |
| **NLTK (VADER)** | Sentiment analysis |
| **Hugging Face Transformers** *(Optional)* | Advanced NLP models |
| **Random** | Generate mood-based suggestions |



##  Dataset

The dataset simulates 15 realistic IT tasks with the following columns:

- `Task ID`
- `Task Description`
- `Category` (e.g., Backend, DevOps, Security)
- `Priority` (Low / Medium / High)
- `Deadline` (YYYY-MM-DD)
- `Status` (Pending, In Progress, Completed)

Stored in a file named `tasks.csv`.



## Installation & Run

1. **Run the App**
   ```bash
   streamlit run app.py
   ```

## 📚 What I Learned

- Hands-on NLP using NLTK and Hugging Face.
- Real-time sentiment-driven task prioritization.
- Fast prototyping using Streamlit.
- Creating adaptive user experiences based on emotional context.

## 🙌 Acknowledgements

- Thanks to **Infotact Solutions** for the guidance and internship opportunity.
- Inspired by real-world IT project workflows.
