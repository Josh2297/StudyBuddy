function pageinsert() {
    var selectoption=document.getElementById('id_option_process')
    var injectoption=document.getElementById('jin') //Div To Inject
    //switch Statement
    selectoption.addEventListener('click',function() {
        switch (selectoption.value){
            case "page_process":
                injectoption.innerHTML="<input type=\"text\" name=\"page_process\" placeholder=\"Enter Pages to Summarize\" id=\"id_page_process\" class=\"form-control\" max_length=\"100\">\
                 <p class=\"text-danger bold\">Enter Pages Seperated With Comma e.g 1-10,17,25</p>"
                 break;
            case "page_omit":
                injectoption.innerHTML="<input type=\"text\" name=\"page_omit\" placeholder=\"Enter Pages to Omit\" id=\"id_page_omit\" class=\"form-control\" max_length=\"100\">\
                 <p class=\"text-danger bold\">Enter Pages Seperated With Comma e.g 1-10,17,25</p>"
                 break;
            case "none":
                injectoption.innerHTML=""
                break;
                }

    })
if (selectoption.value=='page_process'){ 
    injectoption.innerHTML="<input type=\"text\" name=\"page_process\" placeholder=\"Enter Pages to Summarize\" id=\"id_page_process\" class=\"form-control\" max_length=\"100\">\
    <p class=\"text-danger bold\">Enter Pages Seperated With Comma e.g 1-10,17,25</p>"
}
if (selectoption.value=='page_omit'){
    injectoption.innerHTML="<input type=\"text\" name=\"page_omit\" placeholder=\"Enter Pages to Omit\" id=\"id_page_omit\" class=\"form-control\" max_length=\"100\">\
    <p class=\"text-danger bold\">Enter Pages Seperated With Comma e.g 1-10,17,25</p>"
}
// Handle Spinners
var spin=document.getElementById('summary_spinner');genbtn=spin.parentNode;summary_form=document.forms[0];
summary_form.addEventListener('submit',function(){
    spin.style.visibility="visible"
})
    
}

window.addEventListener('load',pageinsert)