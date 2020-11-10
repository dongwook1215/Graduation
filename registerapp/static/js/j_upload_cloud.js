let ex_file;

function printLoading(){
    var str = "";
    str += "<div class=\"loading\">";
    str += "<span>L</span>";
    str += "<span>O</span>";
    str += "<span>A</span>";
    str += "<span>D</span>";
    str += "<span>I</span>";
    str += "<span>N</span>";
    str += "<span>G</span>";
    str += "</div>";

    $("body").append(str);
}

function removeLoading(){
    $(".loading").remove();
    $(".uploading").remove();
    $(".downloading").remove();
}

function save_file(event){
    ex_file=event.target.files[0];
    console.log("현재파일: ", ex_file);
}
window.onload=function(){
    console.log("csrf 결과값", temp);
    let prediction_button=document.getElementById("prediction");
    let file_button=document.getElementById("file");

    file_button.addEventListener("change",save_file);

    prediction_button.addEventListener("click",function(){
        console.log("예측 버튼을 눌렀습니다.");
        let formData = new FormData();

        formData.append('file', ex_file);
        
        formData.append('csrfmiddlewaretoken', temp);

        $.ajax({
            url: "dataTransmit/",
            type: "post",
            data : formData,
            processData:false,
            contentType:false,
            async: true,
            beforeSend: function(){
                printLoading();
            },
            success: function (result) {
                console.log(result);
            },
            error: function (err) {
                removeLoading();
            },
            complete: function(){
                removeLoading();
            }
        });
    })
}