# airdrop_tools
## replace wallet address in the l0scan_url
> l0scan_url = "https://layerzeroscan.com/api/trpc/messages.list?input=%7B%22filters%22%3A%7B%22address%22%3A%22[wallet address]%22%2C%22stage%22%3A%22mainnet%22%2C%22created%22%3A%7B%7D%7D%7D"

## run script
>  python layerzero_airdrop_checker.py 

## Exception known
> {'error': {'message': 'TOO_MANY_REQUESTS', 'code': -32029, 'data': {'code': 'TOO_MANY_REQUESTS', 'httpStatus': 429, 'path': 'messages.list'}}}
- Solution: wait some minutes,then try again.