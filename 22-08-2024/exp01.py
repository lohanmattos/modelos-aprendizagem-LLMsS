#pip install duckduckgo-search
#pip install langchain
#pip install langchain_community

from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()

resultado = ddg_search.run("Ultimas informações economia brasileira")

print(resultado)