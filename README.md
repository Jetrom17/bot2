# bot2

## Resumo:

- Usado software VSCode (https://code.visualstudio.com/Download).
- Usado terminal no VSCode.
- Usado servidor Heroku free.
- Usado linguagem de programação; Python.
- Usado no python; telebot (version: 0.0.4).
- Usado git (version 2.34.1).
- Usado S.O Linux Mint.

### Guia definitivo

- Primeiro antes de tudo, crie uma conta em **Heroku** caso já tenha prossiga:

https://www.heroku.com/

- Crie um app e dê um nome quaisquer, caso já tenha prossiga.

- Agora, clone o repositório no seu terminal, para isso abra-o:

```
$ git clone https://github.com/Jeiel17/bot2/tree/main/ENIGMA
```

- Execute o comando no seu terminal ainda:

```
$ cd ENIGMA
$ code .
```

Após ter entrado na pasta, em seguida acessado o programa VSCode, prossiga. **OBS:** Se usado o comando no terminal no VSCode, não execute o comando __code__.

- Agora execute para baixar o __git__ via terminal:

```
apt install git
```

- Em seguida modifique o __ENIGMA.py__ para seu bot ou contribua. Não esqueça de inserir o __My token__ a qual o @BotFather lhe dá.

- Por fim execute os comandos do Heroku no terminal:

```
$ heroku login
```

Usado uma única vez:

```
$ heroku git:clone -a topenigma 
$ cd topenigma
```

Todas as vezes que for fazer atualizações no bot, executar:

```
$ git add .
$ git commit -am "seu comentário"
$ git push heroku main
```

**OBS:** __main__ ou __master__ caso ocorra algum erro.

- Executar o bot.

```
heroku ps:scale bot=1
```

- Parar de executar o bot.

```
heroku ps:scale bot=0
```

# FIM.

Bot funcionando. Espero que tenha conseguido. 


Link **Telegram:** https://t.me/+eQ2Kz6LP_tc1NGYx Válido por ~67 dias (25/10/2022)

Link **Site:** https://jetronix.tk
