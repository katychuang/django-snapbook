
WebFontConfig = {
google: { families: [ 'Poiret+One::latin','Lato', 'Walter+Turncoat::latin', 'Muli', 'Swanky+and+Moo+Moo', 'Cardo'] }};
(function() {
var wf = document.createElement('script');
wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
  '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
wf.type = 'text/javascript';
wf.async = 'true';
var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(wf, s);
})(); 
