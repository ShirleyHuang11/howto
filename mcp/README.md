# howto MCP server 🤖🦾

Give your agent the **verified steps for 1,300+ everyday tasks** — at inference time, over the
[Model Context Protocol](https://modelcontextprotocol.io). Instead of guessing (and confidently
skipping the step that actually matters), the agent searches the corpus and reads the recipe:
every step with its **expected observation**, ⚠ markers on **irreversible** steps, failure
recovery, and a checkable **"done when"**.

## Tools

| Tool | What it does |
|---|---|
| `list_domains()` | List task domains with recipe counts. |
| `search_howto(query, domain?, limit?)` | Find recipes for a task, ranked. |
| `get_howto(id)` | Full step-by-step for one recipe id (e.g. `transit/ride-a-subway`). |

## Install

```bash
git clone https://github.com/ShirleyHuang11/howto.git
cd howto
pip install -r mcp/requirements.txt      # mcp, pyyaml
python3 mcp/server.py                     # speaks MCP over stdio
```

## Wire it into a client

**Claude Code**

```bash
claude mcp add howto -- python3 /absolute/path/to/howto/mcp/server.py
```

**Claude Desktop / Cursor** — add to the MCP config (`claude_desktop_config.json` or the
client's equivalent):

```json
{
  "mcpServers": {
    "howto": {
      "command": "python3",
      "args": ["/absolute/path/to/howto/mcp/server.py"]
    }
  }
}
```

Then ask your agent something like *"before you do this, check howto for how to change a flat
tire"* — it will call `search_howto` → `get_howto` and follow the verified procedure, warnings
and all.

## Notes

- Recipes are parsed with the repo's own parser (`../scripts/export.py`), so what the agent
  reads never drifts from what the validator enforces.
- The whole corpus loads into memory once at startup (~1,500 small markdown files); no network,
  no database.
- Content is CC BY 4.0 — see the repo [LICENSE](../LICENSE).
