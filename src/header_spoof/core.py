"""Sonda configuracoes de seguranca web (cabecalhos/CORS)."""
from __future__ import annotations
import urllib.request

CHECKS = ['cors']

def fetch_headers(url: str) -> dict:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as r:
            return dict(r.headers)
    except Exception:
        return {}

def audit(url: str) -> dict:
    h = {k.lower(): v for k, v in fetch_headers(url).items()}
    out = {}
    if "security-headers" in CHECKS:
        out["hsts"] = "strict-transport-security" in h
        out["csp"] = "content-security-policy" in h
        out["xframe"] = "x-frame-options" in h
    else:
        out["hsts"] = out["csp"] = out["xframe"] = False
    if "cors" in CHECKS:
        out["cors_acao"] = h.get("access-control-allow-origin")
    else:
        out["cors_acao"] = None
    return out

def main(argv=None):
    import sys, json
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("uso: __PKG__ <url>")
        return 2
        print(json.dumps(audit(argv[0]), indent=2))
        return 0
