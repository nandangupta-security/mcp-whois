# WHOIS MCP Server

A simple MCP server that performs WHOIS lookups for any domain, built with [FastMCP](https://github.com/jlowin/fastmcp).

---

## Requirements

- Python 3.8+
- Claude Desktop

---

## Installation

**1. Clone or download the server file**

Save `whois_server.py` to a directory on your machine, e.g.:
```
~/mcp-servers/whois_server.py
```

**Option A — Without a virtual environment (simple)**

```bash
pip install mcp python-whois
```

**Option B — With a virtual environment (recommended)**

A virtual environment keeps dependencies isolated from the rest of your system.

```bash
python -m venv venv
```

Activate it:

- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

Then install dependencies:

```bash
pip install mcp python-whois
```

> To deactivate the virtual environment later, run `deactivate`.

---

## Configure Claude Desktop

Open your Claude Desktop config file:

- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the following:

**Without virtual environment:**

```json
{
  "mcpServers": {
    "whois": {
      "command": "python",
      "args": ["/full/path/to/whois_server.py"]
    }
  }
}
```

**With virtual environment:**

```json
{
  "mcpServers": {
    "whois": {
      "command": "/full/path/to/venv/bin/python",
      "args": ["/full/path/to/whois_server.py"]
    }
  }
}
```

> - **Mac/Linux venv path:** `path/to/venv/bin/python`
> - **Windows venv path:** `path\to\venv\Scripts\python.exe`
> - Always use the full absolute path. On Mac/Linux, run `realpath whois_server.py` to get it.

**Restart Claude Desktop** after saving the config.

---

## Usage

Once installed, you can ask Claude things like:

- _"What is the WHOIS info for google.com?"_
- _"When does apple.com expire?"_
- _"Who registered openai.com?"_

### Example Output

```
Domain Name: google.com
Registrar: MarkMonitor Inc.
Creation Date: 1997-09-15 04:00:00
Expiration Date: 2028-09-14 04:00:00
Updated Date: 2019-09-09 15:39:04
Name Servers: ns1.google.com, ns2.google.com, ns3.google.com, ns4.google.com
Status: clientDeleteProhibited, clientTransferProhibited
Emails: abusecomplaints@markmonitor.com
Country: US
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `command not found: python` | Use `python3` instead in the config |
| `ModuleNotFoundError: whois` | Run `pip install python-whois` |
| No data returned | Some TLDs have restricted WHOIS data |
| Tool not showing in Claude | Double-check the file path and restart Claude Desktop |

---

## File Structure

```
mcp-servers/
└── whois_server.py   # The MCP server
└── README.md         # This file
```
