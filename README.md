# node-watchdog

🐶 Simple watchdog for blockchain RPC endpoints.

## Quick start
```bash
git clone https://github.com/Kuk5466/node-watchdog.git
cd node-watchdog
pip install -r requirements.txt
python -m watchdog.monitor --rpc https://rpc.ankr.com/eth --tries 5

