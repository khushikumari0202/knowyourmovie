# 🎬 KnowYourMovie

KnowYourMovie is a **Movie Recommendation System** that suggests movies based on user preferences using **Machine Learning (Content-Based Filtering)**. It analyzes movie features like genres, cast, keywords, and overview to recommend similar movies.

---

## 🚀 Features

- 🔍 Search movies by name
- 🎯 Get top similar movie recommendations
- 🧠 Uses ML for similarity detection
- 📊 Clean and simple interface
- ⚡ Fast and efficient performance

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK
- **Model:** CountVectorizer + Cosine Similarity
- **Dataset:** TMDB Movie Dataset
- **Frontend (if used):** React / HTML / CSS / Tailwind

---

## 📂 Project Structure

```

knowyourmovie/
│
├── app.py                # Main application file
├── model.pkl             # Saved ML model
├── similarity.pkl        # Similarity matrix
├── requirements.txt      # Dependencies
└── README.md

````

---

## ⚙️ How It Works

1. **Data Collection**
   - Movie dataset is loaded (TMDB dataset)

2. **Data Preprocessing**
   - Select important columns:
     - Genres
     - Keywords
     - Cast
     - Crew
     - Overview

3. **Feature Engineering**
   - Combine all features into a single column called `tags`

4. **Text Vectorization**
   - Convert text into vectors using `CountVectorizer`

5. **Similarity Calculation**
   - Compute similarity using **Cosine Similarity**

6. **Recommendation**
   - Find top 5 most similar movies based on input

---

## 🧪 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/khushikumari0202/knowyourmovie.git
cd knowyourmovie
````

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```bash
python app.py
```

---

## 📌 Example

**Input:**

```
Avatar
```

**Output:**

```
Titanic
Guardians of the Galaxy
Interstellar
The Avengers
Inception
```

---
---

## 💡 Future Enhancements

* ⭐ Add user rating system
* 🎥 Show movie trailers
* 👤 Add login/signup (authentication)
* 🌐 Deploy using AWS / Render / Vercel
* 🤖 Improve model using deep learning

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👩‍💻 Author

**Khushi Kumari**
🎓 CSE Student @ VIT Bhopal
💻 Web Developer | AI Enthusiast

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

```

---

