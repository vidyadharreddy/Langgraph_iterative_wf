# Langgraph_iterative_wf
Langgraph iterative workflow
AI Social Media Post Generator using LangGraph
Overview

This project is an AI-powered Twitter/X post generation workflow built using:

LangGraph
LangChain
Groq LLM (llama-3.3-70b-versatile)
Pydantic
Python

The application generates creative social media posts on a given topic, evaluates the generated content, and automatically improves the post until it gets approved.

Features
AI-generated Twitter/X posts
Automated post evaluation
Feedback-driven post optimization
Iterative refinement workflow
Structured output using Pydantic
Workflow orchestration using LangGraph
Workflow
START
   ↓
Generate Post
   ↓
Evaluate Post
   ↓
Approved ? ─── Yes ──→ END
   ↓ No
Optimize Post
   ↓
Evaluate Again
Tech Stack
Python
LangGraph
LangChain
Groq API
Pydantic
dotenv
Installation
1. Clone Repository
git clone https://github.com/yourusername/social-post-generator.git

cd social-post-generator
2. Create Virtual Environment
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Requirements

Create a requirements.txt file:

langgraph
langchain
langchain-core
langchain-groq
python-dotenv
pydantic
Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

Get your API key from:

https://console.groq.com/

Project Structure
project/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
Code Explanation
1. Generate Post

The generate() function creates a Twitter/X post based on the given topic.

Features:
Humorous
Informative
Creative
Non-critical content
2. Evaluate Post

The evaluate_post() function checks whether the post is:

Humorous
Realistic
Informative
Original

It returns:

{
   "evaluation": "Approved",
   "feedback": "..."
}
3. Optimize Post

If the post is not approved, the optimize_post() function regenerates the post using evaluator feedback.

4. LangGraph Workflow
graph = StateGraph(post_create)

Workflow Nodes:

generate
evaluate_post
optimize_post

Conditional routing decides whether to:

End workflow
Continue optimization
Running the Project
python main.py

Example:

Enter topic: Artificial Intelligence
Example Output
🚀 AI is changing the world faster than your phone battery drains at 5%!

From generating art to writing code, GenAI is becoming the ultimate digital sidekick...
Future Improvements
Add LinkedIn/Facebook/Instagram support
Add image generation
Add hashtag optimization
Store post history in database
Add Streamlit UI
Add sentiment analysis
Add multilingual support
Known Issues
Typo in Code

Replace:

state["fedback"]

With:

state["feedback"]
Add Max Iteration Logic

Currently max_iteration is not enforced.

Suggested fix:

if iteration >= max_iteration:
    return "Approved"
Sample Improvements

You can improve prompts by:

Adding audience targeting
Tone customization
Emoji control
Post length control