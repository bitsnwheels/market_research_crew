import streamlit as st
import warnings
from dotenv import load_dotenv
from src.market_research_crew.crew import MarketResearchCrew

# Suppress warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load environment variables
load_dotenv()

# Set up the web page layout
st.set_page_config(page_title="AI Market Research Generator", page_icon="📊", layout="wide")
st.title("AI Market Research Generator")
st.write("Enter your AI product idea below, and our multi-agent system will generate a comprehensive business report.")

# Input from the user
product_idea = st.text_area("Product Idea", placeholder="e.g., An AI-powered tool that summarizes YouTube videos...")

# Button to trigger the research
if st.button("Generate Report"):
    if not product_idea.strip():
        st.warning("Please enter a product idea.")
    else:
        with st.spinner("Our AI agents are conducting research. This may take a few minutes..."):
            try:
                # Set up inputs
                inputs = {'product_idea': product_idea}
                
                # Kick off the crew
                result = MarketResearchCrew().crew().kickoff(inputs=inputs)
                
                # Display the output
                st.success("Research Complete!")
                
                # CrewAI returns a CrewOutput object. We cast it to string to get the markdown text.
                st.markdown(str(result))
                
            except Exception as e:
                st.error(f"An error occurred: {e}")