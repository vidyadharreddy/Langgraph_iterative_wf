from langgraph.graph import StateGraph,START,END
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from typing import TypedDict,Literal,Annotated
import operator
from pydantic import Field,BaseModel
from langchain_groq import ChatGroq
load_dotenv()
class post_create(TypedDict):
    topic : str =Field(description="Topic on which social platform post required")
    post : str
    evaluation : str = Literal["Approved","Not approved"]
    feedback : str
    iteration : int
    max_iteration : int


class postEvaluation(BaseModel):
    evaluation : Literal["Approved","Not approved"] = Field(description="Final evaluation")
    feedback : str = Field(description="Feedback on the post given mentioning merits and demerits in 100 words ")

llm = ChatGroq(model="llama-3.3-70b-versatile")
structured_model=llm.with_structured_output(postEvaluation)

def generate ( state: post_create) :
    topic=state["topic"]
    messages=[ SystemMessage  (content = "You are social platform post generator"),
                HumanMessage  (content = f"""Generate a post in 200 words on topic {topic} for publishing in my twitter!
                                            post must be creative, it should contain new content, humorous, informative
                                            there should not  be any critisisam """)
            ]
    post=llm.invoke(messages)

    return {"post": post.content}

def evaluate_post(state:post_create):
  
    post=state["post"]
    messages=[ SystemMessage  (content = "You are social platform post critic and evaluator"),
                HumanMessage  (content = f"""evaluate the the post: {state["post"]}, check whether this post is humourous, 
                                            realiasti, informative, new contect  and genetate evaluation in fallowing format \n
                                            evaluation : "Approved", "Not approved" \n
                                            feedback: Here mention merita snd demerita of the post""")

    
            ]
    result=structured_model.invoke(messages)
   
    return {"evaluation": result.evaluation, "feedback":result.feedback}

def optimize_post(state:post_create) :
    #feedback = state["fedback"]
    #evaluation = state["evaluation"]
    iteration= state["iteration"] +1
    messages=[ SystemMessage  (content = "You are social platform post critic and evaluator and advisor"),
                HumanMessage  (content = f"""evaluate the the post based on feedback\n post: {state["post"]},
                                            feedback :{ state["fedback"]} \n on topic:{state["topic"]}  check whether this post is humourous, 
                                            realiasti, informative, new contect  and genetate new post for my twitter \n
                                            """)]
  
    post=llm.invoke(messages)

    return {"post": post.content, "iteration" : iteration }

def route_evaluation (state : post_create):
    evaluation=state["evaluation"]
    print(evaluation)
    iteration=state["iteration"]
    max_iteration=state["max_iteration"]

    if evaluation == "Approved" :
        return "Approved"

    else :
        return "Not approved"
    
graph = StateGraph(post_create)
graph.add_node("generate", generate)
graph.add_node("evaluate_post", evaluate_post)

graph.add_node("optimize_post", optimize_post)


graph.add_edge(START, "generate")
graph.add_edge("generate", "evaluate_post")
graph.add_conditional_edges("evaluate_post",route_evaluation,{"Approved":END, "Not approved":"optimize_post"})
graph.add_edge("optimize_post","evaluate_post")

wf=graph.compile()

topic=input("Enter topic:")

input= {"iteration" : 1, "topic": topic, "max_iteration" : 5}
result=wf.invoke(input)
print(result["post"])
