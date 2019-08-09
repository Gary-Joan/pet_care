django.jQuery(document).ready(function () {
  django.jQuery("#id_object_id")[0].options.length = 0; //vaciar options
  django.jQuery("#id_object_id")[0].options[0] = new Option("-------"); //vaciar options
  django.jQuery("#id_content_type").change(function () {
    django.jQuery("#id_object_id")[0].options.length = 0;
    django.jQuery("#id_object_id")[0].options[0] = new Option("-------");
    var value = django.jQuery("#id_content_type")[0].value;
    var url  = "/admin/agenda/agenda/update/" + value + "/";
    django.jQuery.getJSON(url, function(data) {
      for(i=0; i<data.length; i++){
        django.jQuery("#id_object_id")[0].options[i+1] = new Option(data[i][1], data[i][0]);
    }
    });
  });
});      
