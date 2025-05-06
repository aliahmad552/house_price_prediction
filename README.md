# 🏠 House Price Prediction Web App

A simple and intuitive web application that predicts house prices based on user input (location, total square feet, number of bathrooms, and number of bedrooms). This app is built using **Flask** on the backend and a trained **Linear Regression model** pipeline using **scikit-learn**.

---

## 🚀 Features

- Predict house prices in different locations.
- Uses a trained machine learning model with OneHotEncoding and StandardScaler.
- Built with Python, Flask, HTML, CSS, and JavaScript.
- Dynamic location dropdown using values from a CSV.
- Responsive and user-friendly interface.

---

## 🧠 Technologies Used

- Python 3
- Flask
- HTML/CSS/JavaScript
- scikit-learn
- pandas
- pickle (for saving model)
- OneHotEncoder, StandardScaler, LinearRegression

---

## 🗂️ Project Structure

project/
│
├── templates/
│ └── index.html # Frontend HTML form
├── lr.pkl # Trained pipeline model (pickled)
├── locations.csv # List of unique locations
├── app.py # Flask backend server
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
2. Create Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
Sample requirements.txt:

nginx
Copy
Edit
Flask
scikit-learn
pandas
4. Run the Flask App
bash
Copy
Edit
python app.py
Then visit http://localhost:5000 in your browser.

🧠 Model Details
Trained using LinearRegression()

Pipeline includes:

OneHotEncoder for 'location'

StandardScaler for numerical features

Trained on housing dataset with features:

location

total_sqft

bath

bhk

🧪 Example Inputs
Location	Total Sqft	Bath	BHK	Predicted Price
Whitefield	1200	2	2	₹ 85.45 Lakhs
Electronic City	1500	3	3	₹ 105.30 Lakhs

📸 Screenshots
You can add screenshots of your app here

🤝 Contributing
Feel free to fork the repo and submit a pull request for any feature or improvement.

📧 Contact
If you have any questions or suggestions, feel free to contact:

Ali Ahmad
📧 ali@example.com
🎓 Software Engineering | Islamia University of Bahawalpur

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

Would you like me to generate the `requirements.txt` as well for your exact setup?
