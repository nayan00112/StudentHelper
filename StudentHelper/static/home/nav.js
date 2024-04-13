
let s = 0;
function navclick() {
if (s == 0){
    document.getElementsByClassName('fordesk')[0].style = "display:flex;  background-color:white; z-index: 1;"
    document.getElementsByClassName('fordesk')[1].style = "display:flex; background-color:white; z-index: 1;"
    s = 1;
}
else{
    document.getElementsByClassName('fordesk')[0].style = "display:none;"
    document.getElementsByClassName('fordesk')[1].style = "display:none;"
    s = 0;
}
}