var BOSH_SERVICE = 'https://jabber.hot-chilli.net/http-bind';
var connection = null;
var fromJid = "mary@jabber.hot-chilli.net";
//var toJid = "ciro@jabber.hot-chilli.net";
var toJid = "cleopatra2@jabber.hot-chilli.net";

document.addEventListener('DOMContentLoaded', bot_connect, false);

function bot_connect() {  // clic per cambiare i messaggi

  /*
	$( "#send" ).click(function() { // click sul modalResponse
	  send();
	});
  */


  connection = new Strophe.Connection(BOSH_SERVICE);
   connection.connect("mary@jabber.hot-chilli.net","Mary1994",  onConnect);

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
    }
    /*
    console.log("setting canvas");
    var action1 = Mirador.actions.setCanvas('main_window', 'http://localhost/~salvatore/alba/msprova/index.json/canvas/1')
	// Now we can dispatch it.
	miradorInstance.store.dispatch(action1);
	
	console.log("remove manifest");
    var action3 = Mirador.actions.removeManifest('msprova/manifest.json');
	// Now we can dispatch it.
	miradorInstance.store.dispatch(action3);
	
	console.log("adding manifest");
	var action2 = Mirador.actions.addResource('http://143.225.20.99/alba/manifest.json')
	// Now we can dispatch it.
	miradorInstance.store.dispatch(action2);
	*/
    
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
	
	
	console.log('Message from ' + from + ': ' + Strophe.getText(body));
	var messagebody =  Strophe.getText(body);
	text = messagebody;
	say222();
	//log('Message from ' + from + ': ' + Strophe.getText(body));
    
	// we must return true to keep the handler alive.  
    // returning false would remove it after it finishes.
    
    /*
    var action = Mirador.actions.setCanvas('main_window', 'http://localhost/~salvatore/alba/msprova/index.json/canvas/1')
	// Now we can dispatch it.
	miradorInstance.store.dispatch(action);
	
	var action = Mirador.actions.setCanvas('main_window', 'http://localhost/~salvatore/alba/msprova/index.json/canvas/1')
	// Now we can dispatch it.
	miradorInstance.store.dispatch(action);
	*/ 

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
	  



  
