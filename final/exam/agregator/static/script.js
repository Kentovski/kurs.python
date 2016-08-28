$( document ).ready(function() {
    $("button").click(function(){
        var q = $("input").val();
        var query_string = "/?query=" + q;
        $.get(query_string, function(data, status){
            $('#instagram .row').html(function(){
                var output = '';
                data.instagram.forEach(function(item){
                    output +=  `
                        <div class="col-md-2">
                            <a href="${item.direct_link}" target="_blank">
                                <img src="${item.direct_link}" style="width:150px;height:150px">
                                <a href="${item.source_link}" target="_blank" class="center-block">Источник</a>
                            </a>
                        </div>
                    `;
                });
                return output
            })

            $('#yandex .row').html(function(){
                var output = '';
                data.yandex.forEach(function(item){
                    output +=  `
                        <div class="col-md-2">
                            <a href="${item.direct_link}" target="_blank">
                                <img src="${item.direct_link}" style="width:150px;height:150px">
                                <a href="${item.source_link}" target="_blank" class="center-block">Источник</a>
                            </a>
                        </div>
                    `;
                });
                return output
            })

            $('#google .row').html(function(){
                var output = '';
                data.google.forEach(function(item){
                    output +=  `
                        <div class="col-md-2">
                            <a href="${item.direct_link}" target="_blank">
                                <img src="${item.direct_link}" style="width:150px;height:150px">
                                <a href="${item.source_link}" target="_blank" class="center-block">Источник</a>
                            </a>
                        </div>
                    `;
                });
                return output
            })
        });
    });
});
