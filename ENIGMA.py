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
    msg = "https://jetronix.tk/bot".format(cmd)
    app.send_message(chat_dest, msg)

@app.route('/maxplay ?(.*)')
def example_command3(message, cmd):
    chat_dest = message['chat']['id']
    msg = "https://play.google.com/store/apps/details?id=br.com.well.musicas&gl=US".format(cmd)
    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   user_msg = message['text']

   msg = "Saiba mais sobre mim: https://jetronix.tk/bot".format(user_msg)
   app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = 'My token'
    app.poll(debug=True)
