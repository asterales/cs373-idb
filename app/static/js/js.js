$( document ).ready(function() {
    // match panel heights
    var heights = $(".panel-match").map(function() {
        return $(this).height();
    }).get(),
    maxHeight = Math.max.apply(null, heights);
    $(".panel-match").height(maxHeight);
});
