var BOSH_SERVICE = 'https://jabber.hot-chilli.net/http-bind';
var connection = null;
var fromJid = "mary@jabber.hot-chilli.net";
//var toJid = "ciro@jabber.hot-chilli.net";
var toJid = "test2@bots.cleopatra-agents.cloud";

window.addEventListener('load', waitForElement, 'test');
//document.addEventListener('DOMContentLoaded', bot_connect, false);

function waitForElement(){
	let jid = sessionStorage.getItem("nick");
	console.log(jid);
    if(jid !== null){
		console.log('defined');
        bot_connect();
    }
    else{
				console.log('undefined');

        setTimeout(waitForElement, 2500);
    }
}


function waitForJid(){
	let jid = sessionStorage.getItem("nick");
    if(jid){
		console.log('found');
        return true;
    }
    else{
        return false;
    }
}


function bot_connect() {  // clic per cambiare i messaggi

	let jid = sessionStorage.getItem("nick");

    if(jid){
        console.log(jid);


        connection = new Strophe.Connection('https://conversejs.org/http-bind/');
	   
        connection.connect('chat.cleopatra-agents.cloud',null, onConnect);
		
    }


};



function log(msg)
{
    console.log(msg);
}


function onConnect(status)
{
    if (status == Strophe.Status.CONNECTING) {
        log('Strophe is connecting.');
    } else if (status == Strophe.Status.CONNFAIL) {
        log('Strophe failed to connect.');
    } else if (status == Strophe.Status.DISCONNECTING) {
        log('Strophe is disconnecting.');
    } else if (status == Strophe.Status.DISCONNECTED) {
        log('Strophe is disconnected.');
    } else if (status == Strophe.Status.CONNECTED) {
        log('Strophe is connected.');
        //log('ECHOBOT: Send a message to ' + connection.jid +  to talk to me.');

        connection.addHandler(onMessage, null, 'message', null, null,  null);
        connection.send($pres().tree());
		let jid = sessionStorage.getItem("nick");
		//jid=true;
		while(!jid){
			let jid = sessionStorage.getItem("nick");
			sleep(2000);
		}
		sendMyMsg(jid);
    }
}

//Questa funzione viene chiamata quando devo ricevere un messaggio (una sorta di listener,
// viene chiamato anche quando il mio interlocutore inzia a scrivere nella nostra chat)
function onMessage(msg) {
    console.log("Ho chiamato onMessage");
    var to = msg.getAttribute('to');
    var from = msg.getAttribute('from');
    var type = msg.getAttribute('type');
    var elems = msg.getElementsByTagName('body');

    if (type == "chat" && elems.length > 0) {
        var body = elems[0];

        var messagebody =  Strophe.getText(body);
		var typeMessage = messagebody.split('==')[0];
		var textOrCanvas = messagebody.split('==')[1];
		if(typeMessage == 'action'){
			var action = Mirador.actions.setCanvas('main_window', textOrCanvas)
			miradorInstance.store.dispatch(action);
		}
		else{
			    text = messagebody.split('==')[1];;
				say222();
		}

        console.log('Message from ' + from + ': ' + Strophe.getText(body));
        //log('Message from ' + from + ': ' + Strophe.getText(body));

        // we must return true to keep the handler alive.
        // returning false would remove it after it finishes.


    }


    return true;
}



//viene chiamata all'invio di un messaggio
function send() {
    /*
    console.log("Ho chiamato send()");
    // var from = $('#jid').get(0).value;
    // var to = "mary@jabber.hot-chilli.net";
    var txt = $('#message').get(0).value;
    log("request:" + txt);
    var request = $msg({to: toJid, from: fromJid, type: 'chat'}).c("body").t(txt);
    connection.send(request.tree
    */

}

function sendMyMsg(myText) {
    console.log("Ho chiamato sendMyMsg()");
    // var from = $('#jid').get(0).value;
    // var to = "mary@jabber.hot-chilli.net";
    var txt = myText;
    console.log("request:" + txt);
    var request = $msg({to: toJid, from: fromJid, type: 'chat'}).c("body").t(myText);
    connection.send(request.tree());
}

function provaProva() {
    console.log("Ho chiamato provaProva");
}


