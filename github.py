import os
import asyncio


async def init():

	options = int(input('\n---------------------------------------\n1) Create a new repository\n2) Push an existing repository\n'))
	if options == 1:
		os.system('git init')
		await asyncio.sleep(1.5)
		git_add = input('\n---------------------------------------\ngit add ')
		os.system(f'git add {git_add}')
		git_commit = input('git commit -m ')
		os.system(f'git commit -m {git_commit}')
		os.system('git branch -M main')
		git_remote = input('git remote add origin ')
		os.system(f'git remote add origin {git_remote}')
		os.system('git push -u origin main')

	if options == 2:
		git_add = input('\n---------------------------------------\ngit add ')
		os.system(f'git add {git_add}')
		git_commit = input('git commit -m ')
		os.system(f'git commit -m {git_commit}')
		os.system('git branch -M main')
		os.system('git push -u origin main')


asyncio.run(init())

