
let s = 0;
function navclick() {
if (s == 0){
    document.getElementsByClassName('fordesk')[0].style = "display:flex;"
    document.getElementsByClassName('fordesk')[1].style = "display:flex;"
    s = 1;
}
else{
    document.getElementsByClassName('fordesk')[0].style = "display:none;"
    document.getElementsByClassName('fordesk')[1].style = "display:none;"
    s = 0;
}
}
