$(document).ready(function(){


    var carousel = $('#carousel');

    var important_images = {
        container: carousel.length ? carousel : $('.app-list')
    };
    important_images = $.extend({}, important_images, {
        loaded: 0,
        total: important_images.container.find('figure').length,
        logos_loaded: false,

        load_logos: function() {
            /* Load all logos tkong data from the surrouding a */
            if (important_images.load_logos_timer) {
                clearTimeout(important_images.load_logos_timer);
                important_images.load_logos_timer = null;
            }
            if (important_images.logos_loaded) { return; }
            important_images.logos_loaded = true;
            $('li.dropdown.authors li a').each(function() {
                var a = $(this)
                    img_src = a.data('img-src');
                if (img_src) {
                    a.prepend($('<img/>').attr('src', img_src));
                }
            });
        },

        on_img_loaded: function() {
            /* Load logos when the last important image is loaded */
            important_images.loaded++;
            if (important_images.loaded == important_images.total) {
                important_images.load_logos();
                $(this).unbind('load', important_images.on_img_loaded);
            }
        },

        carousel: {
            current_width: 440,
            widths: [440, 538, 712, 870],

            resized: function(first_run) {
                /* Use images adapted to the carousel width (so, the screen width) */
                var new_width = null,
                    test_width = $('#carousel').innerWidth();
                // look for maximal matching width
                for (var i = 0; i < important_images.carousel.widths.length; i += 1) {
                    if (test_width <= important_images.carousel.widths[i]) {
                        new_width = important_images.carousel.widths[i];
                        break;
                    }
                };
                // if new width of first run (which will replace placeholder with an image)
                if (first_run || (new_width && new_width != important_images.carousel.current_width)) {
                    var old_current_width = important_images.carousel.current_width;
                    important_images.carousel.current_width = new_width;
                    var all =  carousel.find('figure img, figure b');
                    var update_src = function(node, on_load) {
                        var is_img = !!(node.get(0).nodeName == 'IMG'),
                            src = is_img ? node.attr('src') : node.data('img-src'),
                            new_src = src.replace(old_current_width + 'x0_q85', new_width + 'x0_q85');
                        if (is_img && src == new_src) { return; }
                        if (!is_img) {
                            var img = $('<img />').attr('alt', node.data('img-alt')).attr('src', new_src);
                            if (on_load) {
                                img.load(on_load);
                            }
                            img.load(important_images.on_img_loaded);
                            node.parent().prepend(img);
                            node.remove();
                        } else {
                            if (on_load) {
                                node.load(on_load);
                            }
                            node.attr('src', new_src);
                        }
                    };
                    var on_first_loaded = function() {
                        $(this).unbind('load', on_first_loaded);
                        carousel.find('figure img, figure span').each(function() {
                            update_src($(this));
                        });
                    };
                    update_src(carousel.find('figure img, figure span').eq(0), on_first_loaded);
                }
            },

            run: function() {
                important_images.carousel.resized(true);
                var on_win_resize = function() { important_images.carousel.resized(false) }
                $(window).resize(on_win_resize);
            }

        }, // carousel

        load_logos_timer: null,
        run: function() {
            if (important_images.total) {
                important_images.load_logos_timer = setTimeout(important_images.load_logos, 30000);
                important_images.container.find('figure img').load(important_images.on_img_loaded);
            } else {
                important_images.load_logos();
            }
            if (carousel.length) {
                important_images.carousel.run();
            }
        }
    }); // important_images

    important_images.run();

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




