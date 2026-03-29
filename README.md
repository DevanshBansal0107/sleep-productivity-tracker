# Sleep and Productivity Tracker (CLI)

## Overview

This is a simple command line based project that tries to estimate or predict how productive a student might be based on a few daily lifestyle inputs. The idea is not too complex, but it is practical and something many students can relate to in real life.

The system takes inputs like sleep hours, study time, screen usage and stress level, and then gives a productivity score. It kind of helps in understanding how these factors are connected, or at least gives a rough indication.

---

## Problem Statement

A lot of students face issues with managing time properly, sometimes they sleep less, sometimes they overuse screens, and overall productivity gets affected. There is no simple tool which directly shows how these habits might influence performance.

So this project tries to model that situation in a basic way.

---

## Approach

The project uses a dataset which contains multiple entries of student habits and their corresponding productivity score. The data is slightly irregular and not perfectly linear, so it doesn’t just memorise values.

A machine learning model is trained on this data and later used to make predictions based on user input. The idea is not perfect accuracy, but a reasonable approximation.

---

## Features

* CLI based interaction (no GUI, simple terminal usage)
* Model training option
* Predict productivity based on user inputs
* Uses multiple input factors instead of just one

---

## Technologies Used

* Python
* pandas (for handling data)
* scikit-learn (for model training)

---

## How to Run

1. Install the required libraries:

```id="c3a9rf"
pip install -r requirements.txt
```

2. Run the main program:

```id="0xqbtr"
python src/main.py
```

3. First train the model, then use prediction

---

## Notes

The program is intentionally kept simple. There is no fancy interface or optimisation, but it focuses more on logic and understanding rather than presentation.

Also, results may vary slightly depending on input since the dataset is not perfectly structured.

---

## Learning Outcome

While working on this project, I got a better understanding of how basic ML models work, how data affects predictions, and how even small changes in input can change output.

It also helped in structuring a small project properly instead of just writing random code.

---

## Final Thought

This project is simple but useful in concept. It doesn’t claim to be fully accurate, but it gives an idea of how everyday habits can impact productivity, which is something most students deal with.

---
