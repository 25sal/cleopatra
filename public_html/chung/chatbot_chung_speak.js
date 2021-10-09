// chatbot_chung_speak a program by NGUYEN.Chung (freeware 2015)
var paudio=[],iaudio=0;

function speak(){

if(textspeakall.length>99){

   var i=99;

   for(var j=0;j<40;j++){

       if(textspeakall.substr(i-j,1)==" "){break;};}	   

   i=i-j;

   textspeak=textspeakall.substr(0,i);

   textspeakall=textspeakall.substr(i,textspeakall.length-i);

}else{textspeak=textspeakall;textspeakall="";}

textspeak=textspeak.toLowerCase();

//auxvar=(window.speechSynthesis)+"/tsay="+tsay;

   speakhtml();if(tsay==1){return;};

tsay=0;
}
