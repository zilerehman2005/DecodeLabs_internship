# Project 3 — AI Recommendation Logic
**DecodeLabs Industrial Training Kit | Batch 2026**

## 📌 Overview
Project 3 moves from classification into **personalization**. The goal is
to build a simple **content-based recommendation engine** that matches a
user's stated skills/interests to the most relevant items — without
needing any historical user-behavior data.

**Capstone assignment:** *Tech Stack Recommender* — maps a user's raw
skills and career goals to the most relevant job roles.

**Technique used:** TF-IDF vectorization + Cosine Similarity
(Content-Based Filtering)

## 🎯 Key Requirements Covered
- [x] Take user input (minimum 3 skills/interests)
- [x] Match preferences using similarity logic (not random suggestions)
- [x] Display ranked recommended items (Top-N list)
- [x] Vector mapping of qualitative data into numerical arrays
- [x] TF-IDF weighting (rewards specific skills, penalizes generic ones)
- [x] Cosine similarity scoring (robust to profile-size differences)
- [x] Cold-start handling for unmatched skills

## 🗂️ Files
| File | Description |
|---|---|
| `Project3_Tech_Stack_Recommender.ipynb` | Full Colab-ready notebook with all code and explanations |
| `README.md` | This file |

> **Note on data:** The notebook generates its own `raw_skills.csv` dataset
> in the first code cell (12 job roles, each tagged with representative
> skills) so it runs with **zero uploads** in Colab. You can freely edit
> that cell to add more job roles or skills.

## ▶️ How to Run in Google Colab
1. Go to [colab.research.google.com](https://colab.research.google.com).
2. Click **File → Upload notebook** and select
   `Project3_Tech_Stack_Recommender.ipynb`.
3. Click **Runtime → Run all**.
4. Scroll to the **"Try It — Enter Your Own Skills"** section, edit the
   `my_skills` list with your own three (or more) skills, and re-run that
   cell to get personalized recommendations.

All required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`,
`scikit-learn`) are pre-installed in Colab by default.

## 🧠 Pipeline (IPO Framework)

```
INPUT                          PROCESS                       OUTPUT
─────                          ───────                       ──────
User skills (≥3)         →     TF-IDF Vector Mapping   →     Ranked Top-N
raw_skills.csv (items)   →     Cosine Similarity              Job Role List
```

1. **Ingestion** — capture the user's skills as a list of strings (e.g.
   `["Python", "Cloud Computing", "Automation"]`).
2. **Vector Mapping** — fit one shared `TfidfVectorizer` on all job-role
   skill strings, so user input and item data live in the exact same
   numerical vocabulary space.
3. **Scoring** — transform the user's skill list into a vector using that
   same fitted vectorizer, then compute cosine similarity against every
   job role's vector.
4. **Sorting** — rank all job roles by descending similarity score.
5. **Filtering** — truncate to the Top-N (default 3) most relevant roles
   to prevent choice overload.

## 📐 Why TF-IDF + Cosine Similarity (Not Just Binary Overlap)?
- **Binary/Jaccard overlap** treats every skill equally — a generic skill
  like "Python" (appearing in many roles) counts the same as a specific
  skill like "Kubernetes." This produces noisy matches.
- **TF-IDF** downweights common/generic skills and upweights rare,
  descriptive ones, so the match reflects genuinely distinguishing signal.
- **Cosine similarity** measures the *angle* between the user's vector and
  each item's vector, making it insensitive to vector length/magnitude —
  a user with 3 skills can still score highly against a job role tagged
  with 7 skills, as long as the *direction* of interest aligns.

## 🧊 Cold-Start Handling
This project uses **content-based filtering**, which is naturally immune
to the *item* cold-start problem — a brand-new job role becomes
recommendable the moment it has skill tags (no interaction history
needed). The notebook also guards against the *user* cold-start case: if
none of the user's input skills exist anywhere in the vocabulary, all
similarity scores come out to zero, and the function detects this and
returns a clear fallback message instead of a meaningless ranking.

## 🔜 Suggested Extensions (Optional, for Deeper Learning)
- Expand `raw_skills.csv` with more job roles and richer, more granular
  skill tags.
- Weight certain skills manually (e.g. give "Leadership" less weight than
  "Kubernetes") and observe how rankings shift.
- Swap the job-roles dataset for a different domain (movies, courses,
  products) — the same vectorize → score → sort → filter skeleton applies
  directly to any content-based recommender.
- Compare results against a simple Jaccard/binary-overlap baseline to see
  TF-IDF's improvement firsthand.

---
*Submitted as part of the DecodeLabs Industrial Training Kit, Batch 2026.*
