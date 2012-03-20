$(document).ready(function(){
    $('a.app-link').click(function() {
        var link = $(this),
            app_slug = link.data('app-slug'),
            app_id = link.data('app-id');
        if (!app_slug || !app_id) { return true; }
        if (ANALYTICS_CODE && typeof(_gaq) != 'undefined') {
            _gaq.push(['_trackEvent', 'Applications', 'click', app_slug]);
        }
        if (APP_CID) {
            $.get('/viewtracker/' + APP_CID + '/' + app_id +'/');
        }
    });
});




