import os

git_url=input('Enter git repository URL:')

os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "first commit"')
os.system('git branch -M main')
os.system('git remote add origin '+ git_url)
os.system('git push -f origin main')

print('\n',10*'==', 'update cmpleted.........! Thank you..!',10*'==')
print()