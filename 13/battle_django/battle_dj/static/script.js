$( document ).ready(function() {
google.charts.load('current', {'packages':['bar']});
 
    //Функция длч чтения csrf токена.
    function getCookie(name) {
           var cookieValue = null;
           if (document.cookie && document.cookie != '') {
             var cookies = document.cookie.split(';');
             for (var i = 0; i < cookies.length; i++) {
             var cookie = jQuery.trim(cookies[i]);
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
              }
         }
     }
     return cookieValue;
    }


    //Обработчик кнопок "Закодировать" и "Раскодировать"
     $(":button").click(function(e) {
         e.preventDefault();

         //Выставляем режим в зависимости от того, какая кнопка нажата: "Закодировать" или "Раскодировать"
         if ( $(this).is("#encode_btn") ){
            var mode = "e";
            $("#brute").addClass("hidden");
         }else{
            var mode = "d";
            $("#brute").removeClass("hidden");
         };

         //Получаем данные из форм и куков
         var csrftoken = getCookie('csrftoken');
         var rot = $('#id_rot').val();
         var encode = $('#id_encode').val();

         //Посылаем синхронный запрос на сервер с введенными данными 
         $.ajax({
                     url : window.location.href, 
                     type : "POST",
                     data : { csrfmiddlewaretoken : csrftoken, 
                     encode : encode,
                     rot : rot,
                     mode: mode,
                      },

             //Обработка ошибок из forms.errors
             success : function(json) {
                  if (!json['encode'] && json['rot']) {
                        $("#errmsg").html(json['rot']).removeClass("hidden");
                  }else if (!json['rot'] && json['encode']) {
                        $("#errmsg").html(json['encode']).removeClass("hidden");
                  }else if (json['rot'] && json['encode']){
                         $("#errmsg").html(json['encode'] + "</br>" + json['rot']).removeClass("hidden");
                  }else if (!json['rot'] && !json['encode']){
                         $("#errmsg").addClass("hidden");
                         $("#decode").html(json['result']);
                         
                         //Создаем диаграмму
                         google.charts.setOnLoadCallback(drawStuff);    
                         function drawStuff() {
                                var data = new google.visualization.DataTable(json['diagram_data']);
                                var options = {
                                          title: 'Частотная диаграмма',
                                          width: 900,
                                          height: 400,
                                          legend: { position: 'none' },
                                          chart: { subtitle: 'Сколько раз встречается буквы в зашифрованной фразе' },
                                          axes: {
                                            x: {
                                              0: { side: 'bottom'} // Top x-axis.
                                            }
                                          },
                                          bar: { groupWidth: "90%" }
                                 };
                          var chart = new google.charts.Bar(document.getElementById('diagram'));
                          chart.draw(data, google.charts.Bar.convertOptions(options));
                          };
                  }
             },

             //Если что-то пошло не так во время ajax-запроса
             error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); 
             }
         });

    });

});
