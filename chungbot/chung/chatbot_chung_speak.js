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
if (('speechSynthesis' in window)&&(tsay==1)){
   speakhtml();if(tsay==1){return;};
}
tsay=0;
var ttslang=lang;
//alert(textspeak);
//audiosrc ='http://translate.google.com/translate_tts?ie=utf-8&tl=en&q='+encodeURIComponent(textspeak);
//audiosrc ='http://translate.google.com/translate_tts?&tl=en&q='+encodeURIComponent(textspeak);
audiosrc ="http://translate.google.com/translate_tts?&tl="+ttslang+"&q="+encodeURIComponent(textspeak);
audiosrc='http://translate.google.com/translate_tts?tl='+ttslang+'&q='+encodeURIComponent(textspeak)+'&ie=UTF-8&total=1&idx=0&client=t';
textspeak = textspeak.replace(/^\s+|\s+$/g, "");
textspeak=textspeak.split(' ').filter(s => s).join('+');
audiosrc='https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q='+textspeak;
console.log(audiosrc);
//audiosrc ='http://translate.google.com/translate_tts?&tl=es&q='+encodeURIComponent(textspeak);
//audiosrc ='http://translate.google.com/translate_tts?&tl=fr&q='+encodeURIComponent(textspeak);
//audiosrc ='http://translate.google.com/translate_tts?&tl=de&q='+encodeURIComponent(textspeak);
//audiosrc ='http://translate.google.com/translate_tts?&tl=it&q='+encodeURIComponent(textspeak);
//text=encodeURIComponent(textspeak);
//audiosrc='http://translate.google.com/translate_tts?ie=UTF-8&q='+text+'&tl=en&total=1&idx=0&textlen='+text.length+'&prev=input';
textspeak=textspeak+" ";

if(iaudio>0){paudio[iaudio].src=null;}
iaudio+=1;
paudio[iaudio]=new Audio();
audio=paudio[iaudio];
 
audio.type="audio/mp3";//"x-wav";
audio.src=audiosrc;
var Timer=-1;
//audio.addEventListener('loadedmetadata',function(){
audio.addEventListener('canplay',function(){
 tsay=0;
 if(Timer<0){ Timer=gettimer()/1000.0;
 audiotime0=Timer;
 audiotime1=Timer+audio.duration;
 if(textspeakall.length>1){audiotime1-=0.05;}//0.5
 //alert(audiotime1-audiotime0);
 //audio.playbackRate=0.7;
 audio.play();
 };
});
//audio.addEventListener('ended',function(){audio.src="";});
tsay=1;audiotime1=8+gettimer()/1000.0;
audio.load();
//audio.play();//load();
//alert("say0="+textspeak);
//alert("$"+vars['_y']);
//alert("$ "+vars['_x']+eval("if(vars['_x']){alert(vars['_x']);};"));eval("vars['_x']='ok1'");


/*salvatore
document.getElementById('intext').value="";
document.getElementById('intext').focus();
document.getElementById('ntest').innerHTML=" "+ntest0;
*/ 
}

