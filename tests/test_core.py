from header_spoof import core

def test_audit_missing():
    # url inexistente -> cabecalhos vazios -> hsts/csp falsos
    r = core.audit("http://127.0.0.1:1/nope")
    assert r.get("hsts") is False
    assert r.get("csp") is False

def test_fetch_headers_empty():
    assert core.fetch_headers("http://127.0.0.1:1/x") == {}
