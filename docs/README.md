# 🛍️ DeepShop
![Chatbot](https://img.shields.io/badge/Chatbot-Intelligent-blue?style=for-the-badge&logo=chatbot) 
![LM-Studio](https://img.shields.io/badge/LM--Studio-AI-darkviolet?style=for-the-badge&logo=🤖) 
![Streamlit](https://img.shields.io/badge/Streamlit-white?style=for-the-badge&logo=streamlit) 
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white) 
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)

DeepShop is an intelligent chatbot 🤖 that helps you choose the best products through advanced comparison tables. It analyzes features, prices, and reviews to provide personalized recommendations.✨

## 📌 Requirements
- [LM-Studio](https://lmstudio.ai/) 🚀
- Python 3.x 🐍
- Dependencies specified in the `requirements.txt` file 📂

## 🔧 Installation
1. **Download and install LM-Studio** 💾
   - Follow the instructions on the official LM-Studio website.

2. **Download the model** 📥
   - Download the `deepseek-r1-distill-llama-8b` model from LM-Studio's model hub.

3. **Clone the repository** 🖥️
   ```sh
   git clone https://github.com/VincenzoVillanova/DeepShop.git
   cd DeepShop
   ```

4. **Install dependencies** 📌
   ```sh
   pip install -r requirements.txt
   ```

5. **Configure LM-Studio** ⚙️
   - Load the `deepseek-r1-distill-llama-8b` model into LM-Studio.
   - Copy the contents of the `prompt.txt` file into the system prompt of the chatbot within LM-Studio.
   - Start the model in local mode. 🚀

6. **Run the chatbot** ▶️
   ```sh
   streamlit run deep_shop.py
   ```

## ⚙️ Configuration
Make sure LM-Studio is running with the `deepseek-r1-distill-llama-8b` model loaded and properly configured to support DeepShop. Ensure the `prompt.txt` file is set as the system prompt for optimal performance. ✅

## 💡 Usage
Interact with the chatbot to receive shopping recommendations based on intelligent comparison tables. 🛒

## 📜 License
This project is distributed under the MIT license. For more details, see the `LICENSE` file. 📄

## 📁 Project Structure
```sh
DeepShop/
│
├── src/                    
│   └── deep_shop.py        
│
├── data/                  
│   └── prompt.txt           
│
├── docs/                  
│   ├── README.md           
│   └── LICENSE            
│
├── requirements.txt        
```
