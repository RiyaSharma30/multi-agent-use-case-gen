# multi-agent-use-case-gen
This repository hosts a multi-agent system to generate AI and GenAI use cases for companies or industries. It features market research, trend-based use case suggestions, resource link retrieval, and a Streamlit interface. Powered by LangChain and FAISS for efficient insights.
# Multi-Agent AI Use Case Generator

## Overview
This repository contains a multi-agent architecture system designed to generate AI and Generative AI (GenAI) use cases for a specified company or industry. By integrating advanced market research capabilities and trend analysis, the system delivers actionable insights and recommendations with efficiency and precision.

## Key Features
- **Market Research**: Conducts automated, detailed analysis of a company's focus areas, offerings, and vision within its industry.
- **Use Case Suggestions**: Provides industry-specific AI and GenAI use case proposals based on the latest trends and opportunities.
- **Resource Asset Links**: Fetches relevant datasets and resources to facilitate implementation.
- **Streamlit Interface**: Offers an intuitive front-end for user input and real-time result visualization.

## Technologies Used
- **LangChain**: Orchestrates multi-agent workflows and LLM interactions.
- **OpenAI GPT-4**: Powers natural language processing for generating research insights.
- **Streamlit**: Provides a user-friendly web application interface.
- **FAISS and OpenAI Embeddings**: Manages and queries vectorized data for efficient information retrieval.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository-name
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Add your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Access the application in your browser at `http://localhost:8501`.

## File Structure
- `app.py`: Main script for the Streamlit application.
- `requirements.txt`: Lists all dependencies for the project.
- `README.md`: Documentation for the project.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request for review.


## Contact
For questions or feedback, please contact riyasharmaa030@gmail.com.
