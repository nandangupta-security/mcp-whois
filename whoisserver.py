# MCP Server — WHOIS Lookup
# Install: pip install mcp python-whois

from mcp.server.fastmcp import FastMCP
import whois

mcp = FastMCP("WHOIS Server")

@mcp.tool()
def whois_lookup(domain: str) -> str:
    """Perform a WHOIS lookup for a domain and return registration details."""
    try:
        w = whois.whois(domain)
        fields = {
            "Domain Name":     w.domain_name,
            "Registrar":       w.registrar,
            "Creation Date":   w.creation_date,
            "Expiration Date": w.expiration_date,
            "Updated Date":    w.updated_date,
            "Name Servers":    w.name_servers,
            "Status":          w.status,
            "Emails":          w.emails,
            "Registrant Org":  w.org,
            "Country":         w.country,
        }
        lines = []
        for label, value in fields.items():
            if value is None:
                continue
            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)
            lines.append(f"{label}: {value}")
        return "\n".join(lines) if lines else "No WHOIS data found."
    except Exception as e:
        return f"WHOIS lookup failed: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
