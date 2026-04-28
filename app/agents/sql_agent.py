from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm
from app.core.database import run_query


llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert SQL generator."),
    ("human", """
Convert the user query into SQL.

Table: sales

Columns:
date, region, product, category, units_sold, revenue, cost, profit

Rules:
- Use SQLite syntax
- Handle case sensitivity using LOWER()
- Example: LOWER(region) = 'south'
- Return ONLY SQL

Query: {query}
""")
])

def clean_sql(sql: str) -> str:
    # Remove markdown code blocks
    sql = sql.replace("```sql", "").replace("```", "")
    
    # Remove extra whitespace/newlines
    sql = sql.strip()
    
    return sql


def sql_node(state):
    query = state["query"]

    response = llm.invoke(
        prompt.format_messages(query=query)
    )

    raw_sql = response.content
    sql_query = clean_sql(raw_sql)

    return {
        "sql_query": sql_query
    }

def execute_sql_node(state):
    sql_query = state["sql_query"]

    data = run_query(sql_query)

    return {
        "data": data
    }