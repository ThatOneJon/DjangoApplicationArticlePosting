
document.addEventListener('DOMContentLoaded', () => {
    try{
    let bttn=document.getElementById("edit");
        bttn.onclick = function () {
            document.getElementById("article_Content").style.display="none";
            document.getElementById("edit_Article").style.display = 'flex';  
        }
    }

    catch(TypeError){
    //If a Type error occurs, skipp the function -> Error because different templates Use this function -> Python: pass statement
        }
try{
let bttn2=document.getElementById("editArt_Profile");
    bttn2.onclick = () => {
    document.getElementById("Edit_Profile").style.display="flex";
    document.getElementById("unedited_Profile").style.display="none";
    document.getElementById("yourArticles").style.display="none";
    }
}catch(TypeError){

}
    

})