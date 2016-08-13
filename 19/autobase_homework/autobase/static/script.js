$( document ).ready(function() {
    $("button[buy]").click(function(){
        var id = $(this).attr("auto");
        setCookie('auto_' + id, id, 7)
    });
    $("button[delete]").click(function(){
        var id = $(this).attr("auto");
        delCookie('auto_' + id);
        location.reload();
    });
    $("tr[cart]").each(function(){
        var quantity = $(this).find("input[quantity]").attr("quantity");
        var input = $(this).find("input").val();
        if (quantity <= 0){
            $(this).addClass("danger");
        }else{
            $(this).removeClass("danger");
        }
    });
    $(".col-sm-6 > input").change(function(){
        var quantity = $(this).attr("quantity");
        var input = $(this).val();
        if (input > quantity){
            $(this).parents("tr").addClass("danger");
        }else{
            $(this).parents("tr").removeClass("danger");
        }
    });
    $("td > strong").text(function(){
        var sum = 0;
        var elems = $("td[price]").each(function(){
            sum += parseInt($(this).text());
        });
        return sum + " $";
    });
    
});

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function delCookie(name) {
  setCookie(name, "", {
    expires: -1
  })
}