import os
import json
from langchain.agents import initialize_agent, Tool
from langchain.tools import WebSearchTool
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.output_parsers import MarkdownOutputParser
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders.web import WebLoader
from langchain.utilities import CSVLoader
import streamlit as st

# Constants and configurations
DATASET_SOURCES = ["https://www.kaggle.com", "https://huggingface.co", "https://github.com"]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def setup_agent():
    """Sets up the multi-agent architecture."""
    llm = OpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
    search_tool = WebSearchTool()

    research_template = PromptTemplate(
        input_variables=["company", "industry"],
        template="Conduct detailed market research on {company} in the {industry} sector. Segment key focus areas, offerings, and vision.",
    )
    research_chain = LLMChain(llm=llm, prompt=research_template)

    use_case_template = PromptTemplate(
        input_variables=["industry"],
        template="Analyze current industry trends in {industry}. Suggest innovative AI and GenAI use cases.",
    )
    use_case_chain = LLMChain(llm=llm, prompt=use_case_template)

    return initialize_agent(
        [Tool(name="web_search", func=search_tool.search)],
        agent_type="zero-shot-react-description",
    ), research_chain, use_case_chain

def collect_resource_links(use_cases):
    """Collects resource links for the use cases generated."""
    links = []
    for source in DATASET_SOURCES:
        for use_case in use_cases:
            search_query = f"{use_case} dataset site:{source}"
            links.append(WebSearchTool().search(search_query))
    return links

def main():
    """Main function for Streamlit app deployment."""
    st.title("Market Research & Use Case Generator")

    agent, research_chain, use_case_chain = setup_agent()

    # Inputs
    company = st.text_input("Enter the company name:")
    industry = st.text_input("Enter the industry:")

    if st.button("Generate Report"):
        with st.spinner("Conducting market research..."):
            research_results = research_chain.run({"company": company, "industry": industry})
        st.subheader("Market Research")
        st.write(research_results)

        with st.spinner("Generating use cases..."):
            use_cases = use_case_chain.run({"industry": industry})
        st.subheader("Use Case Proposals")
        st.write(use_cases)

        with st.spinner("Fetching resource links..."):
            resource_links = collect_resource_links(use_cases)
        st.subheader("Resource Asset Links")
        for link_set in resource_links:
            st.markdown(f"- [Link]({link_set})")

if __name__ == "__main__":
    main()
