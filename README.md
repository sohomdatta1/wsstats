# wsstats

A repo for [this tool](https://wsstats.toolforge.org). Wsstats is a sucessor of phetool's statistics component rewritten in more modern technologies like VueJS and Flask. It is hosted on Toolforge and mainatined by [Sohom Datta](https://meta.wikimedia.org/wiki/User:Sohom_Datta)

## Deployment

To deploy on toolforge:

```sh
toolforge build start https://gitlab.wikimedia.org/toolforge-repos/wsstats.git
toolforge webservice --backend=kubernetes --mount=none buildservice start
```

To redeploy:

```sh
toolforge build start https://gitlab.wikimedia.org/toolforge-repos/wsstats.git
toolforge webservice --backend=kubernetes --mount=none buildservice restart
```

To deploy the statistics crawler you can use the following commands:

```sh
git clone https://gitlab.wikimedia.org/toolforge-repos/wsstats.git
cd wsstats && toolforge jobs load jobs.yaml
```

To setup the template update bot, edit `user-config.tmpl` to use the name of your bot account. Setup [OAuth for your bot account](https://www.mediawiki.org/wiki/Manual:Pywikibot/OAuth/Wikimedia#Registering_your_bot_with_the_wiki_software) and then run the following commands

```sh
toolforge envvars create CONSUMER_KEY <your consumer key>
toolforge envvars create CONSUMER_SECRET <your consumer secret>
toolforge envvars create ACCESS_TOKEN <your access token>
toolforge envvars create ACCESS_SECRET <your access secret>
```

## Contributions

Contributions are welcomed :)
