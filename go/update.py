from pathlib import Path

import workflow

from .utils import create_db_conn

CWD = Path(__file__).parent

wf = workflow.Workflow()
url = wf.get_arg(1)

db_conn = create_db_conn()
db_conn.execute(f"UPDATE routes SET hits = hits + 1 WHERE url='{url}'")
db_conn.execute(f"UPDATE routes SET last_access = CURRENT_TIMESTAMP WHERE url='{url}'")
db_conn.commit()
