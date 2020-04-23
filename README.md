### settings.json
```
{
  "team.showWelcomeMessage": false,
  "python.dataScience.sendSelectionToInteractiveWindow": true,
  "git.enableSmartCommit": true,
  "powershell.codeFormatting.useCorrectCasing": true,
  // "files.autoSave": "onWindowChange",
  "python.pythonPath": "nenv/bin/python",
  "python.linting.pylintPath": "nenv/bin/pylint",
  "python.linting.pylintArgs": ["--load-plugins=pylint_django"]
}

```

### Demo
```
LiveDemo: https://be-audiovyvy-django.herokuapp.com/
```

### Tree menu
```
{
   "menu":[
      {
         "id":"contact",
         "leaf":true,
         "description":"Contact Us",
         "link":"",
         "content":"contactUs.html",
         "cssClass":"static-content",
         "menu":null
      },
      {
         "id":"rules",
         "leaf":false,
         "description":"Sports Betting Rules",
         "link":"",
         "content":"",
         "cssClass":"",
         "menu":[
            {
               "id":"types",
               "leaf":true,
               "description":"Wager Types",
               "link":"",
               "content":"wagerTypes.html",
               "cssClass":"static-content wager-types",
               "menu":null
            },
            {
               "id":"odds",
               "leaf":true,
               "description":"Odds & Lines",
               "link":"",
               "content":"oddsAndLines.html",
               "cssClass":"static-content",
               "menu":null
            },
            {
               "id":"policies",
               "leaf":true,
               "description":"Rules & Policies",
               "link":"",
               "content":"rulesAndPolicies.html",
               "cssClass":"static-content rules-policies",
               "menu":null
            },
            {
               "id":"bonuses",
               "leaf":true,
               "description":"Sports Bonuses",
               "link":"",
               "content":"sportsBonuses.html",
               "cssClass":"static-content",
               "menu":null
            }
         ]
      },
      {
         "id":"conditions",
         "leaf":false,
         "description":"Terms & Conditions",
         "link":"",
         "content":"",
         "cssClass":"",
         "menu":[
            {
               "id":"termsOfService",
               "leaf":true,
               "description":"Terms of Service",
               "link":"",
               "content":"termsOfService.html",
               "cssClass":"static-content",
               "menu":null
            },
            {
               "id":"privacy",
               "leaf":true,
               "description":"Privacy Policy",
               "link":"",
               "content":"privacy.html",
               "cssClass":"static-content",
               "menu":null
            }
         ]
      },
      {
         "id":"view",
         "leaf":true,
         "description":"View in: Mobile | Full Site",
         "link":"",
         "content":"view.html",
         "cssClass":"static-content",
         "menu":null
      }
   ]
}
```