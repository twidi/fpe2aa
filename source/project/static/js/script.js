$(document).ready(function(){

    $('li.dropdown.authors li a').each(function() {
        var a = $(this)
            img_src = a.data('img-src');
        if (img_src) {
            a.prepend($('<img/>').attr('src', img_src));
        }
    });


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




