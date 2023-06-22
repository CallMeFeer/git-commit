import os
import asyncio


async def init():
	os.system('git init')
	await asyncio.sleep(1.5)
	options = int(input('\n---------------------------------------\n1) Create a new repository\n2) Push an existing repository\n'))
	if options == 1:
		#git_add = input('git add ')
		os.system('git add .')

		git_commit = input('git commit -m ')
		print(git_commit)
		os.system(f'git add {git_commit}')

		os.system('git branch -M main')

		git_remote = input('git remote add origin ')
		os.system(f'git add {git_commit}')

		os.system('git push -u origin main')
		

asyncio.run(init())

