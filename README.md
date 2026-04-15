## Nexus: AI-Powered Network Intrusion Detection System (NIDS)
Nexus is a machine learning-based security solution designed to detect and classify network intrusions in real-time. By utilizing Deep Learning architectures, the system analyzes network traffic patterns to identify potential threats, helping to safeguard digital infrastructure from unauthorized access and malicious activities.

## 🚀 Features
* **Deep Learning Classification:** Utilizes a trained neural network (nids_model.h5) for high-accuracy threat detection.
* **Real-time Dashboard:** A user-friendly interface built with Streamlit for monitoring and analysis.
* **Data Preprocessing:** Automated scaling and transformation of network data using a pre-trained scaler.pkl.
* **Comprehensive Documentation:** Includes a full project report and presentation video for detailed insights.

## 🛠️ Tech Stack
* **Language:** Python.
* **Framework:** Streamlit (Frontend Dashboard).
* **Machine Learning:** TensorFlow/Keras (Deep Learning), Scikit-learn (Preprocessing).
* **Data Handling:** Pandas, NumPy.
* **Training Environment:** Jupyter Notebook (NIDS.ipynb).

## 📁 Repository Structure
* **app.py:** The main entry point for the Streamlit web application.
* **nids_model.h5:** The saved Deep Learning model after training.
* **scaler.pkl:** The saved scaler object used for normalizing input data.
* **NIDS.ipynb:** The notebook containing data exploration, preprocessing, and model training logic.
* **Project Report.docx:** Detailed academic and technical documentation of the project.
* **Presentation (2).mp4:** A video walkthrough of the project and its results.
* **requirements.txt:** List of Python dependencies required to run the project.

## ⚙️ Installation & Setup
1. **Clone the Repository:**
   ```Bash
   git clone https://github.com/Hibaa0022/Ai-Ml-project.git
   cd Ai-Ml-project
   ```
2. **Create a Virtual Environment (Recommended):**
   ```Bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```Bash
   pip install -r requirements.txt.txt
   ```
4. **Run the Application:**
   ```Bash
   streamlit run app.py
   ```

## 📊 Dataset
The model was trained and evaluated using the NSL-KDD dataset, a benchmark dataset for network security research that addresses many of the inherent problems of the original KDD'99 dataset.

## 📝 License
This project is for educational purposes. Feel free to use the code for learning and development.

## 
Developed as a Course Learning project.











