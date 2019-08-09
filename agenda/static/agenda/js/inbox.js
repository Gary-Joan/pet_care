var Inbox = function(){
    var _url = window.location.href;
    var buttons = $('.delete_link');
    var checkboxs = $('.invite_ck');
    var invites = $('.invite');

    invites.click(function(event){
        var invite_id = this.id.split('-');
        var action = '';
        if ($(this.id).hasClass('new')){
            action = 'mark';
            $(this.id).removeClass('new');
            $(this.id).addClass('old');
        }else{
            action = 'unmark';
            $(this.id).addClass('new');
            $(this.id).removeClass('old');
        }
            
        var new_url = _url + '?action=' + action +  '&invite_id=' + invite_id[2];
        $.getJSON(new_url, function(data){
            if (data.status=='ok'){
                //parent.html('');
            }else{
                alert('error');
            }
        });
    });

    buttons.click(function(event){
        var invite_id = this.id.split('.')
        var container_id = "#invite-container-" + invite_id[1];
        var parent = $(container_id);
        var new_url = _url + '?action=delete' + '&invite_id=' + invite_id[1];
        $.getJSON(new_url, function(data){
            if (data.status=='ok'){
                parent.html('');
            }else{
                alert('error');
            }
        });
    });

    checkboxs.click(function(event){
        var invite_id = this.id.split('.')
        var container_id = "#invite-container-" + invite_id[1];
        var action = '';
        if (this.checked){
            action = 'attend';
        }else{
            action = 'unattend';
        }

        var new_url = _url + '?action=' + action  + '&invite_id=' + invite_id[1];
        $.getJSON(new_url, function(data){
            if (data.status=='ok'){
                //parent.html('');
            }else{
                alert('error');
            }

        });
    });
};
$(document).ready(function(){
    var inbox = Inbox();
});
