# AI Sustainable Business Growth Copilot

A multi-agent AI system designed to help businesses create sustainable growth strategies through intelligent planning, research, and analysis.

## Features

- **Multi-Agent Architecture**: Planner, Research, Strategy, Sustainability, and Reviewer agents
- **Session Management**: Persistent session storage for multi-step workflows
- **FastAPI Backend**: RESTful API for web integration
- **CLI Interface**: Command-line interface for batch processing
- **Sustainability Focus**: Environmental impact analysis and recommendations

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Required API Keys**
   - `GEMINI_API_KEY`: Google Gemini API key for AI text generation
   - `GOOGLE_SEARCH_API_KEY`: Google Custom Search API key (optional)
   - `GOOGLE_SEARCH_CSE_ID`: Custom Search Engine ID (optional)

## Running the Application

### Web API Server
```bash
python run.py
```
The API will be available at `http://localhost:8000`

### CLI Interface
```bash
python -m src.main --profile demo_cases.json --session_id my_session
```



## API Endpoints

- `GET /`: Health check
- `POST /onboard`: Store business profile
- `POST /plan`: Generate business plan only
- `POST /full_pipeline`: Run complete multi-agent workflow
- `POST /resume`: Resume existing session
- `GET /session/{session_id}`: Get session data

## Project Structure

```
src/
├── agents/          # AI agents (Planner, Research, Strategy, etc.)
├── llm/            # LLM client integrations
├── memory/         # Session and memory management
├── tools/          # Business calculation and analysis tools
├── utils/          # Logging, schemas, and utilities
├── tests/          # Unit tests
├── app.py          # FastAPI application
└── main.py         # CLI interface
```

## Testing

```bash
pytest src/tests/
```

## Recent Fixes Applied

1. **Import Path Corrections**: Fixed all relative imports to use absolute imports from `src` package
2. **API Key Security**: Fixed hardcoded API key in gemini_client.py to use environment variables
3. **Dependencies**: Added missing `google-api-python-client` to requirements.txt
4. **Environment Setup**: Created proper `.env.example` file with all required variables
5. **Test Fixes**: Corrected test imports and method calls to match actual implementation
6. **Startup Script**: Added `run.py` for easy application startup with environment support

## Usage Example

```python
# Business profile example
profile = {
    "business_name": "EcoTech Solutions",
    "industry": "Technology",
    "products": ["Solar panels", "Energy management software"],
    "current_revenue": 500000,
    "employees": 25
}

# API call to generate full strategy
response = requests.post("http://localhost:8000/full_pipeline", json={
    "session_id": "eco_session_1",
    "profile": profile
})
```

The system will generate comprehensive business growth strategies with sustainability recommendations.