$(function(){
    var xmlhttp;
    var loveFlag; 
    

    $(function(){
        if(window.XMLHttpRequest)
        {
            xmlhttp = new XMLHttpRequest();
        }
        else{
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function(){
            if(xmlhttp.readyState==4 && xmlhttp.status==200){
                if(xmlhttp.responseText==0)
                {
                    loveFlag = 0;
                    $('#love-btn').button('dispose');
                }
                if(xmlhttp.responseText==1)
                {
                    loveFlag = 1;
                    $('#love-btn').button('toggle');
                }
            }
        }
        xmlhttp.open("GET","#URL",true);
        xmlhttp.send();
    });
    
    function loveChange(){
        if(loveFlag==0)
            loveFlag = 1;
        else
            loveFlag = 0;
            var postData= { //（2）传递参数到后台，注意后台接收方式 
                "loveFlag":loveFlag}
       /**重点：ajax的type,url,dataType,data属性*/
        $.ajax({
                async : false,
                cache : false,
                type : 'POST',
                url : 'area/delete',
                dataType : "json",
                data : postData,            
                error : function() {
                    alert('请求失败 ');
                },
                success : function(data) {
                    alert(data);
                }
    
            });
    }
    
});

   
