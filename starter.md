#DB
##Config
First run containers.

	docker-compose up -d

Second create db in **postgresql** container, **remember change "<db_name\>" by your custom database name.**

	docker-compose exec postgresql bash -c "su postgres -c 'createdb <db_name>'"
    
Third go to `node/app/project-conf/conf.json`, looks like:

```json
{
	"secret": "T5taxYXCXUuIFTTIycIy5lkkf09iHaJaZ34KOojbF9fLYL3aJEdC4NT3tKr4EMB",
	"server": {
		"HOST": "0.0.0.0",
		"PORT": 8000
	},
	"database": {
		"database": "db_name",
		"username": "super",
		"password": "root",
		"host": "postgresql",
		"dialect": "postgres",
		"pool": {
			"max": 10,
			"min": 0,
			"acquire": 30000,
			"idle": 10000
		},
		"query": {
			"raw": true
		}
	},
	"templates": {
		"path": "static",
		"_comment": "'engine' property can be used"
	},
	"tests": {
		"database": {
			"dialect": "sqlite"
		}
	}
}
```

Now you can change `database.database` by your db_name and edit other configurations if needed.

It is **highly recommended change `secret`** because it is used for cryptographic purposes.

Your db password in the json file needs to be equal to your db password in the `docker-compose.yml` configuration of the postgresql container:

```yaml
postgresql:
        image: paintedfox/postgresql
        volumes:
            - ./postgresql:/data
        ports:
            - "5432:5432"
        environment:
            - USER=<DB_USERNAME>
            - PASS=<DB_PASSWORD>
        restart: unless-stopped
        networks:
            - custom_network
```

##Models
To configure the models first you need to create them in the folder `node/app/project-db/lib/db/models/` and then create custom wrapper for the model in `node/app/project-db/lib/models/`.

Next go to `node/app/project-db/lib/db/index.js`, import models and models wrappers, now create models relations with sequelize interface and pass models to models wrapper to export them.

Example:

```javascript
'use strict'

const setupDatabase = require('./db')
// ******* IMPORT Models
const setupModel1Model = require('./models/model1')

// ******* IMPORT CModels
const setupModel1 = require('../models/model1')

const conf = require('project-conf/conf.json')
const defaults = require('defaults')
const dbConf = conf.database
const debug = require('debug')('project:db')
const chalk = require('chalk')

const handleError = require('project-utils/errors').handleError

async function setupDBAndCmodels (_conf) {
  debug(`${chalk.blue('[Initializing setupDBAndCmodels]')}`)

  _conf = defaults(_conf, dbConf)

  const sequelize = setupDatabase(_conf)

  debug(`${chalk.blue('[Authenticating DB]')}`, _conf)

  await sequelize.authenticate()
    .catch(handleAuthenticationError)

  debug(`${chalk.blue('[Setup Models]')}`)
  
  //******* INSTANCIATE MODELS
  const Model1Model = setupModel1Model(_conf)

  debug(`${chalk.blue('[Setup Relations]')}`)
  // ******* SET RELATIONS
  // EggModel.IPs = EggModel.hasMany(IPModel, { as: 'ips', onDelete: 'CASCADE' })
  // IPModel.Egg = IPModel.belongsTo(EggModel, { as: 'egg' })
  // IPModel.Clicks = IPModel.hasMany(ClickModel, { as: 'clicks', onDelete: 'CASCADE' })
  // ClickModel.IP = ClickModel.belongsTo(IPModel, { as: 'ip' })

  if (_conf.setup) {
    debug(`${chalk.blue('[Synchronizing DB]')}`)
    await sequelize.sync({ force: true })
      .catch(handleSyncError)
  }

  debug(`${chalk.blue('[Setup Cmodels]')}`)

  const Model1 = setupModel1(Model1Model, ...(others models whether needed))

  debug(`${chalk.blue('[Before return setupDBAndCmodels]')}`)
  
  // ******* EXPORT MODELS WRAPPERS
  return {
    Model1
  }
}
```


