set -euo pipefail
IFS =$'\n\t'

PORT=8083

usage() {
  cat <<EOF
Usage: $0 {local|remote|<host>} [port]
  local           →  http://127.0.0.1:\$PORT
  remote          →  http://141.85.224.115:\$PORT
  <host> [port]   →  http://<host>:<port>
EOF
  exit 1
}

[[ $# -ge 1 ]] || usage

case "$1" in
  local)
    url="http://127.0.0.1:${PORT}"
    ;;
  remote)
    url="http://141.85.224.115:${PORT}"
    ;;
  *)
    host="$1"
    port="${2:-$PORT}"
    url="http://${host}:${port}"
    ;;
esac

echo "Target URL: ${url}/santa/"

main_js=$(curl -sSL "${url}/santa/assets/js/main.js")
b64=$(grep -oP 'atob\("\K[^"]+' <<< "$main_js")
flag=$(printf '%s' "$b64" | base64 -d)

echo "Flag is: $flag"
