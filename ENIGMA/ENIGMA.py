from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/consulta_cpf ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "@buscacpfbot".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/bot ?(.*)')
def example_command2(message, cmd):
    chat_dest = message['chat']['id']
    msg = "https://jetronix.tk/bot.html".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/bible ?(.*)')
def biblie(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Via Tor, Google, IPFS: \n https://bible4u.app/".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/deepweb ?(.*)')
def deep(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Use Tor: \n http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/lofi ?(.*)')
def lofi(message, cmd):
    chat_dest = message['chat']['id']
    msg = "https://app.lofi.co".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/livraria ?(.*)')
def livraria(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Via deep web ou Google. Para livros: \n https://1lib.domains/ \n Para artigos: \n https://1lib.domains/?articles".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/maxplay ?(.*)')
def example_command3(message, cmd):
    chat_dest = message['chat']['id']
    msg = "https://play.google.com/store/apps/details?id=br.com.well.musicas&gl=US".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/imune ?(.*)')
def example_command4(message, cmd):
    chat_dest = message['chat']['id']
    msg = "https://www.digitbin.com/whatsapp-mod/".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/tel ?(.*)')
def example_command5(message, cmd):
    chat_dest = message['chat']['id']
    msg = "https://ddd.guiamais.com.br/".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/start ?(.*)')
def start(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Bip Bop! Veja meus outros comandos ou aguarde um atendente:  \n \n https://media.tenor.com/4-063AYho6cAAAAM/robot-goodbye.gif".format(cmd)
    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   user_msg = message['text']

   msg = "Doe via pix (Bipa): \n a93ea08c-4239-44d8-8ffa-6a5687b1ed1c \n https://jetronix.tk/".format(user_msg)
   app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = 'SEU TOKEN'
    app.poll(debug=True)
