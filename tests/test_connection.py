from app.connection import Connection

def test_execute(caplog):
    conn = Connection()
    rows = conn.execute("select * from transactions limit 10")
    assert len(rows) == 10