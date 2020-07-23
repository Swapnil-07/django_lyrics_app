git remote -v
# git remote add upstream https://github.com/Swapnil-07/django_lyrics_app.git
git fetch upstream
git checkout master
git merge upstream/master
git push
