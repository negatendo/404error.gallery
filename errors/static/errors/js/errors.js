$('.artlink').hover(
    function(){ $(this).addClass('glitch') },
    function(){ $(this).removeClass('glitch') }
)

$('#randoform').on('submit', function(e) {
    e.preventDefault();
    document.location = 'http://404error.gallery/' + $('#randovalue').val()
});

window.setTimeout(glitch_header,5000);
function glitch_header() {
    $("#header").addClass('glitch-header');
    $("#header").one('webkitAnimationEnd oanimationend msAnimationEnd animationend',
    function (e) {
        $("#header").removeClass('glitch-header');
    });
    window.setTimeout(glitch_header,5000);
}

window.setTimeout(glitch_bits,3000);
function glitch_bits() {
    $(".glitchy-bit").addClass('glitch-bit');
    $(".glitchy-bit").one('webkitAnimationEnd oanimationend msAnimationEnd animationend',
    function (e) {
        $(".glitchy-bit").removeClass('glitch-bit');
    });
    window.setTimeout(glitch_bits,3000);
}
