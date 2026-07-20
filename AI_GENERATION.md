# AI Generation — make plans purely with an AI (0 budget)

`hustle_forge` can produce plans two ways:

1. **Pre-authored AI plans** (default, no setup). The repo ships
   `ai_plans/<niche>.md` files already written by an AI. `gen` uses them
   directly — so the delivered plans are genuinely AI-made, with zero
   network and zero cost.
2. **Live LLM call** (optional). Set an OpenAI-compatible endpoint and the
   tool asks the model to author a fresh plan on demand.

## Enable live AI generation (free)
The client is dependency-free (uses `urllib`). Point it at any
OpenAI-compatible API:

```bash
# Local, 100% free — Ollama (https://ollama.com)
ollama pull llama3.1
export HUSTLE_LLM_BASE_URL="http://localhost:11434/v1"
export HUSTLE_LLM_MODEL="llama3.1"

# …or a hosted free/cheap endpoint
# export HUSTLE_LLM_BASE_URL="https://api.openai.com/v1"
# export HUSTLE_LLM_KEY="sk-..."
# export HUSTLE_LLM_MODEL="gpt-4o-mini"
```

Then:
```bash
python -m hustle_forge gen ai-resume-rewrite --ai
```

If the endpoint is unreachable or unset, `gen` silently falls back to the
shipped AI plan, then to the offline template — so it always works at €0.

## Force the offline template
```bash
python -m hustle_forge gen ai-resume-rewrite --template
```
