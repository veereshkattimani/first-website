import os
print(os.listdir())
print(os.listdir('./'))



try:
    print(os.listdir('./git_tutorial'))
except FileNotFoundError:
    print('git_tutorial directory not found')

