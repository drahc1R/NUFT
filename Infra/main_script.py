import multiprocessing as mp
import concurrent.futures as cf
import Binance_Websocket as bc
import Kucoin_Websocket as ks
import Coinbase_Websocket as cb
import Kraken_Websocket as kr
import pandas as pd
import asyncio

#All functions imported need to be non-async! If you commit async functions, our code will not work, and we will have an emergency debugging in your 'honor'.

#Stage code
async def main(coins):
	with cf.ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
		# executor.submit(ks.run(coins))
		# executor.submit(cb.run(coins))
		# executor.submit(bc.run(coins))
		executor.submit(kr.run(coins))

#Run code
coins = []
if __name__ == '__main__':
	asyncio.get_event_loop().run_until_complete((main(coins)))
