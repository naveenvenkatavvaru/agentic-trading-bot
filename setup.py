from setuptools import find_packages, setup

setup(name="agentic-trading-system",
      version="0.0.1",
      author="Naveen",
      author_email="naveenvenkatavvaru@gmail.com",
      packages=find_packages(),
      install_requires=['langchain','lancedb','langgraph','tavily-python','polygon']
)

    
   