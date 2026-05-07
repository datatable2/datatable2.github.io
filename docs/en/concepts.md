# Basic Concepts

## FRM Array

An FRM array is a binary data format for storing results of sociological and marketing research.

Each array consists of:
- ✅ Questionnaires — respondent answers
- ✅ Questions (signs/variables) — list of survey questions
- ✅ Alternatives — answer options for each question

## Question Types

| Type | Description |
|---|---|
| `qm` | **Metric** — numeric value (age, income, rating) |
| `qn` | **Nominal** — single answer from options (gender, city, education) |
| `qj` | **Multi-variant** — multiple answers simultaneously (product usage, information sources) |

## Questionnaire Structure

Each questionnaire has a fixed size in bytes. Questions are stored sequentially one after another.

> 💡 **Limitation:** Maximum size of a single questionnaire is 30,000 bytes
