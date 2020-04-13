# interactive

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fm75/interactive/master) Jupyter

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fm75/interactive/master?urlpath=lab) JupyterLab

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fm75/interactive/master?urlpath=lab%2Ftree%2Fnotebook.ipynb) Lab notebook

[heroku](https://panel-exp.herokuapp.com/
)
## Getting interactive working in Jupyterlab

## Attempting to build app via Panel
https://panel.holoviz.org/user_guide/Server_Deployment.html. 
Trying first to get it to work on Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fm75/interactive/master?urlpath=%2Fproxy%2F5006%2Fpanel_exp) App

## Heroku deployment
1. [Create account](https://signup.heroku.com/)
1. [Download heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
1. Clone repo to localhost
1. Select app-name (lowercase letters, numbers, and -)
1. Modify `Procfile` using that name instead of `app-name` and your notebook-name in:
```sh
web: panel serve --address="0.0.0.0" --port=$PORT notebook-name.ipynb --allow-websocket-origin=app-name.herokuapp.com
```
1. Create app in CLI with 
```sh
heroku create [app-name]
```
1. Push the repo to heroku
```sh
git push heroku master
```
1. Run the app at https://app-name.herokuapp.com




[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fm75/interactive/master?urlpath=%2Fproxy%2F5006%2Fpanel_exp) App
