$(document).ready(function(){

    var load_logos = function() {
        $('li.dropdown.authors li a').each(function() {
            var a = $(this)
                img_src = a.data('img-src');
            if (img_src) {
                a.prepend($('<img/>').attr('src', img_src));
            }
        });
    }

    var important_images = $('#carousel li.item img');
    if (!$('#carousel').length) {
        important_images = $('.app-list figure img');
    }
    if (important_images.length) {
        var total_loaded = 0,
            on_important_img_loaded = function() {
                total_loaded++;
                if (total_loaded == important_images.length) {
                    load_logos();
                    important_images.unbind('load', on_important_img_loaded);
                }
            };
        important_images.load(on_important_img_loaded);
    } else {
        load_logos();
    }

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




