# %%
import sys
if 'ipykernel' not in sys.modules:
    from load_ava_02 import get_processed_dataset # type: ignore

df = get_processed_dataset()

df.head()
# %%
