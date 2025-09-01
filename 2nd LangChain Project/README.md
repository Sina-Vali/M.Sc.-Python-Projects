**Project description:**
Create a chain that takes the name of an area as input and returns the approximate time to cook a local dish and dockerize it. 

**How to run locally:**
- Download/clone this project and replace ... with your OpenAi api key in `OPENAI_API_KEY.txt`.
  
- For security, Create a file named .dockerignore in the project root with the following content:
  
  `# To not send secrets or local env files`
  
  `OPENAI_API_KEY.txt`
  
  `.env`
  
  `# Prevent sending version control or IDE junk`
  
  `.git`
  
  `.gitignore`
  
  `*.swp`
  
  `*.swo`
  
  `*.DS_Store`

  `.vscode/`

  `__pycache__/ `
  
  `*.pyc`
  

- Open your terminal and run the following:
  
  `docker build -t langchain-project:latest`
  `docker run -it --rm   -v "$(pwd)/OPENAI_API_KEY.txt:/app/OPENAI_API_KEY.txt:ro"   2nd-langchain-project:latest`
  
